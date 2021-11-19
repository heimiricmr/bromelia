# -*- coding: utf-8 -*-
"""
    tests.avps.etsi_3gpp.test_ts_183_017
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for ETSI TS 183 017.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(testing_dir))

sys.path.insert(0, base_dir)

from bromelia.avps.etsi_3gpp.ts_183_017 import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_reservation_priority_avp_stream(self):
        stream = bytes.fromhex("000001ca80000010000032db00000005")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ReservationPriorityAVP))
        self.assertEqual(avps[0].code, RESERVATION_PRIORITY_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_ETSI)
        self.assertEqual(avps[0].data, PRIORITY_FIVE)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 458 [Reservation-Priority] VENDOR>")


class TestReservationPriorityAVP(unittest.TestCase):
    def test__reservation_priority_avp__no_value(self):
        avp = ReservationPriorityAVP()

    def test__reservation_priority_avp__repr_dunder(self):
        avp = ReservationPriorityAVP()
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 458 [Reservation-Priority] VENDOR>")

    def test__reservation_priority_avp__diameter_avp_convert_classmethod(self):
        avp = ReservationPriorityAVP()

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__reservation_priority_avp__1(self):
        avp = ReservationPriorityAVP()
        ref = "000001ca80000010000032db00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reservation_priority_avp__2(self):
        avp = ReservationPriorityAVP(PRIORITY_ONE)
        ref = "000001ca80000010000032db00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reservation_priority_avp__3(self):
        avp = ReservationPriorityAVP(PRIORITY_TWO)
        ref = "000001ca80000010000032db00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reservation_priority_avp__4(self):
        avp = ReservationPriorityAVP(PRIORITY_THREE)
        ref = "000001ca80000010000032db00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reservation_priority_avp__5(self):
        avp = ReservationPriorityAVP(PRIORITY_FOUR)
        ref = "000001ca80000010000032db00000004"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reservation_priority_avp__6(self):
        avp = ReservationPriorityAVP(PRIORITY_FIVE)
        ref = "000001ca80000010000032db00000005"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reservation_priority_avp__7(self):
        avp = ReservationPriorityAVP(PRIORITY_SIX)
        ref = "000001ca80000010000032db00000006"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reservation_priority_avp__8(self):
        avp = ReservationPriorityAVP(PRIORITY_SEVEN)
        ref = "000001ca80000010000032db00000007"
        self.assertEqual(avp.dump().hex(), ref)


if __name__ == "__main__":
    unittest.main()