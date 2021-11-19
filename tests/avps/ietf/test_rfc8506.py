# -*- coding: utf-8 -*-
"""
    tests.avps.ietf.test_rfc8506
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for IETF RFC 8506.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.avps.ietf.rfc8506 import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_cc_request_number_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_cc_request_type_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_rating_group_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_service_identifier_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_user_equipment_info_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_user_equipment_info_type_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_user_equipment_info_value_avp_stream(self):
        pass


class TestCcRequestNumberAVP(unittest.TestCase):
    pass


class TestCcRequestTypeAVP(unittest.TestCase):
    pass


class TestRatingGroupAVP(unittest.TestCase):
    pass


class TestServiceIdentifierAVP(unittest.TestCase):
    pass


class TestUserEquipmentInfoAVP(unittest.TestCase):
    pass


class TestUserEquipmentInfoTypeAVP(unittest.TestCase):
    pass


class TestUserEquipmentInfoValueAVP(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()