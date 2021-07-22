# -*- coding: utf-8 -*-
"""
    test.etsi_3gpp_s6b.test_avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP unittests 
	for 3GPP S6b Diameter Application Id.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(testing_dir))

sys.path.insert(0, base_dir)

from bromelia.avps import *
from bromelia.base import *
from bromelia.constants import *
from bromelia.exceptions import *

from bromelia.etsi_3gpp_s6b.avps import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_mip6_feature_vector_avp_stream(self):
        stream = bytes.fromhex("0000007c400000100000400000000000")

        avps = DiameterAVP.load(stream)
        # self.assertTrue(isinstance(avps[0], Mip6FeatureVectorAVP))    # it needs to be reviewed
        self.assertEqual(avps[0].code, MIP6_FEATURE_VECTOR_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, bytes.fromhex("0000400000000000"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 124 [Mip6-Feature-Vector] MANDATORY>")


class TestMip6FeatureVectorAVP(unittest.TestCase):
    def test__mip6_feature_vector_avp__no_value(self):
        self.assertRaises(TypeError, Mip6FeatureVectorAVP)

    def test__mip6_feature_vector_avp__repr_dunder(self):
        value = bytes.fromhex("0000400000000000")
        avp = Mip6FeatureVectorAVP(value)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 124 [Mip6-Feature-Vector] MANDATORY>")

    def test__mip6_feature_vector_avp__1(self):
        value = bytes.fromhex("0000400000000000")
        avp = Mip6FeatureVectorAVP(value)
        ref = "0000007c400000100000400000000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__mip6_feature_vector_avp__2(self):
        avp = Mip6FeatureVectorAVP(70368744177664)
        ref = "0000007c400000100000400000000000"
        self.assertEqual(avp.dump().hex(), ref)
        
