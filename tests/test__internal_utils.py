# -*- coding: utf-8 -*-
"""
    test.test__internal_utils
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Bromelia _internal_utils unittests.
    
    :copyright: (c) 2021 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys
import struct

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia._internal_utils import *
from bromelia.avps import *
from bromelia.base import *
from bromelia.constants import *


class TestConvertTo1Byte(unittest.TestCase):
    def test__convert_to_1_byte__1(self):
        content = convert_to_1_byte(1)
        self.assertEqual(content.hex(), "01")

    def test__convert_to_1_byte__2(self):
        content = convert_to_1_byte(2)
        self.assertEqual(content.hex(), "02")

    def test__convert_to_1_byte__16(self):
        content = convert_to_1_byte(16)
        self.assertEqual(content.hex(), "10")

    def test__convert_to_1_byte__255(self):
        content = convert_to_1_byte(255)
        self.assertEqual(content.hex(), "ff")

    def test__convert_to_1_byte__256(self):
        with self.assertRaises(struct.error) as cm: 
            content = convert_to_1_byte(256)
        self.assertEqual(cm.exception.args[0], "ubyte format requires 0 <= number <= 255")


class TestConvertTo2Bytes(unittest.TestCase):
    def test__convert_to_2_bytes__1(self):
        content = convert_to_2_bytes(1)
        self.assertEqual(content.hex(), "0001")

    def test__convert_to_2_bytes__2(self):
        content = convert_to_2_bytes(2)
        self.assertEqual(content.hex(), "0002")

    def test__convert_to_2_bytes__16(self):
        content = convert_to_2_bytes(16)
        self.assertEqual(content.hex(), "0010")

    def test__convert_to_2_bytes__255(self):
        content = convert_to_2_bytes(255)
        self.assertEqual(content.hex(), "00ff")

    def test__convert_to_2_bytes__256(self):
        content = convert_to_2_bytes(256)
        self.assertEqual(content.hex(), "0100")

    def test__convert_to_2_bytes__1024(self):
        content = convert_to_2_bytes(1024)
        self.assertEqual(content.hex(), "0400")

    def test__convert_to_2_bytes__16384(self):
        content = convert_to_2_bytes(16384)
        self.assertEqual(content.hex(), "4000")

    def test__convert_to_2_bytes__65535(self):
        content = convert_to_2_bytes(65535)
        self.assertEqual(content.hex(), "ffff")

    def test__convert_to_2_bytes__524288(self):
        with self.assertRaises(struct.error) as cm: 
            content = convert_to_2_bytes(524288)
        self.assertEqual(cm.exception.args[0], "'H' format requires 0 <= number <= 65535")


class TestConvertTo3Bytes(unittest.TestCase):
    def test__convert_to_3_bytes__1(self):
        content = convert_to_3_bytes(1)
        self.assertEqual(content.hex(), "000001")

    def test__convert_to_3_bytes__2(self):
        content = convert_to_3_bytes(2)
        self.assertEqual(content.hex(), "000002")

    def test__convert_to_3_bytes__16(self):
        content = convert_to_3_bytes(16)
        self.assertEqual(content.hex(), "000010")

    def test__convert_to_3_bytes__255(self):
        content = convert_to_3_bytes(255)
        self.assertEqual(content.hex(), "0000ff")

    def test__convert_to_3_bytes__256(self):
        content = convert_to_3_bytes(256)
        self.assertEqual(content.hex(), "000100")

    def test__convert_to_3_bytes__1024(self):
        content = convert_to_3_bytes(1024)
        self.assertEqual(content.hex(), "000400")

    def test__convert_to_3_bytes__16384(self):
        content = convert_to_3_bytes(16384)
        self.assertEqual(content.hex(), "004000")

    def test__convert_to_3_bytes__65535(self):
        content = convert_to_3_bytes(65535)
        self.assertEqual(content.hex(), "00ffff")

    def test__convert_to_3_bytes__524288(self):
        content = convert_to_3_bytes(524288)
        self.assertEqual(content.hex(), "080000")

    def test__convert_to_3_bytes__8388608(self):
        content = convert_to_3_bytes(8388608)
        self.assertEqual(content.hex(), "800000")

    def test__convert_to_3_bytes__16777215(self):
        content = convert_to_3_bytes(16777215)
        self.assertEqual(content.hex(), "ffffff")

    def test__convert_to_3_bytes__16777216(self):
        with self.assertRaises(OverflowError) as cm: 
            content = convert_to_3_bytes(16777216)
        self.assertEqual(cm.exception.args[0], "int too big to convert")


class TestConvertTo4Bytes(unittest.TestCase):
    def test__convert_to_4_bytes__1(self):
        content = convert_to_4_bytes(1)
        self.assertEqual(content.hex(), "00000001")

    def test__convert_to_4_bytes__2(self):
        content = convert_to_4_bytes(2)
        self.assertEqual(content.hex(), "00000002")

    def test__convert_to_4_bytes__16(self):
        content = convert_to_4_bytes(16)
        self.assertEqual(content.hex(), "00000010")

    def test__convert_to_4_bytes__255(self):
        content = convert_to_4_bytes(255)
        self.assertEqual(content.hex(), "000000ff")

    def test__convert_to_4_bytes__256(self):
        content = convert_to_4_bytes(256)
        self.assertEqual(content.hex(), "00000100")

    def test__convert_to_4_bytes__1024(self):
        content = convert_to_4_bytes(1024)
        self.assertEqual(content.hex(), "00000400")

    def test__convert_to_4_bytes__16384(self):
        content = convert_to_4_bytes(16384)
        self.assertEqual(content.hex(), "00004000")

    def test__convert_to_4_bytes__65535(self):
        content = convert_to_4_bytes(65535)
        self.assertEqual(content.hex(), "0000ffff")

    def test__convert_to_4_bytes__524288(self):
        content = convert_to_4_bytes(524288)
        self.assertEqual(content.hex(), "00080000")

    def test__convert_to_4_bytes__8388608(self):
        content = convert_to_4_bytes(8388608)
        self.assertEqual(content.hex(), "00800000")

    def test__convert_to_4_bytes__16777215(self):
        content = convert_to_4_bytes(16777215)
        self.assertEqual(content.hex(), "00ffffff")

    def test__convert_to_4_bytes__4294967295(self):
        content = convert_to_4_bytes(4294967295)
        self.assertEqual(content.hex(), "ffffffff")

    def test__convert_to_4_bytes__4294967296(self):
        with self.assertRaises(struct.error) as cm: 
            content = convert_to_4_bytes(4294967296)
        self.assertEqual(cm.exception.args[0], "'L' format requires 0 <= number <= 4294967295")


class TestConvertTo6Bytes(unittest.TestCase):
    def test__convert_to_6_bytes__1(self):
        content = convert_to_6_bytes(1)
        self.assertEqual(content.hex(), "000000000001")

    def test__convert_to_6_bytes__2(self):
        content = convert_to_6_bytes(2)
        self.assertEqual(content.hex(), "000000000002")

    def test__convert_to_6_bytes__16(self):
        content = convert_to_6_bytes(16)
        self.assertEqual(content.hex(), "000000000010")

    def test__convert_to_6_bytes__255(self):
        content = convert_to_6_bytes(255)
        self.assertEqual(content.hex(), "0000000000ff")

    def test__convert_to_6_bytes__256(self):
        content = convert_to_6_bytes(256)
        self.assertEqual(content.hex(), "000000000100")

    def test__convert_to_6_bytes__1024(self):
        content = convert_to_6_bytes(1024)
        self.assertEqual(content.hex(), "000000000400")

    def test__convert_to_6_bytes__16384(self):
        content = convert_to_6_bytes(16384)
        self.assertEqual(content.hex(), "000000004000")

    def test__convert_to_6_bytes__65535(self):
        content = convert_to_6_bytes(65535)
        self.assertEqual(content.hex(), "00000000ffff")

    def test__convert_to_6_bytes__524288(self):
        content = convert_to_6_bytes(524288)
        self.assertEqual(content.hex(), "000000080000")

    def test__convert_to_6_bytes__8388608(self):
        content = convert_to_6_bytes(8388608)
        self.assertEqual(content.hex(), "000000800000")

    def test__convert_to_6_bytes__16777215(self):
        content = convert_to_6_bytes(16777215)
        self.assertEqual(content.hex(), "000000ffffff")

    def test__convert_to_6_bytes__4294967295(self):
        content = convert_to_6_bytes(4294967295)
        self.assertEqual(content.hex(), "0000ffffffff")

    def test__convert_to_6_bytes__1099511627775(self):
        content = convert_to_6_bytes(1099511627775)
        self.assertEqual(content.hex(), "00ffffffffff")

    def test__convert_to_6_bytes__281474976710655(self):
        content = convert_to_6_bytes(281474976710655)
        self.assertEqual(content.hex(), "ffffffffffff")

    def test__convert_to_6_bytes__281474976710656(self):
        with self.assertRaises(OverflowError) as cm:
            content = convert_to_6_bytes(281474976710656)
        self.assertEqual(cm.exception.args[0], "int too big to convert")


class TestConvertTo8Bytes(unittest.TestCase):
    def test__convert_to_8_bytes__1(self):
        content = convert_to_8_bytes(1)
        self.assertEqual(content.hex(), "0000000000000001")

    def test__convert_to_8_bytes__2(self):
        content = convert_to_8_bytes(2)
        self.assertEqual(content.hex(), "0000000000000002")

    def test__convert_to_8_bytes__16(self):
        content = convert_to_8_bytes(16)
        self.assertEqual(content.hex(), "0000000000000010")

    def test__convert_to_8_bytes__255(self):
        content = convert_to_8_bytes(255)
        self.assertEqual(content.hex(), "00000000000000ff")

    def test__convert_to_8_bytes__256(self):
        content = convert_to_8_bytes(256)
        self.assertEqual(content.hex(), "0000000000000100")

    def test__convert_to_8_bytes__1024(self):
        content = convert_to_8_bytes(1024)
        self.assertEqual(content.hex(), "0000000000000400")

    def test__convert_to_8_bytes__16384(self):
        content = convert_to_8_bytes(16384)
        self.assertEqual(content.hex(), "0000000000004000")

    def test__convert_to_8_bytes__65535(self):
        content = convert_to_8_bytes(65535)
        self.assertEqual(content.hex(), "000000000000ffff")

    def test__convert_to_8_bytes__524288(self):
        content = convert_to_8_bytes(524288)
        self.assertEqual(content.hex(), "0000000000080000")

    def test__convert_to_8_bytes__8388608(self):
        content = convert_to_8_bytes(8388608)
        self.assertEqual(content.hex(), "0000000000800000")

    def test__convert_to_8_bytes__16777215(self):
        content = convert_to_8_bytes(16777215)
        self.assertEqual(content.hex(), "0000000000ffffff")

    def test__convert_to_8_bytes__4294967295(self):
        content = convert_to_8_bytes(4294967295)
        self.assertEqual(content.hex(), "00000000ffffffff")

    def test__convert_to_8_bytes__1099511627775(self):
        content = convert_to_8_bytes(1099511627775)
        self.assertEqual(content.hex(), "000000ffffffffff")

    def test__convert_to_8_bytes__281474976710655(self):
        content = convert_to_8_bytes(281474976710655)
        self.assertEqual(content.hex(), "0000ffffffffffff")

    def test__convert_to_8_bytes__72057594037927935(self):
        content = convert_to_8_bytes(72057594037927935)
        self.assertEqual(content.hex(), "00ffffffffffffff")

    def test__convert_to_8_bytes__1152921504606846975(self):
        content = convert_to_8_bytes(1152921504606846975)
        self.assertEqual(content.hex(), "0fffffffffffffff")

    def test__convert_to_8_bytes__18446744073709551616(self):
        with self.assertRaises(struct.error) as cm:
            content = convert_to_8_bytes(18446744073709551616)
        self.assertEqual(cm.exception.args[0], "int too large to convert")


class TestConvertToIntegerFromBytes(unittest.TestCase):
    def test__convert_to_integer_from_bytes__1(self):
        content = convert_to_integer_from_bytes(convert_to_1_byte(255))
        self.assertEqual(content, 255)

    def test__convert_to_integer_from_bytes__2(self):
        content = convert_to_integer_from_bytes(convert_to_2_bytes(255))
        self.assertEqual(content, 255)

    def test__convert_to_integer_from_bytes__3(self):
        content = convert_to_integer_from_bytes(convert_to_3_bytes(255))
        self.assertEqual(content, 255)

    def test__convert_to_integer_from_bytes__4(self):
        content = convert_to_integer_from_bytes(convert_to_4_bytes(255))
        self.assertEqual(content, 255)

    def test__convert_to_integer_from_bytes__6(self):
        content = convert_to_integer_from_bytes(convert_to_6_bytes(255))
        self.assertEqual(content, 255)

    def test__convert_to_integer_from_bytes__8(self):
        content = convert_to_integer_from_bytes(convert_to_8_bytes(255))
        self.assertEqual(content, 255)


class TestHeaderRepresentation(unittest.TestCase):
    def test__header_representation__asa__set_error_bit(self):
        header = DiameterHeader(1, 40, 274, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'ASA', 'cmd_code_int': 274, 'flag_representation': ' ERR', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_RESPONSE_AND_ERROR, ABORT_SESSION_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'ASA', 'cmd_code_int': 274, 'flag_representation': ' ERR', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__asa(self):
        header = DiameterHeader(1, 0, 274, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'ASA', 'cmd_code_int': 274, 'flag_representation': '', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_RESPONSE, ABORT_SESSION_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'ASA', 'cmd_code_int': 274, 'flag_representation': '', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__asr__set_error_bit(self):
        header = DiameterHeader(1, 128, 274, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'ASR', 'cmd_code_int': 274, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_REQUEST, ABORT_SESSION_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'ASR', 'cmd_code_int': 274, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__asr(self):
        header = DiameterHeader(1, 128, 274, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'ASR', 'cmd_code_int': 274, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_REQUEST, ABORT_SESSION_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'ASR', 'cmd_code_int': 274, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__cea__set_error_bit(self):
        header = DiameterHeader(1, 40, 257, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'CEA', 'cmd_code_int': 257, 'flag_representation': ' ERR', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_RESPONSE_AND_ERROR, CAPABILITIES_EXCHANGE_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'CEA', 'cmd_code_int': 257, 'flag_representation': ' ERR', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__cea(self):
        header = DiameterHeader(1, 0, 257, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'CEA', 'cmd_code_int': 257, 'flag_representation': '', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_RESPONSE, CAPABILITIES_EXCHANGE_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'CEA', 'cmd_code_int': 257, 'flag_representation': '', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__cer__set_error_bit(self):
        header = DiameterHeader(1, 128, 257, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'CER', 'cmd_code_int': 257, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_REQUEST, CAPABILITIES_EXCHANGE_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'CER', 'cmd_code_int': 257, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__cer(self):
        header = DiameterHeader(1, 128, 257, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'CER', 'cmd_code_int': 257, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_REQUEST, CAPABILITIES_EXCHANGE_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'CER', 'cmd_code_int': 257, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__dwa__set_error_bit(self):
        header = DiameterHeader(1, 40, 280, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DWA', 'cmd_code_int': 280, 'flag_representation': ' ERR', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_RESPONSE_AND_ERROR, DEVICE_WATCHDOG_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DWA', 'cmd_code_int': 280, 'flag_representation': ' ERR', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__dwa(self):
        header = DiameterHeader(1, 0, 280, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DWA', 'cmd_code_int': 280, 'flag_representation': '', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_RESPONSE, DEVICE_WATCHDOG_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DWA', 'cmd_code_int': 280, 'flag_representation': '', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__dwr__set_error_bit(self):
        header = DiameterHeader(1, 128, 280, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DWR', 'cmd_code_int': 280, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_REQUEST, DEVICE_WATCHDOG_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DWR', 'cmd_code_int': 280, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__dwr(self):
        header = DiameterHeader(1, 128, 280, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DWR', 'cmd_code_int': 280, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_REQUEST, DEVICE_WATCHDOG_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DWR', 'cmd_code_int': 280, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__dpa__set_error_bit(self):
        header = DiameterHeader(1, 40, 282, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DPA', 'cmd_code_int': 282, 'flag_representation': ' ERR', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_RESPONSE_AND_ERROR, DISCONNECT_PEER_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DPA', 'cmd_code_int': 282, 'flag_representation': ' ERR', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__dpa(self):
        header = DiameterHeader(1, 0, 282, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DPA', 'cmd_code_int': 282, 'flag_representation': '', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_RESPONSE, DISCONNECT_PEER_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DPA', 'cmd_code_int': 282, 'flag_representation': '', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__dpr__set_error_bit(self):
        header = DiameterHeader(1, 128, 282, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DPR', 'cmd_code_int': 282, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_REQUEST, DISCONNECT_PEER_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DPR', 'cmd_code_int': 282, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

    def test__header_representation__dpr(self):
        header = DiameterHeader(1, 128, 282, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DPR', 'cmd_code_int': 282, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})

        header = DiameterHeader(1, FLAG_REQUEST, DISCONNECT_PEER_MESSAGE, 0, 11111, 11111)
        header_repr = header_representation(header)
        self.assertEqual(header_repr, {'cmd_code_str': 'DPR', 'cmd_code_int': 282, 'flag_representation': ' REQ', 'app_id_str': 'Diameter common message', 'app_id_int': 0})


class TestApplicationIdLookUp(unittest.TestCase):
    def test__application_id_look_up__DEFAULT(self):
        app_id_str, app_id_num = application_id_look_up(DIAMETER_APPLICATION_DEFAULT)
        self.assertEqual(app_id_str, "Diameter common message")
        self.assertEqual(app_id_num, 0)

    def test__application_id_look_up__Cx(self):
        app_id_str, app_id_num = application_id_look_up(DIAMETER_APPLICATION_Cx)
        self.assertEqual(app_id_str, "3GPP Cx")
        self.assertEqual(app_id_num, 16777216)

    def test__application_id_look_up__Sh(self):
        app_id_str, app_id_num = application_id_look_up(DIAMETER_APPLICATION_Sh)
        self.assertEqual(app_id_str, "3GPP Sh")
        self.assertEqual(app_id_num, 16777217)

    def test__application_id_look_up__Zh(self):
        app_id_str, app_id_num = application_id_look_up(DIAMETER_APPLICATION_Zh)
        self.assertEqual(app_id_str, "3GPP Zh")
        self.assertEqual(app_id_num, 16777221)

    def test__application_id_look_up__Rx(self):
        app_id_str, app_id_num = application_id_look_up(DIAMETER_APPLICATION_Rx)
        self.assertEqual(app_id_str, "3GPP Rx")
        self.assertEqual(app_id_num, 16777236)

    def test__application_id_look_up__Gx(self):
        app_id_str, app_id_num = application_id_look_up(DIAMETER_APPLICATION_Gx)
        self.assertEqual(app_id_str, "3GPP Gx")
        self.assertEqual(app_id_num, 16777238)

    def test__application_id_look_up__S6a(self):
        app_id_str, app_id_num = application_id_look_up(DIAMETER_APPLICATION_S6a)
        self.assertEqual(app_id_str, "3GPP S6a")
        self.assertEqual(app_id_num, 16777251)

    def test__application_id_look_up__S13(self):
        app_id_str, app_id_num = application_id_look_up(DIAMETER_APPLICATION_S13)
        self.assertEqual(app_id_str, "3GPP S13")
        self.assertEqual(app_id_num, 16777252)

    def test__application_id_look_up__SWm(self):
        app_id_str, app_id_num = application_id_look_up(DIAMETER_APPLICATION_SWm)
        self.assertEqual(app_id_str, "3GPP SWm")
        self.assertEqual(app_id_num, 16777264)

    def test__application_id_look_up__SWx(self):
        app_id_str, app_id_num = application_id_look_up(DIAMETER_APPLICATION_SWx)
        self.assertEqual(app_id_str, "3GPP SWx")
        self.assertEqual(app_id_num, 16777265)

    def test__application_id_look_up__S6b(self):
        app_id_str, app_id_num = application_id_look_up(DIAMETER_APPLICATION_S6b)
        self.assertEqual(app_id_str, "3GPP S6b")
        self.assertEqual(app_id_num, 16777272)

    def test__application_id_look_up__SLh(self):
        app_id_str, app_id_num = application_id_look_up(DIAMETER_APPLICATION_SLh)
        self.assertEqual(app_id_str, "3GPP SLh")
        self.assertEqual(app_id_num, 16777291)

    def test__application_id_look_up__UNKNOWN(self):
        app_id_str, app_id_num = application_id_look_up(DIAMETER_APPLICATION_UNKNOWN)
        self.assertEqual(app_id_str, "")
        self.assertEqual(app_id_num, "Unknown")

    def test__application_id_look_up__RELAY(self):
        app_id_str, app_id_num = application_id_look_up(DIAMETER_APPLICATION_RELAY)
        self.assertEqual(app_id_str, "Relay")
        self.assertEqual(app_id_num, 4294967295)


class TestCommandCodeLookUp(unittest.TestCase):
    def test__command_code_look_up__ASR_ASA(self):
        cmd_str, cmd_num = command_code_look_up(ABORT_SESSION_MESSAGE)
        self.assertEqual(cmd_str, "ASR/ASA")
        self.assertEqual(cmd_num, 274)

    def test__command_code_look_up__CER_CEA(self):
        cmd_str, cmd_num = command_code_look_up(CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(cmd_str, "CER/CEA")
        self.assertEqual(cmd_num, 257)

    def test__command_code_look_up__DWR_DWA(self):
        cmd_str, cmd_num = command_code_look_up(DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(cmd_str, "DWR/DWA")
        self.assertEqual(cmd_num, 280)

    def test__command_code_look_up__DPR_DPA(self):
        cmd_str, cmd_num = command_code_look_up(DISCONNECT_PEER_MESSAGE)
        self.assertEqual(cmd_str, "DPR/DPA")
        self.assertEqual(cmd_num, 282)

    def test__command_code_look_up__RAR_RAA(self):
        cmd_str, cmd_num = command_code_look_up(RE_AUTH_MESSAGE)
        self.assertEqual(cmd_str, "RAR/RAA")
        self.assertEqual(cmd_num, 258)

    def test__command_code_look_up__STR_STA(self):
        cmd_str, cmd_num = command_code_look_up(SESSION_TERMINATION_MESSAGE)
        self.assertEqual(cmd_str, "STR/STA")
        self.assertEqual(cmd_num, 275)


class TestAvpLookUp(unittest.TestCase):
    def test__user_name_avp(self):
        avp = UserNameAVP("my-user@nai.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avp_look_up(avp), "User-Name")

    def test__class_avp(self):
        avp = ClassAVP("CLOSED")
        self.assertEqual(avp_look_up(avp), "Class")

    def test__session_timeout_avp(self):
        avp = SessionTimeoutAVP(10799)
        self.assertEqual(avp_look_up(avp), "Session-Timeout")

    def test__proxy_state_avp(self):
        avp = ProxyStateAVP("CLOSED")
        self.assertEqual(avp_look_up(avp), "Proxy-State")

    def test__acct_session_id(self):
        avp = AcctSessionIdAVP(convert_to_4_bytes(6733))
        self.assertEqual(avp_look_up(avp), "Acct-Session-Id")

    def test__acct_multi_session_id(self):
        avp = AcctMultiSessionIdAVP("es2")
        self.assertEqual(avp_look_up(avp), "Acct-Multi-Session-Id")

    def test__event_timestamp(self):
        avp = EventTimestampAVP()
        self.assertEqual(avp_look_up(avp), "Event-Timestamp")

    def test__acct_interim_interval(self):
        avp = AcctInterimIntervalAVP(DIAMETER_APPLICATION_SWm)
        self.assertEqual(avp_look_up(avp), "Acct-Interim-Interval")

    def test__host_ip_address(self):
        avp = HostIpAddressAVP("10.129.241.235")
        self.assertEqual(avp_look_up(avp), "Host-IP-Address")


class TestGetAppIds(unittest.TestCase):
    def test__get_app_ids__DEFAULT(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_DEFAULT}])
        self.assertEqual(app_ids, "Diameter common message")

    def test__get_app_ids__Cx(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_Cx}])
        self.assertEqual(app_ids, "3GPP Cx")

    def test__get_app_ids__Sh(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_Sh}])
        self.assertEqual(app_ids, "3GPP Sh")

    def test__get_app_ids__Zh(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_Zh}])
        self.assertEqual(app_ids, "3GPP Zh")

    def test__get_app_ids__Rx(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_Rx}])
        self.assertEqual(app_ids, "3GPP Rx")

    def test__get_app_ids__Gx(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_Gx}])
        self.assertEqual(app_ids, "3GPP Gx")

    def test__get_app_ids__S6a(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_S6a}])
        self.assertEqual(app_ids, "3GPP S6a")

    def test__get_app_ids__S13(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_S13}])
        self.assertEqual(app_ids, "3GPP S13")

    def test__get_app_ids__SWm(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_SWm}])
        self.assertEqual(app_ids, "3GPP SWm")

    def test__get_app_ids__SWx(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_SWx}])
        self.assertEqual(app_ids, "3GPP SWx")

    def test__get_app_ids__S6b(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_S6b}])
        self.assertEqual(app_ids, "3GPP S6b")

    def test__get_app_ids__SLh(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_SLh}])
        self.assertEqual(app_ids, "3GPP SLh")

    def test__get_app_ids__UNKNOWN(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_UNKNOWN}])
        self.assertEqual(app_ids, "")

    def test__get_app_ids__RELAY(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_RELAY}])
        self.assertEqual(app_ids, "Relay")

    def test__get_app_ids__Cx_Sh(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_Cx}, {"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_Sh}])
        self.assertEqual(app_ids, "3GPP Cx;3GPP Sh")

    def test__get_app_ids__Cx_Sh_Rx(self):
        app_ids = get_app_ids([{"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_Cx}, {"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_Sh}, {"vendor_id": VENDOR_ID_3GPP, "app_id": DIAMETER_APPLICATION_Rx}])
        self.assertEqual(app_ids, "3GPP Cx;3GPP Sh;3GPP Rx")


class TestGetAvpNameFormatted(unittest.TestCase):
    def test__get_avp_name_formatted__1(self):
        avp_name = get_avp_name_formatted("user_name")
        self.assertEqual(avp_name, "user_name_avp")

    def test__get_avp_name_formatted__2(self):
        avp_name = get_avp_name_formatted("origin_host")
        self.assertEqual(avp_name, "origin_host_avp")

    def test__get_avp_name_formatted__3(self):
        avp_name = get_avp_name_formatted("origin_realm")
        self.assertEqual(avp_name, "origin_realm_avp")

    def test__get_avp_name_formatted__4(self):
        avp_name = get_avp_name_formatted("destination_host")
        self.assertEqual(avp_name, "destination_host_avp")

    def test__get_avp_name_formatted__5(self):
        avp_name = get_avp_name_formatted("destination_realm")
        self.assertEqual(avp_name, "destination_realm_avp")

    def test__get_avp_name_formatted__6(self):
        avp_name = get_avp_name_formatted("user_name__1")
        self.assertEqual(avp_name, "user_name_avp__1")

    def test__get_avp_name_formatted__7(self):
        avp_name = get_avp_name_formatted("user_name__10")
        self.assertEqual(avp_name, "user_name_avp__10")

    def test__get_avp_name_formatted__8(self):
        avp_name = get_avp_name_formatted("max_requested_bw_dl__256")
        self.assertEqual(avp_name, "max_requested_bw_dl_avp__256")


class TestGetLoggingFileName(unittest.TestCase):
    def setUp(self):
        self.prog = re.compile(r"log\-(.*)\-(\d{4}\-\d{2}\-\d{2})\-(\d{2}\-\d{2}\-\d{2})\-UTC(.*)\-pid\_(\d*)", re.X)

    def test__get_logging_filename__1(self):
        filename = get_logging_filename("AAA")
        match = self.prog.match(filename).groups()

        self.assertEqual(match[0], "aaa")

    def test__get_logging_filename__2(self):
        filename = get_logging_filename("HSS")
        match = self.prog.match(filename).groups()

        self.assertEqual(match[0], "hss")

    def test__get_logging_filename__3(self):
        filename = get_logging_filename("PCRF")
        match = self.prog.match(filename).groups()

        self.assertEqual(match[0], "pcrf")

    def test__get_logging_filename__4(self):
        filename = get_logging_filename("OCS")
        match = self.prog.match(filename).groups()

        self.assertEqual(match[0], "ocs")

    def test__get_logging_filename__5(self):
        filename = get_logging_filename("DRA")
        match = self.prog.match(filename).groups()

        self.assertEqual(match[0], "dra")

    def test__get_logging_filename__6(self):
        filename = get_logging_filename("")
        match = self.prog.match(filename).groups()

        self.assertEqual(match[0], "dsa")

    def test__get_logging_filename__7(self):
        filename = get_logging_filename()
        match = self.prog.match(filename).groups()

        self.assertEqual(match[0], "dsa")

    def test__get_logging_filename__invalid__1(self):
        with self.assertRaises(Exception) as cm:
            filename = get_logging_filename("DRA-HSS")
        self.assertEqual(cm.exception.args[0], "Invalid symbol found")

    def test__get_logging_filename__invalid__2(self):
        with self.assertRaises(Exception) as cm:
            filename = get_logging_filename("DRA+HSS")
        self.assertEqual(cm.exception.args[0], "Invalid symbol found")

    def test__get_logging_filename__invalid__3(self):
        with self.assertRaises(Exception) as cm:
            filename = get_logging_filename("DRA=HSS")
        self.assertEqual(cm.exception.args[0], "Invalid symbol found")


if __name__ == "__main__":
    unittest.main()