# -*- coding: utf-8 -*-
"""
    tests.avps.ietf.test_rfc8506
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for IETF RFC 8506.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.avps.ietf.rfc8506 import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_cc_request_number_avp_stream(self):
        stream = bytes.fromhex("0000019f4000000c00000001")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], CcRequestNumberAVP))
        self.assertEqual(avps[0].code, CC_REQUEST_NUMBER_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"\x00\x00\x00\x01")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 415 [Cc-Request-Number] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_cc_request_type_avp_stream(self):
        stream = bytes.fromhex("000001a04000000c00000001")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], CcRequestTypeAVP))
        self.assertEqual(avps[0].code, CC_REQUEST_TYPE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, CC_REQUEST_TYPE_INITIAL_REQUEST)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 416 [Cc-Request-Type] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_rating_group_avp_stream(self):
        stream = bytes.fromhex("000001b04000000c00000001")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], RatingGroupAVP))
        self.assertEqual(avps[0].code, RATING_GROUP_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"\x00\x00\x00\x01")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 432 [Rating-Group] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_service_identifier_avp_stream(self):
        stream = bytes.fromhex("000001b74000000c00000001")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], ServiceIdentifierAVP))
        self.assertEqual(avps[0].code, SERVICE_IDENTIFIER_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"\x00\x00\x00\x01")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 439 [Service-Identifier] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_user_equipment_info_avp_stream(self):
        stream = bytes.fromhex("000001ca4000002c000001cb4000000c00000000000001cc4000001633353335383531313030333431370000")
        
        avps = DiameterAVP.load(stream)
        
        self.assertTrue(isinstance(avps[0], UserEquipmentInfoAVP))
        self.assertEqual(avps[0].code, USER_EQUIPMENT_INFO_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 44)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data.hex(), "000001cb4000000c00000000000001cc4000001633353335383531313030333431370000")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 458 [User-Equipment-Info] MANDATORY>")

        user_equipment_info_type_avp = avps[0].user_equipment_info_type_avp
        user_equipment_info_value_avp = avps[0].user_equipment_info_value_avp

        #: User-Equipment-Info AVP > User-Equipment-Info-Type AVP
        self.assertTrue(isinstance(user_equipment_info_type_avp, UserEquipmentInfoTypeAVP))
        self.assertEqual(user_equipment_info_type_avp.code, USER_EQUIPMENT_INFO_TYPE_AVP_CODE)
        self.assertFalse(user_equipment_info_type_avp.is_vendor_id())
        self.assertTrue(user_equipment_info_type_avp.is_mandatory())
        self.assertFalse(user_equipment_info_type_avp.is_protected())
        self.assertEqual(user_equipment_info_type_avp.get_length(), 12)
        self.assertIsNone(user_equipment_info_type_avp.vendor_id)
        self.assertEqual(user_equipment_info_type_avp.data, USER_EQUIPMENT_INFO_TYPE_IMEISV)
        self.assertIsNone(user_equipment_info_type_avp.get_padding_length())
        self.assertEqual(user_equipment_info_type_avp.__repr__(), "<Diameter AVP: 459 [User-Equipment-Info-Type] MANDATORY>")

        #: User-Equipment-Info AVP > User-Equipment-Info-Value AVP
        self.assertTrue(isinstance(user_equipment_info_value_avp, UserEquipmentInfoValueAVP))
        self.assertEqual(user_equipment_info_value_avp.code, USER_EQUIPMENT_INFO_VALUE_AVP_CODE)
        self.assertFalse(user_equipment_info_value_avp.is_vendor_id())
        self.assertTrue(user_equipment_info_value_avp.is_mandatory())
        self.assertFalse(user_equipment_info_value_avp.is_protected())
        self.assertEqual(user_equipment_info_value_avp.get_length(), 22)
        self.assertIsNone(user_equipment_info_value_avp.vendor_id)
        self.assertEqual(user_equipment_info_value_avp.data, b"35358511003417")
        self.assertEqual(user_equipment_info_value_avp.get_padding_length(), 2)
        self.assertEqual(user_equipment_info_value_avp.__repr__(), "<Diameter AVP: 460 [User-Equipment-Info-Value] MANDATORY>")


    def test_diameter_avp__load_staticmethod__parsing_user_equipment_info_type_avp_stream(self):
        stream = bytes.fromhex("000001cb4000000c00000000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], UserEquipmentInfoTypeAVP))
        self.assertEqual(avps[0].code, USER_EQUIPMENT_INFO_TYPE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, USER_EQUIPMENT_INFO_TYPE_IMEISV)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 459 [User-Equipment-Info-Type] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_user_equipment_info_value_avp_stream(self):
        stream = bytes.fromhex("000001cc4000001633353335383531313030333431370000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], UserEquipmentInfoValueAVP))
        self.assertEqual(avps[0].code, USER_EQUIPMENT_INFO_VALUE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 22)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"35358511003417")
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 460 [User-Equipment-Info-Value] MANDATORY>")


class TestCcRequestNumberAVP(unittest.TestCase):
    def test_cc_request_number_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = CcRequestNumberAVP()
        
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test_cc_request_number_avp__repr_dunder(self):
        avp = CcRequestNumberAVP(1)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 415 [Cc-Request-Number] MANDATORY>")

    def test_cc_request_number_avp__diameter_avp_convert_classmethod(self):
        avp = CcRequestNumberAVP(1)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_cc_request_number_avp__3gpp(self):
        avp = CcRequestNumberAVP(1)
        ref = "0000019f4000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestCcRequestTypeAVP(unittest.TestCase):
    def test_cc_request_type_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = CcRequestTypeAVP()
        
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test_cc_request_type_avp__repr_dunder(self):
        avp = CcRequestTypeAVP(CC_REQUEST_TYPE_INITIAL_REQUEST)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 416 [Cc-Request-Type] MANDATORY>")

    def test_cc_request_type_avp__diameter_avp_convert_classmethod(self):
        avp = CcRequestTypeAVP(CC_REQUEST_TYPE_INITIAL_REQUEST)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_cc_request_type_avp___initial_request(self):
        avp = CcRequestTypeAVP(CC_REQUEST_TYPE_INITIAL_REQUEST)
        ref = "000001a04000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_cc_request_type_avp___initial_request(self):
        avp = CcRequestTypeAVP(CC_REQUEST_TYPE_INITIAL_REQUEST)
        ref = "000001a04000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_cc_request_type_avp___update_request(self):
        avp = CcRequestTypeAVP(CC_REQUEST_TYPE_UPDATE_REQUEST)
        ref = "000001a04000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_cc_request_type_avp___termination_request(self):
        avp = CcRequestTypeAVP(CC_REQUEST_TYPE_TERMINATION_REQUEST)
        ref = "000001a04000000c00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test_cc_request_type_avp___event_request(self):
        avp = CcRequestTypeAVP(CC_REQUEST_TYPE_EVENT_REQUEST)
        ref = "000001a04000000c00000004"
        self.assertEqual(avp.dump().hex(), ref)


class TestRatingGroupAVP(unittest.TestCase):
    def test_rating_group_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = RatingGroupAVP()

        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test_rating_group_avp__repr_dunder(self):
        avp = RatingGroupAVP(1)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 432 [Rating-Group] MANDATORY>")

    def test_rating_group_avp__diameter_avp_convert_classmethod(self):
        avp = RatingGroupAVP(1)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_rating_group_avp__1(self):
        avp = RatingGroupAVP(1)
        ref = "000001b04000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_rating_group_avp__2(self):
        avp = RatingGroupAVP(2)
        ref = "000001b04000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_rating_group_avp__3(self):
        avp = RatingGroupAVP(3)
        ref = "000001b04000000c00000003"
        self.assertEqual(avp.dump().hex(), ref)


class TestServiceIdentifierAVP(unittest.TestCase):
    def test_service_identifier_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = ServiceIdentifierAVP()

        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test_service_identifier_avp__repr_dunder(self):
        avp = ServiceIdentifierAVP(1)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 439 [Service-Identifier] MANDATORY>")

    def test_service_identifier_avp__diameter_avp_convert_classmethod(self):
        avp = ServiceIdentifierAVP(1)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_service_identifier_avp__1(self):
        avp = ServiceIdentifierAVP(1)
        ref = "000001b74000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_service_identifier_avp__2(self):
        avp = ServiceIdentifierAVP(2)
        ref = "000001b74000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_service_identifier_avp__3(self):
        avp = ServiceIdentifierAVP(3)
        ref = "000001b74000000c00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test_service_identifier_avp__824(self):
        avp = ServiceIdentifierAVP(824)
        ref = "000001b74000000c00000338"
        self.assertEqual(avp.dump().hex(), ref)


class TestUserEquipmentInfoAVP(unittest.TestCase):
    def test_user_equipment_info_avp__no_value(self):
        with self.assertRaises(TypeError) as cm:
            avp = UserEquipmentInfoAVP()
        
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test_user_equipment_info_avp__repr_dunder(self):
        avp = UserEquipmentInfoAVP([
                        UserEquipmentInfoTypeAVP(USER_EQUIPMENT_INFO_TYPE_IMEISV), 
                        UserEquipmentInfoValueAVP("35358511003417")
        ])
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 458 [User-Equipment-Info] MANDATORY>")

    def test_user_equipment_info_avp__diameter_avp_convert_classmethod(self):
        avp = UserEquipmentInfoAVP([
                        UserEquipmentInfoTypeAVP(USER_EQUIPMENT_INFO_TYPE_IMEISV), 
                        UserEquipmentInfoValueAVP("35358511003417")
        ])

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_user_equipment_info_avp__default_1(self):
        avp = UserEquipmentInfoAVP([
                        UserEquipmentInfoTypeAVP(USER_EQUIPMENT_INFO_TYPE_IMEISV), 
                        UserEquipmentInfoValueAVP("35358511003417")
        ])
        ref = "000001ca4000002c000001cb4000000c00000000000001cc4000001633353335383531313030333431370000"
        self.assertEqual(avp.dump().hex(), ref)
      

class TestUserEquipmentInfoTypeAVP(unittest.TestCase):
    def test_user_equipment_info_type_avp__no_value(self):
        with self.assertRaises(TypeError) as cm:
            avp = UserEquipmentInfoTypeAVP()
        
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test_user_equipment_info_type_avp__repr_dunder(self):
        avp = UserEquipmentInfoTypeAVP(USER_EQUIPMENT_INFO_TYPE_IMEISV)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 459 [User-Equipment-Info-Type] MANDATORY>")

    def test_user_equipment_info_type_avp__diameter_avp_convert_classmethod(self):
        avp = UserEquipmentInfoTypeAVP(USER_EQUIPMENT_INFO_TYPE_IMEISV)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_user_equipment_info_type_avp__imeisv(self):
        avp = UserEquipmentInfoTypeAVP(USER_EQUIPMENT_INFO_TYPE_IMEISV)
        ref = "000001cb4000000c00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_user_equipment_info_type_avp__mac(self):
        avp = UserEquipmentInfoTypeAVP(USER_EQUIPMENT_INFO_TYPE_MAC)
        ref = "000001cb4000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_user_equipment_info_type_avp__eui64(self):
        avp = UserEquipmentInfoTypeAVP(USER_EQUIPMENT_INFO_TYPE_EUI64)
        ref = "000001cb4000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_user_equipment_info_type_avp__modified_eui64(self):
        avp = UserEquipmentInfoTypeAVP(USER_EQUIPMENT_INFO_TYPE_MODIFIED_EUI64)
        ref = "000001cb4000000c00000003"
        self.assertEqual(avp.dump().hex(), ref)


class TestUserEquipmentInfoValueAVP(unittest.TestCase):
    def test_user_equipment_info_value_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = UserEquipmentInfoAVP()

        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test_user_equipment_info_value_avp__repr_dunder(self):
        avp = UserEquipmentInfoValueAVP("35358511003417")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 460 [User-Equipment-Info-Value] MANDATORY>")

    def test_user_equipment_info_value_avp__diameter_avp_convert_classmethod(self):
        avp = UserEquipmentInfoValueAVP("35358511003417")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_user_equipment_info_value_avp__1(self):
        avp = UserEquipmentInfoValueAVP("35358511003417")
        ref = "000001cc4000001633353335383531313030333431370000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_user_equipment_info_value_avp__2(self):
        avp = UserEquipmentInfoValueAVP("353987100150862")
        ref = "000001cc4000001733353339383731303031353038363200"
        self.assertEqual(avp.dump().hex(), ref)

    def test_user_equipment_info_value_avp__3(self):
        avp = UserEquipmentInfoValueAVP("359440080055416")
        ref = "000001cc4000001733353934343030383030353534313600"
        self.assertEqual(avp.dump().hex(), ref)


if __name__ == "__main__":
    unittest.main()