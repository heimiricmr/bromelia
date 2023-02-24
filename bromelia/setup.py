# -*- coding: utf-8 -*-
"""
    bromelia.setup
    ~~~~~~~~~~~~~~
    
    This module implements the central Diameter application object. It works
    as per Peer State Machine defined in RFC 6733 in order to establish a 
    Diameter association with another Peer Node.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import copy
import datetime
import logging
import platform
import queue
import socket 
import sys
import threading
import time
from contextlib import contextmanager
from typing import Any, List, Type

from ._internal_utils import _convert_config_to_connection_obj
from ._internal_utils import get_app_ids
from ._internal_utils import application_id_look_up
from ._internal_utils import Connection
from .base import DiameterMessage
from .config import Config
from .config import DiameterLogging
from .config import (SLEEP_TIMER, WAITING_CONN_TIMER,
                     LISTENING_TICKER, SEND_BUFFER_MAXIMUM_SIZE)
from .config import CLOSED, I_OPEN, R_OPEN
from .constants import DIAMETER_AGENT_CLIENT_MODE
from .constants import DIAMETER_AGENT_SERVER_MODE
from .constants import DIAMETER_AGENT_TRANSPORT_TYPE_TCP
from .constants import DIAMETER_AGENT_TRANSPORT_TYPE_SCTP
from .exceptions import AVPParsingError
from .exceptions import DiameterApplicationError
from .exceptions import DiameterAssociationError
from .messages import DiameterAnswer
from .messages import DiameterRequest
from .proxy import BaseMessages
from .proxy import DiameterBaseProxy
from .statemachine import PeerStateMachine
from .transport import TcpClient
from .transport import TcpServer
from .transport import SctpClient
from .transport import SctpServer
from .utils import is_base_request
from .utils import is_base_answer

diameter_conn_logger = logging.getLogger("DiameterConnection")
diameter_logger = logging.getLogger("Diameter")


def make_logging(msg, disable_else=False):
    if msg.has_avp("user_name_avp"):
        diameter_conn_logger.debug(f"Message from "\
                                   f"postprocess_recv_messages Queue: "\
                                   f"{application_id_look_up(msg.header.application_id)[0]}, "\
                                   f"{msg.header.get_command_code()}, "\
                                   f"{msg.header.is_request()}, "\
                                   f"{msg.header.hop_by_hop.hex()}, "\
                                   f"{len(msg)}, "\
                                   f"{msg.user_name_avp.data}")
    else:
        if disable_else:
            return

        diameter_conn_logger.debug(f"Message from "\
                                   f"postprocess_recv_messages Queue: "\
                                   f"{application_id_look_up(msg.header.application_id)[0]}, "\
                                   f"{msg.header.get_command_code()}, "\
                                   f"{msg.header.is_request()}, "\
                                   f"{msg.header.hop_by_hop.hex()}, "\
                                   f"{len(msg)}")


class DiameterAssociation(object):
    def __init__(self, connection: Connection, base: BaseMessages) -> None:
        self.connection = connection
        self.base = base

        self.state_is_active = False
        self.transport = None
        self.error_has_raised = False
        self._stop_threads = False

        self.num_answers = 0
        self.num_requests = 0

        self.watchdog_timeout = self.connection.watchdog_timeout
        self.tracking_events_count = 0

        self.end_to_end_identifiers = list()
        self.pending_requests = dict()

        self._recv_messages = queue.Queue()
        self._send_messages = queue.Queue()

        self.postprocess_recv_messages = queue.Queue() 
        self.postprocess_recv_messages_ready = threading.Event()
        self.postprocess_recv_messages_lock = threading.Lock()
        self.lock = threading.Lock()


    def is_connected(self) -> bool:
        if self.transport:
           return self.transport.is_connected
        
        return False


    def __is_connected(self) -> bool:
        if not self.is_connected():
            raise DiameterAssociationError("There is no transport "\
                                           "connection up for this PeerNode.")


    def start(self) -> None:
        self._stop_threads = False

        if self.connection.mode == DIAMETER_AGENT_CLIENT_MODE:
            if self.connection.transport_type == DIAMETER_AGENT_TRANSPORT_TYPE_TCP:
                self.transport = TcpClient(self.connection.peer_node.ip_address,
                                          self.connection.peer_node.port)
            elif self.connection.transport_type == DIAMETER_AGENT_TRANSPORT_TYPE_SCTP:
                self.transport = SctpClient(self.connection.peer_node.ip_address,
                                           self.connection.peer_node.port)
            else:
                raise DiameterAssociationError("Invalid Diameter Agent transport type.")

        elif self.connection.mode == DIAMETER_AGENT_SERVER_MODE:
            if self.connection.transport_type == DIAMETER_AGENT_TRANSPORT_TYPE_TCP:
                self.transport = TcpServer(self.connection.local_node.ip_address,
                                        self.connection.local_node.port)
            elif self.connection.transport_type == DIAMETER_AGENT_TRANSPORT_TYPE_SCTP:
                self.transport = SctpServer(self.connection.local_node.ip_address,
                                       self.connection.local_node.port)
            else:
                raise DiameterAssociationError("Invalid Diameter Agent transport type.")

        else:
            raise DiameterAssociationError("Invalid Diameter Agent mode.")

        self.transport.start()
        self.transport.run()

        threading.Thread(name="recv_message_monitor",
                         target=self.recv_message_from_queue).start()


    def close(self) -> None:
        self.__is_connected()

        self.state_is_active = False
        self._stop_threads = True
        self.transport.close()
        self.transport = None


    def recv_message_from_queue(self) -> None:
        while not self._stop_threads and self.transport:
            self.transport._recv_data_available.wait(timeout=1)

            self.lock.acquire()

            if self.transport is None:
                break

            data_stream = copy.copy(self.transport._recv_data_stream)
            self.transport._recv_data_stream = b""
            self.transport._recv_data_available.clear()

            diameter_conn_logger.debug("Grabbing data stream from "\
                                       "Transport Layer to Diameter Layer.")

            try:
                msgs = DiameterMessage.load(data_stream)
                for msg in msgs:
                    make_logging(msg, disable_else=True)
                    self._recv_messages.put(msg)
                
                diameter_conn_logger.debug(f"Found {len(msgs)} Diameter "\
                                           f"Message(s).")
            except AVPParsingError:
                diameter_conn_logger.exception(f"AVPParsingError has "\
                                               f"been raised due stream: "\
                                               f"{self.transport._recv_data_stream.hex()}")

            self.lock.release()


    def put_message_into_send_queue(self, msg: Type[DiameterMessage]) -> None:
        self.lock.acquire()

        self.__is_connected()
        self._send_messages.put(msg)

        hop_by_hop = msg.header.hop_by_hop

        if isinstance(msg, DiameterRequest):
            diameter_conn_logger.debug(f"[{hop_by_hop.hex()}] Diameter "\
                                       f"Request have been put into "\
                                       f"_send_messages Queue.")

            key = msg.header.end_to_end.hex()
            self.end_to_end_identifiers.append(key)

        elif isinstance(msg, DiameterAnswer):
            diameter_conn_logger.debug(f"[{hop_by_hop.hex()}] Diameter "\
                                       f"Answer have been put into "\
                                       f"_send_messages Queue.")

        elif isinstance(msg, DiameterMessage):
            if msg.header.is_request():
                diameter_conn_logger.debug(f"[{hop_by_hop.hex()}] Diameter "\
                                           f"Message (Request) have been put "\
                                           f"into _send_messages Queue.")

                key = msg.header.end_to_end.hex()
                self.end_to_end_identifiers.append(key)

            else:
                diameter_conn_logger.debug(f"[{hop_by_hop.hex()}] Diameter "\
                                           f"Message (Answer) have been put "\
                                           f"into _send_messages Queue.")
                
        self.lock.release()


    def send_message_from_queue(self) -> None:
        self.lock.acquire()
        self.__is_connected()

        diameter_conn_logger.debug(f"There is/are "\
                                   f"{self._send_messages.qsize()} Diameter "\
                                   f"Message(s) in the Sending Queue.")

        stream = b""
        while not self._send_messages.empty() and \
                len(stream) <= SEND_BUFFER_MAXIMUM_SIZE:
            msg = self._send_messages.get()
            diameter_conn_logger.debug(f"[{msg.header.hop_by_hop.hex()}] "\
                                       f"Preparing message to be sent.")

            MESSAGE_LENGTH = len(msg.dump())

            if MESSAGE_LENGTH > SEND_BUFFER_MAXIMUM_SIZE - len(stream):
                self._send_messages.put(msg)
                break

            if isinstance(msg, DiameterRequest):
                key = msg.header.hop_by_hop.hex()
                self.pending_requests.update({key: msg})
                diameter_conn_logger.debug(f"[{msg.header.hop_by_hop.hex()}] "\
                                           f"Diameter Request have been "\
                                           f"put into Pending Request Queue.")
    
            stream += msg.dump()

        if self.transport:
            if not self.transport.is_write_mode():
                diameter_conn_logger.debug("Transport Layer is not in WRITE "\
                                           "mode, so we can send data stream.")

                self.transport._set_selector_events_mask("rw", stream)
            else:
                diameter_conn_logger.debug("Transport Layer is in WRITE "\
                                           "mode, so we cannot send data "\
                                           "stream.")

                while not self._stop_threads and self.transport:
                    self.transport.write_mode_on.wait()
                    if not self.transport.is_write_mode():
                        diameter_conn_logger.debug("Transport Layer is not in "\
                                                   "WRITE mode again, so we "\
                                                   "can send data stream.")
    
                        self.transport._set_selector_events_mask("rw", stream)
                        
                        # maybe include a verification here before the "break" if a given message has been sent from transport layer.
                        break


        self.lock.release()


    def get_postprocess_recv_message(self):
        self.lock.acquire()
        diameter_conn_logger.debug("Acquired DiameterAssociation lock")

        self.postprocess_recv_messages_lock.acquire()
        msg = self.postprocess_recv_messages.get()
        self.postprocess_recv_messages_lock.release()

        make_logging(msg)

        self.postprocess_recv_messages_ready.clear()
        diameter_conn_logger.debug("Cleared go ahead for "\
                                   "postprocess_recv_messages_ready")

        self.lock.release()
        diameter_conn_logger.debug("Released DiameterAssociation lock")
        return msg


    def get_message(self) -> Type[DiameterMessage]:
        while not self._stop_threads:
            if self.postprocess_recv_messages.empty():
                self.postprocess_recv_messages_ready.wait()
                diameter_conn_logger.debug("Got go ahead for "\
                                           "postprocess_recv_messages_ready")
            else:
                diameter_conn_logger.debug("No need to wait for go ahead for "\
                                           "postprocess_recv_messages_ready")
    
            return self.get_postprocess_recv_message()


    def tracking_events(self) -> None:
        try:
            if (not self.transport.events) and (self.transport.tracking_events_count >= self.watchdog_timeout):
                self.put_message_into_send_queue(self.base.dwr)
                diameter_conn_logger.debug("Generating a DWR message.")

                self.transport.tracking_events_count = 0
        
        except AttributeError as e:
            if e.args[0] == "'TcpServer' object has no attribute 'events'":
                pass


class Diameter:
    config_class = Config

    default_config = {
            "MODE": "CLIENT",
            "APPLICATIONS": [],
            "LOCAL_NODE_HOSTNAME": platform.node(),
            "LOCAL_NODE_REALM": socket.getfqdn(),
            "LOCAL_NODE_IP_ADDRESS": socket.gethostbyname(platform.node()),
            "LOCAL_NODE_PORT": 3868,
            "PEER_NODE_HOSTNAME": None,
            "PEER_NODE_REALM": None,
            "PEER_NODE_IP_ADDRESS": None,
            "PEER_NODE_PORT": 3868,
            "WATCHDOG_TIMEOUT": 60
        }


    def __init__(self,
                 config: dict = None,
                 debug: bool = False,
                 is_logging: bool = False,
                 app_name: str = None) -> None:
        
        self.logging = DiameterLogging(debug, is_logging, app_name)
        
        self.config = self.make_config(config)
        self._connection = _convert_config_to_connection_obj(self.config)
        self._base = self.get_base_messages()
        self._association = None
        self._peer_state_machine = None


    def make_config(self, config: dict) -> Config:
        if config:
            return self.config_class(config)
        return self.config_class(Diameter.default_config)


    def get_base_messages(self, msgs: List[Type[DiameterMessage]] = None) -> BaseMessages:
        proxy = DiameterBaseProxy(self._connection)
        if msgs:
            return proxy.get_custom_messages(msgs)
        else:
            return proxy.get_default_messages()


    def get_current_state(self) -> Any:
        if self._peer_state_machine:
            return self._peer_state_machine.get_current_state()
        return CLOSED


    def start(self) -> None:
        current_state = self.get_current_state()

        if current_state != CLOSED:
            raise DiameterApplicationError("Cannot start the application. "\
                                           "Peer State Machine is already "\
                                           "running")

        self._association = DiameterAssociation(self._connection, self._base)
        self._peer_state_machine = PeerStateMachine(self._association)

        self._peer_state_machine.start()
        self._association.start()


    def reset(self) -> None:
        current_state = self.get_current_state()

        if current_state == CLOSED:
            raise DiameterApplicationError("Cannot reset the application. "\
                                           "Peer State Machine is already "\
                                           "closed")

        self.close()
        time.sleep(SLEEP_TIMER)
        self.start()


    def close(self) -> None:
        current_state = self.get_current_state()
        
        if current_state == CLOSED:
            raise DiameterApplicationError("Cannot stop the application. "\
                                           "Peer State Machine is already "\
                                           "closed")

        self._peer_state_machine.close()


    def send_messages(self, msgs: List[Type[DiameterMessage]]) -> None:
        for msg in msgs:
            self._association.put_message_into_send_queue(msg)


    def send_message(self, msg: Type[DiameterMessage], avoid: bool = True) -> Any:
        if isinstance(msg, DiameterRequest):
            diameter_logger.debug(f"External app wants to send a Diameter "\
                                  f"Request: "\
                                  f"{application_id_look_up(msg.header.application_id)[0]}, "\
                                  f"{msg.header.get_command_code()}, "\
                                  f"{msg.header.hop_by_hop.hex()}, "\
                                  f"LEN: {len(msg)}")

            if is_base_request(msg):
                raise DiameterApplicationError("Cannot send a Base protocol "\
                                               "request")

            self._association.put_message_into_send_queue(msg)
            if not avoid:
                return self._association.get_message(msg)

        elif isinstance(msg, DiameterAnswer):
            diameter_logger.debug(f"External app wants to send a Diameter "\
                                  f"Answer: "\
                                  f"{application_id_look_up(msg.header.application_id)[0]}, "\
                                  f"{msg.header.get_command_code()}, "\
                                  f"{msg.header.hop_by_hop.hex()}, "\
                                  f"LEN: {len(msg)}")

            if is_base_answer(msg):
                raise DiameterApplicationError("Cannot send a Base protocol "\
                                               "answer")

            self._association.put_message_into_send_queue(msg)

        elif isinstance(msg, DiameterMessage):
            if msg.header.is_request():
                if is_base_request(msg):
                    raise DiameterApplicationError("Cannot send a Base protocol "\
                                                   "request")

                self._association.put_message_into_send_queue(msg)
                if not avoid:
                    return self._association.get_answer_from_request(msg)

            else:
                if is_base_answer(msg):
                    raise DiameterApplicationError("Cannot send a Base protocol "\
                                                   "answer")
                
                self._association.put_message_into_send_queue(msg)


        else:
            raise DiameterApplicationError("Either Diameter Request or "\
                                           "Diameter Answer objects are "\
                                           "allowed to be sent")


    def get_message(self) -> Type[DiameterMessage]:
        return self._association.get_message()


    @contextmanager
    def context(self) -> None:
        app_ids = get_app_ids(self.config["APPLICATIONS"])
        print(f"  * Running Diameter app ({app_ids}) on "\
              f"{self.config['LOCAL_NODE_IP_ADDRESS']}"\
              f":{self.config['LOCAL_NODE_PORT']} as "\
              f"{self.config['MODE']} mode (CEX)")

        try:
            self.start()

            start = datetime.datetime.utcnow()
            while True:
                time.sleep(LISTENING_TICKER)
                stop = datetime.datetime.utcnow()

                if self.is_open():
                    break
                
                if self.is_closed() and (stop - start).seconds >= 5:
                    start = datetime.datetime.utcnow()
                    self.start()

            print(f"  * Diameter connection on "\
                  f"{self.config['LOCAL_NODE_IP_ADDRESS']}:"\
                  f"{self.config['LOCAL_NODE_PORT']} is now up")

            time.sleep(WAITING_CONN_TIMER)
            yield self

            if self.is_open():
                self.close()

        except KeyboardInterrupt:
            print(f"  * Diameter connection on "\
                  f"{self.config['LOCAL_NODE_IP_ADDRESS']}:"\
                  f"{self.config['LOCAL_NODE_PORT']} is now down")

            sys.exit(0)

        print(f"  * Diameter connection on "\
              f"{self.config['LOCAL_NODE_IP_ADDRESS']}:"\
              f"{self.config['LOCAL_NODE_PORT']} is now down")


    def is_open(self) -> bool:
        try:
            if self.get_current_state() == I_OPEN or \
               self.get_current_state() == R_OPEN:
                return True
            return False
        except TypeError:
            if "'NoneType' object is not subscriptable":
                return False


    def is_closed(self) -> bool:
        try:
            if self.get_current_state() == CLOSED:
                return True
            return False
        except TypeError:
            if "'NoneType' object is not subscriptable":
                return False
