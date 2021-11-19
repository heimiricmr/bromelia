# -*- coding: utf-8 -*-
"""
    tests.avps.ietf.test_rfc4006
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for IETF RFC 4006.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.avps.ietf.rfc4006 import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_subscription_id_data_avp_stream(self):
        stream = bytes.fromhex("000001bc4000001535353131313233343536373839000000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], SubscriptionIdDataAVP))
        self.assertEqual(avps[0].code, SUBSCRIPTION_ID_DATA_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 21)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"5511123456789")
        self.assertEqual(avps[0].get_padding_length(), 3)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 444 [Subscription-Id-Data] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_subscription_id_type_avp_stream(self):
        stream = bytes.fromhex("000001c24000000c00000001")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], SubscriptionIdTypeAVP))
        self.assertEqual(avps[0].code, SUBSCRIPTION_ID_TYPE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, END_USER_IMSI)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 450 [Subscription-Id-Type] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_subscription_id_avp_stream(self):
        stream = bytes.fromhex("000001bb4000002c000001c24000000c00000000000001bc4000001535353636313233343536373839000000")

        avps = DiameterAVP.load(stream)

        subscription_id_avp = avps[0]
        self.assertTrue(isinstance(subscription_id_avp, SubscriptionIdAVP))
        self.assertEqual(subscription_id_avp.code, SUBSCRIPTION_ID_AVP_CODE)
        self.assertFalse(subscription_id_avp.is_vendor_id())
        self.assertTrue(subscription_id_avp.is_mandatory())
        self.assertFalse(subscription_id_avp.is_protected())
        self.assertEqual(subscription_id_avp.get_length(), 44)
        self.assertIsNone(subscription_id_avp.vendor_id)
        self.assertEqual(subscription_id_avp.data.hex(), "000001c24000000c00000000000001bc4000001535353636313233343536373839000000")
        self.assertIsNone(subscription_id_avp.get_padding_length())
        self.assertEqual(subscription_id_avp.__repr__(), "<Diameter AVP: 443 [Subscription-Id] MANDATORY>")

        subscription_id_type_avp = subscription_id_avp.subscription_id_type_avp
        subscription_id_data_avp = subscription_id_avp.subscription_id_data_avp

        self.assertTrue(isinstance(subscription_id_type_avp, SubscriptionIdTypeAVP))
        self.assertEqual(subscription_id_type_avp.code, SUBSCRIPTION_ID_TYPE_AVP_CODE)
        self.assertFalse(subscription_id_type_avp.is_vendor_id())
        self.assertTrue(subscription_id_type_avp.is_mandatory())
        self.assertFalse(subscription_id_type_avp.is_protected())
        self.assertEqual(subscription_id_type_avp.get_length(), 12)
        self.assertIsNone(subscription_id_type_avp.vendor_id)
        self.assertEqual(subscription_id_type_avp.data, END_USER_E164)
        self.assertIsNone(subscription_id_type_avp.get_padding_length())
        self.assertEqual(subscription_id_type_avp.__repr__(), "<Diameter AVP: 450 [Subscription-Id-Type] MANDATORY>")

        self.assertTrue(isinstance(subscription_id_data_avp, SubscriptionIdDataAVP))
        self.assertEqual(subscription_id_data_avp.code, SUBSCRIPTION_ID_DATA_AVP_CODE)
        self.assertFalse(subscription_id_data_avp.is_vendor_id())
        self.assertTrue(subscription_id_data_avp.is_mandatory())
        self.assertFalse(subscription_id_data_avp.is_protected())
        self.assertEqual(subscription_id_data_avp.get_length(), 21)
        self.assertIsNone(subscription_id_data_avp.vendor_id)
        self.assertEqual(subscription_id_data_avp.data, b"5566123456789")
        self.assertEqual(subscription_id_data_avp.get_padding_length(), 3)
        self.assertEqual(subscription_id_data_avp.__repr__(), "<Diameter AVP: 444 [Subscription-Id-Data] MANDATORY>")


class TestSubscriptionIdDataAVP(unittest.TestCase):
    def test_subscription_id_data_avp__no_value(self):
        self.assertRaises(TypeError, SubscriptionIdDataAVP)

    def test_subscription_id_data_avp__repr_dunder(self):
        avp = SubscriptionIdDataAVP("5522123456789")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 444 [Subscription-Id-Data] MANDATORY>")

    def test_subscription_id_data_avp__diameter_avp_convert_classmethod(self):
        avp = SubscriptionIdDataAVP("5511123456789")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_subscription_id_data_avp__1(self):
        avp = SubscriptionIdDataAVP("5511123456789")
        ref = "000001bc4000001535353131313233343536373839000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_subscription_id_data_avp__2(self):
        avp = SubscriptionIdDataAVP("5522123456789")
        ref = "000001bc4000001535353232313233343536373839000000"
        self.assertEqual(avp.dump().hex(), ref)
      

class TestSubscriptionIdTypeAVP(unittest.TestCase):
    def test_subscription_id_type_avp__no_value(self):
        self.assertRaises(TypeError, SubscriptionIdTypeAVP)

    def test_subscription_id_type_avp__repr_dunder(self):
        avp = SubscriptionIdTypeAVP(END_USER_E164)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 450 [Subscription-Id-Type] MANDATORY>")

    def test_subscription_id_type_avp__diameter_avp_convert_classmethod(self):
        avp = SubscriptionIdTypeAVP(END_USER_PRIVATE)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_subscription_id_type_avp__end_user_e164(self):
        avp = SubscriptionIdTypeAVP(END_USER_E164)
        ref = "000001c24000000c00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_subscription_id_type_avp__end_user_imsi(self):
        avp = SubscriptionIdTypeAVP(END_USER_IMSI)
        ref = "000001c24000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_subscription_id_type_avp__end_user_sip_uri(self):
        avp = SubscriptionIdTypeAVP(END_USER_SIP_URI)
        ref = "000001c24000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_subscription_id_type_avp__end_user_nai(self):
        avp = SubscriptionIdTypeAVP(END_USER_NAI)
        ref = "000001c24000000c00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test_subscription_id_type_avp__end_user_private(self):
        avp = SubscriptionIdTypeAVP(END_USER_PRIVATE)
        ref = "000001c24000000c00000004"
        self.assertEqual(avp.dump().hex(), ref)


class TestSubscriptionIdAVP(unittest.TestCase):
    def test_subscription_id_avp__no_value(self):
        self.assertRaises(TypeError, SubscriptionIdAVP)

    def test_subscription_id_avp__repr_dunder(self):
        subscription_id_type_avp = SubscriptionIdTypeAVP(END_USER_E164)
        subscription_id_data_avp = SubscriptionIdDataAVP("5566123456789")

        avps = [subscription_id_type_avp, subscription_id_data_avp]
        avp = SubscriptionIdAVP(avps)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 443 [Subscription-Id] MANDATORY>")

    def test_subscription_id_avp__diameter_avp_convert_classmethod(self):
        subscription_id_type_avp = SubscriptionIdTypeAVP(END_USER_E164)
        subscription_id_data_avp = SubscriptionIdDataAVP("5566123456789")

        avps = [subscription_id_type_avp, subscription_id_data_avp]
        avp = SubscriptionIdAVP(avps)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_subscription_id_avp__default(self):
        ref = "000001bb4000002c000001c24000000c00000000000001bc4000001535353636313233343536373839000000"
      
        subscription_id_type_avp = SubscriptionIdTypeAVP(END_USER_E164)
        subscription_id_data_avp = SubscriptionIdDataAVP("5566123456789")

        avps = [subscription_id_type_avp, subscription_id_data_avp]

        avp = SubscriptionIdAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)

    def test_subscription_id_avp__subscription_id_type_only(self):
        subscription_id_type_avp = SubscriptionIdTypeAVP(END_USER_E164)
        avps = [subscription_id_type_avp]

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp = SubscriptionIdAVP(avps)
        
        self.assertEqual(cm.exception.args[1], DIAMETER_MISSING_AVP)

    def test_subscription_id_avp__subscription_id_data_only(self):
        subscription_id_type_avp = SubscriptionIdDataAVP("5521993082672")
        avps = [subscription_id_type_avp]

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp = SubscriptionIdAVP(avps)
        
        self.assertEqual(cm.exception.args[1], DIAMETER_MISSING_AVP)


if __name__ == "__main__":
    unittest.main()