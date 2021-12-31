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

from bromelia.__version__ import __version__
from bromelia._internal_utils import _convert_config_to_connection_obj
from bromelia.avps import *
from bromelia.base import *
from bromelia.constants import *
from bromelia.proxy import DiameterBaseProxy


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

    def test_diameter_message__refresh_method__1(self):
        header = DiameterHeader()

        origin_host_avp = OriginHostAVP("host.example.com")
        origin_realm_avp = OriginRealmAVP("example.com")
        avps = [origin_host_avp, origin_realm_avp]

        message = DiameterMessage(header, avps)

        #: Check Diameter Header
        self.assertEqual(message.dump().hex(), "01000040000000000000000000000000000000000000010840000018686f73742e6578616d706c652e636f6d00000128400000136578616d706c652e636f6d00")
        self.assertEqual(message.header.version, DIAMETER_VERSION)
        self.assertEqual(message.header.flags, FLAG_RESPONSE)
        self.assertEqual(message.header.get_length(), 64)
        self.assertEqual(message.header.command_code, DIAMETER_UNKNOWN_COMMAND_CODE)
        self.assertEqual(message.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(message.avps[0].dump().hex(), "0000010840000018686f73742e6578616d706c652e636f6d")
        self.assertEqual(message.avps[0].get_length(), 24)
        self.assertEqual(message.avps[0].data, b"host.example.com")

        #: Origin-Realm AVP
        self.assertEqual(message.avps[1].dump().hex(), "00000128400000136578616d706c652e636f6d00")
        self.assertEqual(message.avps[1].get_length(), 19)
        self.assertEqual(message.avps[1].data, b"example.com")

        #: Update Origin-Host & Origin-Realm AVPs
        message.origin_host_avp.data = "new_host.new_example.com"
        message.origin_realm_avp.data = "new_example.com"

        #: Origin-Host AVP updated
        self.assertEqual(message.avps[0].dump().hex(), "00000108400000206e65775f686f73742e6e65775f6578616d706c652e636f6d")
        self.assertEqual(message.avps[0].get_length(), 32)
        self.assertEqual(message.avps[0].data, b"new_host.new_example.com")

        #: Origin-Realm AVP updated
        self.assertEqual(message.avps[1].dump().hex(), "00000128400000176e65775f6578616d706c652e636f6d00")
        self.assertEqual(message.avps[1].get_length(), 23)
        self.assertEqual(message.avps[1].data, b"new_example.com")

        #: In order to update the length field with the new value
        message.refresh()
        self.assertEqual(message.header.get_length(), 76) # instead the previous 64
        self.assertEqual(len(message), 76) # instead the previous 64

        #: If pop a given DiameterAVP object, there is no need to refresh
        message.pop("origin_host_avp")
        self.assertEqual(message.header.get_length(), 44)
        self.assertEqual(len(message), 44)

        #: If append a given DiameterAVP object, there is no need to refresh
        message.append(origin_host_avp)
        self.assertEqual(message.header.get_length(), 76)
        self.assertEqual(len(message), 76)

        #: If cleanup all DiameterAVP objects, there is no need to refresh
        message.cleanup()
        self.assertEqual(message.header.get_length(), 20)
        self.assertEqual(len(message), 20)

        #: If extend DiameterAVP objects, there is no need to refresh
        message.extend([origin_host_avp, origin_realm_avp])
        self.assertEqual(message.header.get_length(), 76)
        self.assertEqual(len(message), 76)

    def test_diameter_message__refresh_method__2(self):
        stream = bytes.fromhex("01000040000000000000000000000000000000000000010840000018686f73742e6578616d706c652e636f6d00000128400000136578616d706c652e636f6d00")
        messages = DiameterMessage.load(stream)
        message = messages[0]

        #: Check Diameter Header
        self.assertEqual(message.dump().hex(), "01000040000000000000000000000000000000000000010840000018686f73742e6578616d706c652e636f6d00000128400000136578616d706c652e636f6d00")
        self.assertEqual(message.header.version, DIAMETER_VERSION)
        self.assertEqual(message.header.flags, FLAG_RESPONSE)
        self.assertEqual(message.header.get_length(), 64)
        self.assertEqual(message.header.command_code, DIAMETER_UNKNOWN_COMMAND_CODE)
        self.assertEqual(message.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(message.avps[0].dump().hex(), "0000010840000018686f73742e6578616d706c652e636f6d")
        self.assertEqual(message.avps[0].get_length(), 24)
        self.assertEqual(message.avps[0].data, b"host.example.com")

        #: Origin-Realm AVP
        self.assertEqual(message.avps[1].dump().hex(), "00000128400000136578616d706c652e636f6d00")
        self.assertEqual(message.avps[1].get_length(), 19)
        self.assertEqual(message.avps[1].data, b"example.com")

        #: Update Origin-Host & Origin-Realm AVPs
        message.origin_host_avp.data = "new_host.new_example.com"
        message.origin_realm_avp.data = "new_example.com"

        #: Origin-Host & Origin-Realm AVPs
        origin_host_avp = message.origin_host_avp
        origin_realm_avp = message.origin_realm_avp

        #: Origin-Host AVP updated
        self.assertEqual(message.avps[0].dump().hex(), "00000108400000206e65775f686f73742e6e65775f6578616d706c652e636f6d")
        self.assertEqual(message.avps[0].get_length(), 32)
        self.assertEqual(message.avps[0].data, b"new_host.new_example.com")

        #: Origin-Realm AVP updated
        self.assertEqual(message.avps[1].dump().hex(), "00000128400000176e65775f6578616d706c652e636f6d00")
        self.assertEqual(message.avps[1].get_length(), 23)
        self.assertEqual(message.avps[1].data, b"new_example.com")

        #: In order to update the length field with the new value
        message.refresh()
        self.assertEqual(message.header.get_length(), 76) # instead the previous 64
        self.assertEqual(len(message), 76) # instead the previous 64

        #: If pop a given DiameterAVP object, there is no need to refresh
        message.pop("origin_host_avp")
        self.assertEqual(message.header.get_length(), 44)
        self.assertEqual(len(message), 44)

        #: If append a given DiameterAVP object, there is no need to refresh
        message.append(origin_host_avp)
        self.assertEqual(message.header.get_length(), 76)
        self.assertEqual(len(message), 76)

        #: If cleanup all DiameterAVP objects, there is no need to refresh
        message.cleanup()
        self.assertEqual(message.header.get_length(), 20)
        self.assertEqual(len(message), 20)

        #: If extend DiameterAVP objects, there is no need to refresh
        message.extend([origin_host_avp, origin_realm_avp])
        self.assertEqual(message.header.get_length(), 76)
        self.assertEqual(len(message), 76)

    def test_diameter_message__refresh_method__3(self):
        stream = bytes.fromhex("010001a0c000013e01000023116846741168467400000107400000516d6d652e6570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b393430343633393834000000000001154000000c00000001000001084000002d6d6d652e6570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f726700000000000128400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72670000000000011b400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72670000000000000140000017373234303031313131313131313131000000057fc000000f000028af27f4500000000104400000200000010a4000000c000028af000001024000000c010000230000012540000030687373736d322e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f726700000580c000002c000028af00000582c0000010000028af0000000200000584c0000010000028af00000001")
        messages = DiameterMessage.load(stream)
        message = messages[0]

        #: Check Diameter Header
        self.assertEqual(message.dump().hex(), "010001a0c000013e01000023116846741168467400000107400000516d6d652e6570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b393430343633393834000000000001154000000c00000001000001084000002d6d6d652e6570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f726700000000000128400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72670000000000011b400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72670000000000000140000017373234303031313131313131313131000000057fc000000f000028af27f4500000000104400000200000010a4000000c000028af000001024000000c010000230000012540000030687373736d322e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f726700000580c000002c000028af00000582c0000010000028af0000000200000584c0000010000028af00000001")
        self.assertEqual(message.header.version, DIAMETER_VERSION)
        self.assertEqual(message.header.flags, FLAG_REQUEST_AND_PROXYABLE)
        self.assertEqual(message.header.length.hex(), "0001a0")
        self.assertEqual(message.header.get_length(), 416)
        self.assertEqual(message.header.command_code, AUTHENTICATION_INFORMATION_MESSAGE)
        self.assertEqual(message.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Session-Id AVP
        self.assertEqual(message.session_id_avp.dump().hex(), "00000107400000516d6d652e6570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b393430343633393834000000")
        self.assertEqual(message.avps[0].dump().hex(), "00000107400000516d6d652e6570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b393430343633393834000000")
        self.assertEqual(message.avps[0].code, SESSION_ID_AVP_CODE)
        self.assertEqual(message.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[0].vendor_id)
        self.assertEqual(message.avps[0].length.hex(), "000051")
        self.assertEqual(message.avps[0].get_length(), 81)
        self.assertEqual(message.avps[0].data, b"mme.epc.mnc000.mcc724.3gppnetwork.org;1559529822;356549175;2.17;940463984")
        self.assertEqual(message.avps[0].get_padding_length(), 3)

        #: Auth-Session-State AVP
        self.assertEqual(message.auth_session_state_avp.dump().hex(), "000001154000000c00000001")
        self.assertEqual(message.avps[1].dump().hex(), "000001154000000c00000001")
        self.assertEqual(message.avps[1].code, AUTH_SESSION_STATE_AVP_CODE)
        self.assertEqual(message.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[1].vendor_id)
        self.assertEqual(message.avps[1].length.hex(), "00000c")
        self.assertEqual(message.avps[1].get_length(), 12)
        self.assertEqual(message.avps[1].data, NO_STATE_MAINTAINED)
        self.assertIsNone(message.avps[1].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(message.origin_host_avp.dump().hex(), "000001084000002d6d6d652e6570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f7267000000")
        self.assertEqual(message.avps[2].dump().hex(), "000001084000002d6d6d652e6570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f7267000000")
        self.assertEqual(message.avps[2].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(message.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[2].vendor_id)
        self.assertEqual(message.avps[2].length.hex(), "00002d")
        self.assertEqual(message.avps[2].get_length(), 45)
        self.assertEqual(message.avps[2].data, b"mme.epc.mnc000.mcc724.3gppnetwork.org")
        self.assertEqual(message.avps[2].get_padding_length(), 3)

        #: Origin-Realm AVP
        self.assertEqual(message.origin_realm_avp.dump().hex(), "00000128400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f7267000000")
        self.assertEqual(message.avps[3].dump().hex(), "00000128400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f7267000000")
        self.assertEqual(message.avps[3].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(message.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[3].vendor_id)
        self.assertEqual(message.avps[3].length.hex(), "000029")
        self.assertEqual(message.avps[3].get_length(), 41)
        self.assertEqual(message.avps[3].data, b"epc.mnc000.mcc724.3gppnetwork.org")
        self.assertEqual(message.avps[3].get_padding_length(), 3)

        #: Destination-Realm AVP
        self.assertEqual(message.destination_realm_avp.dump().hex(), "0000011b400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f7267000000")
        self.assertEqual(message.avps[4].dump().hex(), "0000011b400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f7267000000")
        self.assertEqual(message.avps[4].code, DESTINATION_REALM_AVP_CODE)
        self.assertEqual(message.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[4].vendor_id)
        self.assertEqual(message.avps[4].length.hex(), "000029")
        self.assertEqual(message.avps[4].get_length(), 41)
        self.assertEqual(message.avps[4].data, b"epc.mnc000.mcc724.3gppnetwork.org")
        self.assertEqual(message.avps[4].get_padding_length(), 3)

        #: User-Name AVP
        self.assertEqual(message.user_name_avp.dump().hex(), "000000014000001737323430303131313131313131313100")
        self.assertEqual(message.avps[5].dump().hex(), "000000014000001737323430303131313131313131313100")
        self.assertEqual(message.avps[5].code, USER_NAME_AVP_CODE)
        self.assertEqual(message.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[5].vendor_id)
        self.assertEqual(message.avps[5].length.hex(), "000017")
        self.assertEqual(message.avps[5].get_length(), 23)
        self.assertEqual(message.avps[5].data, b"724001111111111")
        self.assertEqual(message.avps[5].get_padding_length(), 1)

        #: Visited-PLMN-Id AVP
        self.assertEqual(message.visited_plmn_id_avp.dump().hex(), "0000057fc000000f000028af27f45000")
        self.assertEqual(message.avps[6].dump().hex(), "0000057fc000000f000028af27f45000")
        self.assertEqual(message.avps[6].code, VISITED_PLMN_ID_AVP_CODE)
        self.assertEqual(message.avps[6].flags, FLAG_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertEqual(message.avps[6].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(message.avps[6].length.hex(), "00000f")
        self.assertEqual(message.avps[6].get_length(), 15)
        self.assertEqual(message.avps[6].data.hex(), "27f450")
        self.assertEqual(message.avps[6].get_padding_length(), 1)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(message.vendor_specific_application_id_avp.dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000023")
        self.assertEqual(message.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000023")
        self.assertEqual(message.avps[7].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(message.avps[7].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[7].vendor_id)
        self.assertEqual(message.avps[7].length.hex(), "000020")
        self.assertEqual(message.avps[7].get_length(), 32)
        self.assertEqual(message.avps[7].data.hex(), "0000010a4000000c000028af000001024000000c01000023")
        self.assertIsNone(message.avps[7].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(message.avps[7].vendor_id_avp.dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(message.avps[7].avps[0].dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(message.avps[7].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(message.avps[7].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[7].avps[0].vendor_id)
        self.assertEqual(message.avps[7].avps[0].length.hex(), "00000c")
        self.assertEqual(message.avps[7].avps[0].get_length(), 12)
        self.assertEqual(message.avps[7].avps[0].data, VENDOR_ID_3GPP)
        self.assertIsNone(message.avps[7].avps[0].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(message.avps[7].auth_application_id_avp.dump().hex(), "000001024000000c01000023")
        self.assertEqual(message.avps[7].avps[1].dump().hex(), "000001024000000c01000023")
        self.assertEqual(message.avps[7].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(message.avps[7].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[7].avps[1].vendor_id)
        self.assertEqual(message.avps[7].avps[0].length.hex(), "00000c")
        self.assertEqual(message.avps[7].avps[1].get_length(), 12)
        self.assertEqual(message.avps[7].avps[1].data, DIAMETER_APPLICATION_S6a)
        self.assertIsNone(message.avps[7].avps[1].get_padding_length())

        #: Destination-Host AVP
        self.assertEqual(message.destination_host_avp.dump().hex(), "0000012540000030687373736d322e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f7267")
        self.assertEqual(message.avps[8].dump().hex(), "0000012540000030687373736d322e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f7267")
        self.assertEqual(message.avps[8].code, DESTINATION_HOST_AVP_CODE)
        self.assertEqual(message.avps[8].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[8].vendor_id)
        self.assertEqual(message.avps[8].length.hex(), "000030")
        self.assertEqual(message.avps[8].get_length(), 48)
        self.assertEqual(message.avps[8].data, b"hsssm2.epc.mnc005.mcc724.3gppnetwork.org")
        self.assertIsNone(message.avps[8].get_padding_length())

        #: Request-EUTRAN-Authentication-Info AVP
        self.assertEqual(message.requested_eutran_authentication_info_avp.dump().hex(), "00000580c000002c000028af00000582c0000010000028af0000000200000584c0000010000028af00000001")
        self.assertEqual(message.avps[9].dump().hex(), "00000580c000002c000028af00000582c0000010000028af0000000200000584c0000010000028af00000001")
        self.assertEqual(message.avps[9].code, REQUESTED_EUTRAN_AUTHENTICATION_INFO_AVP_CODE)
        self.assertEqual(message.avps[9].flags, FLAG_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertEqual(message.avps[9].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(message.avps[9].length.hex(), "00002c")
        self.assertEqual(message.avps[9].get_length(), 44)
        self.assertEqual(message.avps[9].data.hex(), "00000582c0000010000028af0000000200000584c0000010000028af00000001")
        self.assertIsNone(message.avps[9].get_padding_length())

        ##: Now we are going to make a few changes

        #: Update Origin-Host AVP
        message.origin_host_avp.data = "mme.epc.3gppnetwork.org"

        self.assertEqual(message.origin_host_avp.dump().hex(), "000001084000001f6d6d652e6570632e336770706e6574776f726b2e6f726700")
        self.assertEqual(message.avps[2].dump().hex(), "000001084000001f6d6d652e6570632e336770706e6574776f726b2e6f726700")
        self.assertEqual(message.avps[2].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(message.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[2].vendor_id)
        self.assertEqual(message.avps[2].length.hex(), "00001f")
        self.assertEqual(message.avps[2].get_length(), 31)
        self.assertEqual(message.avps[2].data, b"mme.epc.3gppnetwork.org")
        self.assertEqual(message.avps[2].get_padding_length(), 1)

        #: See the needed to refresh it. Before call it the length is wrong if 
        #: you try to access through the Header object
        self.assertEqual(message.header.length.hex(), "0001a0")
        self.assertEqual(message.header.get_length(), 416)
        self.assertEqual(len(message.header), 416)
        self.assertEqual(message.dump().hex(), "010001a0c000013e01000023116846741168467400000107400000516d6d652e6570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b393430343633393834000000000001154000000c00000001000001084000001f6d6d652e6570632e336770706e6574776f726b2e6f72670000000128400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72670000000000011b400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72670000000000000140000017373234303031313131313131313131000000057fc000000f000028af27f4500000000104400000200000010a4000000c000028af000001024000000c010000230000012540000030687373736d322e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f726700000580c000002c000028af00000582c0000010000028af0000000200000584c0000010000028af00000001")

        message.refresh()

        self.assertEqual(message.header.length.hex(), "000190")
        self.assertEqual(message.header.get_length(), 400)
        self.assertEqual(len(message.header), 400)
        self.assertEqual(message.dump().hex(), "01000190c000013e01000023116846741168467400000107400000516d6d652e6570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b393430343633393834000000000001154000000c00000001000001084000001f6d6d652e6570632e336770706e6574776f726b2e6f72670000000128400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72670000000000011b400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72670000000000000140000017373234303031313131313131313131000000057fc000000f000028af27f4500000000104400000200000010a4000000c000028af000001024000000c010000230000012540000030687373736d322e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f726700000580c000002c000028af00000582c0000010000028af0000000200000584c0000010000028af00000001")


        #: Update Origin-Realm AVP
        message.origin_realm_avp.data = "epc.3gppnetwork.org"

        self.assertEqual(message.origin_realm_avp.dump().hex(), "000001284000001b6570632e336770706e6574776f726b2e6f726700")
        self.assertEqual(message.avps[3].dump().hex(), "000001284000001b6570632e336770706e6574776f726b2e6f726700")
        self.assertEqual(message.avps[3].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(message.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[3].vendor_id)
        self.assertEqual(message.avps[3].length.hex(), "00001b")
        self.assertEqual(message.avps[3].get_length(), 27)
        self.assertEqual(message.avps[3].data, b"epc.3gppnetwork.org")
        self.assertEqual(message.avps[3].get_padding_length(), 1)

        #: See the needed to refresh it. Before call it the length is wrong if 
        #: you try to access through the Header object
        self.assertEqual(message.header.length.hex(), "000190")
        self.assertEqual(message.header.get_length(), 400)
        self.assertEqual(len(message.header), 400)
        self.assertEqual(message.dump().hex(), "01000190c000013e01000023116846741168467400000107400000516d6d652e6570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b393430343633393834000000000001154000000c00000001000001084000001f6d6d652e6570632e336770706e6574776f726b2e6f726700000001284000001b6570632e336770706e6574776f726b2e6f7267000000011b400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72670000000000000140000017373234303031313131313131313131000000057fc000000f000028af27f4500000000104400000200000010a4000000c000028af000001024000000c010000230000012540000030687373736d322e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f726700000580c000002c000028af00000582c0000010000028af0000000200000584c0000010000028af00000001")

        message.refresh()

        self.assertEqual(message.header.length.hex(), "000180")
        self.assertEqual(message.header.get_length(), 384)
        self.assertEqual(len(message.header), 384)
        self.assertEqual(message.dump().hex(), "01000180c000013e01000023116846741168467400000107400000516d6d652e6570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b393430343633393834000000000001154000000c00000001000001084000001f6d6d652e6570632e336770706e6574776f726b2e6f726700000001284000001b6570632e336770706e6574776f726b2e6f7267000000011b400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72670000000000000140000017373234303031313131313131313131000000057fc000000f000028af27f4500000000104400000200000010a4000000c000028af000001024000000c010000230000012540000030687373736d322e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f726700000580c000002c000028af00000582c0000010000028af0000000200000584c0000010000028af00000001")


        #: Update Session-Id AVP
        message.session_id_avp.data = "mme.epc.3gppnetwork.org;1559529822;356549175;2.17;940463984"

        self.assertEqual(message.session_id_avp.dump().hex(), "00000107400000436d6d652e6570632e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b39343034363339383400")
        self.assertEqual(message.avps[0].dump().hex(), "00000107400000436d6d652e6570632e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b39343034363339383400")
        self.assertEqual(message.avps[0].code, SESSION_ID_AVP_CODE)
        self.assertEqual(message.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[0].vendor_id)
        self.assertEqual(message.avps[0].length.hex(), "000043")
        self.assertEqual(message.avps[0].get_length(), 67)
        self.assertEqual(message.avps[0].data, b"mme.epc.3gppnetwork.org;1559529822;356549175;2.17;940463984")
        self.assertEqual(message.avps[0].get_padding_length(), 1)

        #: See the needed to refresh it. Before call it the length is wrong if 
        #: you try to access through the Header object
        self.assertEqual(message.header.length.hex(), "000180")
        self.assertEqual(message.header.get_length(), 384)
        self.assertEqual(len(message.header), 384)
        self.assertEqual(message.dump().hex(), "01000180c000013e01000023116846741168467400000107400000436d6d652e6570632e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b39343034363339383400000001154000000c00000001000001084000001f6d6d652e6570632e336770706e6574776f726b2e6f726700000001284000001b6570632e336770706e6574776f726b2e6f7267000000011b400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72670000000000000140000017373234303031313131313131313131000000057fc000000f000028af27f4500000000104400000200000010a4000000c000028af000001024000000c010000230000012540000030687373736d322e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f726700000580c000002c000028af00000582c0000010000028af0000000200000584c0000010000028af00000001")

        message.refresh()

        self.assertEqual(message.header.length.hex(), "000170")
        self.assertEqual(message.header.get_length(), 368)
        self.assertEqual(len(message.header), 368)
        self.assertEqual(message.dump().hex(), "01000170c000013e01000023116846741168467400000107400000436d6d652e6570632e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b39343034363339383400000001154000000c00000001000001084000001f6d6d652e6570632e336770706e6574776f726b2e6f726700000001284000001b6570632e336770706e6574776f726b2e6f7267000000011b400000296570632e6d6e633030302e6d63633732342e336770706e6574776f726b2e6f72670000000000000140000017373234303031313131313131313131000000057fc000000f000028af27f4500000000104400000200000010a4000000c000028af000001024000000c010000230000012540000030687373736d322e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f726700000580c000002c000028af00000582c0000010000028af0000000200000584c0000010000028af00000001")


        #: Update Destination-Realm AVP
        message.destination_realm_avp.data = "epc.3gppnetwork.org"

        self.assertEqual(message.destination_realm_avp.dump().hex(), "0000011b4000001b6570632e336770706e6574776f726b2e6f726700")
        self.assertEqual(message.avps[4].dump().hex(), "0000011b4000001b6570632e336770706e6574776f726b2e6f726700")
        self.assertEqual(message.avps[4].code, DESTINATION_REALM_AVP_CODE)
        self.assertEqual(message.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[4].vendor_id)
        self.assertEqual(message.avps[4].length.hex(), "00001b")
        self.assertEqual(message.avps[4].get_length(), 27)
        self.assertEqual(message.avps[4].data, b"epc.3gppnetwork.org")
        self.assertEqual(message.avps[4].get_padding_length(), 1)

        #: See the needed to refresh it. Before call it the length is wrong if 
        #: you try to access through the Header object
        self.assertEqual(message.header.length.hex(), "000170")
        self.assertEqual(message.header.get_length(), 368)
        self.assertEqual(len(message.header), 368)
        self.assertEqual(message.dump().hex(), "01000170c000013e01000023116846741168467400000107400000436d6d652e6570632e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b39343034363339383400000001154000000c00000001000001084000001f6d6d652e6570632e336770706e6574776f726b2e6f726700000001284000001b6570632e336770706e6574776f726b2e6f7267000000011b4000001b6570632e336770706e6574776f726b2e6f7267000000000140000017373234303031313131313131313131000000057fc000000f000028af27f4500000000104400000200000010a4000000c000028af000001024000000c010000230000012540000030687373736d322e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f726700000580c000002c000028af00000582c0000010000028af0000000200000584c0000010000028af00000001")

        message.refresh()

        self.assertEqual(message.header.length.hex(), "000160")
        self.assertEqual(message.header.get_length(), 352)
        self.assertEqual(len(message.header), 352)
        self.assertEqual(message.dump().hex(), "01000160c000013e01000023116846741168467400000107400000436d6d652e6570632e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b39343034363339383400000001154000000c00000001000001084000001f6d6d652e6570632e336770706e6574776f726b2e6f726700000001284000001b6570632e336770706e6574776f726b2e6f7267000000011b4000001b6570632e336770706e6574776f726b2e6f7267000000000140000017373234303031313131313131313131000000057fc000000f000028af27f4500000000104400000200000010a4000000c000028af000001024000000c010000230000012540000030687373736d322e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f726700000580c000002c000028af00000582c0000010000028af0000000200000584c0000010000028af00000001")


        #: Update User-Name AVP
        message.user_name_avp.data = "frodo"

        self.assertEqual(message.user_name_avp.dump().hex(), "000000014000000d66726f646f000000")
        self.assertEqual(message.avps[5].dump().hex(), "000000014000000d66726f646f000000")
        self.assertEqual(message.avps[5].code, USER_NAME_AVP_CODE)
        self.assertEqual(message.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(message.avps[5].vendor_id)
        self.assertEqual(message.avps[5].length.hex(), "00000d")
        self.assertEqual(message.avps[5].get_length(), 13)
        self.assertEqual(message.avps[5].data, b"frodo")
        self.assertEqual(message.avps[5].get_padding_length(), 3)

        #: See the needed to refresh it. Before call it the length is wrong if 
        #: you try to access through the Header object
        self.assertEqual(message.header.length.hex(), "000160")
        self.assertEqual(message.header.get_length(), 352)
        self.assertEqual(len(message.header), 352)
        self.assertEqual(message.dump().hex(), "01000160c000013e01000023116846741168467400000107400000436d6d652e6570632e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b39343034363339383400000001154000000c00000001000001084000001f6d6d652e6570632e336770706e6574776f726b2e6f726700000001284000001b6570632e336770706e6574776f726b2e6f7267000000011b4000001b6570632e336770706e6574776f726b2e6f726700000000014000000d66726f646f0000000000057fc000000f000028af27f4500000000104400000200000010a4000000c000028af000001024000000c010000230000012540000030687373736d322e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f726700000580c000002c000028af00000582c0000010000028af0000000200000584c0000010000028af00000001")

        message.refresh()

        self.assertEqual(message.header.length.hex(), "000158")
        self.assertEqual(message.header.get_length(), 344)
        self.assertEqual(len(message.header), 344)
        self.assertEqual(message.dump().hex(), "01000158c000013e01000023116846741168467400000107400000436d6d652e6570632e336770706e6574776f726b2e6f72673b313535393532393832323b3335363534393137353b322e31373b39343034363339383400000001154000000c00000001000001084000001f6d6d652e6570632e336770706e6574776f726b2e6f726700000001284000001b6570632e336770706e6574776f726b2e6f7267000000011b4000001b6570632e336770706e6574776f726b2e6f726700000000014000000d66726f646f0000000000057fc000000f000028af27f4500000000104400000200000010a4000000c000028af000001024000000c010000230000012540000030687373736d322e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f726700000580c000002c000028af00000582c0000010000028af0000000200000584c0000010000028af00000001")

    def test_diameter_message__update_avps_method__1(self):
        #: Initial Setup
        config = {
                "MODE": "CLIENT",
                "APPLICATIONS": [
                                    {
                                        "vendor_id": VENDOR_ID_3GPP, 
                                        "app_id": DIAMETER_APPLICATION_Cx
                                    },
                                    {
                                        "vendor_id": VENDOR_ID_3GPP,
                                        "app_id": DIAMETER_APPLICATION_Rx
                                    }
                ],
                "LOCAL_NODE_HOSTNAME": "client.network",
                "LOCAL_NODE_REALM": "network",
                "LOCAL_NODE_IP_ADDRESS": "127.0.0.1",
                "LOCAL_NODE_PORT": None,
                "PEER_NODE_HOSTNAME": "server.network",
                "PEER_NODE_REALM": "network",
                "PEER_NODE_IP_ADDRESS": "127.0.0.1",
                "PEER_NODE_PORT": None,
                "WATCHDOG_TIMEOUT": 30
            }
        connection = _convert_config_to_connection_obj(config)
        cea = DiameterBaseProxy.load_cea(connection)

        cea.append(OriginStateIdAVP(64))
        cea.append(SupportedVendorIdAVP(VENDOR_ID_ETSI))

        #: Check Diameter Header
        self.assertEqual(cea.header.version, DIAMETER_VERSION)
        self.assertEqual(cea.header.flags, FLAG_RESPONSE)
        self.assertEqual(cea.header.length.hex(), "0000e0")
        self.assertEqual(cea.header.get_length(), 224)
        self.assertEqual(cea.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(cea.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(cea.__repr__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 11 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(cea.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[0].vendor_id)
        self.assertEqual(cea.avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[0].get_length(), 12)
        self.assertEqual(cea.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(cea.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(cea.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[1].vendor_id)
        self.assertEqual(cea.avps[1].length.hex(), "000016")
        self.assertEqual(cea.avps[1].get_length(), 22)
        self.assertEqual(cea.avps[1].data, b"client.network")
        self.assertEqual(cea.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(cea.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cea.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[2].vendor_id)
        self.assertEqual(cea.avps[2].length.hex(), "00000f")
        self.assertEqual(cea.avps[2].get_length(), 15)
        self.assertEqual(cea.avps[2].data, b"network")
        self.assertEqual(cea.avps[2].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(cea.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cea.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[3].vendor_id)
        self.assertEqual(cea.avps[3].length.hex(), "00000e")
        self.assertEqual(cea.avps[3].get_length(), 14)
        self.assertEqual(cea.avps[3].data.hex(), "00017f000001")
        self.assertEqual(cea.avps[3].get_ip_address(), "127.0.0.1")
        self.assertEqual(cea.avps[3].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(cea.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cea.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[4].vendor_id)
        self.assertEqual(cea.avps[4].length.hex(), "00000c")
        self.assertEqual(cea.avps[4].get_length(), 12)
        self.assertEqual(cea.avps[4].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(cea.avps[4].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(cea.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cea.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[5].vendor_id)
        self.assertEqual(cea.avps[5].length.hex(), "000017")
        self.assertEqual(cea.avps[5].get_length(), 23)
        self.assertEqual(cea.avps[5].data, b"Python bromelia")
        self.assertEqual(cea.avps[5].get_padding_length(), 1)

        #: Auth-Application-Id AVP
        self.assertEqual(cea.auth_application_id_avp.dump().hex(), "000001024000000c00000000")
        self.assertEqual(cea.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[6].vendor_id)
        self.assertEqual(cea.avps[6].length.hex(), "00000c")
        self.assertEqual(cea.avps[6].get_length(), 12)
        self.assertEqual(cea.avps[6].data, DIAMETER_APPLICATION_DEFAULT)
        self.assertIsNone(cea.avps[6].get_padding_length())

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp.dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(cea.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(cea.avps[7].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].vendor_id)
        self.assertEqual(cea.avps[7].length.hex(), "000020")
        self.assertEqual(cea.avps[7].get_length(), 32)
        self.assertEqual(cea.avps[7].data.hex(), "0000010a4000000c000028af000001024000000c01000000")
        self.assertIsNone(cea.avps[7].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[7].avps[0].dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[7].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].avps[0].vendor_id)
        self.assertEqual(cea.avps[7].avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[7].avps[0].get_length(), 12)
        self.assertEqual(cea.avps[7].avps[0].data, VENDOR_ID_3GPP)
        self.assertIsNone(cea.avps[7].avps[0].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.dump().hex(), "000001024000000c01000000")
        self.assertEqual(cea.avps[7].avps[1].dump().hex(), "000001024000000c01000000")
        self.assertEqual(cea.avps[7].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].avps[1].vendor_id)
        self.assertEqual(cea.avps[7].avps[1].length.hex(), "00000c")
        self.assertEqual(cea.avps[7].avps[1].get_length(), 12)
        self.assertEqual(cea.avps[7].avps[1].data, DIAMETER_APPLICATION_Cx)
        self.assertIsNone(cea.avps[7].avps[1].get_padding_length())

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp__1.dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000014")
        self.assertEqual(cea.avps[8].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000014")
        self.assertEqual(cea.avps[8].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].vendor_id)
        self.assertEqual(cea.avps[8].length.hex(), "000020")
        self.assertEqual(cea.avps[8].get_length(), 32)
        self.assertEqual(cea.avps[8].data.hex(), "0000010a4000000c000028af000001024000000c01000014")
        self.assertIsNone(cea.avps[8].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[8].avps[0].dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[8].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].avps[0].vendor_id)
        self.assertEqual(cea.avps[8].avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[8].avps[0].get_length(), 12)
        self.assertEqual(cea.avps[8].avps[0].data, VENDOR_ID_3GPP)
        self.assertIsNone(cea.avps[8].avps[0].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.dump().hex(), "000001024000000c01000014")
        self.assertEqual(cea.avps[8].avps[1].dump().hex(), "000001024000000c01000014")
        self.assertEqual(cea.avps[8].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].avps[1].vendor_id)
        self.assertEqual(cea.avps[8].avps[1].length.hex(), "00000c")
        self.assertEqual(cea.avps[8].avps[1].get_length(), 12)
        self.assertEqual(cea.avps[8].avps[1].data, DIAMETER_APPLICATION_Rx)
        self.assertIsNone(cea.avps[8].avps[1].get_padding_length())        


        #: Update all AVPs
        avps = {
            "result_code": DIAMETER_MULTI_ROUND_AUTH,
            "origin_host": "hss.ims.3gppnetwork.org",
            "origin_realm": "ims.3gppnetwork.org",
            "host_ip_address": "10.129.241.235",
            "vendor_id": VENDOR_ID_ETSI,
            "product_name": f"Python Bromelia vX.Y.Z",
            "auth_application_id": DIAMETER_APPLICATION_Gx,
        }
        cea.update_avps(avps)

        #: Result-Code AVP
        self.assertEqual(cea.avps[0].dump().hex(), "0000010c4000000c000003e9")
        self.assertEqual(cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[0].vendor_id)
        self.assertEqual(cea.avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[0].get_length(), 12)
        self.assertEqual(cea.avps[0].data, DIAMETER_MULTI_ROUND_AUTH)
        self.assertIsNone(cea.avps[0].get_padding_length())

        self.assertEqual(cea.result_code_avp.dump().hex(), "0000010c4000000c000003e9")
        self.assertEqual(cea.result_code_avp.code, RESULT_CODE_AVP_CODE)
        self.assertEqual(cea.result_code_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.result_code_avp.vendor_id)
        self.assertEqual(cea.result_code_avp.length.hex(), "00000c")
        self.assertEqual(cea.result_code_avp.get_length(), 12)
        self.assertEqual(cea.result_code_avp.data, DIAMETER_MULTI_ROUND_AUTH)
        self.assertIsNone(cea.result_code_avp.get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(cea.avps[1].dump().hex(), "000001084000001f6873732e696d732e336770706e6574776f726b2e6f726700")
        self.assertEqual(cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[1].vendor_id)
        self.assertEqual(cea.avps[1].length.hex(), "00001f")
        self.assertEqual(cea.avps[1].get_length(), 31)
        self.assertEqual(cea.avps[1].data, b"hss.ims.3gppnetwork.org")
        self.assertEqual(cea.avps[1].get_padding_length(), 1)

        self.assertEqual(cea.origin_host_avp.dump().hex(), "000001084000001f6873732e696d732e336770706e6574776f726b2e6f726700")
        self.assertEqual(cea.origin_host_avp.code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(cea.origin_host_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.origin_host_avp.vendor_id)
        self.assertEqual(cea.origin_host_avp.length.hex(), "00001f")
        self.assertEqual(cea.origin_host_avp.get_length(), 31)
        self.assertEqual(cea.origin_host_avp.data, b"hss.ims.3gppnetwork.org")
        self.assertEqual(cea.origin_host_avp.get_padding_length(), 1)

        #: Origin-Realm AVP
        self.assertEqual(cea.avps[2].dump().hex(), "000001284000001b696d732e336770706e6574776f726b2e6f726700")
        self.assertEqual(cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[2].vendor_id)
        self.assertEqual(cea.avps[2].length.hex(), "00001b")
        self.assertEqual(cea.avps[2].get_length(), 27)
        self.assertEqual(cea.avps[2].data, b"ims.3gppnetwork.org")
        self.assertEqual(cea.avps[2].get_padding_length(), 1)

        self.assertEqual(cea.origin_realm_avp.dump().hex(), "000001284000001b696d732e336770706e6574776f726b2e6f726700")
        self.assertEqual(cea.origin_realm_avp.code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(cea.origin_realm_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.origin_realm_avp.vendor_id)
        self.assertEqual(cea.origin_realm_avp.length.hex(), "00001b")
        self.assertEqual(cea.origin_realm_avp.get_length(), 27)
        self.assertEqual(cea.origin_realm_avp.data, b"ims.3gppnetwork.org")
        self.assertEqual(cea.origin_realm_avp.get_padding_length(), 1)

        # #: Host-IP-Address AVP
        self.assertEqual(cea.avps[3].dump().hex(), "000001014000000e00010a81f1eb0000")
        self.assertEqual(cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[3].vendor_id)
        self.assertEqual(cea.avps[3].length.hex(), "00000e")
        self.assertEqual(cea.avps[3].get_length(), 14)
        self.assertEqual(cea.avps[3].data.hex(), "00010a81f1eb")
        self.assertEqual(cea.avps[3].get_ip_address(), "10.129.241.235")
        self.assertEqual(cea.avps[3].get_padding_length(), 2)

        self.assertEqual(cea.host_ip_address_avp.dump().hex(), "000001014000000e00010a81f1eb0000")
        self.assertEqual(cea.host_ip_address_avp.code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(cea.host_ip_address_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.host_ip_address_avp.vendor_id)
        self.assertEqual(cea.host_ip_address_avp.length.hex(), "00000e")
        self.assertEqual(cea.host_ip_address_avp.get_length(), 14)
        self.assertEqual(cea.host_ip_address_avp.data.hex(), "00010a81f1eb")
        self.assertEqual(cea.host_ip_address_avp.get_ip_address(), "10.129.241.235")
        self.assertEqual(cea.host_ip_address_avp.get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(cea.avps[4].dump().hex(), "0000010a4000000c000032db")
        self.assertEqual(cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[4].vendor_id)
        self.assertEqual(cea.avps[4].length.hex(), "00000c")
        self.assertEqual(cea.avps[4].get_length(), 12)
        self.assertEqual(cea.avps[4].data, VENDOR_ID_ETSI)
        self.assertIsNone(cea.avps[4].get_padding_length())

        self.assertEqual(cea.vendor_id_avp.dump().hex(), "0000010a4000000c000032db")
        self.assertEqual(cea.vendor_id_avp.code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.vendor_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.vendor_id_avp.vendor_id)
        self.assertEqual(cea.vendor_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.vendor_id_avp.get_length(), 12)
        self.assertEqual(cea.vendor_id_avp.data, VENDOR_ID_ETSI)
        self.assertIsNone(cea.vendor_id_avp.get_padding_length())

        #: Product-Name AVP
        self.assertEqual(cea.avps[5].dump().hex(), "0000010d0000001e507974686f6e2042726f6d656c69612076582e592e5a0000")
        self.assertEqual(cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[5].vendor_id)
        self.assertEqual(cea.avps[5].length.hex(), "00001e")
        self.assertEqual(cea.avps[5].get_length(), 30)
        self.assertEqual(cea.avps[5].data, b"Python Bromelia vX.Y.Z")
        self.assertEqual(cea.avps[5].get_padding_length(), 2)

        self.assertEqual(cea.product_name_avp.dump().hex(), "0000010d0000001e507974686f6e2042726f6d656c69612076582e592e5a0000")
        self.assertEqual(cea.product_name_avp.code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(cea.product_name_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.product_name_avp.vendor_id)
        self.assertEqual(cea.product_name_avp.length.hex(), "00001e")
        self.assertEqual(cea.product_name_avp.get_length(), 30)
        self.assertEqual(cea.product_name_avp.data, b"Python Bromelia vX.Y.Z")
        self.assertEqual(cea.product_name_avp.get_padding_length(), 2)

        #: Auth-Application-Id AVP
        self.assertEqual(cea.avps[6].dump().hex(), "000001024000000c01000016")
        self.assertEqual(cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[6].vendor_id)
        self.assertEqual(cea.avps[6].length.hex(), "00000c")
        self.assertEqual(cea.avps[6].get_length(), 12)
        self.assertEqual(cea.avps[6].data, DIAMETER_APPLICATION_Gx)
        self.assertIsNone(cea.avps[6].get_padding_length())

        self.assertEqual(cea.auth_application_id_avp.dump().hex(), "000001024000000c01000016")
        self.assertEqual(cea.auth_application_id_avp.code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.auth_application_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.auth_application_id_avp.vendor_id)
        self.assertEqual(cea.auth_application_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.auth_application_id_avp.get_length(), 12)
        self.assertEqual(cea.auth_application_id_avp.data, DIAMETER_APPLICATION_Gx)
        self.assertIsNone(cea.auth_application_id_avp.get_padding_length())

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(cea.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(cea.avps[7].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].vendor_id)
        self.assertEqual(cea.avps[7].length.hex(), "000020")
        self.assertEqual(cea.avps[7].get_length(), 32)
        self.assertEqual(cea.avps[7].data.hex(), "0000010a4000000c000028af000001024000000c01000000")
        self.assertIsNone(cea.avps[7].get_padding_length())

        self.assertEqual(cea.vendor_specific_application_id_avp.dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(cea.vendor_specific_application_id_avp.code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.vendor_specific_application_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.vendor_specific_application_id_avp.vendor_id)
        self.assertEqual(cea.vendor_specific_application_id_avp.length.hex(), "000020")
        self.assertEqual(cea.vendor_specific_application_id_avp.get_length(), 32)
        self.assertEqual(cea.vendor_specific_application_id_avp.data.hex(), "0000010a4000000c000028af000001024000000c01000000")
        self.assertIsNone(cea.vendor_specific_application_id_avp.get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(cea.avps[7].avps[0].dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[7].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].avps[0].vendor_id)
        self.assertEqual(cea.avps[7].avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[7].avps[0].get_length(), 12)
        self.assertEqual(cea.avps[7].avps[0].data, VENDOR_ID_3GPP)
        self.assertIsNone(cea.avps[7].avps[0].get_padding_length())

        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.vendor_specific_application_id_avp.vendor_id_avp.vendor_id)
        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.get_length(), 12)
        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertIsNone(cea.vendor_specific_application_id_avp.vendor_id_avp.get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(cea.avps[7].avps[1].dump().hex(), "000001024000000c01000000")
        self.assertEqual(cea.avps[7].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].avps[1].vendor_id)
        self.assertEqual(cea.avps[7].avps[1].length.hex(), "00000c")
        self.assertEqual(cea.avps[7].avps[1].get_length(), 12)
        self.assertEqual(cea.avps[7].avps[1].data, DIAMETER_APPLICATION_Cx)
        self.assertIsNone(cea.avps[7].avps[1].get_padding_length())

        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.dump().hex(), "000001024000000c01000000")
        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.vendor_specific_application_id_avp.auth_application_id_avp.vendor_id)
        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.get_length(), 12)
        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.data, DIAMETER_APPLICATION_Cx)
        self.assertIsNone(cea.vendor_specific_application_id_avp.auth_application_id_avp.get_padding_length())

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(cea.avps[8].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000014")
        self.assertEqual(cea.avps[8].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].vendor_id)
        self.assertEqual(cea.avps[8].length.hex(), "000020")
        self.assertEqual(cea.avps[8].get_length(), 32)
        self.assertEqual(cea.avps[8].data.hex(), "0000010a4000000c000028af000001024000000c01000014")
        self.assertIsNone(cea.avps[8].get_padding_length())

        self.assertEqual(cea.vendor_specific_application_id_avp__1.dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000014")
        self.assertEqual(cea.vendor_specific_application_id_avp__1.code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.vendor_specific_application_id_avp__1.vendor_id)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.length.hex(), "000020")
        self.assertEqual(cea.vendor_specific_application_id_avp__1.get_length(), 32)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.data.hex(), "0000010a4000000c000028af000001024000000c01000014")
        self.assertIsNone(cea.vendor_specific_application_id_avp__1.get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(cea.avps[8].avps[0].dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[8].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].avps[0].vendor_id)
        self.assertEqual(cea.avps[8].avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[8].avps[0].get_length(), 12)
        self.assertEqual(cea.avps[8].avps[0].data, VENDOR_ID_3GPP)
        self.assertIsNone(cea.avps[8].avps[0].get_padding_length())

        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.vendor_specific_application_id_avp__1.vendor_id_avp.vendor_id)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.get_length(), 12)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertIsNone(cea.vendor_specific_application_id_avp__1.vendor_id_avp.get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(cea.avps[8].avps[1].dump().hex(), "000001024000000c01000014")
        self.assertEqual(cea.avps[8].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].avps[1].vendor_id)
        self.assertEqual(cea.avps[8].avps[1].length.hex(), "00000c")
        self.assertEqual(cea.avps[8].avps[1].get_length(), 12)
        self.assertEqual(cea.avps[8].avps[1].data, DIAMETER_APPLICATION_Rx)
        self.assertIsNone(cea.avps[8].avps[1].get_padding_length())

        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.dump().hex(), "000001024000000c01000014")
        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.vendor_id)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.get_length(), 12)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.data, DIAMETER_APPLICATION_Rx)
        self.assertIsNone(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.get_padding_length())

        #: Origin-State-Id AVP
        self.assertEqual(cea.avps[9].dump().hex(), "000001164000000c00000040")
        self.assertEqual(cea.avps[9].code, ORIGIN_STATE_ID_AVP_CODE)
        self.assertEqual(cea.avps[9].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[9].vendor_id)
        self.assertEqual(cea.avps[9].length.hex(), "00000c")
        self.assertEqual(cea.avps[9].get_length(), 12)
        self.assertEqual(cea.avps[9].data.hex(), "00000040")
        self.assertIsNone(cea.avps[9].get_padding_length())

        self.assertEqual(cea.origin_state_id_avp.dump().hex(), "000001164000000c00000040")
        self.assertEqual(cea.origin_state_id_avp.code, ORIGIN_STATE_ID_AVP_CODE)
        self.assertEqual(cea.origin_state_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.origin_state_id_avp.vendor_id)
        self.assertEqual(cea.origin_state_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.origin_state_id_avp.get_length(), 12)
        self.assertEqual(cea.origin_state_id_avp.data.hex(), "00000040")
        self.assertIsNone(cea.origin_state_id_avp.get_padding_length())

        #: Supported-Vendor-Id AVP
        self.assertEqual(cea.avps[10].dump().hex(), "000001094000000c000032db")
        self.assertEqual(cea.avps[10].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[10].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[10].vendor_id)
        self.assertEqual(cea.avps[10].length.hex(), "00000c")
        self.assertEqual(cea.avps[10].get_length(), 12)
        self.assertEqual(cea.avps[10].data, VENDOR_ID_ETSI)
        self.assertIsNone(cea.avps[10].get_padding_length())

        self.assertEqual(cea.supported_vendor_id_avp.dump().hex(), "000001094000000c000032db")
        self.assertEqual(cea.supported_vendor_id_avp.code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.supported_vendor_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.supported_vendor_id_avp.vendor_id)
        self.assertEqual(cea.supported_vendor_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.supported_vendor_id_avp.get_length(), 12)
        self.assertEqual(cea.supported_vendor_id_avp.data, VENDOR_ID_ETSI)
        self.assertIsNone(cea.supported_vendor_id_avp.get_padding_length())

    def test_diameter_message__update_avps_method__2(self):
        stream = bytes.fromhex("010000e0000001010000000000000000000000000000010c4000000c000007d10000010840000016636c69656e742e6e6574776f726b0000000001284000000f6e6574776f726b00000001014000000e00017f00000100000000010a4000000c000000000000010d00000017507974686f6e2062726f6d656c696100000001024000000c0000000000000104400000200000010a4000000c000028af000001024000000c0100000000000104400000200000010a4000000c000028af000001024000000c01000014000001164000000c00000040000001094000000c000032db")
        msgs = DiameterMessage.load(stream)
        cea = msgs[0]

        #: Check Diameter Header
        self.assertEqual(cea.header.version, DIAMETER_VERSION)
        self.assertEqual(cea.header.flags, FLAG_RESPONSE)
        self.assertEqual(cea.header.length.hex(), "0000e0")
        self.assertEqual(cea.header.get_length(), 224)
        self.assertEqual(cea.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(cea.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(cea.__repr__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 11 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(cea.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[0].vendor_id)
        self.assertEqual(cea.avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[0].get_length(), 12)
        self.assertEqual(cea.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(cea.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(cea.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[1].vendor_id)
        self.assertEqual(cea.avps[1].length.hex(), "000016")
        self.assertEqual(cea.avps[1].get_length(), 22)
        self.assertEqual(cea.avps[1].data, b"client.network")
        self.assertEqual(cea.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(cea.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cea.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[2].vendor_id)
        self.assertEqual(cea.avps[2].length.hex(), "00000f")
        self.assertEqual(cea.avps[2].get_length(), 15)
        self.assertEqual(cea.avps[2].data, b"network")
        self.assertEqual(cea.avps[2].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(cea.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cea.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[3].vendor_id)
        self.assertEqual(cea.avps[3].length.hex(), "00000e")
        self.assertEqual(cea.avps[3].get_length(), 14)
        self.assertEqual(cea.avps[3].data.hex(), "00017f000001")
        self.assertEqual(cea.avps[3].get_ip_address(), "127.0.0.1")
        self.assertEqual(cea.avps[3].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(cea.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cea.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[4].vendor_id)
        self.assertEqual(cea.avps[4].length.hex(), "00000c")
        self.assertEqual(cea.avps[4].get_length(), 12)
        self.assertEqual(cea.avps[4].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(cea.avps[4].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(cea.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cea.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[5].vendor_id)
        self.assertEqual(cea.avps[5].length.hex(), "000017")
        self.assertEqual(cea.avps[5].get_length(), 23)
        self.assertEqual(cea.avps[5].data, b"Python bromelia")
        self.assertEqual(cea.avps[5].get_padding_length(), 1)

        #: Auth-Application-Id AVP
        self.assertEqual(cea.auth_application_id_avp.dump().hex(), "000001024000000c00000000")
        self.assertEqual(cea.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[6].vendor_id)
        self.assertEqual(cea.avps[6].length.hex(), "00000c")
        self.assertEqual(cea.avps[6].get_length(), 12)
        self.assertEqual(cea.avps[6].data, DIAMETER_APPLICATION_DEFAULT)
        self.assertIsNone(cea.avps[6].get_padding_length())

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp.dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(cea.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(cea.avps[7].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].vendor_id)
        self.assertEqual(cea.avps[7].length.hex(), "000020")
        self.assertEqual(cea.avps[7].get_length(), 32)
        self.assertEqual(cea.avps[7].data.hex(), "0000010a4000000c000028af000001024000000c01000000")
        self.assertIsNone(cea.avps[7].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[7].avps[0].dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[7].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].avps[0].vendor_id)
        self.assertEqual(cea.avps[7].avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[7].avps[0].get_length(), 12)
        self.assertEqual(cea.avps[7].avps[0].data, VENDOR_ID_3GPP)
        self.assertIsNone(cea.avps[7].avps[0].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.dump().hex(), "000001024000000c01000000")
        self.assertEqual(cea.avps[7].avps[1].dump().hex(), "000001024000000c01000000")
        self.assertEqual(cea.avps[7].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].avps[1].vendor_id)
        self.assertEqual(cea.avps[7].avps[1].length.hex(), "00000c")
        self.assertEqual(cea.avps[7].avps[1].get_length(), 12)
        self.assertEqual(cea.avps[7].avps[1].data, DIAMETER_APPLICATION_Cx)
        self.assertIsNone(cea.avps[7].avps[1].get_padding_length())

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp__1.dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000014")
        self.assertEqual(cea.avps[8].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000014")
        self.assertEqual(cea.avps[8].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].vendor_id)
        self.assertEqual(cea.avps[8].length.hex(), "000020")
        self.assertEqual(cea.avps[8].get_length(), 32)
        self.assertEqual(cea.avps[8].data.hex(), "0000010a4000000c000028af000001024000000c01000014")
        self.assertIsNone(cea.avps[8].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[8].avps[0].dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[8].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].avps[0].vendor_id)
        self.assertEqual(cea.avps[8].avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[8].avps[0].get_length(), 12)
        self.assertEqual(cea.avps[8].avps[0].data, VENDOR_ID_3GPP)
        self.assertIsNone(cea.avps[8].avps[0].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.dump().hex(), "000001024000000c01000014")
        self.assertEqual(cea.avps[8].avps[1].dump().hex(), "000001024000000c01000014")
        self.assertEqual(cea.avps[8].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].avps[1].vendor_id)
        self.assertEqual(cea.avps[8].avps[1].length.hex(), "00000c")
        self.assertEqual(cea.avps[8].avps[1].get_length(), 12)
        self.assertEqual(cea.avps[8].avps[1].data, DIAMETER_APPLICATION_Rx)
        self.assertIsNone(cea.avps[8].avps[1].get_padding_length())        

        #: Update all AVPs
        avps = {
            "result_code": DIAMETER_LIMITED_SUCCESS,
            "origin_host": "aaa.s6b.epc.3gppnetwork.org",
            "origin_realm": "epc.3gppnetwork.org",
            "host_ip_address": "10.129.241.214",
            "vendor_id": VENDOR_ID_DEFAULT,
            "product_name": f"Bromelia-AAA",
            "auth_application_id": DIAMETER_APPLICATION_S6b,
            "vendor_specific_application_id": [
                                                VendorIdAVP(VENDOR_ID_ETSI), 
                                                AuthApplicationIdAVP(DIAMETER_APPLICATION_SWm)
            ],
            "vendor_specific_application_id__1": [
                                                VendorIdAVP(VENDOR_ID_ETSI), 
                                                AuthApplicationIdAVP(DIAMETER_APPLICATION_SWx)
            ],
            "origin_state_id": 42,
            "supported_vendor_id": VENDOR_ID_DEFAULT
        }
        cea.update_avps(avps)

        #: Result-Code AVP
        self.assertEqual(cea.avps[0].dump().hex(), "0000010c4000000c000007d2")
        self.assertEqual(cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[0].vendor_id)
        self.assertEqual(cea.avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[0].get_length(), 12)
        self.assertEqual(cea.avps[0].data, DIAMETER_LIMITED_SUCCESS)
        self.assertIsNone(cea.avps[0].get_padding_length())

        self.assertEqual(cea.result_code_avp.dump().hex(), "0000010c4000000c000007d2")
        self.assertEqual(cea.result_code_avp.code, RESULT_CODE_AVP_CODE)
        self.assertEqual(cea.result_code_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.result_code_avp.vendor_id)
        self.assertEqual(cea.result_code_avp.length.hex(), "00000c")
        self.assertEqual(cea.result_code_avp.get_length(), 12)
        self.assertEqual(cea.result_code_avp.data, DIAMETER_LIMITED_SUCCESS)
        self.assertIsNone(cea.result_code_avp.get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(cea.avps[1].dump().hex(), "00000108400000236161612e7336622e6570632e336770706e6574776f726b2e6f726700")
        self.assertEqual(cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[1].vendor_id)
        self.assertEqual(cea.avps[1].length.hex(), "000023")
        self.assertEqual(cea.avps[1].get_length(), 35)
        self.assertEqual(cea.avps[1].data, b"aaa.s6b.epc.3gppnetwork.org")
        self.assertEqual(cea.avps[1].get_padding_length(), 1)

        self.assertEqual(cea.origin_host_avp.dump().hex(), "00000108400000236161612e7336622e6570632e336770706e6574776f726b2e6f726700")
        self.assertEqual(cea.origin_host_avp.code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(cea.origin_host_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.origin_host_avp.vendor_id)
        self.assertEqual(cea.origin_host_avp.length.hex(), "000023")
        self.assertEqual(cea.origin_host_avp.get_length(), 35)
        self.assertEqual(cea.origin_host_avp.data, b"aaa.s6b.epc.3gppnetwork.org")
        self.assertEqual(cea.origin_host_avp.get_padding_length(), 1)

        #: Origin-Realm AVP
        self.assertEqual(cea.avps[2].dump().hex(), "000001284000001b6570632e336770706e6574776f726b2e6f726700")
        self.assertEqual(cea.avps[2].dump().hex(), "000001284000001b6570632e336770706e6574776f726b2e6f726700")
        self.assertEqual(cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[2].vendor_id)
        self.assertEqual(cea.avps[2].length.hex(), "00001b")
        self.assertEqual(cea.avps[2].get_length(), 27)
        self.assertEqual(cea.avps[2].data, b"epc.3gppnetwork.org")
        self.assertEqual(cea.avps[2].get_padding_length(), 1)

        self.assertEqual(cea.origin_realm_avp.dump().hex(), "000001284000001b6570632e336770706e6574776f726b2e6f726700")
        self.assertEqual(cea.origin_realm_avp.code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(cea.origin_realm_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.origin_realm_avp.vendor_id)
        self.assertEqual(cea.origin_realm_avp.length.hex(), "00001b")
        self.assertEqual(cea.origin_realm_avp.get_length(), 27)
        self.assertEqual(cea.origin_realm_avp.data, b"epc.3gppnetwork.org")
        self.assertEqual(cea.origin_realm_avp.get_padding_length(), 1)

        # #: Host-IP-Address AVP
        self.assertEqual(cea.avps[3].dump().hex(), "000001014000000e00010a81f1d60000")
        self.assertEqual(cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[3].vendor_id)
        self.assertEqual(cea.avps[3].length.hex(), "00000e")
        self.assertEqual(cea.avps[3].get_length(), 14)
        self.assertEqual(cea.avps[3].data.hex(), "00010a81f1d6")
        self.assertEqual(cea.avps[3].get_ip_address(), "10.129.241.214")
        self.assertEqual(cea.avps[3].get_padding_length(), 2)

        self.assertEqual(cea.host_ip_address_avp.dump().hex(), "000001014000000e00010a81f1d60000")
        self.assertEqual(cea.host_ip_address_avp.code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(cea.host_ip_address_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.host_ip_address_avp.vendor_id)
        self.assertEqual(cea.host_ip_address_avp.length.hex(), "00000e")
        self.assertEqual(cea.host_ip_address_avp.get_length(), 14)
        self.assertEqual(cea.host_ip_address_avp.data.hex(), "00010a81f1d6")
        self.assertEqual(cea.host_ip_address_avp.get_ip_address(), "10.129.241.214")
        self.assertEqual(cea.host_ip_address_avp.get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(cea.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[4].vendor_id)
        self.assertEqual(cea.avps[4].length.hex(), "00000c")
        self.assertEqual(cea.avps[4].get_length(), 12)
        self.assertEqual(cea.avps[4].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(cea.avps[4].get_padding_length())

        self.assertEqual(cea.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cea.vendor_id_avp.code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.vendor_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.vendor_id_avp.vendor_id)
        self.assertEqual(cea.vendor_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.vendor_id_avp.get_length(), 12)
        self.assertEqual(cea.vendor_id_avp.data, VENDOR_ID_DEFAULT)
        self.assertIsNone(cea.vendor_id_avp.get_padding_length())

        #: Product-Name AVP
        self.assertEqual(cea.avps[5].dump().hex(), "0000010d0000001442726f6d656c69612d414141")
        self.assertEqual(cea.avps[5].dump().hex(), "0000010d0000001442726f6d656c69612d414141")
        self.assertEqual(cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[5].vendor_id)
        self.assertEqual(cea.avps[5].length.hex(), "000014")
        self.assertEqual(cea.avps[5].get_length(), 20)
        self.assertEqual(cea.avps[5].data, b"Bromelia-AAA")
        self.assertIsNone(cea.avps[5].get_padding_length())

        self.assertEqual(cea.product_name_avp.dump().hex(), "0000010d0000001442726f6d656c69612d414141")
        self.assertEqual(cea.product_name_avp.code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(cea.product_name_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.product_name_avp.vendor_id)
        self.assertEqual(cea.product_name_avp.length.hex(), "000014")
        self.assertEqual(cea.product_name_avp.get_length(), 20)
        self.assertEqual(cea.product_name_avp.data, b"Bromelia-AAA")
        self.assertIsNone(cea.product_name_avp.get_padding_length())

        #: Auth-Application-Id AVP
        self.assertEqual(cea.avps[6].dump().hex(), "000001024000000c01000038")
        self.assertEqual(cea.avps[6].dump().hex(), "000001024000000c01000038")
        self.assertEqual(cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[6].vendor_id)
        self.assertEqual(cea.avps[6].length.hex(), "00000c")
        self.assertEqual(cea.avps[6].get_length(), 12)
        self.assertEqual(cea.avps[6].data, DIAMETER_APPLICATION_S6b)
        self.assertIsNone(cea.avps[6].get_padding_length())

        self.assertEqual(cea.auth_application_id_avp.dump().hex(), "000001024000000c01000038")
        self.assertEqual(cea.auth_application_id_avp.code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.auth_application_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.auth_application_id_avp.vendor_id)
        self.assertEqual(cea.auth_application_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.auth_application_id_avp.get_length(), 12)
        self.assertEqual(cea.auth_application_id_avp.data, DIAMETER_APPLICATION_S6b)
        self.assertIsNone(cea.auth_application_id_avp.get_padding_length())

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(cea.avps[7].dump().hex(), "00000104400000200000010a4000000c000032db000001024000000c01000030")
        self.assertEqual(cea.avps[7].dump().hex(), "00000104400000200000010a4000000c000032db000001024000000c01000030")
        self.assertEqual(cea.avps[7].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].vendor_id)
        self.assertEqual(cea.avps[7].length.hex(), "000020")
        self.assertEqual(cea.avps[7].get_length(), 32)
        self.assertEqual(cea.avps[7].data.hex(), "0000010a4000000c000032db000001024000000c01000030")
        self.assertIsNone(cea.avps[7].get_padding_length())

        self.assertEqual(cea.vendor_specific_application_id_avp.dump().hex(), "00000104400000200000010a4000000c000032db000001024000000c01000030")
        self.assertEqual(cea.vendor_specific_application_id_avp.code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.vendor_specific_application_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.vendor_specific_application_id_avp.vendor_id)
        self.assertEqual(cea.vendor_specific_application_id_avp.length.hex(), "000020")
        self.assertEqual(cea.vendor_specific_application_id_avp.get_length(), 32)
        self.assertEqual(cea.vendor_specific_application_id_avp.data.hex(), "0000010a4000000c000032db000001024000000c01000030")
        self.assertIsNone(cea.vendor_specific_application_id_avp.get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(cea.avps[7].avps[0].dump().hex(), "0000010a4000000c000032db")
        self.assertEqual(cea.avps[7].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].avps[0].vendor_id)
        self.assertEqual(cea.avps[7].avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[7].avps[0].get_length(), 12)
        self.assertEqual(cea.avps[7].avps[0].data, VENDOR_ID_ETSI)
        self.assertIsNone(cea.avps[7].avps[0].get_padding_length())

        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.dump().hex(), "0000010a4000000c000032db")
        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.vendor_specific_application_id_avp.vendor_id_avp.vendor_id)
        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.get_length(), 12)
        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.data, VENDOR_ID_ETSI)
        self.assertIsNone(cea.vendor_specific_application_id_avp.vendor_id_avp.get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(cea.avps[7].avps[1].dump().hex(), "000001024000000c01000030")
        self.assertEqual(cea.avps[7].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].avps[1].vendor_id)
        self.assertEqual(cea.avps[7].avps[1].length.hex(), "00000c")
        self.assertEqual(cea.avps[7].avps[1].get_length(), 12)
        self.assertEqual(cea.avps[7].avps[1].data, DIAMETER_APPLICATION_SWm)
        self.assertIsNone(cea.avps[7].avps[1].get_padding_length())

        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.dump().hex(), "000001024000000c01000030")
        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.vendor_specific_application_id_avp.auth_application_id_avp.vendor_id)
        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.get_length(), 12)
        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.data, DIAMETER_APPLICATION_SWm)
        self.assertIsNone(cea.vendor_specific_application_id_avp.auth_application_id_avp.get_padding_length())

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(cea.avps[8].dump().hex(), "00000104400000200000010a4000000c000032db000001024000000c01000031")
        self.assertEqual(cea.avps[8].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].vendor_id)
        self.assertEqual(cea.avps[8].length.hex(), "000020")
        self.assertEqual(cea.avps[8].get_length(), 32)
        self.assertEqual(cea.avps[8].data.hex(), "0000010a4000000c000032db000001024000000c01000031")
        self.assertIsNone(cea.avps[8].get_padding_length())

        self.assertEqual(cea.vendor_specific_application_id_avp__1.dump().hex(), "00000104400000200000010a4000000c000032db000001024000000c01000031")
        self.assertEqual(cea.vendor_specific_application_id_avp__1.code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.vendor_specific_application_id_avp__1.vendor_id)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.length.hex(), "000020")
        self.assertEqual(cea.vendor_specific_application_id_avp__1.get_length(), 32)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.data.hex(), "0000010a4000000c000032db000001024000000c01000031")
        self.assertIsNone(cea.vendor_specific_application_id_avp__1.get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(cea.avps[8].avps[0].dump().hex(), "0000010a4000000c000032db")
        self.assertEqual(cea.avps[8].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].avps[0].vendor_id)
        self.assertEqual(cea.avps[8].avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[8].avps[0].get_length(), 12)
        self.assertEqual(cea.avps[8].avps[0].data, VENDOR_ID_ETSI)
        self.assertIsNone(cea.avps[8].avps[0].get_padding_length())

        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.dump().hex(), "0000010a4000000c000032db")
        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.vendor_specific_application_id_avp__1.vendor_id_avp.vendor_id)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.get_length(), 12)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.data, VENDOR_ID_ETSI)
        self.assertIsNone(cea.vendor_specific_application_id_avp__1.vendor_id_avp.get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(cea.avps[8].avps[1].dump().hex(), "000001024000000c01000031")
        self.assertEqual(cea.avps[8].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].avps[1].vendor_id)
        self.assertEqual(cea.avps[8].avps[1].length.hex(), "00000c")
        self.assertEqual(cea.avps[8].avps[1].get_length(), 12)
        self.assertEqual(cea.avps[8].avps[1].data, DIAMETER_APPLICATION_SWx)
        self.assertIsNone(cea.avps[8].avps[1].get_padding_length())

        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.dump().hex(), "000001024000000c01000031")
        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.vendor_id)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.get_length(), 12)
        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.data, DIAMETER_APPLICATION_SWx)
        self.assertIsNone(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.get_padding_length())

        #: Origin-State-Id AVP
        self.assertEqual(cea.avps[9].dump().hex(), "000001164000000c0000002a")
        self.assertEqual(cea.avps[9].code, ORIGIN_STATE_ID_AVP_CODE)
        self.assertEqual(cea.avps[9].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[9].vendor_id)
        self.assertEqual(cea.avps[9].length.hex(), "00000c")
        self.assertEqual(cea.avps[9].get_length(), 12)
        self.assertEqual(cea.avps[9].data.hex(), "0000002a")
        self.assertIsNone(cea.avps[9].get_padding_length())

        self.assertEqual(cea.origin_state_id_avp.dump().hex(), "000001164000000c0000002a")
        self.assertEqual(cea.origin_state_id_avp.code, ORIGIN_STATE_ID_AVP_CODE)
        self.assertEqual(cea.origin_state_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.origin_state_id_avp.vendor_id)
        self.assertEqual(cea.origin_state_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.origin_state_id_avp.get_length(), 12)
        self.assertEqual(cea.origin_state_id_avp.data.hex(), "0000002a")
        self.assertIsNone(cea.origin_state_id_avp.get_padding_length())

        #: Supported-Vendor-Id AVP
        self.assertEqual(cea.avps[10].dump().hex(), "000001094000000c00000000")
        self.assertEqual(cea.avps[10].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[10].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[10].vendor_id)
        self.assertEqual(cea.avps[10].length.hex(), "00000c")
        self.assertEqual(cea.avps[10].get_length(), 12)
        self.assertEqual(cea.avps[10].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(cea.avps[10].get_padding_length())

        self.assertEqual(cea.supported_vendor_id_avp.dump().hex(), "000001094000000c00000000")
        self.assertEqual(cea.supported_vendor_id_avp.code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.supported_vendor_id_avp.flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.supported_vendor_id_avp.vendor_id)
        self.assertEqual(cea.supported_vendor_id_avp.length.hex(), "00000c")
        self.assertEqual(cea.supported_vendor_id_avp.get_length(), 12)
        self.assertEqual(cea.supported_vendor_id_avp.data, VENDOR_ID_DEFAULT)
        self.assertIsNone(cea.supported_vendor_id_avp.get_padding_length())


if __name__ == "__main__":
    unittest.main()