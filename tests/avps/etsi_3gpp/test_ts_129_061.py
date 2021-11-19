# -*- coding: utf-8 -*-
"""
    tests.avps.etsi_3gpp.test_ts_129_061
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for ETSI TS 129 061.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(testing_dir))

sys.path.insert(0, base_dir)

from bromelia.avps.etsi_3gpp.ts_129_061 import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_3gpp_charging_characteristics_avp_stream(self):
        stream = bytes.fromhex("0000000d80000010000028af30423030")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], X3gppChargingCharacteristicsAVP))
        self.assertEqual(avps[0].code, X_3GPP_CHARGING_CHARACTERISTICS_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "30423030")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 13 [X3gpp-Charging-Characteristics] VENDOR>")


class TestX3gppChargingCharacteristicsAVP(unittest.TestCase):
    def test__3gpp_charging_characteristics_avp__no_value(self):
        self.assertRaises(TypeError, X3gppChargingCharacteristicsAVP)

    def test__3gpp_charging_characteristics_avp__repr_dunder(self):
        value = bytes.fromhex("30343030")                #: 0400
        avp = X3gppChargingCharacteristicsAVP(value)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 13 [X3gpp-Charging-Characteristics] VENDOR>")

    def test__3gpp_charging_characteristics_avp__1(self):
        value = bytes.fromhex("30343030")                #: 0400
        avp = X3gppChargingCharacteristicsAVP(value)
        ref = "0000000d80000010000028af30343030"
        self.assertEqual(avp.dump().hex(), ref)

    def test__3gpp_charging_characteristics_avp__2(self):
        value = bytes.fromhex("30323030")                #: 0200
        avp = X3gppChargingCharacteristicsAVP(value)
        ref = "0000000d80000010000028af30323030"
        self.assertEqual(avp.dump().hex(), ref)

    def test__3gpp_charging_characteristics_avp__3(self):
        value = bytes.fromhex("30353030")                #: 0500
        avp = X3gppChargingCharacteristicsAVP(value)
        ref = "0000000d80000010000028af30353030"
        self.assertEqual(avp.dump().hex(), ref)

    def test__3gpp_charging_characteristics_avp__4(self):
        value = bytes.fromhex("30383030")                #: 0800
        avp = X3gppChargingCharacteristicsAVP(value)
        ref = "0000000d80000010000028af30383030"
        self.assertEqual(avp.dump().hex(), ref)

    def test__3gpp_charging_characteristics_avp__5(self):
        value = bytes.fromhex("30413030")                #: 0A00
        avp = X3gppChargingCharacteristicsAVP(value)
        ref = "0000000d80000010000028af30413030"
        self.assertEqual(avp.dump().hex(), ref)

    def test__3gpp_charging_characteristics_avp__6(self):
        value = bytes.fromhex("30423030")                #: 0B00
        avp = X3gppChargingCharacteristicsAVP(value)
        ref = "0000000d80000010000028af30423030"
        self.assertEqual(avp.dump().hex(), ref)

    def test__3gpp_charging_characteristics_avp__7(self):
        value = bytes.fromhex("30453030")                #: 0E00
        avp = X3gppChargingCharacteristicsAVP(value)
        ref = "0000000d80000010000028af30453030"
        self.assertEqual(avp.dump().hex(), ref)


if __name__ == "__main__":
    unittest.main()