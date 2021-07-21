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

from ._internal_utils import _convert_config_to_connection_obj
from ._internal_utils import get_app_ids
from .base import DiameterMessage
from .config import Config
from .config import DiameterLogging
from .config import LISTENING_TICKER
from .config import SEND_BUFFER_MAXIMUM_SIZE
from .config import SLEEP_TIMER
from .config import WAITING_CONN_TIMER
from .constants import DIAMETER_AGENT_CLIENT_MODE
from .constants import DIAMETER_AGENT_SERVER_MODE
from .exceptions import AVPParsingError
from .exceptions import DiameterApplicationError
from .exceptions import DiameterAssociationError
from .messages import DiameterAnswer
from .messages import DiameterRequest
from .proxy import DiameterBaseProxy
from .statemachine import PeerStateMachine
from .statemachine import CLOSED, I_OPEN, R_OPEN
from .transport import TcpClient
from .transport import TcpServer
from .utils import is_base_request
from .utils import is_base_answer

diameter_conn_logger = logging.getLogger("DiameterConnection")
diameter_logger = logging.getLogger("Diameter")


class DiameterAssociation(object):
    def __init__(self, connection, base):
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
        self.postprocess_recv_requests = queue.Queue() 
        self.postprocess_recv_answers = dict() 
        self.postprocess_recv_messages = queue.Queue() 

        self.postprocess_recv_requests_ready = threading.Event()
        self.postprocess_recv_answers_ready = threading.Event()
        self.postprocess_recv_messages_ready = threading.Event()

        self.postprocess_recv_requests_lock = threading.Lock()
        self.postprocess_recv_answers_lock = threading.Lock()
        self.lock = threading.Lock()


    def is_connected(self):
        if self.transport:
           return self.transport.is_connected
        
        return False


    def __is_connected(self):
        if not self.is_connected():
            raise DiameterAssociationError("There is no transport "\
                                           "connection up for this PeerNode.")


    def start(self):
        self._stop_threads = False

        if self.connection.mode == DIAMETER_AGENT_CLIENT_MODE:
               self.transport = TcpClient(self.connection.peer_node.ip_address, 
                                          self.connection.peer_node.port)
            
        elif self.connection.mode == DIAMETER_AGENT_SERVER_MODE:
            self.transport = TcpServer(self.connection.local_node.ip_address, 
                                       self.connection.local_node.port)

        else:
            raise DiameterAssociationError("Invalid Diameter Agent mode.")

        self.transport.start()
        self.transport.run()

        threading.Thread(name="recv_message_from_queue",
                         target=self.recv_message_from_queue).start()


    def close(self):
        self.__is_connected()

        self.state_is_active = False
        self._stop_threads = True
        self.transport.close()
        self.transport = None


    def recv_message_from_queue(self):
        while not self._stop_threads and self.transport:
            self.transport._recv_data_available.wait()

            self.lock.acquire()

            data_stream = copy.copy(self.transport._recv_data_stream) 
            self.transport._recv_data_stream = b""

            diameter_conn_logger.debug("Grabbing data stream from "\
                                       "Transport Layer to Diameter Layer.")

            try:
                msgs = DiameterMessage.load(data_stream)
                for msg in msgs:
                    self._recv_messages.put(msg)            
                
                diameter_conn_logger.debug(f"Found {len(msgs)} Diameter "\
                                           f"Message(s).")
            except AVPParsingError:
                diameter_conn_logger.exception(f"AVPParsingError has "\
                                               f"been raised due stream: "\
                                               f"{self.transport._recv_data_stream.hex()}")

            self.transport._recv_data_available.clear()

            self.lock.release()


    def put_message_into_send_queue(self, msg):
        self.lock.acquire()

        self.__is_connected()
        self._send_messages.put(msg)

        if isinstance(msg, DiameterRequest):
            diameter_conn_logger.debug("Diameter Request have been put "\
                                       "into _send_messages Queue.")

            key = msg.header.end_to_end.hex()
            self.end_to_end_identifiers.append(key)

        elif isinstance(msg, DiameterAnswer):
            diameter_conn_logger.debug("Diameter Answer have been put "\
                                       "into _send_messages Queue.")

        elif isinstance(msg, DiameterMessage):
            if msg.header.is_request():
                diameter_conn_logger.debug("Diameter Request have been put "\
                                           "into _send_messages Queue.")

                key = msg.header.end_to_end.hex()
                self.end_to_end_identifiers.append(key)

            else:
                diameter_conn_logger.debug("Diameter Answer have been put "\
                                           "into _send_messages Queue.")
                
        self.lock.release()


    def send_message_from_queue(self):
        self.lock.acquire()

        self.__is_connected()

        diameter_conn_logger.debug(f"There is/are "\
                                   f"{self._send_messages.qsize()} Diameter "\
                                   f"Message(s) in the Sending Queue.")

        stream = b""
        while not self._send_messages.empty() and \
                len(stream) <= SEND_BUFFER_MAXIMUM_SIZE:
            msg = self._send_messages.get()

            MESSAGE_LENGTH = len(msg.dump())

            if MESSAGE_LENGTH > SEND_BUFFER_MAXIMUM_SIZE - len(stream):
                self._send_messages.put(msg)
                break

            if isinstance(msg, DiameterRequest):
                key = msg.header.hop_by_hop.hex()
                self.pending_requests.update({key: msg})
                diameter_conn_logger.debug("Diameter Request have been "\
                                           "put into Pending Request Queue.")
    
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
                        diameter_conn_logger.debug("Transport Layer is back "\
                                                   "in WRITE mode, so we can "\
                                                   "send data stream.")
    
                        self.transport._set_selector_events_mask("rw", stream)
                        break

        self.lock.release()


    def get_request(self):
        while not self._stop_threads:
            self.postprocess_recv_requests_ready.wait()
    
            while not self.postprocess_recv_requests.empty():
                self.postprocess_recv_requests_ready.clear()
                self.postprocess_recv_requests_lock.release()

                return self.postprocess_recv_requests.get()
        return None


    def get_answer_from_request(self, msg):
        end_to_end_key = msg.header.end_to_end.hex()
        hop_by_hop_key = msg.header.hop_by_hop.hex()

        while not self._stop_threads:
            self.postprocess_recv_answers_ready.wait()
            self.postprocess_recv_answers_lock.acquire()
            self.postprocess_recv_answers_ready.clear()

            if hop_by_hop_key in self.postprocess_recv_answers:
                answer = self.postprocess_recv_answers.pop(hop_by_hop_key, None)
                self.end_to_end_identifiers.remove(end_to_end_key)
                self.postprocess_recv_answers_lock.release()
                return answer


    def tracking_events(self):
        try:
            if (not self.transport.events) and (self.transport.tracking_events_count >= self.watchdog_timeout):
                self._association.put_message_into_send_queue(self.base.dwr)
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


    def __init__(self, debug=False, is_logging=False, config=None):
        logging.info(f">> debug: {debug}")
        logging.info(f">> is_logging: {is_logging}")
        logging.info(f">> config: {config}")
        
        self.__logging = DiameterLogging(debug, is_logging)
        self.config = self.make_config(config)

        self._association = None
        self._peer_state_machine = None


    def make_config(self, config):
        if config:
            return self.config_class(config)
        return self.config_class(Diameter.default_config)


    def get_base_messages(self, msgs=None):
        proxy = DiameterBaseProxy(self._connection)
        if msgs:
            return proxy.get_custom_messages(msgs)
        else:
            return proxy.get_default_messages()


    def get_current_state(self):
        if self._peer_state_machine:
            return self._peer_state_machine.get_current_state()
        return CLOSED


    def start(self):
        current_state = self.get_current_state()

        if current_state != CLOSED:
            raise DiameterApplicationError("Cannot start the application. "\
                                           "Peer State Machine is already "\
                                           "running")

        self._connection = _convert_config_to_connection_obj(self.config)
        self._base = self.get_base_messages()

        self._association = DiameterAssociation(self._connection, self._base)
        self._peer_state_machine = PeerStateMachine(self._association)

        self._peer_state_machine.start()
        self._association.start()


    def reset(self):
        current_state = self.get_current_state()

        if current_state == CLOSED:
            raise DiameterApplicationError("Cannot reset the application. "\
                                           "Peer State Machine is already "\
                                           "closed")

        self.close()
        time.sleep(SLEEP_TIMER)
        self.start()


    def close(self):
        current_state = self.get_current_state()
        
        if current_state == CLOSED:
            raise DiameterApplicationError("Cannot stop the application. "\
                                           "Peer State Machine is already "\
                                           "closed")

        self._peer_state_machine.close()


    def send_messages(self, msgs):
        for msg in msgs:
            self._association.put_message_into_send_queue(msg)


    def send_message(self, msg, avoid=True):    
        if isinstance(msg, DiameterRequest):
            diameter_logger.debug(f"External app wants to send a Diameter "\
                                  f"Request Message: {msg}")

            if is_base_request(msg):
                raise DiameterApplicationError("Cannot send a Base protocol "\
                                               "request")

            self._association.put_message_into_send_queue(msg)
            if not avoid:
                return self._association.get_answer_from_request(msg)

        elif isinstance(msg, DiameterAnswer):
            diameter_logger.debug(f"External app wants to send a Diameter "\
                                  f"Answer Message: {msg}")

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


    def get_message(self):
        return self._association.get_request()


    @contextmanager
    def context(self):
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
            sys.exit(0)

        print(f"  * Diameter connection on "\
              f"{self.config['LOCAL_NODE_IP_ADDRESS']}:"\
              f"{self.config['LOCAL_NODE_PORT']} is now down")


    def is_open(self):
        try:
            if self.get_current_state() == I_OPEN or \
               self.get_current_state() == R_OPEN:
                return True
            return False
        except TypeError:
            if "'NoneType' object is not subscriptable":
                return False


    def is_closed(self):
        try:
            if self.get_current_state() == CLOSED:
                return True
            return False
        except TypeError:
            if "'NoneType' object is not subscriptable":
                return False
