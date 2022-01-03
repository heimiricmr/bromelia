# -*- coding: utf-8 -*-
"""
    bromelia.statemachine
    ~~~~~~~~~~~~~~~~~~~~~

    This module contains the finite state machine defined in Section 5.6 of
    IETF RFC 6733.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import logging
import threading
import time

from typing import Any, Literal, Type

from ._internal_utils import application_id_look_up
from .base import DiameterMessage
from .config import *
from .process import BaseMessageProcessor
from .utils import is_client_mode
from .utils import is_server_mode
from .utils import is_dwa_message as has_recv_dwa
from .utils import is_dwr_message as has_recv_dwr
from .utils import is_dpa_message as has_recv_dpa
from .utils import is_dpr_message as has_recv_dpr
from .utils import is_cea_message as has_recv_cea
from .utils import is_cer_message as has_recv_cer


""" 
    @ `state` column:
    -> It relies on state classes that SHOULD BE implemented.

    -> State classes have the `run` method and another methods with the 
    `event_` prefixed.
    
    -> `run` method in the entrypoint tracking diameter_connection object. 
    Depeding on the object's state, it triggers its `event_` prefixed methods 
    in order to execute a series of actions.


    @ `event` column:
    -> It relies on state classes methods which begins with `event_` preffix. 
    Each method is triggered by the `run` method whenever the 
    diameter_connection object state changes. Inside the methods a series 
    of actions is implemented.


    @ `action` column:
    -> It relies on actions that SHOULD be taken when a given `event_` prefixed 
    method is called by `run` method. The last step of the actions is define 
    the next state by calling a self.next_state with the updated value.


    @ `next state` column:
    -> It represents the self.next_state value for each state class depending 
    on the event/actions triggered (which in turn depends on 
    diameter_connection object state). The State Machine needs to implement a 
    central attribute which tracks all possible states plus a 
    `get_next_state()` method to get the next state object.
"""

closed_logger = logging.getLogger("Closed")
wait_conn_ack_logger = logging.getLogger("WaitConnAck")
wait_initiator_cea_logger = logging.getLogger("WaitInitiatorCEA")
open_logger = logging.getLogger("Open")
wait_returns_logger = logging.getLogger("WaitReturns")
wait_conn_ack_elect_logger = logging.getLogger("WaitConnAckElect")
closing_logger = logging.getLogger("Closing")

statemachine_logger = logging.getLogger("PeerStateMachine")


def make_logging(msg):
    if msg.has_avp("user_name"):
        open_logger.debug(f"Message from _recv_messages: "\
                            f"{application_id_look_up(msg.header.application_id)[0]}, "\
                            f"{msg.header.get_command_code()}, "\
                            f"{msg.header.is_request()}, "\
                            f"{msg.header.hop_by_hop.hex()}, "\
                            f"LEN: {len(msg)}, "\
                            f"USERNAME: {msg.user_name_avp.data}")
    else:
        open_logger.debug(f"Message from _recv_messages: "\
                            f"{application_id_look_up(msg.header.application_id)[0]}, "\
                            f"{msg.header.get_command_code()}, "\
                            f"{msg.header.is_request()}, "\
                            f"{msg.header.hop_by_hop.hex()}, "\
                            f"LEN: {len(msg)}")


class State():
    def __init__(self, diameter_association) -> None:
        self.association = diameter_association
        self.processor = BaseMessageProcessor(diameter_association)


    def run(self) -> None:
        assert(0, "Function not implemented.")


    def next(self) -> None:
        assert(0, "Function not implemented.")


    def send_message(self, msg: Type[DiameterMessage] = None) -> None:
        if msg is not None:
            self.association.put_message_into_send_queue(msg)
        self.association.send_message_from_queue()


    def get_message(self):
        self.association.lock.acquire()
        msg = self.association._recv_messages.get()
        self.association.lock.release()
        return msg


    def notify_postprocess_message(self, msg: Type[DiameterMessage]) -> None:
        self.association.postprocess_recv_messages_lock.acquire()
        self.association.postprocess_recv_messages.put(msg)
        self.association.postprocess_recv_messages_lock.release()

        self.association.postprocess_recv_messages_ready.set()


    def make_default_logging(self, queue: Literal["send", "recv"] = "recv"):
        message = f"Got message from _{queue}_messages Queue. Now there "\
                  f"is/are {self.association._recv_messages.qsize()} "\
                  f"Diameter Message(s)."
        
        if isinstance(self, Closed):
            closed_logger.debug(message)

        elif isinstance(self, WaitConnAck):
            wait_conn_ack_logger.debug(message)

        elif isinstance(self, WaitInitiatorCEA):
            wait_initiator_cea_logger.debug(message)

        elif isinstance(self, Open):
            open_logger.debug(message)

        elif isinstance(self, WaitReturns):
            wait_returns_logger.debug(message)

        elif isinstance(self, WaitConnAckElect):
            wait_conn_ack_elect_logger.debug(message)


    def has_recv_queue_message(self):
        return not self.association._recv_messages.empty()


    def has_send_queue_message(self):
        return not self.association._send_messages.empty()


    def set_closed_state(self, set_name: bool = False, force: bool = False) -> None:
        if force:
            time.sleep(SLEEP_TIMER)

            self.association._stop_threads = True
            self.association.postprocess_recv_messages_ready.set()

        if set_name:
            self.name = self.next_state = CLOSED
        self.next_state = CLOSED


    def set_wait_conn_ack_state(self, set_name: bool = False) -> None:
        if set_name:
            self.name = self.next_state = WAIT_CONN_ACK
        self.next_state = WAIT_CONN_ACK


    def set_wait_initiator_cea_state(self, set_name: bool = False) -> None:
        if set_name:
            self.name = self.next_state = WAIT_I_CEA
        self.next_state = WAIT_I_CEA


    def set_open_state(self, set_name: bool = False, early_stage: bool = False) -> None:
        if early_stage:
            self.association.state_is_active = True

        if set_name:
            self.name = self.next_state = OPEN
        self.next_state = OPEN


    def set_wait_returns_state(self, set_name: bool = False, early_stage: bool = False) -> None:
        if early_stage:
            self.association.state_is_active = True

        if set_name:
            self.name = self.next_state = WAIT_RETURNS
        self.next_state = WAIT_RETURNS


    def set_wait_conn_ack_elect_state(self, set_name: bool = False, early_stage: bool = False) -> None:
        if early_stage:
            self.association.state_is_active = True

        if set_name:
            self.name = self.next_state = WAIT_CONN_ACK_ELECT
        self.next_state = WAIT_CONN_ACK_ELECT


    def set_closing_state(self, set_name: bool = False) -> None:
        if set_name:
            self.name = self.next_state = CLOSING
        self.next_state = CLOSING


    def is_set_release_signal_from_local(self):
        return not self.association.state_is_active


    def is_set_release_signal_from_peer(self):
        return self.association.transport._stop_threads


class Closed(State):
    def run(self) -> None:
        self.set_closed_state(set_name=True)

        if is_client_mode(self.association):
            self.event_start()
        
        elif is_server_mode(self.association):
            if self.has_recv_queue_message():
                self.msg = self.get_message()

                self.make_default_logging()

                if has_recv_cer(self.msg):
                    self.event_responder_conn_cer()


    def event_start(self) -> None:
        closed_logger.debug("Event has been triggered.")

        self.set_wait_conn_ack_state()


    def event_responder_conn_cer(self) -> None:
        closed_logger.debug("Event has been triggered.")

        if self.processor.is_valid_capability_exchange(msg=self.msg):
            cea = self.processor.create_answer(msg=self.msg)
            self.send_message(msg=cea)
            self.set_open_state(early_stage=True)


class WaitConnAck(State):
    def run(self) -> None:
        self.set_wait_conn_ack_state(set_name=True)

        if self.association.is_connected():
            if self.association.transport.test_connection():
                self.event_initiator_rcv_conn_ack()  
            else:
                self.event_initiator_rcv_conn_nack()

        if self.has_recv_queue_message():
            self.msg = self.get_message()

            self.make_default_logging()

            if has_recv_cer(self.msg):
                self.event_responder_conn_cer()            


    def event_initiator_rcv_conn_ack(self) -> None:
        wait_conn_ack_logger.debug("Event has been triggered.")

        self.send_message(msg=self.association.base.cer)
        self.set_wait_initiator_cea_state()


    def event_initiator_rcv_conn_nack(self) -> None:
        wait_conn_ack_logger.debug("Event has been triggered.")

        self.set_closed_state()


    def event_responder_conn_cer(self) -> None:
        wait_conn_ack_logger.debug("Event has been triggered.")

        if self.processor.is_valid_capability_exchange(msg=self.msg):
            self.set_wait_conn_ack_elect_state(early_stage=True)


    def event_timeout(self) -> None:
        """ It needs to be coded """
        wait_conn_ack_logger.debug("Event has been triggered.")

        self.set_closed_state()


class WaitInitiatorCEA(State):
    def run(self) -> None:
        self.set_wait_initiator_cea_state(set_name=True)

        if self.has_recv_queue_message():
            self.msg = self.get_message()

            self.make_default_logging()

            if has_recv_cea(self.msg):
                self.event_open_rcv_cea()            

            elif has_recv_cer(self.msg):
                self.event_responder_conn_cer()

            else:
                self.event_initiator_rcv_non_cea()


    def event_open_rcv_cea(self) -> None:
        wait_initiator_cea_logger.debug("Event has been triggered.")

        if self.processor.is_valid_capability_exchange(msg=self.msg):
            self.set_open_state(early_stage=True)


    def event_responder_conn_cer(self) -> None:
        wait_initiator_cea_logger.debug("Event has been triggered.")

        if self.processor.is_valid_capability_exchange(msg=self.msg):
            self.set_wait_returns_state(early_stage=True)


    def event_initiator_peer_disc(self) -> None:
        """ It needs to be coded """
        wait_initiator_cea_logger.debug("Event has been triggered.")

        self.set_closed_state()

    
    def event_initiator_rcv_non_cea(self) -> None:
        wait_initiator_cea_logger.debug("Event has been triggered.")

        self.set_closed_state()


    def event_timeout(self) -> None:
        """ It needs to be coded """
        wait_initiator_cea_logger.debug("Event has been triggered.")

        self.set_closed_state()


class Open(State):
    def run(self) -> None:
        self.set_open_state(set_name=True)

        self.association.tracking_events()

        if self.is_set_release_signal_from_peer():
            self.event_open_peer_disc()      

        if self.is_set_release_signal_from_local():
            self.event_stop()

        if self.has_send_queue_message():
            self.make_default_logging(queue="send")

            self.event_send_message()

        elif self.has_recv_queue_message():
            self.msg = self.get_message()

            self.make_default_logging()

            if has_recv_dwr(self.msg):
                self.event_open_rcv_dwr()
            
            elif has_recv_dwa(self.msg):
                self.event_open_rcv_dwa()

            elif has_recv_dpr(self.msg):
                self.event_open_rcv_dpr()
           
            elif has_recv_cer(self.msg):
                self.event_open_rcv_cer()

            elif has_recv_cea(self.msg):
                self.event_open_rcv_cea()

            else:
                self.event_open_rcv_message()
            
            self.msg = None


    def event_send_message(self) -> None:
        open_logger.debug("Event has been triggered.")

        self.send_message()
        self.set_open_state()


    def event_open_rcv_message(self) -> None:
        open_logger.debug("Event has been triggered.")

        self.processor.check_message(self.msg)

        make_logging(self.msg)

        open_logger.debug("Putting into postprocess_recv_messages Queue")
        self.notify_postprocess_message(self.msg)

        open_logger.debug("Just notified postprocess_recv_messages_ready")
        self.set_open_state()


    def event_open_rcv_dwr(self) -> None:
        open_logger.debug("Event has been triggered.")

        if self.processor.is_valid_device_watchdog(msg=self.msg):
            dwa = self.processor.create_answer(msg=self.msg)
            self.send_message(msg=dwa)
            self.set_open_state()

    
    def event_open_rcv_dwa(self) -> None:
        open_logger.debug("Event has been triggered.")

        if self.processor.is_valid_device_watchdog(msg=self.msg):
            self.set_open_state()
        else:
            self.set_closing_state()

    
    def event_responder_conn_cer(self) -> None:
        open_logger.debug("Event has been triggered.")

        self.set_open_state()


    def event_stop(self) -> None:
        open_logger.debug("Event has been triggered.")

        self.send_message(msg=self.association.base.dpr)
        self.set_closing_state()


    def event_open_rcv_dpr(self) -> None:
        open_logger.debug("Event has been triggered.")

        if self.processor.is_valid_disconnect_peer(msg=self.msg):
            dpa = self.processor.create_answer(msg=self.msg)
            self.send_message(msg=dpa)

        self.set_closed_state(force=True)


    def event_open_peer_disc(self) -> None:
        open_logger.debug("Event has been triggered.")

        self.set_closed_state()


    def event_open_rcv_cer(self) -> None:
        open_logger.debug("Event has been triggered.")

        if self.processor.is_valid_capability_exchange(msg=self.msg):
            cea = self.processor.create_answer(msg=self.msg)
            self.send_message(msg=cea)

        self.set_open_state()


    def event_open_rcv_cea(self) -> None:
        open_logger.debug("Event has been triggered.")

        if self.processor.is_valid_capability_exchange(msg=self.msg):
            self.set_open_state()


class WaitReturns(State):
    def run(self) -> None:
        self.set_wait_returns_state(set_name=True)
    

class WaitConnAckElect(State):
    def run(self) -> None:
        self.set_wait_conn_ack_elect_state(set_name=True)


class Closing(State):
    def run(self) -> None:
        self.set_closing_state(set_name=True)

        if self.has_recv_queue_message():
            self.msg = self.get_message()

            self.make_default_logging()

            if has_recv_dpa(self.msg):
                self.event_rcv_dpa()


    def event_rcv_dpa(self) -> None:
        open_logger.debug("Event has been triggered.")

        self.set_closed_state(force=True)


class PeerStateMachine():
    def __init__(self, diameter_association) -> None:
        statemachine_logger.debug("PeerStateMachine has been called.")
        self.association = diameter_association
        self._load_states()


    def _load_states(self) -> None:
        statemachine_logger.debug("Loading available states.")
        self.states = {
                        CLOSED: Closed(self.association),
                        WAIT_CONN_ACK: WaitConnAck(self.association),
                        WAIT_I_CEA: WaitInitiatorCEA(self.association),
                        OPEN: Open(self.association),
                        WAIT_RETURNS: WaitReturns(self.association),
                        WAIT_CONN_ACK_ELECT: WaitConnAckElect(self.association),
                        CLOSING: Closing(self.association),
        }

        self.current_state = self.states[CLOSED]
        self.is_running = False


    def get_next_state(self, next_state: str) -> Any:
        if next_state == CLOSED and self.current_state.name == CLOSED:
            return self.states[CLOSED]

        elif next_state == CLOSED and self.current_state.name != CLOSED:
            self.is_running = False
            self.association.close()

        if next_state in self.states:
            if self.current_state.name != next_state:
                statemachine_logger.info(f"Changing from "\
                                         f"{self.current_state.name.upper()} "\
                                         f"to {next_state.upper()} state.")

            return self.states[next_state]

        else:
            raise TypeError("Input not supported for current state.")        


    def start(self) -> None:
        statemachine_logger.debug("Starting PeerStateMachine's thread.")

        threading.Thread(name=f"{self.association.connection.mode.lower()}_psm_thread", 
                         target=self.__start).start()


    def __start(self) -> None:
        if not self.is_running:
            self.is_running = True

        while (self.is_running and not self.association.error_has_raised):
            time.sleep(STATE_MACHINE_TICKER)

            self.current_state.run()
            _state = self.current_state.next_state
            self.current_state = self.get_next_state(_state)


    def close(self) -> None:
        statemachine_logger.debug("Closing PeerStateMachine's thread.")
        self.association.state_is_active = False


    def get_current_state(self) -> str:
        if isinstance(self.current_state, Closed):
            return CLOSED
        elif isinstance(self.current_state, WaitConnAck):
            return WAIT_CONN_ACK
        elif isinstance(self.current_state, WaitInitiatorCEA):
            return WAIT_I_CEA
        elif isinstance(self.current_state, WaitConnAckElect):
            return WAIT_CONN_ACK_ELECT
        elif isinstance(self.current_state, WaitReturns):
            return WAIT_RETURNS
        elif isinstance(self.current_state, Open):
            if is_client_mode(self.association):
                return I_OPEN
            elif is_server_mode(self.association):
                return R_OPEN
        elif isinstance(self.current_state, Closing):
            return CLOSING