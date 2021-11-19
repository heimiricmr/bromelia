# -*- coding: utf-8 -*-
"""
    test.test_base
    ~~~~~~~~~~~~~~

    This module contains the Diameter protocol base unittests.
    
    :copyright: (c) 2020 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.avps import *
from bromelia.base import *
from bromelia.constants import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__vendor_id_bit__default(self):
        avp = DiameterAVP()
        self.assertFalse(avp.is_vendor_id())

        avp.set_vendor_id_bit(True)
        self.assertTrue(avp.is_vendor_id())

        avp.set_vendor_id_bit(False)
        self.assertFalse(avp.is_vendor_id())

        avp.set_vendor_id_bit(True)
        self.assertTrue(avp.is_vendor_id())

        avp.set_vendor_id_bit(False)
        self.assertFalse(avp.is_vendor_id())

    def test_diameter_avp__vendor_id_bit__unset_when_is_unset(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.set_vendor_id_bit(False)
        
        self.assertEqual(cm.exception.args[0], "V-bit was already unset")

    def test_diameter_avp__vendor_id_bit__set_when_is_set(self):
        avp = DiameterAVP()
        self.assertFalse(avp.is_vendor_id())

        avp.set_vendor_id_bit(True)
        self.assertTrue(avp.is_vendor_id())

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.set_vendor_id_bit(True)
        
        self.assertEqual(cm.exception.args[0], "V-bit was already set")

    def test_diameter_avp__mandatory_bit__default(self):
        avp = DiameterAVP()
        self.assertFalse(avp.is_mandatory())

        avp.set_mandatory_bit(True)
        self.assertTrue(avp.is_mandatory())

        avp.set_mandatory_bit(False)
        self.assertFalse(avp.is_mandatory())

        avp.set_mandatory_bit(True)
        self.assertTrue(avp.is_mandatory())

        avp.set_mandatory_bit(False)
        self.assertFalse(avp.is_mandatory())

    def test_diameter_avp__mandatory_bit__unset_when_is_unset(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.set_mandatory_bit(False)
        
        self.assertEqual(cm.exception.args[0], "M-bit was already unset")

    def test_diameter_avp__mandatory_bit__set_when_is_set(self):
        avp = DiameterAVP()
        self.assertFalse(avp.is_mandatory())

        avp.set_mandatory_bit(True)
        self.assertTrue(avp.is_mandatory())

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.set_mandatory_bit(True)
        
        self.assertEqual(cm.exception.args[0], "M-bit was already set")

    def test_diameter_avp__protected_bit__default(self):
        avp = DiameterAVP()
        self.assertFalse(avp.is_protected())

        avp.set_protected_bit(True)
        self.assertTrue(avp.is_protected())

        avp.set_protected_bit(False)
        self.assertFalse(avp.is_protected())

        avp.set_protected_bit(True)
        self.assertTrue(avp.is_protected())

        avp.set_protected_bit(False)
        self.assertFalse(avp.is_protected())

    def test_diameter_avp__protected_bit__unset_when_is_unset(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.set_protected_bit(False)
        
        self.assertEqual(cm.exception.args[0], "P-bit was already unset")

    def test_diameter_avp__protected_bit__set_when_is_set(self):
        avp = DiameterAVP()
        self.assertFalse(avp.is_protected())

        avp.set_protected_bit(True)
        self.assertTrue(avp.is_protected())

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.set_protected_bit(True)
        
        self.assertEqual(cm.exception.args[0], "P-bit was already set")

    def test_diameter_avp__default_object(self):
        avp = DiameterAVP()
        
        self.assertEqual(avp.code.hex(), "00000000")
        self.assertEqual(avp.flags.hex(), "00")
        self.assertIsNone(avp.vendor_id)
        self.assertEqual(avp.length.hex(), "000008")
        self.assertIsNone(avp.data)
        self.assertIsNone(avp.padding)

        self.assertEqual(avp.dump().hex(), "0000000000000008")

        self.assertEqual(avp.get_code(), 0)
        self.assertEqual(avp.get_flags(), 0)
        self.assertIsNone(avp.get_vendor_id())
        self.assertEqual(avp.get_length(), 8)

    def test_diameter_avp__custom_object_by_constructor(self):
        avp = DiameterAVP(code=1, vendor_id=3, flags=2, data="srcrary")

        self.assertEqual(avp.code.hex(), "00000001")
        self.assertEqual(avp.flags.hex(), "02")
        self.assertEqual(avp.vendor_id.hex(), "00000003")
        self.assertEqual(avp.length.hex(), "000013")
        self.assertEqual(avp.data.hex(), "73726372617279")
        self.assertEqual(avp.padding.hex(), "00")

        self.assertEqual(avp.dump().hex(), "0000000102000013000000037372637261727900")

        self.assertEqual(avp.get_code(), 1)
        self.assertEqual(avp.get_flags(), 2)
        self.assertEqual(avp.get_vendor_id(), 3)
        self.assertEqual(avp.get_length(), 19)
        self.assertEqual(avp.get_padding_length(), 1)

    def test_diameter_avp__custom_object_by_instance_attributes(self):
        avp = DiameterAVP()

        avp.code = 1
        avp.flags = 2
        avp.vendor_id = 3
        avp.data = "srcrary"

        self.assertEqual(avp.code.hex(), "00000001")
        self.assertEqual(avp.flags.hex(), "02")
        self.assertEqual(avp.vendor_id.hex(), "00000003")
        self.assertEqual(avp.length.hex(), "000013")
        self.assertEqual(avp.data.hex(), "73726372617279")
        self.assertEqual(avp.padding.hex(), "00")

        self.assertEqual(avp.dump().hex(), "0000000102000013000000037372637261727900")

        self.assertEqual(avp.get_code(), 1)
        self.assertEqual(avp.get_flags(), 2)
        self.assertEqual(avp.get_vendor_id(), 3)
        self.assertEqual(avp.get_length(), 19)

    def test_diameter_avp__custom_object__invalid_code_value__string(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.code = "4294967296"
        
        self.assertEqual(cm.exception.args[0], "invalid code attribute value")

    def test_diameter_avp__custom_object__invalid_code_value__list(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.code = ["4294967296"]
 
        self.assertEqual(cm.exception.args[0], "invalid code attribute value")

    def test_diameter_avp__custom_object__invalid_code_value__integer_1(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.code = 4294967296
        
        self.assertEqual(cm.exception.args[0], "code attribute has 4-bytes length long")

    def test_diameter_avp__custom_object__invalid_code_value__integer_2(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.code = -1
        
        self.assertEqual(cm.exception.args[0], "code attribute has 4-bytes length long")

    def test_diameter_avp__custom_object__invalid_code_value__bytes_1(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.code = bytes.fromhex("00")
        
        self.assertEqual(cm.exception.args[0], "code attribute has 4-bytes length long")

    def test_diameter_avp__custom_object__invalid_code_value__bytes_2(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.code = bytes.fromhex("0000")
        
        self.assertEqual(cm.exception.args[0], "code attribute has 4-bytes length long")

    def test_diameter_avp__custom_object__invalid_code_value__bytes_3(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.code = bytes.fromhex("000000")
        
        self.assertEqual(cm.exception.args[0], "code attribute has 4-bytes length long")

    def test_diameter_avp__custom_object__invalid_code_value__bytes_4(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.code = bytes.fromhex("0000000001")
        
        self.assertEqual(cm.exception.args[0], "code attribute has 4-bytes length long")

    def test_diameter_avp__custom_object__invalid_flags_value__string(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.flags = "256"
        
        self.assertEqual(cm.exception.args[0], "invalid flags attribute value")

    def test_diameter_avp__custom_object__invalid_flags_value__list(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.flags = ["256"]
 
        self.assertEqual(cm.exception.args[0], "invalid flags attribute value")

    def test_diameter_avp__custom_object__invalid_flags_value__integer_1(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.flags = 256
        
        self.assertEqual(cm.exception.args[0], "flags attribute has 1-byte length long")

    def test_diameter_avp__custom_object__invalid_flags_value__integer_2(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.flags = -1
        
        self.assertEqual(cm.exception.args[0], "flags attribute has 1-byte length long")

    def test_diameter_avp__custom_object__invalid_flags_value__bytes_1(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.flags = bytes.fromhex("0000")
        
        self.assertEqual(cm.exception.args[0], "flags attribute has 1-byte length long")

    def test_diameter_avp__custom_object__invalid_flags_value__bytes_2(self):
        avp = DiameterAVP()

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp.flags = bytes.fromhex("000000")
        
        self.assertEqual(cm.exception.args[0], "flags attribute has 1-byte length long")

    def test_diameter_avp__custom_object__flags_by_setting_class_attributes(self):
        avp = DiameterAVP()

        avp.flags = DiameterAVP.flag_vendor_id_bit
        self.assertEqual(avp.flags.hex(), "80")

        avp.flags = DiameterAVP.flag_mandatory_bit
        self.assertEqual(avp.flags.hex(), "40")

        avp.flags = DiameterAVP.flag_protected_bit
        self.assertEqual(avp.flags.hex(), "20")

        avp.flags = DiameterAVP.flag_reserved5_bit
        self.assertEqual(avp.flags.hex(), "10")

        avp.flags = DiameterAVP.flag_reserved4_bit
        self.assertEqual(avp.flags.hex(), "08")

        avp.flags = DiameterAVP.flag_reserved3_bit
        self.assertEqual(avp.flags.hex(), "04")

        avp.flags = DiameterAVP.flag_reserved2_bit
        self.assertEqual(avp.flags.hex(), "02")

        avp.flags = DiameterAVP.flag_reserved1_bit
        self.assertEqual(avp.flags.hex(), "01")

    def test_diameter_avp__custom_object__flags_by_set_flags_methods(self):
        avp = DiameterAVP()

        avp.set_protected_bit(True)
        avp.set_mandatory_bit(True)
        self.assertEqual(avp.flags.hex(), "60")

        avp.set_vendor_id_bit(True)
        self.assertEqual(avp.flags.hex(), "e0")

        avp.set_protected_bit(False)
        self.assertEqual(avp.flags.hex(), "c0")

        avp.set_protected_bit(True)
        avp.set_mandatory_bit(False)
        self.assertEqual(avp.flags.hex(), "a0")

        avp.set_protected_bit(False)
        self.assertEqual(avp.flags.hex(), "80")

        avp.set_vendor_id_bit(False)
        self.assertEqual(avp.flags.hex(), "00")

        avp.set_protected_bit(True)
        self.assertEqual(avp.flags.hex(), "20")

        avp.set_mandatory_bit(True)
        avp.set_protected_bit(False)
        self.assertEqual(avp.flags.hex(), "40")

        avp.set_protected_bit(True)
        self.assertEqual(avp.flags.hex(), "60")

    def test_diameter_avp__custom_object__length_by_using_len_builtin_function(self):
        avp = DiameterAVP(1, 2, 3, "srcrary")
        self.assertEqual(len(avp), avp.get_length())

        avp = DiameterAVP(1, 2, 3, "Pythonicsrcrary")
        self.assertEqual(len(avp), avp.get_length())

    def test_diameter_avp__custom_object__length_changing_based_on_data(self):
        avp = DiameterAVP()
        
        avp.data = "srcrary"
        self.assertEqual(avp.get_length(), 15)
        self.assertEqual(avp.get_padding_length(), 1)

        avp.data += b"FOO"
        self.assertEqual(avp.get_length(), 18)
        self.assertEqual(avp.get_padding_length(), 2)

        avp.data += b"BAR"
        self.assertEqual(avp.get_length(), 21)
        self.assertEqual(avp.get_padding_length(), 3)

        avp.data += b"F"
        self.assertEqual(avp.get_length(), 22)
        self.assertEqual(avp.get_padding_length(), 2)

        avp.data += b"B"
        self.assertEqual(avp.get_length(), 23)
        self.assertEqual(avp.get_padding_length(), 1)
        
        avp.data += b"="
        self.assertEqual(avp.get_length(), 24)
        self.assertIsNone(avp.get_padding_length())

    def test_diameter_avp__custom_object__length_by_adding_vendor_id(self):
        avp = DiameterAVP()
        
        avp.data = "srcrary"
        self.assertEqual(avp.get_length(), 15)
        self.assertEqual(avp.get_padding_length(), 1)

        avp.vendor_id = VENDOR_ID_3GPP
        self.assertEqual(avp.get_length(), 19)
        self.assertEqual(avp.get_padding_length(), 1)

        avp.data += b"FooBar"
        self.assertEqual(avp.get_length(), 25)
        self.assertEqual(avp.get_padding_length(), 3)

        avp.data = b""
        self.assertEqual(avp.get_length(), 12)
        self.assertIsNone(avp.get_padding_length())

        avp.vendor_id = None
        self.assertEqual(avp.get_length(), 8)
        self.assertIsNone(avp.get_padding_length())

    def test_diameter_avp__eq_dunder(self):
        avp1 = DiameterAVP()
        avp2 = DiameterAVP()

        self.assertEqual(avp1, avp2)

        avp1.set_mandatory_bit(True)
        self.assertNotEqual(avp1, avp2)

        avp2.set_mandatory_bit(True)
        self.assertEqual(avp1, avp2)

        avp2 = OriginHostAVP("host")
        self.assertNotEqual(avp1, avp2)

        avp1.code = avp2.code
        avp1.flags = avp2.flags
        avp1.data = avp2.data
        self.assertEqual(avp1, avp2)

        self.assertEqual(avp1.__repr__(), "<Diameter AVP: 264 [Origin-Host] MANDATORY>")
        self.assertEqual(avp2.__repr__(), "<Diameter AVP: 264 [Origin-Host] MANDATORY>")

    # include tests for data attribute and vendor_id

    def test_diameter_avp__custom_object__padding_not_allowed_to_set(self):
        avp = DiameterAVP()

        with self.assertRaises(AttributeError) as cm: 
            avp.padding = bytes.fromhex("0000")
        self.assertEqual(cm.exception.args[0], "can't set attribute")


class TestDiameterHeader(unittest.TestCase):
    def test_diameter_header__repr_dunder_default(self):
        header = DiameterHeader()
        self.assertEqual(header.__str__(), "<Diameter Header: Unknown [], 0 [Diameter common message]>")

    def test_diameter_header__repr_dunder_diameter_common_and_cer(self):
        header = DiameterHeader()

        header.application_id = DIAMETER_APPLICATION_DEFAULT
        self.assertEqual(header.__str__(), "<Diameter Header: Unknown [], 0 [Diameter common message]>")

        header.command_code = CAPABILITIES_EXCHANGE_MESSAGE
        self.assertEqual(header.__str__(), "<Diameter Header: 257 [CEA], 0 [Diameter common message]>")

        header.set_request_bit(True)
        self.assertEqual(header.__str__(), "<Diameter Header: 257 [CER] REQ, 0 [Diameter common message]>")

        header.set_proxiable_bit(True)
        self.assertEqual(header.__str__(), "<Diameter Header: 257 [CER] REQ|PXY, 0 [Diameter common message]>")

        header.set_request_bit(False)
        self.assertEqual(header.__str__(), "<Diameter Header: 257 [CEA] PXY, 0 [Diameter common message]>")

        header.set_error_bit(True)
        self.assertEqual(header.__str__(), "<Diameter Header: 257 [CEA] PXY|ERR, 0 [Diameter common message]>")

        header.set_proxiable_bit(False)
        self.assertEqual(header.__str__(), "<Diameter Header: 257 [CEA] ERR, 0 [Diameter common message]>")

        header.set_error_bit(False)
        self.assertEqual(header.__str__(), "<Diameter Header: 257 [CEA], 0 [Diameter common message]>")

        header.application_id = None
        self.assertEqual(header.__str__(), "<Diameter Header: 257 [CEA], Unknown []>")

        header.command_code = None
        self.assertEqual(header.__str__(), "<Diameter Header: Unknown [], Unknown []>")

    def test_diameter_header__repr_dunder_diameter_common_and_dwr(self):
        header = DiameterHeader()

        header.application_id = DIAMETER_APPLICATION_DEFAULT
        self.assertEqual(header.__str__(), "<Diameter Header: Unknown [], 0 [Diameter common message]>")

        header.command_code = DEVICE_WATCHDOG_MESSAGE
        self.assertEqual(header.__str__(), "<Diameter Header: 280 [DWA], 0 [Diameter common message]>")

        header.set_request_bit(True)
        self.assertEqual(header.__str__(), "<Diameter Header: 280 [DWR] REQ, 0 [Diameter common message]>")

        header.set_proxiable_bit(True)
        self.assertEqual(header.__str__(), "<Diameter Header: 280 [DWR] REQ|PXY, 0 [Diameter common message]>")

        header.set_request_bit(False)
        self.assertEqual(header.__str__(), "<Diameter Header: 280 [DWA] PXY, 0 [Diameter common message]>")

        header.set_error_bit(True)
        self.assertEqual(header.__str__(), "<Diameter Header: 280 [DWA] PXY|ERR, 0 [Diameter common message]>")

        header.set_proxiable_bit(False)
        self.assertEqual(header.__str__(), "<Diameter Header: 280 [DWA] ERR, 0 [Diameter common message]>")

        header.set_error_bit(False)
        self.assertEqual(header.__str__(), "<Diameter Header: 280 [DWA], 0 [Diameter common message]>")

        header.application_id = None
        self.assertEqual(header.__str__(), "<Diameter Header: 280 [DWA], Unknown []>")

        header.command_code = None
        self.assertEqual(header.__str__(), "<Diameter Header: Unknown [], Unknown []>")

    def test_diameter_header__repr_dunder_diameter_common_and_dpr(self):
        header = DiameterHeader()

        header.application_id = DIAMETER_APPLICATION_DEFAULT
        self.assertEqual(header.__str__(), "<Diameter Header: Unknown [], 0 [Diameter common message]>")

        header.command_code = DISCONNECT_PEER_MESSAGE
        self.assertEqual(header.__str__(), "<Diameter Header: 282 [DPA], 0 [Diameter common message]>")

        header.set_request_bit(True)
        self.assertEqual(header.__str__(), "<Diameter Header: 282 [DPR] REQ, 0 [Diameter common message]>")

        header.set_proxiable_bit(True)
        self.assertEqual(header.__str__(), "<Diameter Header: 282 [DPR] REQ|PXY, 0 [Diameter common message]>")

        header.set_request_bit(False)
        self.assertEqual(header.__str__(), "<Diameter Header: 282 [DPA] PXY, 0 [Diameter common message]>")

        header.set_error_bit(True)
        self.assertEqual(header.__str__(), "<Diameter Header: 282 [DPA] PXY|ERR, 0 [Diameter common message]>")

        header.set_proxiable_bit(False)
        self.assertEqual(header.__str__(), "<Diameter Header: 282 [DPA] ERR, 0 [Diameter common message]>")

        header.set_error_bit(False)
        self.assertEqual(header.__str__(), "<Diameter Header: 282 [DPA], 0 [Diameter common message]>")

        header.application_id = None
        self.assertEqual(header.__str__(), "<Diameter Header: 282 [DPA], Unknown []>")

        header.command_code = None
        self.assertEqual(header.__str__(), "<Diameter Header: Unknown [], Unknown []>")

    def test_diameter_header__repr_dunder_swm_interface(self):
        header = DiameterHeader()

        header.application_id = DIAMETER_APPLICATION_SWm
        self.assertEqual(header.__str__(), "<Diameter Header: Unknown [], 16777264 [3GPP SWm]>")

        header.command_code = DIAMETER_EAP_MESSAGE
        self.assertEqual(header.__str__(), "<Diameter Header: 268 [DEA], 16777264 [3GPP SWm]>")

        header.set_request_bit(True)
        self.assertEqual(header.__str__(), "<Diameter Header: 268 [DER] REQ, 16777264 [3GPP SWm]>")

        header.command_code = AA_MESSAGE
        self.assertEqual(header.__str__(), "<Diameter Header: 265 [AAR] REQ, 16777264 [3GPP SWm]>")

        header.set_request_bit(False)
        self.assertEqual(header.__str__(), "<Diameter Header: 265 [AAA], 16777264 [3GPP SWm]>")

        header.command_code = SESSION_TERMINATION_MESSAGE
        self.assertEqual(header.__str__(), "<Diameter Header: 275 [STA], 16777264 [3GPP SWm]>")

        header.set_request_bit(True)
        self.assertEqual(header.__str__(), "<Diameter Header: 275 [STR] REQ, 16777264 [3GPP SWm]>")

        header.command_code = ABORT_SESSION_MESSAGE
        self.assertEqual(header.__str__(), "<Diameter Header: 274 [ASR] REQ, 16777264 [3GPP SWm]>")

        header.set_request_bit(False)
        self.assertEqual(header.__str__(), "<Diameter Header: 274 [ASA], 16777264 [3GPP SWm]>")

        header.command_code = RE_AUTH_MESSAGE
        self.assertEqual(header.__str__(), "<Diameter Header: 258 [RAA], 16777264 [3GPP SWm]>")

        header.set_request_bit(True)
        self.assertEqual(header.__str__(), "<Diameter Header: 258 [RAR] REQ, 16777264 [3GPP SWm]>")

        header.application_id = None
        self.assertEqual(header.__str__(), "<Diameter Header: 258 [RAR] REQ, Unknown []>")

        header.command_code = None
        self.assertEqual(header.__str__(), "<Diameter Header: Unknown [] REQ, Unknown []>")

        header.set_request_bit(False)
        self.assertEqual(header.__str__(), "<Diameter Header: Unknown [], Unknown []>")

        header.command_code = DIAMETER_EAP_MESSAGE
        self.assertEqual(header.__str__(), "<Diameter Header: 268 [DEA], Unknown []>")

        header.application_id = DIAMETER_APPLICATION_SWm
        self.assertEqual(header.__str__(), "<Diameter Header: 268 [DEA], 16777264 [3GPP SWm]>")

        header.command_code = None
        self.assertEqual(header.__str__(), "<Diameter Header: Unknown [], 16777264 [3GPP SWm]>")

        header.application_id = None
        self.assertEqual(header.__str__(), "<Diameter Header: Unknown [], Unknown []>")

    def test_diameter_header__eq_dunder(self):
        header1 = DiameterHeader()
        header2 = DiameterHeader()

        self.assertEqual(header1, header2)

        header1.set_request_bit(True)
        self.assertNotEqual(header1, header2)

        header2.set_request_bit(True)
        self.assertEqual(header1, header2)

    def test_diameter_header_request_bit__default(self):
        header = DiameterHeader()
        self.assertFalse(header.is_request())

        header.set_request_bit(True)
        self.assertTrue(header.is_request())

        header.set_request_bit(False)
        self.assertFalse(header.is_request())

        header.set_request_bit(True)
        self.assertTrue(header.is_request())

        header.set_request_bit(False)
        self.assertFalse(header.is_request())

    def test_diameter_header_request_bit__unset_when_is_unset(self):
        header = DiameterHeader()

        with self.assertRaises(DiameterHeaderError) as cm: 
            header.set_request_bit(False)
        
        self.assertEqual(cm.exception.args[0], "R-bit was already unset")

    def test_diameter_header_request_bit__set_when_is_set(self):
        header = DiameterHeader()
        self.assertFalse(header.is_request())

        header.set_request_bit(True)
        self.assertTrue(header.is_request())

        with self.assertRaises(DiameterHeaderError) as cm: 
            header.set_request_bit(True)
        
        self.assertEqual(cm.exception.args[0], "R-bit was already set")

    def test_diameter_header_request_bit__set_when_error_bit_is_set(self):
        header = DiameterHeader()
        self.assertFalse(header.is_request())

        header.set_error_bit(True)
        self.assertTrue(header.is_error())
    
        with self.assertRaises(DiameterHeaderError) as cm: 
            header.set_request_bit(True)
    
        self.assertEqual(cm.exception.args[0], "R-bit MUST NOT be set when E-bit is set")

        header.set_error_bit(False)
        self.assertFalse(header.is_error())

        header.set_request_bit(True)
        self.assertTrue(header.is_request())

    def test_diameter_header_proxiable_bit__default(self):
        header = DiameterHeader()
        self.assertFalse(header.is_proxiable())

        header.set_proxiable_bit(True)
        self.assertTrue(header.is_proxiable())

        header.set_proxiable_bit(False)
        self.assertFalse(header.is_proxiable())

        header.set_proxiable_bit(True)
        self.assertTrue(header.is_proxiable())

        header.set_proxiable_bit(False)
        self.assertFalse(header.is_proxiable())

    def test_diameter_header_proxiable_bit__unset_when_is_unset(self):
        header = DiameterHeader()

        with self.assertRaises(DiameterHeaderError) as cm: 
            header.set_proxiable_bit(False)
        
        self.assertEqual(cm.exception.args[0], "P-bit was already unset")

    def test_diameter_header_proxiable_bit__set_when_is_set(self):
        header = DiameterHeader()
        self.assertFalse(header.is_proxiable())

        header.set_proxiable_bit(True)
        self.assertTrue(header.is_proxiable())

        with self.assertRaises(DiameterHeaderError) as cm: 
            header.set_proxiable_bit(True)
        
        self.assertEqual(cm.exception.args[0], "P-bit was already set")

    def test_diameter_header_error_bit__default(self):
        header = DiameterHeader()
        self.assertFalse(header.is_error())

        header.set_error_bit(True)
        self.assertTrue(header.is_error())

        header.set_error_bit(False)
        self.assertFalse(header.is_error())

        header.set_error_bit(True)
        self.assertTrue(header.is_error())

        header.set_error_bit(False)
        self.assertFalse(header.is_error())

    def test_diameter_header_error_bit__unset_when_is_unset(self):
        header = DiameterHeader()

        with self.assertRaises(DiameterHeaderError) as cm: 
            header.set_error_bit(False)
        
        self.assertEqual(cm.exception.args[0], "E-bit was already unset")

    def test_diameter_header_error_bit__set_when_is_set(self):
        header = DiameterHeader()
        self.assertFalse(header.is_error())

        header.set_error_bit(True)
        self.assertTrue(header.is_error())

        with self.assertRaises(DiameterHeaderError) as cm: 
            header.set_error_bit(True)
        
        self.assertEqual(cm.exception.args[0], "E-bit was already set")

    def test_diameter_header_error_bit__set_when_request_bit_is_set(self):
        header = DiameterHeader()
        self.assertFalse(header.is_error())

        header.set_request_bit(True)
        self.assertTrue(header.is_request())
    
        with self.assertRaises(DiameterHeaderError) as cm: 
            header.set_error_bit(True)
    
        self.assertEqual(cm.exception.args[0], "E-bit MUST NOT be set when R-bit is set")

        header.set_request_bit(False)
        self.assertFalse(header.is_request())

        header.set_error_bit(True)
        self.assertTrue(header.is_error())

    def test_diameter_header_retransmitted_bit__default(self):
        header = DiameterHeader()
        self.assertFalse(header.is_retransmitted())

        header.set_retransmitted_bit(True)
        self.assertTrue(header.is_retransmitted())

        header.set_retransmitted_bit(False)
        self.assertFalse(header.is_retransmitted())

        header.set_retransmitted_bit(True)
        self.assertTrue(header.is_retransmitted())

        header.set_retransmitted_bit(False)
        self.assertFalse(header.is_retransmitted())

    def test_diameter_header_retransmitted_bit__unset_when_is_unset(self):
        header = DiameterHeader()

        with self.assertRaises(DiameterHeaderError) as cm: 
            header.set_retransmitted_bit(False)
        
        self.assertEqual(cm.exception.args[0], "T-bit was already unset")

    def test_diameter_header_retransmitted_bit__set_when_is_set(self):
        header = DiameterHeader()
        self.assertFalse(header.is_retransmitted())

        header.set_retransmitted_bit(True)
        self.assertTrue(header.is_retransmitted())

        with self.assertRaises(DiameterHeaderError) as cm: 
            header.set_retransmitted_bit(True)
        
        self.assertEqual(cm.exception.args[0], "T-bit was already set")


class TestDiameterMessage(unittest.TestCase):
    def test_diameter_message__default(self):
        message = DiameterMessage()
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 0 AVP(s)>")


    def test_diameter_message__repr_dunder_default(self):
        header = DiameterHeader()

        message = DiameterMessage(header)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 0 AVP(s)>")

    def test_diameter_message__invalid_way_of_passing_avp_input_argument__1(self):
        header = DiameterHeader()
        avp = DiameterAVP()

        with self.assertRaises(DiameterMessageError) as cm: 
            message = DiameterMessage(header, avp)
        
        self.assertEqual(cm.exception.args[0], "invalid input argument: 'avps'. It MUST be a list of DiameterAVP objects")

    def test_diameter_message__invalid_way_of_passing_avp_input_argument__2(self):
        header = DiameterHeader()
        avps = [DiameterAVP(), 1]

        with self.assertRaises(DiameterMessageError) as cm: 
            message = DiameterMessage(header, avps)
        
        self.assertEqual(cm.exception.args[0], "invalid element found in list argument: 'avps'. The element 1 in position 1 does not represent a DiameterAVP object")

    def test_diameter_message__invalid_way_of_passing_avp_input_argument__3(self):
        header = DiameterHeader()
        avps = [DiameterAVP(), DiameterAVP(), "DiameterAVP()"]

        with self.assertRaises(DiameterMessageError) as cm:
            message = DiameterMessage(header, avps)
        
        self.assertEqual(cm.exception.args[0], "invalid element found in list argument: 'avps'. The element DiameterAVP() in position 2 does not represent a DiameterAVP object")

    def test_diameter_message__invalid_way_of_passing_avp_input_argument__4(self):
        header = DiameterHeader()
        avps = [DiameterAVP(), OriginHostAVP("host.example.com"), "DiameterAVP()"]

        with self.assertRaises(DiameterMessageError) as cm: 
            message = DiameterMessage(header, avps)
        
        self.assertEqual(cm.exception.args[0], "invalid element found in list argument: 'avps'. The element DiameterAVP() in position 2 does not represent a DiameterAVP object")

    def test_diameter_message__valid_way_of_passing_avp_input_argument(self):
        header = DiameterHeader()
        avps = [DiameterAVP()]

        message = DiameterMessage(header, avps)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 1 AVP(s)>")

    def test_diameter_message__append_method__valid_way_to_call(self):
        header = DiameterHeader()

        origin_host_avp = OriginHostAVP("host.example.com")
        origin_realm_avp = OriginRealmAVP("example.com")

        avps = [origin_host_avp]

        message = DiameterMessage(header, avps)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 1 AVP(s)>")

        message.append(origin_realm_avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 2 AVP(s)>")

    def test_diameter_message__append_method__valid_way_to_call__two_or_more_avps_of_same_type(self):
        header = DiameterHeader()

        origin_host_avp = OriginHostAVP("host.example.com")
        origin_realm_avp = OriginRealmAVP("example.com")

        avps = [origin_host_avp]

        message = DiameterMessage(header, avps)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 1 AVP(s)>")
        self.assertEqual(message.origin_host_avp, origin_host_avp)

        message.append(origin_realm_avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 2 AVP(s)>")
        self.assertEqual(message.origin_realm_avp, origin_realm_avp)

        message.append(origin_host_avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 3 AVP(s)>")
        self.assertEqual(message.origin_host_avp__1, origin_host_avp)

        message.append(origin_realm_avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 4 AVP(s)>")
        self.assertEqual(message.origin_realm_avp__1, origin_realm_avp)

        message.append(origin_host_avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 5 AVP(s)>")
        self.assertEqual(message.origin_host_avp__2, origin_host_avp)

        message.append(origin_realm_avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 6 AVP(s)>")
        self.assertEqual(message.origin_realm_avp__2, origin_realm_avp)

    def test_diameter_message__append_method__valid_way_to_call__creating_cer_like_message(self):
        header = DiameterHeader()
        header.hop_by_hop = bytes.fromhex("00000072")
        header.end_to_end = bytes.fromhex("00000072")

        message = DiameterMessage(header)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 0 AVP(s)>")

        message.append(OriginHostAVP("hss.embratel.com"))
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 1 AVP(s)>")
        self.assertEqual(message.origin_host_avp, OriginHostAVP("hss.embratel.com"))

        message.append(OriginRealmAVP("embratel.com"))
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 2 AVP(s)>")
        self.assertEqual(message.origin_realm_avp, OriginRealmAVP("embratel.com"))

        message.append(HostIpAddressAVP("172.26.0.134"))
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 3 AVP(s)>")
        self.assertEqual(message.host_ip_address_avp, HostIpAddressAVP("172.26.0.134"))

        VENDOR = bytes.fromhex("000007db")
        message.append(VendorIdAVP(VENDOR))
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 4 AVP(s)>")
        self.assertEqual(message.vendor_id_avp, VendorIdAVP(VENDOR))

        message.append(ProductNameAVP("HSS9860"))
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 5 AVP(s)>")
        self.assertEqual(message.product_name_avp, ProductNameAVP("HSS9860"))

        message.append(InbandSecurityIdAVP(INBAND_SECURITY_ID_NO_SECURITY))
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 6 AVP(s)>")
        self.assertEqual(message.inband_security_id_avp, InbandSecurityIdAVP(INBAND_SECURITY_ID_NO_SECURITY))


        vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)

        auth_app_id_avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_Cx)
        avp = VendorSpecificApplicationIdAVP([vendor_id_avp, auth_app_id_avp])
        message.append(avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 7 AVP(s)>")
        self.assertEqual(message.vendor_specific_application_id_avp, avp)

        auth_app_id_avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_Sh)
        avp = VendorSpecificApplicationIdAVP([vendor_id_avp, auth_app_id_avp])
        message.append(avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 8 AVP(s)>")
        self.assertEqual(message.vendor_specific_application_id_avp__1, avp)

        auth_app_id_avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_S13_S13)
        avp = VendorSpecificApplicationIdAVP([vendor_id_avp, auth_app_id_avp])
        message.append(avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 9 AVP(s)>")
        self.assertEqual(message.vendor_specific_application_id_avp__2, avp)

        auth_app_id_avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)
        avp = VendorSpecificApplicationIdAVP([vendor_id_avp, auth_app_id_avp])
        message.append(avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 10 AVP(s)>")
        self.assertEqual(message.vendor_specific_application_id_avp__3, avp)

        auth_app_id_avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_SWx)
        avp = VendorSpecificApplicationIdAVP([vendor_id_avp, auth_app_id_avp])
        message.append(avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 11 AVP(s)>")
        self.assertEqual(message.vendor_specific_application_id_avp__4, avp)

        auth_app_id_avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_SLh)
        avp = VendorSpecificApplicationIdAVP([vendor_id_avp, auth_app_id_avp])
        message.append(avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 12 AVP(s)>")
        self.assertEqual(message.vendor_specific_application_id_avp__5, avp)

        auth_app_id_avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_Zh)
        avp = VendorSpecificApplicationIdAVP([vendor_id_avp, auth_app_id_avp])
        message.append(avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 13 AVP(s)>")
        self.assertEqual(message.vendor_specific_application_id_avp__6, avp)


        vendor_id_avp = VendorIdAVP(VENDOR)
        auth_app_id_avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_UNKNOWN)
        avp = VendorSpecificApplicationIdAVP([vendor_id_avp, auth_app_id_avp])
        message.append(avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 14 AVP(s)>")
        self.assertEqual(message.vendor_specific_application_id_avp__7, avp)

        FIRMWARE_REVISION = convert_to_4_bytes(0)
        message.append(FirmwareRevisionAVP(FIRMWARE_REVISION))
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 15 AVP(s)>")
        self.assertEqual(message.firmware_revision_avp, FirmwareRevisionAVP(FIRMWARE_REVISION))


        message.header.command_code = CAPABILITIES_EXCHANGE_MESSAGE
        self.assertEqual(message.__str__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 15 AVP(s)>")
        
        message.header.application_id = DIAMETER_APPLICATION_DEFAULT
        self.assertEqual(message.__str__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 15 AVP(s)>")

        message.header.set_request_bit(True)
        self.assertEqual(message.__str__(), "<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 15 AVP(s)>")


        #: Loading a well-known CER message from a byte stream.
        _stream = bytes.fromhex("010001848000010100000000000000720000007200000108400000186873732e656d62726174656c2e636f6d0000012840000014656d62726174656c2e636f6d000001014000000e0001ac1a008600000000010a4000000c000007db0000010d0000000f48535339383630000000012b4000000c0000000000000104400000200000010a4000000c000028af000001024000000c0100000000000104400000200000010a4000000c000028af000001024000000c0100000100000104400000200000010a4000000c000028af000001024000000c0100002400000104400000200000010a4000000c000028af000001024000000c0100002300000104400000200000010a4000000c000028af000001024000000c0100003100000104400000200000010a4000000c000028af000001024000000c0100004b00000104400000200000010a4000000c000028af000001024000000c0100000500000104400000200000010a4000000c000007db000001024000000cf5c6f5150000010b0000000c00000000")
        cer = DiameterMessage.load(_stream)[0]

        #: Comparing the CER object with the Custom DiameterMessage object.
        self.assertEqual(message, cer)
        self.assertTrue(isinstance(cer, DiameterMessage))
        self.assertTrue(isinstance(message, DiameterMessage))

    def test_diameter_message__pop_method__valid_way_to_call(self):
        header = DiameterHeader()

        origin_host_avp = OriginHostAVP("host.example.com")
        origin_realm_avp = OriginRealmAVP("example.com")

        avps = [origin_host_avp]
        message = DiameterMessage(header, avps)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 1 AVP(s)>")

        message.append(origin_realm_avp)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 2 AVP(s)>")

        message.pop("origin_host_avp")
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 1 AVP(s)>")

        message.pop("origin_realm_avp")
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 0 AVP(s)>")

        with self.assertRaises(DiameterMessageError) as cm:
            message.pop("origin_realm_avp")
        
        self.assertEqual(cm.exception.args[0], "`avps` attribute is empty. There is no DiameterAVP object to be removed")

    def test_diameter_message__cleanup_method_after_appending_2_avps(self):
        origin_host_avp = OriginHostAVP("host.example.com")
        origin_realm_avp = OriginRealmAVP("example.com")        
        avps = [origin_host_avp, origin_realm_avp]

        message = DiameterMessage(avps=avps)
        self.assertEqual(len(message), 64)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 2 AVP(s)>")
        self.assertEqual(message.origin_host_avp.__str__(), "<Diameter AVP: 264 [Origin-Host] MANDATORY>")
        self.assertEqual(message.origin_realm_avp.__str__(), "<Diameter AVP: 296 [Origin-Realm] MANDATORY>")

        message.cleanup()
        self.assertEqual(len(message), 20)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 0 AVP(s)>")

        with self.assertRaises(AttributeError) as cm:
            message.origin_host_avp
        self.assertEqual(cm.exception.args[0], "'DiameterMessage' object has no attribute 'origin_host_avp'")

        with self.assertRaises(AttributeError) as cm:
            message.origin_realm_avp
        self.assertEqual(cm.exception.args[0], "'DiameterMessage' object has no attribute 'origin_realm_avp'")

    def test_diameter_message__cleanup_method_after_appending_3_avps(self):
        origin_host_avp = OriginHostAVP("host.example.com")
        origin_realm_avp = OriginRealmAVP("example.com")
        origin_state_id_avp = OriginStateIdAVP(1524733202)

        avps = [origin_host_avp, origin_realm_avp, origin_state_id_avp]

        message = DiameterMessage(avps=avps)
        self.assertEqual(len(message), 76)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 3 AVP(s)>")
        self.assertEqual(message.origin_host_avp.__str__(), "<Diameter AVP: 264 [Origin-Host] MANDATORY>")
        self.assertEqual(message.origin_realm_avp.__str__(), "<Diameter AVP: 296 [Origin-Realm] MANDATORY>")
        self.assertEqual(message.origin_state_id_avp.__str__(), "<Diameter AVP: 278 [Origin-State-Id] MANDATORY>")

        message.cleanup()
        self.assertEqual(len(message), 20)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 0 AVP(s)>")

        with self.assertRaises(AttributeError) as cm:
            message.origin_host_avp
        self.assertEqual(cm.exception.args[0], "'DiameterMessage' object has no attribute 'origin_host_avp'")

        with self.assertRaises(AttributeError) as cm:
            message.origin_realm_avp
        self.assertEqual(cm.exception.args[0], "'DiameterMessage' object has no attribute 'origin_realm_avp'")

        with self.assertRaises(AttributeError) as cm:
            message.origin_state_id_avp
        self.assertEqual(cm.exception.args[0], "'DiameterMessage' object has no attribute 'origin_state_id_avp'")

    def test_diameter_message__extend_method__valid_way_to_call__3_avps(self):
        origin_host_avp = OriginHostAVP("host.example.com")
        origin_realm_avp = OriginRealmAVP("example.com")
        origin_state_id_avp = OriginStateIdAVP(1524733202)

        avps = [origin_host_avp, origin_realm_avp, origin_state_id_avp]

        message = DiameterMessage()
        self.assertEqual(len(message), 20)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 0 AVP(s)>")

        message.extend(avps)
        self.assertEqual(len(message), 76)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 3 AVP(s)>")
        self.assertEqual(message.origin_host_avp.__str__(), "<Diameter AVP: 264 [Origin-Host] MANDATORY>")
        self.assertEqual(message.origin_realm_avp.__str__(), "<Diameter AVP: 296 [Origin-Realm] MANDATORY>")
        self.assertEqual(message.origin_state_id_avp.__str__(), "<Diameter AVP: 278 [Origin-State-Id] MANDATORY>")

    def test_diameter_message__extend_method__valid_way_to_call__5_avps(self):
        origin_host_avp = OriginHostAVP("host.example.com")
        origin_realm_avp = OriginRealmAVP("example.com")
        origin_state_id_avp = OriginStateIdAVP(1524733202)
        auth_session_state_avp = AuthSessionStateAVP(STATE_MAINTAINED)
        auth_request_type_avp = AuthRequestTypeAVP(AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY)
        
        avps = [origin_host_avp, origin_realm_avp, origin_state_id_avp, auth_session_state_avp, auth_request_type_avp]

        message = DiameterMessage()
        self.assertEqual(len(message), 20)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 0 AVP(s)>")

        message.extend(avps)
        self.assertEqual(len(message), 100)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 5 AVP(s)>")
        self.assertEqual(message.origin_host_avp.__str__(), "<Diameter AVP: 264 [Origin-Host] MANDATORY>")
        self.assertEqual(message.origin_realm_avp.__str__(), "<Diameter AVP: 296 [Origin-Realm] MANDATORY>")
        self.assertEqual(message.origin_state_id_avp.__str__(), "<Diameter AVP: 278 [Origin-State-Id] MANDATORY>")
        self.assertEqual(message.auth_session_state_avp.__str__(), "<Diameter AVP: 277 [Auth-Session-State] MANDATORY>")
        self.assertEqual(message.auth_request_type_avp.__str__(), "<Diameter AVP: 274 [Auth-Request-Type] MANDATORY>")

    def test_diameter_message__has_avp_method__valid_way_to_call__1(self):
        origin_host_avp = OriginHostAVP("host.example.com")
        origin_realm_avp = OriginRealmAVP("example.com")
        avps = [origin_host_avp, origin_realm_avp]

        message = DiameterMessage()
        self.assertEqual(len(message), 20)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 0 AVP(s)>")
        self.assertFalse(message.has_avp("origin_host_avp"))
        self.assertFalse(message.has_avp("origin_realm_avp"))

        message.append(origin_host_avp)
        self.assertEqual(len(message), 44)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 1 AVP(s)>")
        self.assertEqual(message.origin_host_avp.__str__(), "<Diameter AVP: 264 [Origin-Host] MANDATORY>")
        self.assertTrue(message.has_avp("origin_host_avp"))
        self.assertFalse(message.has_avp("origin_realm_avp"))

        message.append(origin_realm_avp)
        self.assertEqual(len(message), 64)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 2 AVP(s)>")
        self.assertEqual(message.origin_realm_avp.__str__(), "<Diameter AVP: 296 [Origin-Realm] MANDATORY>")
        self.assertTrue(message.has_avp("origin_host_avp"))
        self.assertTrue(message.has_avp("origin_realm_avp"))


    def test_diameter_message__has_avp_method__valid_way_to_call__2(self):
        auth_session_state_avp = AuthSessionStateAVP(STATE_MAINTAINED)
        auth_request_type_avp = AuthRequestTypeAVP(AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY)
        avps = [auth_session_state_avp, auth_request_type_avp]

        message = DiameterMessage(avps=avps)
        self.assertEqual(len(message), 44)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 2 AVP(s)>")
        self.assertEqual(message.auth_session_state_avp.__str__(), "<Diameter AVP: 277 [Auth-Session-State] MANDATORY>")
        self.assertEqual(message.auth_request_type_avp.__str__(), "<Diameter AVP: 274 [Auth-Request-Type] MANDATORY>")
        self.assertTrue(message.has_avp("auth_session_state_avp"))
        self.assertTrue(message.has_avp("auth_request_type_avp"))
        
        self.assertFalse(message.has_avp("origin_host_avp"))
        self.assertFalse(message.has_avp("origin_realm_avp"))
        self.assertFalse(message.has_avp("origin_state_id_avp"))

    def test_diameter_message__has_avp_method__invalid_way_to_call__1(self):
        auth_request_type_avp = AuthRequestTypeAVP(AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY)

        message = DiameterMessage()
        message.extend([auth_request_type_avp, auth_request_type_avp])

        self.assertEqual(len(message), 44)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 2 AVP(s)>")
        self.assertEqual(message.auth_request_type_avp.__str__(), "<Diameter AVP: 274 [Auth-Request-Type] MANDATORY>")
        self.assertEqual(message.auth_request_type_avp__1.__str__(), "<Diameter AVP: 274 [Auth-Request-Type] MANDATORY>")

        self.assertTrue(message.has_avp("auth_request_type_avp"))
        self.assertTrue(message.has_avp("auth_request_type_avp__1"))

        self.assertFalse(message.has_avp("auth_request_type"))
        self.assertFalse(message.has_avp("auth_request_type__1"))
        self.assertFalse(message.has_avp("auth_request_type_avp1"))
        self.assertFalse(message.has_avp("auth_request_type_avp_1"))

        with self.assertRaises(DiameterMessageError) as cm:
            message.has_avp(1)

        self.assertEqual(cm.exception.args[0], "`avp_key` must be str")

    def test_diameter_message__has_avp_method__invalid_way_to_call__2(self):
        auth_request_type_avp = AuthRequestTypeAVP(AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY)

        message = DiameterMessage()
        message.extend([auth_request_type_avp, auth_request_type_avp])

        self.assertEqual(len(message), 44)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 2 AVP(s)>")
        self.assertEqual(message.auth_request_type_avp.__str__(), "<Diameter AVP: 274 [Auth-Request-Type] MANDATORY>")
        self.assertEqual(message.auth_request_type_avp__1.__str__(), "<Diameter AVP: 274 [Auth-Request-Type] MANDATORY>")

        with self.assertRaises(DiameterMessageError) as cm:
            message.has_avp(auth_request_type_avp)

        self.assertEqual(cm.exception.args[0], "`avp_key` must be str")

    def test_diameter_message__update_key_method__valid_way_to_call__1(self):
        disconnect_cause_avp = DisconnectCauseAVP(DISCONNECT_CAUSE_REBOOTING)

        message = DiameterMessage()
        message.append(disconnect_cause_avp)

        self.assertEqual(len(message), 32)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 1 AVP(s)>")
        self.assertEqual(message.disconnect_cause_avp.__str__(), "<Diameter AVP: 273 [Disconnect-Cause] MANDATORY>")

        message.update_key("disconnect_cause_avp", "disconnect_cause")

        self.assertEqual(len(message), 32)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 1 AVP(s)>")
        self.assertEqual(message.disconnect_cause.__str__(), "<Diameter AVP: 273 [Disconnect-Cause] MANDATORY>")

        with self.assertRaises(AttributeError) as cm:
            message.disconnect_cause_avp.__str__()
        self.assertEqual(cm.exception.args[0], "'DiameterMessage' object has no attribute 'disconnect_cause_avp'")

    def test_diameter_message__update_key_method__valid_way_to_call__2(self):
        result_code_avp = ResultCodeAVP(DIAMETER_INVALID_MESSAGE_LENGTH)

        avps = 3*[result_code_avp]

        message = DiameterMessage()
        message.extend(avps)

        self.assertEqual(len(message), 56)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 3 AVP(s)>")
        self.assertEqual(message.result_code_avp.__str__(), "<Diameter AVP: 268 [Result-Code] MANDATORY>")
        self.assertEqual(message.result_code_avp__1.__str__(), "<Diameter AVP: 268 [Result-Code] MANDATORY>")
        self.assertEqual(message.result_code_avp__2.__str__(), "<Diameter AVP: 268 [Result-Code] MANDATORY>")

        message.update_key("result_code_avp", "result_code0")
        message.update_key("result_code_avp__1", "result_code1")
        message.update_key("result_code_avp__2", "result_code2")

        self.assertEqual(len(message), 56)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 3 AVP(s)>")
        self.assertEqual(message.result_code0.__str__(), "<Diameter AVP: 268 [Result-Code] MANDATORY>")
        self.assertEqual(message.result_code1.__str__(), "<Diameter AVP: 268 [Result-Code] MANDATORY>")
        self.assertEqual(message.result_code2.__str__(), "<Diameter AVP: 268 [Result-Code] MANDATORY>")

        with self.assertRaises(AttributeError) as cm:
            message.result_code_avp
            self.assertEqual(cm.exception.args[0], "'DiameterMessage' object has no attribute 'result_code_avp'")

        with self.assertRaises(AttributeError) as cm:
            message.result_code_avp__1
            self.assertEqual(cm.exception.args[0], "'DiameterMessage' object has no attribute 'result_code_avp__1'")

        with self.assertRaises(AttributeError) as cm:
            message.result_code_avp__2
            self.assertEqual(cm.exception.args[0], "'DiameterMessage' object has no attribute 'result_code_avp__2'")

    def test_diameter_message__update_key_method__valid_way_to_call__3(self):
        vendor_id_avp = VendorIdAVP()

        message = DiameterMessage(avps=[vendor_id_avp])
        self.assertEqual(len(message), 32)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 1 AVP(s)>")
        self.assertEqual(message.vendor_id_avp.__str__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")

        message.update_key("vendor_id_avp", "vendor_id_avp__1")

        self.assertEqual(message.vendor_id_avp__1.__str__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")

        with self.assertRaises(AttributeError) as cm:
            message.vendor_id_avp
            self.assertEqual(cm.exception.args[0], "'DiameterMessage' object has no attribute 'vendor_id_avp'")

        message.append(vendor_id_avp)

        self.assertEqual(len(message), 44)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 2 AVP(s)>")
        self.assertEqual(message.vendor_id_avp__1.__str__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")
        self.assertEqual(message.vendor_id_avp.__str__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")

        message.append(vendor_id_avp)

        self.assertEqual(len(message), 56)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 3 AVP(s)>")
        self.assertEqual(message.vendor_id_avp__1.__str__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")
        self.assertEqual(message.vendor_id_avp.__str__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")
        self.assertEqual(message.vendor_id_avp__2.__str__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")

        message.update_key("vendor_id_avp", "vendor_id_avp__3")

        self.assertEqual(message.vendor_id_avp__3.__str__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")

        with self.assertRaises(AttributeError) as cm:
            message.vendor_id_avp
            self.assertEqual(cm.exception.args[0], "'DiameterMessage' object has no attribute 'vendor_id_avp'")


    def test_diameter_message__update_key_method__invalid_way_to_call(self):
        firmware_revision_avp = FirmwareRevisionAVP(1234)

        message = DiameterMessage()
        message.append(firmware_revision_avp)

        self.assertEqual(len(message), 32)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 1 AVP(s)>")
        self.assertEqual(message.firmware_revision_avp.__str__(), "<Diameter AVP: 267 [Firmware-Revision]>")

        message.append(firmware_revision_avp)

        self.assertEqual(len(message), 44)
        self.assertEqual(message.__str__(), "<Diameter Message: Unknown [], 0 [Diameter common message], 2 AVP(s)>")
        self.assertEqual(message.firmware_revision_avp.__str__(), "<Diameter AVP: 267 [Firmware-Revision]>")
        self.assertEqual(message.firmware_revision_avp__1.__str__(), "<Diameter AVP: 267 [Firmware-Revision]>")

        message.update_key("firmware_revision_avp", "firmware0")
        message.update_key("firmware_revision_avp__1", "firmware1")

        self.assertEqual(message.firmware0.__str__(), "<Diameter AVP: 267 [Firmware-Revision]>")
        self.assertEqual(message.firmware1.__str__(), "<Diameter AVP: 267 [Firmware-Revision]>")

        with self.assertRaises(DiameterMessageError) as cm:
            message.update_key("firmware1", "firmware0")
        
        self.assertEqual(cm.exception.args[0], "`firmware0` key already defined")


if __name__ == "__main__":
    unittest.main()