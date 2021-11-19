# -*- coding: utf-8 -*-
"""
    tests.avps.etsi_3gpp.test_ts_129_329
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for ETSI TS 129 329.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(testing_dir))

sys.path.insert(0, base_dir)

from bromelia.avps.etsi_3gpp.ts_129_329 import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_msisdn_avp_stream(self):
        pass

class TestMsisdnAVP(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()