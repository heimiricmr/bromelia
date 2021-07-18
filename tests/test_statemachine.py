# -*- coding: utf-8 -*-
"""
    test.test_statemachine
    ~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol statemachine unittests.
    
    :copyright: (c) 2020 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.constants import *
from bromelia.statemachine import PeerStateMachine
from bromelia.statemachine import Closed
from bromelia.statemachine import WaitConnAck
from bromelia.statemachine import WaitInitiatorCEA
from bromelia.statemachine import Open
from bromelia.statemachine import WaitReturns
from bromelia.statemachine import WaitConnAckElect
from bromelia.statemachine import Closing
from bromelia.setup import DiameterAssociation


@unittest.SkipTest
class TeststatemachineStates(unittest.TestCase):
    def setUp(self):
        association = DiameterAssociation(production_connection)
        self.peer_state_machine = PeerStateMachine(association)
        
    def test_statemachine_has_all_states(self):
        self.assertIn("closed", self.statemachine.states)
        self.assertIn("wait_conn_ack", self.statemachine.states)
        self.assertIn("wait_initiator_cea", self.statemachine.states)
        self.assertIn("open", self.statemachine.states)
        self.assertIn("wait_returns", self.statemachine.states)
        self.assertIn("wait_conn_ack_elect", self.statemachine.states)
        self.assertIn("closing", self.statemachine.states)

    def test_check_first_current_state(self):
        self.assertIsInstance(self.statemachine.current_state, Closed)

    def test_run_method_from_closed_state(self):
        self.closed = Closed(association)
        self.closed.run()


if __name__ == "__main__":
    unittest.main()