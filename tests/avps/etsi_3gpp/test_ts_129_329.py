# -*- coding: utf-8 -*-
"""
    tests.avps.etsi_3gpp.test_ts_129_329
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for ETSI TS 129 329.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(testing_dir))

sys.path.insert(0, base_dir)

from bromelia.avps.etsi_3gpp.ts_129_329 import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_msisdn_avp_stream(self):
        stream = bytes.fromhex("000002bdc0000013000028af551299032876f200")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], MsisdnAVP))
        self.assertEqual(avps[0].code, MSISDN_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 19)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("551299032876f2"))
        self.assertEqual(avps[0].data, bytes.fromhex(encode_to_tbcd("5521993082672")))
        self.assertEqual(avps[0].get_padding_length(), 1)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 701 [Msisdn] VENDOR, MANDATORY>")


class TestMsisdnAVP(unittest.TestCase):
    def test__msisdn_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = MsisdnAVP()
    
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test__msisdn_avp__repr_dunder(self):
        avp = MsisdnAVP(5521993082672)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 701 [Msisdn] VENDOR, MANDATORY>")

    def test__msisdn_avp__diameter_avp_convert_classmethod(self):
        avp = MsisdnAVP(5521993082672)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

        avp = MsisdnAVP("5521993082672")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__msisdn_avp__1(self):
        ref = "000002bdc0000013000028af551299032876f200"

        avp = MsisdnAVP(5521993082672)
        self.assertEqual(avp.dump().hex(), ref)

        avp = MsisdnAVP("5521993082672")
        self.assertEqual(avp.dump().hex(), ref)

    def test__msisdn_avp__2(self):
        ref = "000002bdc0000013000028af559909000000f000"

        avp = MsisdnAVP(5599900000000)
        self.assertEqual(avp.dump().hex(), ref)

        avp = MsisdnAVP("5599900000000")
        self.assertEqual(avp.dump().hex(), ref)


if __name__ == "__main__":
    unittest.main()