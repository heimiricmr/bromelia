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
    def test_unsigned32_type__unable_to_instantiate_class(self):
        data = bytes.fromhex("00000011")
        
        with self.assertRaises(TypeError) as cm: 
            _type = Unsigned32Type(data)
        
        if sys.version_info[1] <= 8:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class Unsigned32Type with abstract methods __init__")
        elif sys.version_info[1] == 9:
            self.assertEqual(cm.exception.args[0], "Can't instantiate abstract class Unsigned32Type with abstract method __init__")


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

