# -*- coding: utf-8 -*-
"""
    tests.avps.ietf.test_rfc7155
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for IETF RFC 7155.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.avps.ietf.rfc7155 import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_framed_ip_address_avp_stream(self):
        stream = bytes.fromhex("000000084000000c0a2d000c")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], FramedIpAddressAVP))
        self.assertEqual(avps[0].code, FRAMED_IP_ADDRESS_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, bytes.fromhex("0a2d000c"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 8 [Framed-Ip-Address] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_called_station_id_avp_stream(self):
        stream = bytes.fromhex("0000001e4000000931000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], CalledStationIdAVP))
        self.assertEqual(avps[0].code, CALLED_STATION_ID_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 9)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"1")
        self.assertEqual(avps[0].get_padding_length(), 3)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 30 [Called-Station-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_framed_ipv6_prefix_avp_stream(self):
        stream = bytes.fromhex("000000614000001a0080280403886010041200b1d8508280babe0000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], FramedIpv6PrefixAVP))
        self.assertEqual(avps[0].code, FRAMED_IPV6_PREFIX_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 26)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, bytes.fromhex("0080280403886010041200b1d8508280babe"))
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 97 [Framed-Ipv6-Prefix] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_calling_station_id_avp_stream(self):
        stream = bytes.fromhex("0000001f4000000d66726f646f000000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], CallingStationIdAVP))
        self.assertEqual(avps[0].code, CALLING_STATION_ID_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 13)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"frodo")
        self.assertEqual(avps[0].get_padding_length(), 3)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 31 [Calling-Station-Id] MANDATORY>")


class TestFramedIpAddressAVP(unittest.TestCase):
    def test__framed_ip_address_avp__no_value(self):
        self.assertRaises(TypeError, FramedIpAddressAVP)

    def test__framed_ip_address_avp__repr_dunder(self):
        value = bytes.fromhex("0a2d0012")
        avp = FramedIpAddressAVP(value)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 8 [Framed-Ip-Address] MANDATORY>")

    def test__framed_ip_address_avp__diameter_avp_convert_classmethod(self):
        value = bytes.fromhex("0a2d0012")
        avp = FramedIpAddressAVP(value)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__framed_ip_address_avp__1(self):
        value = bytes.fromhex("0a2d000c")
        avp = FramedIpAddressAVP(value)
        ref = "000000084000000c0a2d000c"
        self.assertEqual(avp.dump().hex(), ref)

    def test__framed_ip_address_avp__2(self):
        avp = FramedIpAddressAVP("10.45.0.12")
        ref = "000000084000000c0a2d000c"
        self.assertEqual(avp.dump().hex(), ref)


class TestCalledStationIdAVP(unittest.TestCase):
    def test__called_station_id_avp__no_value(self):
        self.assertRaises(TypeError, CalledStationIdAVP)

    def test__called_station_id_avp__repr_dunder(self):
        avp = CalledStationIdAVP("1")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 30 [Called-Station-Id] MANDATORY>")

    def test__called_station_id_avp__diameter_avp_convert_classmethod(self):
        avp = CalledStationIdAVP("1")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__called_station_id_avp__1(self):
        avp = CalledStationIdAVP("1")
        ref = "0000001e4000000931000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__called_station_id_avp__2(self):
        avp = CalledStationIdAVP("2")
        ref = "0000001e4000000932000000"
        self.assertEqual(avp.dump().hex(), ref)


class TestFramedIpv6PrefixAVP(unittest.TestCase):
    def test__framed_ipv6_prefix_avp__no_value(self):
        self.assertRaises(TypeError, FramedIpv6PrefixAVP)

    def test__framed_ipv6_prefix_avp__repr_dunder(self):
        avp = FramedIpv6PrefixAVP(bytes.fromhex("0080280403886010041200b1d8508280babe"))
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 97 [Framed-Ipv6-Prefix] MANDATORY>")

    def test__framed_ipv6_prefix_avp__diameter_avp_convert_classmethod(self):
        avp = FramedIpv6PrefixAVP(bytes.fromhex("0080280403886010041200b1d8508280babe"))

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__framed_ipv6_prefix_avp__1(self):
        avp = FramedIpv6PrefixAVP(bytes.fromhex("0080280403886010041200b1d8508280babe"))
        ref = "000000614000001a0080280403886010041200b1d8508280babe0000"
        self.assertEqual(avp.dump().hex(), ref)


class TestCallingStationIdAVP(unittest.TestCase):
    def test_calling_station_id_avp__no_value(self):
        self.assertRaises(TypeError, CallingStationIdAVP)

    def test_calling_station_id_avp__repr_dunder(self):
        avp = CallingStationIdAVP("my-user")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 31 [Calling-Station-Id] MANDATORY>")

    def test_calling_station_id_avp__diameter_avp_convert_classmethod(self):
        avp = CallingStationIdAVP("my-user")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_calling_station_id_avp__1(self):
        avp = CallingStationIdAVP("frodo")
        ref = "0000001f4000000d66726f646f000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_calling_station_id_avp__2(self):
        avp = CallingStationIdAVP("link")
        ref = "0000001f4000000c6c696e6b"
        self.assertEqual(avp.dump().hex(), ref)


if __name__ == "__main__":
    unittest.main()