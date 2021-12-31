# -*- coding: utf-8 -*-
"""
    test.test_types
    ~~~~~~~~~~~~~~~

    This module contains the Diameter protocol types unittests.
    
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
from bromelia.constants import *
from bromelia.exceptions import *
from bromelia.types import *


class TestOctetStringType(unittest.TestCase):
    def test_octet_string_type__unable_to_instantiate_class(self):
        data = bytes.fromhex("00000011")
        
        with self.assertRaises(TypeError) as cm: 
            _type = OctetStringType(data)
        
        if sys.version_info[1] <= 8:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class OctetStringType with abstract methods __init__")
        elif sys.version_info[1] == 9:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class OctetStringType with abstract method __init__")

    def test_octet_string_type__valid_input_data_for_subclass__str(self):
        avp = ProxyStateAVP("CLOSED")

        self.assertEqual(type(avp.data), bytes)

    def test_octet_string_type__valid_input_data_for_subclass__bytes(self):
        data = bytes.fromhex("00000011")
        avp = ClassAVP(data)

        self.assertEqual(type(avp.data), bytes)

    def test_octet_string_type__valid_input_vendor_id_for_subclass__4_bytes_long(self):
        class CustomAVP(DiameterAVP, OctetStringType):
            code = bytes.fromhex("00000000")

            def __init__(self, data): 
                DiameterAVP.__init__(self, CustomAVP.code)
                DiameterAVP.set_vendor_id_bit(self, True)
                OctetStringType.__init__(self, data=data, vendor_id=bytes.fromhex("11110000"))


        avp = CustomAVP(data=bytes.fromhex("11"))

        self.assertEqual(type(avp.data), bytes)
        
    def test_octet_string_type__invalid_input_data_for_subclass__list(self):
        data = bytes.fromhex("00000011")

        with self.assertRaises(DataTypeError) as cm: 
            avp = AcctSessionIdAVP([data, data])
        
        self.assertEqual(cm.exception.args[0], "OctetStringType MUST have data argument of 'bytes' or 'str'")

    def test_octet_string_type__invalid_input_data_for_subclass__dict(self):
        data = bytes.fromhex("00000011")

        with self.assertRaises(DataTypeError) as cm: 
            avp = AcctSessionIdAVP({"data": data})
        
        self.assertEqual(cm.exception.args[0], "OctetStringType MUST have data argument of 'bytes' or 'str'")

    def test_octet_string_type__invalid_input_vendor_id_for_subclass__1_byte_long(self):
        class CustomAVP(DiameterAVP, OctetStringType):
            code = bytes.fromhex("00000000")

            def __init__(self, data): 
                DiameterAVP.__init__(self, CustomAVP.code)
                DiameterAVP.set_vendor_id_bit(self, True)
                OctetStringType.__init__(self, data=data, vendor_id=bytes.fromhex("11"))


        with self.assertRaises(DataTypeError) as cm: 
            avp = CustomAVP(data=bytes.fromhex("11"))
        
        self.assertEqual(cm.exception.args[0], "Invalid vendor_id format for OctetStringType. It MUST be 4 bytes long")

    def test_octet_string_type__invalid_input_vendor_id_for_subclass__2_bytes_long(self):
        class CustomAVP(DiameterAVP, OctetStringType):
            code = bytes.fromhex("00000000")

            def __init__(self, data): 
                DiameterAVP.__init__(self, CustomAVP.code)
                DiameterAVP.set_vendor_id_bit(self, True)
                OctetStringType.__init__(self, data=data, vendor_id=bytes.fromhex("1111"))


        with self.assertRaises(DataTypeError) as cm: 
            avp = CustomAVP(data=bytes.fromhex("11"))
        
        self.assertEqual(cm.exception.args[0], "Invalid vendor_id format for OctetStringType. It MUST be 4 bytes long")

    def test_octet_string_type__invalid_input_vendor_id_for_subclass__3_bytes_long(self):
        class CustomAVP(DiameterAVP, OctetStringType):
            code = bytes.fromhex("00000000")

            def __init__(self, data): 
                DiameterAVP.__init__(self, CustomAVP.code)
                DiameterAVP.set_vendor_id_bit(self, True)
                OctetStringType.__init__(self, data=data, vendor_id=bytes.fromhex("111100"))


        with self.assertRaises(DataTypeError) as cm: 
            avp = CustomAVP(data=bytes.fromhex("11"))
        
        self.assertEqual(cm.exception.args[0], "Invalid vendor_id format for OctetStringType. It MUST be 4 bytes long")


class TestInteger32Type(unittest.TestCase):
    def test_integer32_type__unable_to_instantiate_class(self):
        data = bytes.fromhex("00000011")
        
        with self.assertRaises(TypeError) as cm: 
            _type = Integer32Type(data)
        
        if sys.version_info[1] <= 8:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class Integer32Type with abstract methods __init__")
        elif sys.version_info[1] == 9:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class Integer32Type with abstract method __init__")

    def test_integer32_type__valid_input_data_for_subclass__4_bytes_long(self):
        class CustomAVP(DiameterAVP, Integer32Type):
            code = bytes.fromhex("00000000")

            def __init__(self, data): 
                DiameterAVP.__init__(self, CustomAVP.code)
                DiameterAVP.set_vendor_id_bit(self, True)
                Integer32Type.__init__(self, data=data, vendor_id=bytes.fromhex("11110000"))

        avp = CustomAVP(data=bytes.fromhex("11001100"))
        self.assertEqual(type(avp.data), bytes)


class TestUnsigned32Type(unittest.TestCase):
    def setUp(self):
        class CustomAVP(DiameterAVP, Unsigned32Type):
            code = bytes.fromhex("00000000")

            def __init__(self, data): 
                DiameterAVP.__init__(self, CustomAVP.code)
                DiameterAVP.set_vendor_id_bit(self, True)
                Unsigned32Type.__init__(self, data=data, vendor_id=bytes.fromhex("11110000"))

        self.CustomAVP = CustomAVP

    def test_unsigned32_type__unable_to_instantiate_class(self):
        data = bytes.fromhex("00000011")
        
        with self.assertRaises(TypeError) as cm: 
            _type = Unsigned32Type(data)
        
        if sys.version_info[1] <= 8:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class Unsigned32Type with abstract methods __init__")
        elif sys.version_info[1] == 9:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class Unsigned32Type with abstract method __init__")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_0(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(0))

        avp.set_bit(0)
        self.assertEqual(avp.data, bytes.fromhex("00000001"))
        self.assertTrue(avp.is_bit_set(0))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(0)
        
        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(0)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(0))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(0)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_1(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(1))

        avp.set_bit(1)
        self.assertEqual(avp.data, bytes.fromhex("00000002"))
        self.assertTrue(avp.is_bit_set(1))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(1)
        
        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(1)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(1))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(1)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_2(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(2))

        avp.set_bit(2)
        self.assertEqual(avp.data, bytes.fromhex("00000004"))
        self.assertTrue(avp.is_bit_set(2))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(2)
        
        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(2)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(2))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(2)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_3(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(3))

        avp.set_bit(3)
        self.assertEqual(avp.data, bytes.fromhex("00000008"))
        self.assertTrue(avp.is_bit_set(3))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(3)
        
        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(3)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(3))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(3)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_4(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(4))

        avp.set_bit(4)
        self.assertEqual(avp.data, bytes.fromhex("00000010"))
        self.assertTrue(avp.is_bit_set(4))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(4)
        
        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(4)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(4))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(4)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_5(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(5))

        avp.set_bit(5)
        self.assertEqual(avp.data, bytes.fromhex("00000020"))
        self.assertTrue(avp.is_bit_set(5))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(5)
        
        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(5)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(5))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(5)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_6(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(6))

        avp.set_bit(6)
        self.assertEqual(avp.data, bytes.fromhex("00000040"))
        self.assertTrue(avp.is_bit_set(6))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(6)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(6)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(6))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(6)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_7(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(7))

        avp.set_bit(7)
        self.assertEqual(avp.data, bytes.fromhex("00000080"))
        self.assertTrue(avp.is_bit_set(7))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(7)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(7)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(7))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(7)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_8(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(8))

        avp.set_bit(8)
        self.assertEqual(avp.data, bytes.fromhex("00000100"))
        self.assertTrue(avp.is_bit_set(8))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(8)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(8)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(8))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(8)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_9(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(9))

        avp.set_bit(9)
        self.assertEqual(avp.data, bytes.fromhex("00000200"))
        self.assertTrue(avp.is_bit_set(9))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(9)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(9)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(9))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(9)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_10(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(10))

        avp.set_bit(10)
        self.assertEqual(avp.data, bytes.fromhex("00000400"))
        self.assertTrue(avp.is_bit_set(10))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(10)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(10)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(10))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(10)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_11(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(11))

        avp.set_bit(11)
        self.assertEqual(avp.data, bytes.fromhex("00000800"))
        self.assertTrue(avp.is_bit_set(11))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(11)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(11)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(11))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(11)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_12(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(12))

        avp.set_bit(12)
        self.assertEqual(avp.data, bytes.fromhex("00001000"))
        self.assertTrue(avp.is_bit_set(12))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(12)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(12)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(12))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(12)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_13(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(13))

        avp.set_bit(13)
        self.assertEqual(avp.data, bytes.fromhex("00002000"))
        self.assertTrue(avp.is_bit_set(13))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(13)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(13)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(13))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(13)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_14(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(14))

        avp.set_bit(14)
        self.assertEqual(avp.data, bytes.fromhex("00004000"))
        self.assertTrue(avp.is_bit_set(14))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(14)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(14)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(14))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(14)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_15(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(15))

        avp.set_bit(15)
        self.assertEqual(avp.data, bytes.fromhex("00008000"))
        self.assertTrue(avp.is_bit_set(15))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(15)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(15)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(15))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(15)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_16(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(16))

        avp.set_bit(16)
        self.assertEqual(avp.data, bytes.fromhex("00010000"))
        self.assertTrue(avp.is_bit_set(16))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(16)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(16)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(16))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(16)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_17(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(17))

        avp.set_bit(17)
        self.assertEqual(avp.data, bytes.fromhex("00020000"))
        self.assertTrue(avp.is_bit_set(17))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(17)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(17)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(17))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(17)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_18(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(18))

        avp.set_bit(18)
        self.assertEqual(avp.data, bytes.fromhex("00040000"))
        self.assertTrue(avp.is_bit_set(18))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(18)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(18)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(18))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(18)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_19(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(19))

        avp.set_bit(19)
        self.assertEqual(avp.data, bytes.fromhex("00080000"))
        self.assertTrue(avp.is_bit_set(19))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(19)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(19)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(19))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(19)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_20(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(20))

        avp.set_bit(20)
        self.assertEqual(avp.data, bytes.fromhex("00100000"))
        self.assertTrue(avp.is_bit_set(20))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(20)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(20)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(20))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(20)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_21(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(21))

        avp.set_bit(21)
        self.assertEqual(avp.data, bytes.fromhex("00200000"))
        self.assertTrue(avp.is_bit_set(21))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(21)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(21)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(21))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(21)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_22(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(22))

        avp.set_bit(22)
        self.assertEqual(avp.data, bytes.fromhex("00400000"))
        self.assertTrue(avp.is_bit_set(22))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(22)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(22)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(22))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(22)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_23(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(23))

        avp.set_bit(23)
        self.assertEqual(avp.data, bytes.fromhex("00800000"))
        self.assertTrue(avp.is_bit_set(23))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(23)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(23)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(23))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(23)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_24(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(24))

        avp.set_bit(24)
        self.assertEqual(avp.data, bytes.fromhex("01000000"))
        self.assertTrue(avp.is_bit_set(24))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(24)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(24)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(24))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(24)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_25(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(25))

        avp.set_bit(25)
        self.assertEqual(avp.data, bytes.fromhex("02000000"))
        self.assertTrue(avp.is_bit_set(25))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(25)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(25)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(25))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(25)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_26(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(26))

        avp.set_bit(26)
        self.assertEqual(avp.data, bytes.fromhex("04000000"))
        self.assertTrue(avp.is_bit_set(26))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(26)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(26)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(26))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(26)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_27(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(27))

        avp.set_bit(27)
        self.assertEqual(avp.data, bytes.fromhex("08000000"))
        self.assertTrue(avp.is_bit_set(27))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(27)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(27)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(27))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(27)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_28(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(28))

        avp.set_bit(28)
        self.assertEqual(avp.data, bytes.fromhex("10000000"))
        self.assertTrue(avp.is_bit_set(28))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(28)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(28)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(28))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(28)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_29(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(29))

        avp.set_bit(29)
        self.assertEqual(avp.data, bytes.fromhex("20000000"))
        self.assertTrue(avp.is_bit_set(29))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(29)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(29)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(29))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(29)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_30(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(30))

        avp.set_bit(30)
        self.assertEqual(avp.data, bytes.fromhex("40000000"))
        self.assertTrue(avp.is_bit_set(30))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(30)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(30)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(30))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(30)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_and_is_bit_set_31(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(31))

        avp.set_bit(31)
        self.assertEqual(avp.data, bytes.fromhex("80000000"))
        self.assertTrue(avp.is_bit_set(31))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(31)

        self.assertEqual(cm.exception.args[0], "Unable to set an already set bit")

        avp.unset_bit(31)
        self.assertEqual(avp.data, bytes.fromhex("00000000"))
        self.assertFalse(avp.is_bit_set(31))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.unset_bit(31)
        
        self.assertEqual(cm.exception.args[0], "Unable to unset an already unset bit")

    def test_unsigned32_type__set_bit_and_unset_bit_32(self):
        avp = self.CustomAVP(data=bytes.fromhex("00000000"))
        self.assertEqual(avp.data, bytes.fromhex("00000000"))

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.set_bit(32)

        self.assertEqual(cm.exception.args[0], "Bit index out of range")

        with self.assertRaises(DiameterTypeError) as cm: 
            avp.is_bit_set(32)
        
        self.assertEqual(cm.exception.args[0], "Bit index out of range")


class TestUnsigned64Type(unittest.TestCase):
    def test_unsigned64_type__unable_to_instantiate_class(self):
        data = bytes.fromhex("00000011")
        
        with self.assertRaises(TypeError) as cm: 
            _type = Unsigned64Type(data)
        
        if sys.version_info[1] <= 8:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class Unsigned64Type with abstract methods __init__")
        elif sys.version_info[1] == 9:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class Unsigned64Type with abstract method __init__")
    

class TestGroupedType(unittest.TestCase):
    def test_grouped_type__unable_to_instantiate_class(self):
        data = bytes.fromhex("00000011")
        
        with self.assertRaises(TypeError) as cm: 
            _type = GroupedType(data)
        
        if sys.version_info[1] <= 8:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class GroupedType with abstract methods __init__")
        elif sys.version_info[1] == 9:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class GroupedType with abstract method __init__")
 

class TestAddressType(unittest.TestCase):
    def test_address_type__unable_to_instantiate_class(self):
        data = bytes.fromhex("00000011")
        
        with self.assertRaises(TypeError) as cm: 
            _type = AddressType(data)
        
        if sys.version_info[1] <= 8:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class AddressType with abstract methods __init__")
        elif sys.version_info[1] == 9:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class AddressType with abstract method __init__")


class TestTimeType(unittest.TestCase):
    def test_time_type__unable_to_instantiate_class(self):
        data = bytes.fromhex("00000011")
        
        with self.assertRaises(TypeError) as cm: 
            _type = TimeType(data)
        
        if sys.version_info[1] <= 8:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class TimeType with abstract methods __init__")
        elif sys.version_info[1] == 9:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class TimeType with abstract method __init__")


class TestUTF8StringType(unittest.TestCase):
    def test_utf8_string_type__unable_to_instantiate_class(self):
        data = bytes.fromhex("00000011")
        
        with self.assertRaises(TypeError) as cm: 
            _type = UTF8StringType(data)
        
        if sys.version_info[1] <= 8:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class UTF8StringType with abstract methods __init__")
        elif sys.version_info[1] == 9:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class UTF8StringType with abstract method __init__")


class TestDiameterIdentityType(unittest.TestCase):
    def test_diameter_identity_type__unable_to_instantiate_class(self):
        data = bytes.fromhex("00000011")
        
        with self.assertRaises(TypeError) as cm: 
            _type = DiameterIdentityType(data)
        
        if sys.version_info[1] <= 8:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class DiameterIdentityType with abstract methods __init__")
        elif sys.version_info[1] == 9:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class DiameterIdentityType with abstract method __init__")


class TestDiameterURIType(unittest.TestCase):
    def test_diameter_uri_type__unable_to_instantiate_class(self):
        data = bytes.fromhex("00000011")
        
        with self.assertRaises(TypeError) as cm: 
            _type = DiameterURIType(data)
        
        if sys.version_info[1] <= 8:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class DiameterURIType with abstract methods __init__")
        elif sys.version_info[1] == 9:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class DiameterURIType with abstract method __init__")



class TestEnumeratedType(unittest.TestCase):
    def test_enumerated_type__unable_to_instantiate_class(self):
        data = bytes.fromhex("00000011")
        
        with self.assertRaises(TypeError) as cm: 
            _type = EnumeratedType(data)
        
        if sys.version_info[1] <= 8:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class EnumeratedType with abstract methods __init__")
        elif sys.version_info[1] == 9:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class EnumeratedType with abstract method __init__")


if __name__ == "__main__":
    unittest.main()