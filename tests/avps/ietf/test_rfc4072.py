# -*- coding: utf-8 -*-
"""
    tests.avps.ietf.test_rfc4072
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for IETF RFC 4072.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.avps.ietf.rfc4072 import *
from bromelia.etsi_3gpp_swm.definitions import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_eap_payload_avp_stream(self):
        stream = bytes.fromhex("000001ce4000003a02000032016d792d75736572406e61692e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], EapPayloadAVP))
        self.assertEqual(avps[0].code, EAP_PAYLOAD_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 58)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"\x02\x00\x002\x01my-user@nai.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 462 [Eap-Payload] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_eap_master_session_key_avp_stream(self):
        stream = bytes.fromhex("000001d000000048ec3208c43154f60862858afa650dd875e8a095dfcd364e73420fcc573388d4c207308ace020aa3e3f9ff76ed1821a044e8deed2470997fbfbf5197d724d51fa1")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], EapMasterSessionKeyAVP))
        self.assertEqual(avps[0].code, EAP_MASTER_SESSION_KEY_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 72)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data.hex(), "ec3208c43154f60862858afa650dd875e8a095dfcd364e73420fcc573388d4c207308ace020aa3e3f9ff76ed1821a044e8deed2470997fbfbf5197d724d51fa1")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 464 [Eap-Master-Session-Key]>")


class TestEapPayloadAVP(unittest.TestCase):
    def setUp(self):
        self.nai = "my-user@nai.epc.mncXXX.mccYYY.3gppnetwork.org"

    def test_eap_payload_avp__no_value(self):
        self.assertRaises(TypeError, EapPayload)

    def test_eap_payload_avp__repr_dunder(self):
        content = {"nai": self.nai, "payload": None}
        eap_payload = EapPayload(eap_code=EAP_CODE_RESPONSE, eap_id=0, eap_type=EAP_TYPE_IDENTITY, content=content)

        avp = EapPayloadAVP(eap_payload)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 462 [Eap-Payload] MANDATORY>")

    def test_eap_payload_avp__diameter_avp_convert_classmethod(self):
        content = {"nai": self.nai, "payload": None}
        eap_payload = EapPayload(eap_code=EAP_CODE_RESPONSE, eap_id=0, eap_type=EAP_TYPE_IDENTITY, content=content)

        avp = EapPayloadAVP(eap_payload)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_eap_payload_avp__eap_type_identity(self):
        content = {"nai": self.nai, "payload": None}
        eap_payload = EapPayload(eap_code=EAP_CODE_RESPONSE, eap_id=0, eap_type=EAP_TYPE_IDENTITY, content=content)

        avp = EapPayloadAVP(eap_payload)
        ref = "000001ce4000003a02000032016d792d75736572406e61692e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_eap_payload_avp__ea_type_umts_authentication_and_key_agreement_eap(self):
        content = {"nai": self.nai, "payload": "AgEAKBcBAAADAwBAtRAM4pAWdZkLBQAANb\/0OV77760sUjmpBDihxA=="}
        eap_payload = EapPayload(eap_code=EAP_CODE_RESPONSE, eap_id=1, eap_type=EAP_TYPE_UMTS_AUTHENTICATION_AND_KEY_AGREEMENT_EAP, content=content)

        avp = EapPayloadAVP(eap_payload)
        ref = "000001ce40000030020100281701000003030040b5100ce2901675990b05000035bff4395efbefad2c5239a90438a1c4"
        self.assertEqual(avp.dump().hex(), ref)


class TestEapMasterSessionKeyAVP(unittest.TestCase):
    def setUp(self):
        self.EAP_MASTER_SESSION_KEY = bytes.fromhex("ec3208c43154f60862858afa650dd875e8a095dfcd364e73420fcc573388d4c207308ace020aa3e3f9ff76ed1821a044e8deed2470997fbfbf5197d724d51fa1")

    def test_eap_master_session_key_avp__no_value(self):
        self.assertRaises(TypeError, EapMasterSessionKeyAVP)

    def test_eap_master_session_key_avp__repr_dunder(self):
        avp = EapMasterSessionKeyAVP(self.EAP_MASTER_SESSION_KEY)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 464 [Eap-Master-Session-Key]>")

    def test_eap_master_session_key_avp__diameter_avp_convert_classmethod(self):
        avp = EapMasterSessionKeyAVP(self.EAP_MASTER_SESSION_KEY)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_eap_master_session_key_avp__1(self):
        avp = EapMasterSessionKeyAVP(self.EAP_MASTER_SESSION_KEY)
        ref = "000001d000000048ec3208c43154f60862858afa650dd875e8a095dfcd364e73420fcc573388d4c207308ace020aa3e3f9ff76ed1821a044e8deed2470997fbfbf5197d724d51fa1"
        self.assertEqual(avp.dump().hex(), ref)


if __name__ == "__main__":
    unittest.main()