# -*- coding: utf-8 -*-
"""
    test.test_utils
    ~~~~~~~~~~~~~~~

    This module contains the Bromelia utils unittests.
    
    :copyright: (c) 2021 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.utils import (convert_to_4_length_bit, decode_from_tbcd,
                            encode_to_tbcd, encode_special_chars_to_tbcd,
                            get_two_bits, is_special_char,
                            transform_bits)

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


class TestConvertTo4LengthBit(unittest.TestCase):
    def test__convert_to_4_length_bit__0(self):
        self.assertEqual(convert_to_4_length_bit(0), "0000")

    def test__convert_to_4_length_bit__1(self):
        self.assertEqual(convert_to_4_length_bit(1), "0001")

    def test__convert_to_4_length_bit__2(self):
        self.assertEqual(convert_to_4_length_bit(2), "0010")

    def test__convert_to_4_length_bit__3(self):
        self.assertEqual(convert_to_4_length_bit(3), "0011")

    def test__convert_to_4_length_bit__4(self):
        self.assertEqual(convert_to_4_length_bit(4), "0100")

    def test__convert_to_4_length_bit__5(self):
        self.assertEqual(convert_to_4_length_bit(5), "0101")

    def test__convert_to_4_length_bit__6(self):
        self.assertEqual(convert_to_4_length_bit(6), "0110")

    def test__convert_to_4_length_bit__7(self):
        self.assertEqual(convert_to_4_length_bit(7), "0111")

    def test__convert_to_4_length_bit__8(self):
        self.assertEqual(convert_to_4_length_bit(8), "1000")

    def test__convert_to_4_length_bit__9(self):
        self.assertEqual(convert_to_4_length_bit(9), "1001")

    def test__convert_to_4_length_bit__10(self):
        self.assertEqual(convert_to_4_length_bit(10), "1010")

    def test__convert_to_4_length_bit__11(self):
        self.assertEqual(convert_to_4_length_bit(11), "1011")

    def test__convert_to_4_length_bit__12(self):
        self.assertEqual(convert_to_4_length_bit(12), "1100")

    def test__convert_to_4_length_bit__13(self):
        self.assertEqual(convert_to_4_length_bit(13), "1101")

    def test__convert_to_4_length_bit__14(self):
        self.assertEqual(convert_to_4_length_bit(14), "1110")

    def test__convert_to_4_length_bit__15(self):
        self.assertEqual(convert_to_4_length_bit(15), "1111")


class TestEncodeSpecialCharsToTbcd(unittest.TestCase):
    def test__encode_special_chars_to_tbcd__0(self):
        self.assertEqual(encode_special_chars_to_tbcd(0), "0000")

    def test__encode_special_chars_to_tbcd__1(self):
        self.assertEqual(encode_special_chars_to_tbcd(1), "0001")

    def test__encode_special_chars_to_tbcd__2(self):
        self.assertEqual(encode_special_chars_to_tbcd(2), "0010")

    def test__encode_special_chars_to_tbcd__3(self):
        self.assertEqual(encode_special_chars_to_tbcd(3), "0011")

    def test__encode_special_chars_to_tbcd__4(self):
        self.assertEqual(encode_special_chars_to_tbcd(4), "0100")

    def test__encode_special_chars_to_tbcd__5(self):
        self.assertEqual(encode_special_chars_to_tbcd(5), "0101")

    def test__encode_special_chars_to_tbcd__6(self):
        self.assertEqual(encode_special_chars_to_tbcd(6), "0110")

    def test__encode_special_chars_to_tbcd__7(self):
        self.assertEqual(encode_special_chars_to_tbcd(7), "0111")

    def test__encode_special_chars_to_tbcd__8(self):
        self.assertEqual(encode_special_chars_to_tbcd(8), "1000")

    def test__encode_special_chars_to_tbcd__9(self):
        self.assertEqual(encode_special_chars_to_tbcd(9), "1001")

    def test__encode_special_chars_to_tbcd__10(self):
        self.assertEqual(encode_special_chars_to_tbcd(10), "1010")

    def test__encode_special_chars_to_tbcd__11(self):
        self.assertEqual(encode_special_chars_to_tbcd(11), "1011")

    def test__encode_special_chars_to_tbcd__12(self):
        self.assertEqual(encode_special_chars_to_tbcd(12), "1100")

    def test__encode_special_chars_to_tbcd__13(self):
        self.assertEqual(encode_special_chars_to_tbcd(13), "1101")

    def test__encode_special_chars_to_tbcd__14(self):
        self.assertEqual(encode_special_chars_to_tbcd(14), "1110")

    def test__encode_special_chars_to_tbcd__15(self):
        self.assertEqual(encode_special_chars_to_tbcd(15), "1111")

    def test__encode_special_chars_to_tbcd__special_char__1(self):
        self.assertEqual(encode_special_chars_to_tbcd("*"), "1010")

    def test__encode_special_chars_to_tbcd__special_char__2(self):
        self.assertEqual(encode_special_chars_to_tbcd("#"), "1011")

    def test__encode_special_chars_to_tbcd__special_char__3(self):
        self.assertEqual(encode_special_chars_to_tbcd("a"), "1100")

    def test__encode_special_chars_to_tbcd__special_char__4(self):
        self.assertEqual(encode_special_chars_to_tbcd("b"), "1101")

    def test__encode_special_chars_to_tbcd__special_char__5(self):
        self.assertEqual(encode_special_chars_to_tbcd("c"), "1110")


class TestGetTwoBits(unittest.TestCase):
    def test__get_two_bits__0(self):
        self.assertEqual(get_two_bits("5521993082672", 2), "21")

    def test__get_two_bits__1(self):
        self.assertEqual(get_two_bits("5521993082672", 4), "99")

    def test__get_two_bits__2(self):
        self.assertEqual(get_two_bits("5521993082672", 6), "30")

    def test__get_two_bits__3(self):
        self.assertEqual(get_two_bits("5521993082672", 8), "82")

    def test__get_two_bits__4(self):
        self.assertEqual(get_two_bits("5521993082672", 10), "67")

    def test__get_two_bits__5(self):
        self.assertEqual(get_two_bits("5521993082672", 12), "2")

    def test__get_two_bits__6(self):
        self.assertEqual(get_two_bits("5521999999999", 0), "55")

    def test__get_two_bits__7(self):
        self.assertEqual(get_two_bits("5521999999999", 2), "21")

    def test__get_two_bits__8(self):
        self.assertEqual(get_two_bits("5521999999999", 4), "99")

    def test__get_two_bits__9(self):
        self.assertEqual(get_two_bits("5521999999999", 6), "99")

    def test__get_two_bits__10(self):
        self.assertEqual(get_two_bits("5521999999999", 8), "99")

    def test__get_two_bits__11(self):
        self.assertEqual(get_two_bits("5521999999999", 10), "99")

    def test__get_two_bits__12(self):
        self.assertEqual(get_two_bits("5521999999999", 12), "9")


class TestTransformBits(unittest.TestCase):
    def test__transform_bits__0(self):
        self.assertEqual(transform_bits("10"), "16")

    def test__transform_bits__1(self):
        self.assertEqual(transform_bits("12"), "18")

    def test__transform_bits__2(self):
        self.assertEqual(transform_bits("99"), "153")

    def test__transform_bits__3(self):
        self.assertEqual(transform_bits("03"), "3")

    def test__transform_bits__4(self):
        self.assertEqual(transform_bits("28"), "40")

    def test__transform_bits__5(self):
        self.assertEqual(transform_bits("76"), "118")

    def test__transform_bits__6(self):
        self.assertEqual(transform_bits("55"), "85")


class TestIsSpecialChar(unittest.TestCase):
    def test__is_special_char__0(self):
        self.assertFalse(is_special_char("12"))

    def test__is_special_char__1(self):
        self.assertFalse(is_special_char("99"))

    def test__is_special_char__2(self):
        self.assertFalse(is_special_char("03"))

    def test__is_special_char__3(self):
        self.assertFalse(is_special_char("12"))

    def test__is_special_char__4(self):
        self.assertFalse(is_special_char("28"))

    def test__is_special_char__5(self):
        self.assertFalse(is_special_char("76"))

    def test__is_special_char__6(self):
        self.assertTrue(is_special_char("*"))

    def test__is_special_char__7(self):
        self.assertTrue(is_special_char("#"))

    def test__is_special_char__8(self):
        self.assertTrue(is_special_char("a"))

    def test__is_special_char__9(self):
        self.assertTrue(is_special_char("b"))

    def test__is_special_char__10(self):
        self.assertTrue(is_special_char("c"))


if __name__ == "__main__":
    unittest.main()