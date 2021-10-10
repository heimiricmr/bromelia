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

from ._internal_utils import application_id_look_up
from .config import *
from .process import process_answer
from .process import process_capability_exchange
from .process import process_device_watchdog
from .process import process_request
from .utils import is_answer_message
from .utils import is_client_mode
from .utils import is_request_message
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


class State():
    def __init__(self, diameter_association):
        self.association = diameter_association

    def run(self):
        assert(0, "Function not implemented.")

    def next(self):
        assert(0, "Function not implemented.")


class Closed(State):
    def run(self):
        self.next_state = CLOSED
        self.name = self.next_state

        if is_client_mode(self.association):
            self.event_start()
        
        elif is_server_mode(self.association):
            if not self.association._recv_messages.empty():
                self.association.lock.acquire()
                self.msg = self.association._recv_messages.get()
                self.association.lock.release()

                closed_logger.debug(f"Got message from _recv_messages Queue. "\
                                    f"Now there is/are "\
                                    f"{self.association._recv_messages.qsize()} "\
                                    f"Diameter Message(s).")

                if has_recv_cer(self.msg):
                    self.event_responder_conn_cer()


    def event_start(self):
        closed_logger.debug("Event has been triggered.")

        self.next_state = WAIT_CONN_ACK


    def event_responder_conn_cer(self):
        closed_logger.debug("Event has been triggered.")

        cer = self.msg
        process = process_capability_exchange(self.association, cer)

        if process.is_valid:
            cea = self.association.base.cea
            cea.header.hop_by_hop = cer.header.hop_by_hop
            cea.header.end_to_end = cer.header.end_to_end

            self.association.put_message_into_send_queue(cea)
            self.association.send_message_from_queue()

            self.association.state_is_active = True
            self.next_state = OPEN


class WaitConnAck(State):
    def run(self):
        self.next_state = WAIT_CONN_ACK
        self.name = self.next_state

        if self.association.is_connected():
            if self.association.transport.test_connection():
                self.event_initiator_rcv_conn_ack()  
            else:
                self.event_initiator_rcv_conn_nack()

        #: Processing the Diameter messages received.
        if not self.association._recv_messages.empty():
            self.association.lock.acquire()
            self.msg = self.association._recv_messages.get()
            self.association.lock.release()

            wait_initiator_cea_logger.debug(f"Got message from _recv_messages "\
                                            f"Queue. Now there is/are "\
                                            f"{self.association._recv_messages.qsize()} "\
                                            f"Diameter Message(s).")

            if has_recv_cer(self.msg):
                self.event_responder_conn_cer()            


    def event_initiator_rcv_conn_ack(self):
        wait_conn_ack_logger.debug("Event has been triggered.")

        cer = self.association.base.cer
        self.association.put_message_into_send_queue(cer)
        self.association.send_message_from_queue()

        self.next_state = WAIT_I_CEA


    def event_initiator_rcv_conn_nack(self):
        wait_conn_ack_logger.debug("Event has been triggered.")

        self.next_state = CLOSED


    def event_responder_conn_cer(self):
        wait_conn_ack_logger.debug("Event has been triggered.")

        cer = self.msg
        process = process_capability_exchange(self.association, cer)

        if process.is_valid:
            self.association.state_is_active = True
            self.next_state = WAIT_CONN_ACK_ELECT


    def event_timeout(self):
        """ It needs to be coded """
        wait_conn_ack_logger.debug("Event has been triggered.")

        self.next_state = CLOSED


class WaitInitiatorCEA(State):
    def run(self):
        self.next_state = WAIT_I_CEA
        self.name = self.next_state

        #: Processing the Diameter messages received.
        if not self.association._recv_messages.empty():
            self.association.lock.acquire()
            self.msg = self.association._recv_messages.get()
            self.association.lock.release()

            wait_initiator_cea_logger.debug(f"Got message from _recv_messages "\
                                            f"Queue. Now there is/are "
                                            f"{self.association._recv_messages.qsize()} "\
                                            f"Diameter Message(s).")

            if has_recv_cea(self.msg):
                self.event_open_rcv_cea()            

            elif has_recv_cer(self.msg):
                self.event_responder_conn_cer()

            else:
                self.event_initiator_rcv_non_cea()


    def event_open_rcv_cea(self):
        wait_initiator_cea_logger.debug("Event has been triggered.")

        cea = self.msg
        process = process_capability_exchange(self.association, cea)

        if process.is_valid:           
            self.association.state_is_active = True
            self.next_state = OPEN


    def event_responder_conn_cer(self):
        wait_initiator_cea_logger.debug("Event has been triggered.")

        cer = self.msg
        process = process_capability_exchange(self.association, cer)

        if process.is_valid:
            self.association.state_is_active = True
            self.next_state = WAIT_RETURNS


    def event_initiator_peer_disc(self):
        """ It needs to be coded """
        wait_initiator_cea_logger.debug("Event has been triggered.")

        self.next_state = CLOSED

    
    def event_initiator_rcv_non_cea(self):
        wait_initiator_cea_logger.debug("Event has been triggered.")

        self.next_state = CLOSED


    def event_timeout(self):
        """ It needs to be coded """
        wait_initiator_cea_logger.debug("Event has been triggered.")

        self.next_state = CLOSED


class Open(State):
    def run(self):
        self.next_state = OPEN
        self.name = self.next_state

        self.association.tracking_events()

        if self.association.transport._stop_threads:
            self.event_open_peer_disc()      

        if not self.association.state_is_active:
            self.event_stop()

        if not self.association._send_messages.empty():
            open_logger.debug(f"Got message from _send_messages "\
                              f"Queue. Now there is/are "\
                              f"{self.association._send_messages.qsize()} "\
                              f"Diameter Message(s).")

            self.event_send_message()

        #: Processing the Diameter messages received.
        elif not self.association._recv_messages.empty():
            self.association.lock.acquire()
            self.msg = self.association._recv_messages.get()
            self.association.lock.release()

            open_logger.debug(f"Got message from _recv_messages Queue. Now "\
                              f"there is/are "\
                              f"{self.association._recv_messages.qsize()} "\
                              f"Diameter Message(s).")

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


    def event_send_message(self):
        open_logger.debug("Event has been triggered.")

        self.association.send_message_from_queue()

        self.next_state = OPEN


    def event_open_rcv_message(self):
        open_logger.debug("Event has been triggered.")

        if is_answer_message(self.msg):
            process_answer(self.association, self.msg)
            
        elif is_request_message(self.msg):
            process_request(self.association, self.msg)

        if self.msg.has_avp("user_name_avp"):
            open_logger.debug(f"Message from _recv_messages: "\
                              f"{application_id_look_up(self.msg.header.application_id)[0]}, "\
                              f"{self.msg.header.get_command_code()}, "\
                              f"{self.msg.header.is_request()}, "\
                              f"{self.msg.header.hop_by_hop.hex()}, "\
                              f"LEN: {len(self.msg)}, "\
                              f"USERNAME: {self.msg.user_name_avp.data}")
        else:
            open_logger.debug(f"Message from _recv_messages: "\
                              f"{application_id_look_up(self.msg.header.application_id)[0]}, "\
                              f"{self.msg.header.get_command_code()}, "\
                              f"{self.msg.header.is_request()}, "\
                              f"{self.msg.header.hop_by_hop.hex()}, "\
                              f"LEN: {len(self.msg)}")

        open_logger.debug("Putting into postprocess_recv_messages Queue")

        self.association.postprocess_recv_messages_lock.acquire()
        self.association.postprocess_recv_messages.put(self.msg)
        self.association.postprocess_recv_messages_lock.release()

        self.association.postprocess_recv_messages_ready.set()

        open_logger.debug("Just notified postprocess_recv_messages_ready")
    
        self.next_state = OPEN


    def event_open_rcv_dwr(self):
        open_logger.debug("Event has been triggered.")

        dwr = self.msg
        process = process_device_watchdog(self.association, dwr)

        if process.is_valid:
            dwa = self.association.base.dwa
            dwa.header.hop_by_hop = dwr.header.hop_by_hop
            dwa.header.end_to_end = dwr.header.end_to_end

            self.association.put_message_into_send_queue(dwa)
            self.association.send_message_from_queue()

            self.next_state = OPEN

    
    def event_open_rcv_dwa(self):
        open_logger.debug("Event has been triggered.")

        dwa = self.msg
        process = process_device_watchdog(self.association, dwa)

        if process.is_valid:
            self.next_state = OPEN
        else:
            self.next_state = CLOSING

    
    def event_responder_conn_cer(self):
        open_logger.debug("Event has been triggered.")

        self.next_state = OPEN


    def event_stop(self):
        open_logger.debug("Event has been triggered.")

        dpr = self.association.base.dpr
        self.association.put_message_into_send_queue(dpr)
        self.association.send_message_from_queue()

        self.next_state = CLOSING


    def event_open_rcv_dpr(self):
        open_logger.debug("Event has been triggered.")

        dpr = self.msg
        process = process_device_watchdog(self.association, dpr)

        if process.is_valid:
            dpa = self.association.base.dpa
            dpa.header.hop_by_hop = dpr.header.hop_by_hop
            dpa.header.end_to_end = dpr.header.end_to_end

            self.association.put_message_into_send_queue(dpa)
            self.association.send_message_from_queue()

        time.sleep(SLEEP_TIMER)

        self.association._stop_threads = True
        self.association.postprocess_recv_messages_ready.set()

        self.next_state = CLOSED
        

    def event_open_peer_disc(self):
        open_logger.debug("Event has been triggered.")

        self.next_state = CLOSED


    def event_open_rcv_cer(self):
        open_logger.debug("Event has been triggered.")

        cer = self.msg
        process = process_capability_exchange(self.association, cer)

        if process.is_valid:
            cea = self.association.base.cea
            cea.header.hop_by_hop = cer.header.hop_by_hop
            cea.header.end_to_end = cer.header.end_to_end

            self.association.put_message_into_send_queue(cea)
            self.association.send_message_from_queue()

        self.next_state = OPEN


    def event_open_rcv_cea(self):
        open_logger.debug("Event has been triggered.")

        cea = self.msg
        process = process_capability_exchange(self.association, cea)

        if process.is_valid:
            self.next_state = OPEN


class WaitReturns(State):
    def run(self):
        self.next_state = WAIT_RETURNS
        self.name = self.next_state
    

class WaitConnAckElect(State):
    def run(self):
        self.next_state = WAIT_CONN_ACK_ELECT
        self.name = self.next_state


class Closing(State):   
    def run(self):
        self.next_state = CLOSING
        self.name = self.next_state

        if not self.association._recv_messages.empty():
            self.association.lock.acquire()
            self.msg = self.association._recv_messages.get()
            self.association.lock.release()

            if has_recv_dpa(self.msg):
                closing_logger.debug(f"Got DPA message from _recv_messages "\
                                     f"Queue. Now there is/are "\
                                     f"{self.association._recv_messages.qsize()} "\
                                     f"Diameter Message(s).")
                self.event_rcv_dpa()
           
            else:
                closing_logger.debug(f"Got a non-DPA message from "\
                                     f"_recv_messages Queue. Now there is/are "\
                                     f"{self.association._recv_messages.qsize()} "\
                                     f"Diameter Message(s).")


    def event_rcv_dpa(self):
        open_logger.debug("Event has been triggered.")

        self.association.send_message_from_queue()
        self.association._stop_threads = True

        self.next_state = CLOSED


class PeerStateMachine():
    def __init__(self, diameter_association):
        statemachine_logger.debug("PeerStateMachine has been called.")
        self.association = diameter_association
        self._load_states()


    def _load_states(self):
        statemachine_logger.debug("Loading available states.")
        self.__closed = Closed(self.association)
        self.__wait_conn_ack = WaitConnAck(self.association)
        self.__wait_initiator_cea = WaitInitiatorCEA(self.association)
        self.__open = Open(self.association)
        self.__wait_returns = WaitReturns(self.association)
        self.__wait_conn_ack_elect = WaitConnAckElect(self.association)
        self.__closing = Closing(self.association)

        self.states = {
                        CLOSED: self.__closed,
                        WAIT_CONN_ACK: self.__wait_conn_ack,
                        WAIT_I_CEA: self.__wait_initiator_cea,
                        OPEN: self.__open,
                        WAIT_RETURNS: self.__wait_returns,
                        WAIT_CONN_ACK_ELECT: self.__wait_conn_ack_elect,
                        CLOSING: self.__closing,
        }

        self.current_state = self.states[CLOSED]
        self.is_running = False


    def get_next_state(self, next_state):
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


    def start(self):
        statemachine_logger.debug("Starting PeerStateMachine's thread.")

        threading.Thread(name="peer_state_machine_bootstrapper", 
                         target=self.__start).start()


    def __start(self):
        if not self.is_running:
            self.is_running = True

        while (self.is_running and not self.association.error_has_raised):
            time.sleep(STATE_MACHINE_TICKER)

            self.current_state.run()
            _state = self.current_state.next_state
            self.current_state = self.get_next_state(_state)


    def close(self):
        statemachine_logger.debug("Closing PeerStateMachine's thread.")
        self.association.state_is_active = False


    def get_current_state(self):
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