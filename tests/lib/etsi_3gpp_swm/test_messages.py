# -*- coding: utf-8 -*-
"""
    tests.etsi_3gpp_swm.test_messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages unittests 
	for 3GPP SWm Diameter Application Id.
    
    :copyright: (c) 2020 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import sys

base_dir = "/Users/henriquemr/Public/SWE/diameter_bromelia/bromelia"
sys.path.insert(0, base_dir)

from bromelia.lib.etsi_3gpp_swm import *
from bromelia.constants import *


class TestCreateMessageDER(unittest.TestCase):
    def test_first_der(self):
        nai = "0123456789012345@nai.epc.mncXXX.mccYYY.3gppnetwork.org"
        content = {"nai": nai, "payload": None}
        eap_payload = EapPayload(eap_code=EAP_CODE_RESPONSE, eap_id=0, eap_type=EAP_TYPE_IDENTITY, content=content)

        custom_avps = {
            "auth_application_id": DIAMETER_APPLICATION_SWm,
            "origin_host": "es2",
            "origin_realm": "cdpesm",
            "destination_realm": "epc.mncXXX.mccYYY.3gppnetwork.org",
            "auth_request_type": AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY,
            "eap_payload": eap_payload,
            "user_name": nai,
            "rat_type": RAT_TYPE_WLAN,
            "auth_session_state": AuthSessionStateAVP(NO_STATE_MAINTAINED)
        }

        msg = DER(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "c0")
        self.assertEqual(msg.header.command_code.hex(), "00010c")
        self.assertEqual(msg.header.application_id.hex(), "01000030")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001024000000c01000030")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001084000000b65733200")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001284000000e63647065736d0000")

        #: Destination-Realm AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000011b400000296570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Auth-Request-Type AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001124000000c00000001")

        #: Eap-Payload AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001ce400000430200003b0130313233343536373839303132333435406e61692e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f726700")

        #: User-Name AVP
        self.assertEqual(msg.avps[7].dump().hex(), "000000014000003e30313233343536373839303132333435406e61692e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000")

        #: Rat-Type AVP
        self.assertEqual(msg.avps[8].dump().hex(), "00000408c0000010000028af00000000")

        #: Auth-Session-State AVP
        self.assertEqual(msg.avps[9].dump().hex(), "000001154000000c00000001")

    def test_second_der(self):
        nai = "0123456789012345@nai.epc.mncXXX.mccYYY.3gppnetwork.org"
        content = {"nai": nai, "payload": "AgEAKBcBAAADAwBAdIpRhyWC5BULBQAAO/fAVBRslCJ9/wQlm3yokg=="}
        eap_payload = EapPayload(eap_code=EAP_CODE_RESPONSE, eap_id=1, eap_type=EAP_TYPE_UMTS_AUTHENTICATION_AND_KEY_AGREEMENT_EAP, content=content)

        custom_avps = {
            "auth_application_id": DIAMETER_APPLICATION_SWm,
            "origin_host": "es2",
            "origin_realm": "cdpesm",
            "destination_realm": "epc.mncXXX.mccYYY.3gppnetwork.org",
            "auth_request_type": AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY,
            "eap_payload": eap_payload,
            "user_name": nai,
            "rat_type": RAT_TYPE_WLAN,
            "auth_session_state": AuthSessionStateAVP(NO_STATE_MAINTAINED)
        }

        msg = DER(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "c0")
        self.assertEqual(msg.header.command_code.hex(), "00010c")
        self.assertEqual(msg.header.application_id.hex(), "01000030")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001024000000c01000030")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001084000000b65733200")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001284000000e63647065736d0000")

        #: Destination-Realm AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000011b400000296570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Auth-Request-Type AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001124000000c00000001")

        #: Eap-Payload AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001ce40000030020100281701000003030040748a51872582e4150b0500003bf7c054146c94227dff04259b7ca892")

        #: User-Name AVP
        self.assertEqual(msg.avps[7].dump().hex(), "000000014000003e30313233343536373839303132333435406e61692e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000")

        #: Rat-Type AVP
        self.assertEqual(msg.avps[8].dump().hex(), "00000408c0000010000028af00000000")

        #: Auth-Session-State AVP
        self.assertEqual(msg.avps[9].dump().hex(), "000001154000000c00000001")


class TestCreateMessageASR(unittest.TestCase):
    def test_asr__1(self):
        custom_avps = {
            "destination_host": "aaa0",
            "destination_realm": "remote",
            "user_name": "frodo",
        }

        msg = ASR(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "c0")
        self.assertEqual(msg.header.command_code.hex(), "000112")
        self.assertEqual(msg.header.application_id.hex(), "01000030")

        #: Destination-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000011b4000000e72656d6f74650000")

        #: Destination-Host AVP
        self.assertEqual(msg.avps[4].dump().hex(), "000001254000000c61616130")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001024000000c01000030")

        #: User-Name AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000000014000000d66726f646f000000")

        #: Auth-Session-State AVP
        self.assertEqual(msg.avps[7].dump().hex(), "000001154000000c00000001")

    def test_asr__2(self):
        custom_avps = {
            "origin_host": "hss0",
            "origin_realm": "local",
            "destination_host": "aaa0",
            "destination_realm": "remote",
            "auth_session_state": DIAMETER_APPLICATION_SWm,
            "user_name": "frodo",
            "auth_session_state": NO_STATE_MAINTAINED,
        }

        msg = ASR(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "c0")
        self.assertEqual(msg.header.command_code.hex(), "000112")
        self.assertEqual(msg.header.application_id.hex(), "01000030")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001084000000c68737330")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000d6c6f63616c000000")

        #: Destination-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000011b4000000e72656d6f74650000")

        #: Destination-Host AVP
        self.assertEqual(msg.avps[4].dump().hex(), "000001254000000c61616130")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001024000000c01000030")

        #: User-Name AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000000014000000d66726f646f000000")

        #: Auth-Session-State AVP
        self.assertEqual(msg.avps[7].dump().hex(), "000001154000000c00000001")


class TestCreateMessageASA(unittest.TestCase):
    def test_asa__1(self):
        msg = ASA()

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "40")
        self.assertEqual(msg.header.command_code.hex(), "000112")
        self.assertEqual(msg.header.application_id.hex(), "01000030")

        #: Result-Code AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010c4000000c000007d1")

    def test_asa__2(self):
        custom_avps = {
            "origin_host": "hss0",
            "origin_realm": "local",
        }

        msg = ASA(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "40")
        self.assertEqual(msg.header.command_code.hex(), "000112")
        self.assertEqual(msg.header.application_id.hex(), "01000030")

        #: Result-Code AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010c4000000c000007d1")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001084000000c68737330")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001284000000d6c6f63616c000000")


if __name__ == "__main__":
    unittest.main()