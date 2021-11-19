# -*- coding: utf-8 -*-
"""
    tests.etsi_3gpp_swx.test_messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages unittests 
	for 3GPP SWx Diameter Application Id.
    
    :copyright: (c) 2020 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import os
import sys
import unittest

base_dir = "/Users/henriquemr/Public/SWE/diameter_bromelia/bromelia"
sys.path.insert(0, base_dir)

from bromelia.avps.etsi_3gpp.ts_129_229 import ReasonInfoAVP
from bromelia.constants import *
from bromelia.lib.etsi_3gpp_swx import *


class TestCreateMessageRTA(unittest.TestCase):
    def test_rta__1(self):
        custom_avps = {
            "origin_host": "hss0",
            "origin_realm": "local",
            "auth_session_state": NO_STATE_MAINTAINED,
            "result_code": DIAMETER_SUCCESS
        }

        msg = RTA(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "40")
        self.assertEqual(msg.header.command_code.hex(), "000130")
        self.assertEqual(msg.header.application_id.hex(), "01000031")

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[1].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000031")

        #: Result-Code AVP
        self.assertEqual(msg.avps[2].dump().hex(), "0000010c4000000c000007d1")

        #: Auth-Session-State AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001154000000c00000001")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[4].dump().hex(), "000001084000000c68737330")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001284000000d6c6f63616c000000")


class TestCreateMessageRTR(unittest.TestCase):
    def test_rtr__1(self):
        deregistration_reason = [
                            ReasonCodeAVP(REASON_CODE_PERMANENT_TERMINATION),
                            ReasonInfoAVP("Subscriber has been removed from NW.")
        ]

        custom_avps = {
            "origin_host": "hss0",
            "origin_realm": "local",
            "destination_host": "aaa0",
            "destination_realm": "remote",
            "user_name": "frodo",
            "auth_session_state": NO_STATE_MAINTAINED,
            "deregistration_reason": deregistration_reason
        }

        msg = RTR(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "c0")
        self.assertEqual(msg.header.command_code.hex(), "000130")
        self.assertEqual(msg.header.application_id.hex(), "01000031")

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[1].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000031")

        #: Auth-Session-State AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001154000000c00000001")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001084000000c68737330")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[4].dump().hex(), "000001284000000d6c6f63616c000000")

        #: Destination-Host AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001254000000c61616130")

        #: Destination-Realm AVP
        self.assertEqual(msg.avps[6].dump().hex(), "0000011b4000000e72656d6f74650000")

        #: User-Name AVP
        self.assertEqual(msg.avps[7].dump().hex(), "000000014000000d66726f646f000000")

        #: Reason-Code AVP
        self.assertEqual(msg.avps[8].dump().hex(), "00000267c000004c000028af00000268c0000010000028af0000000000000269c0000030000028af5375627363726962657220686173206265656e2072656d6f7665642066726f6d204e572e")



if __name__ == "__main__":
    unittest.main()