# -*- coding: utf-8 -*-
"""
    test.test_utils
    ~~~~~~~~~~~~~~~

    This module contains the Bromelia utils functions.
    
    :copyright: (c) 2021 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.etsi_3gpp_swm.avps import *
from bromelia.etsi_3gpp_swm.definitions import *

from bromelia.utils import encode_to_tbcd, encode_special_chars_to_tbcd, decode_from_tbcd


class TestEncodeSpecialCharsToTbcd(unittest.TestCase):
    def test__encode_special_chars_to_tbcd__valid_entries_1(self):
        encoded = encode_special_chars_to_tbcd("*")
        self.assertEqual(encoded, "1010")

        encoded = encode_special_chars_to_tbcd("#")
        self.assertEqual(encoded, "1011")

        encoded = encode_special_chars_to_tbcd("a")
        self.assertEqual(encoded, "1100")

        encoded = encode_special_chars_to_tbcd("b")
        self.assertEqual(encoded, "1101")

        encoded = encode_special_chars_to_tbcd("c")
        self.assertEqual(encoded, "1110")

    def test__encode_special_chars_to_tbcd__valid_entries_2(self):
        encoded = encode_special_chars_to_tbcd(1)
        self.assertEqual(encoded, "0001")

        encoded = encode_special_chars_to_tbcd(2)
        self.assertEqual(encoded, "0010")

        encoded = encode_special_chars_to_tbcd(3)
        self.assertEqual(encoded, "0011")

        encoded = encode_special_chars_to_tbcd(4)
        self.assertEqual(encoded, "0100")

        encoded = encode_special_chars_to_tbcd(5)
        self.assertEqual(encoded, "0101")

        encoded = encode_special_chars_to_tbcd(6)
        self.assertEqual(encoded, "0110")

        encoded = encode_special_chars_to_tbcd(7)
        self.assertEqual(encoded, "0111")

        encoded = encode_special_chars_to_tbcd(8)
        self.assertEqual(encoded, "1000")

        encoded = encode_special_chars_to_tbcd(9)
        self.assertEqual(encoded, "1001")

        encoded = encode_special_chars_to_tbcd(10)
        self.assertEqual(encoded, "1010")

    def test__encode_special_chars_to_tbcd__invalid_entries_1(self):
        encoded = encode_special_chars_to_tbcd("d")
        self.assertIsNone(encoded)

        encoded = encode_special_chars_to_tbcd("e")
        self.assertIsNone(encoded)

        encoded = encode_special_chars_to_tbcd("f")
        self.assertIsNone(encoded)

        encoded = encode_special_chars_to_tbcd("g")
        self.assertIsNone(encoded)

    def test__encode_special_chars_to_tbcd__invalid_entries_2(self):
        encoded = encode_special_chars_to_tbcd("middle_earth")
        self.assertIsNone(encoded)

        encoded = encode_special_chars_to_tbcd("1x")
        self.assertIsNone(encoded)


class TestEncodeToTbcd(unittest.TestCase):
    def test__encode_to_tbcd__1(self):
        encoded = encode_to_tbcd("5521993082672")
        self.assertEqual(encoded, "551299032876f2")

    def test__encode_to_tbcd__2(self):
        encoded = encode_to_tbcd("5521999999999")
        self.assertEqual(encoded, "551299999999f9")


class TestDecodeFromTbcd(unittest.TestCase):
    def test__decode_from_tbcd__1(self):
        decoded = decode_from_tbcd("551299032876f2")
        self.assertEqual(decoded, "5521993082672")

    def test__decode_from_tbcd__2(self):
        decoded = decode_from_tbcd("551299999999f9")
        self.assertEqual(decoded, "5521999999999")

