# -*- coding: utf-8 -*-
"""
    tests.avps.ietf.test_rfc5447
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for IETF RFC 5447.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.avps.ietf.rfc5447 import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_mip_home_agent_host_avp_stream(self):
        stream = bytes.fromhex("0000015c400000700000011b400000296570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000001254000003a746f706f6e2e73357067772e6e6f64652e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000")

        avps = DiameterAVP.load(stream)

        mip_home_agent_host_avp = avps[0]
        self.assertTrue(isinstance(mip_home_agent_host_avp, MipHomeAgentHostAVP))
        self.assertEqual(mip_home_agent_host_avp.code, MIP_HOME_AGENT_HOST_AVP_CODE)
        self.assertFalse(mip_home_agent_host_avp.is_vendor_id())
        self.assertTrue(mip_home_agent_host_avp.is_mandatory())
        self.assertFalse(mip_home_agent_host_avp.is_protected())
        self.assertEqual(mip_home_agent_host_avp.get_length(), 112)
        self.assertIsNone(mip_home_agent_host_avp.vendor_id)
        self.assertEqual(mip_home_agent_host_avp.data.hex(), "0000011b400000296570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000001254000003a746f706f6e2e73357067772e6e6f64652e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000")
        self.assertIsNone(mip_home_agent_host_avp.get_padding_length())
        self.assertEqual(mip_home_agent_host_avp.__repr__(), "<Diameter AVP: 348 [Mip-Home-Agent-Host] MANDATORY>")

        destination_realm_avp = mip_home_agent_host_avp.destination_realm_avp
        destination_host_avp = mip_home_agent_host_avp.destination_host_avp

        self.assertTrue(isinstance(destination_realm_avp, DestinationRealmAVP))
        self.assertEqual(destination_realm_avp.code, DESTINATION_REALM_AVP_CODE)
        self.assertFalse(destination_realm_avp.is_vendor_id())
        self.assertTrue(destination_realm_avp.is_mandatory())
        self.assertFalse(destination_realm_avp.is_protected())
        self.assertEqual(destination_realm_avp.get_length(), 41)
        self.assertIsNone(destination_realm_avp.vendor_id)
        self.assertEqual(destination_realm_avp.data, b"epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(destination_realm_avp.get_padding_length(), 3)
        self.assertEqual(destination_realm_avp.__repr__(), "<Diameter AVP: 283 [Destination-Realm] MANDATORY>")

        self.assertTrue(isinstance(destination_host_avp, DestinationHostAVP))
        self.assertEqual(destination_host_avp.code, DESTINATION_HOST_AVP_CODE)
        self.assertFalse(destination_host_avp.is_vendor_id())
        self.assertTrue(destination_host_avp.is_mandatory())
        self.assertFalse(destination_host_avp.is_protected())
        self.assertEqual(destination_host_avp.get_length(), 58)
        self.assertIsNone(destination_host_avp.vendor_id)
        self.assertEqual(destination_host_avp.data, b"topon.s5pgw.node.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(destination_host_avp.get_padding_length(), 2)
        self.assertEqual(destination_host_avp.__repr__(), "<Diameter AVP: 293 [Destination-Host] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_mip6_agent_info_avp_stream(self):
        self.maxDiff = None
        stream = bytes.fromhex("000001e6400000780000015c400000700000011b400000296570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000001254000003a746f706f6e2e73357067772e6e6f64652e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], Mip6AgentInfoAVP))
        self.assertEqual(avps[0].code, MIP6_AGENT_INFO_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 120)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data.hex(), "0000015c400000700000011b400000296570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000001254000003a746f706f6e2e73357067772e6e6f64652e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 486 [Mip6-Agent-Info] MANDATORY>")

        mip_home_agent_host_avp = avps[0].mip_home_agent_host_avp

        self.assertTrue(isinstance(mip_home_agent_host_avp, MipHomeAgentHostAVP))
        self.assertEqual(mip_home_agent_host_avp.code, MIP_HOME_AGENT_HOST_AVP_CODE)
        self.assertFalse(mip_home_agent_host_avp.is_vendor_id())
        self.assertTrue(mip_home_agent_host_avp.is_mandatory())
        self.assertFalse(mip_home_agent_host_avp.is_protected())
        self.assertEqual(mip_home_agent_host_avp.get_length(), 112)
        self.assertIsNone(mip_home_agent_host_avp.vendor_id)
        self.assertEqual(mip_home_agent_host_avp.data.hex(), "0000011b400000296570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000001254000003a746f706f6e2e73357067772e6e6f64652e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000")
        self.assertIsNone(mip_home_agent_host_avp.get_padding_length())
        self.assertEqual(mip_home_agent_host_avp.__repr__(), "<Diameter AVP: 348 [Mip-Home-Agent-Host] MANDATORY>")

        destination_realm_avp = mip_home_agent_host_avp.destination_realm_avp
        destination_host_avp = mip_home_agent_host_avp.destination_host_avp

        self.assertTrue(isinstance(destination_realm_avp, DestinationRealmAVP))
        self.assertEqual(destination_realm_avp.code, DESTINATION_REALM_AVP_CODE)
        self.assertFalse(destination_realm_avp.is_vendor_id())
        self.assertTrue(destination_realm_avp.is_mandatory())
        self.assertFalse(destination_realm_avp.is_protected())
        self.assertEqual(destination_realm_avp.get_length(), 41)
        self.assertIsNone(destination_realm_avp.vendor_id)
        self.assertEqual(destination_realm_avp.data, b"epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(destination_realm_avp.get_padding_length(), 3)
        self.assertEqual(destination_realm_avp.__repr__(), "<Diameter AVP: 283 [Destination-Realm] MANDATORY>")

        self.assertTrue(isinstance(destination_host_avp, DestinationHostAVP))
        self.assertEqual(destination_host_avp.code, DESTINATION_HOST_AVP_CODE)
        self.assertFalse(destination_host_avp.is_vendor_id())
        self.assertTrue(destination_host_avp.is_mandatory())
        self.assertFalse(destination_host_avp.is_protected())
        self.assertEqual(destination_host_avp.get_length(), 58)
        self.assertIsNone(destination_host_avp.vendor_id)
        self.assertEqual(destination_host_avp.data, b"topon.s5pgw.node.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(destination_host_avp.get_padding_length(), 2)
        self.assertEqual(destination_host_avp.__repr__(), "<Diameter AVP: 293 [Destination-Host] MANDATORY>")


class TestMipHomeAgentHostAVP(unittest.TestCase):
    def test_mip_home_agent_host_avp__no_value(self):
        self.assertRaises(TypeError, MipHomeAgentHostAVP)

    def test_mip_home_agent_host_avp__repr_dunder(self):
        destination_realm_avp = DestinationRealmAVP("epc.mncXXX.mccYYY.3gppnetwork.org")
        destination_host_avp = DestinationHostAVP("topon.s5pgw.node.epc.mncXXX.mccYYY.3gppnetwork.org")

        avps = [destination_realm_avp, destination_host_avp]
        avp = MipHomeAgentHostAVP(avps)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 348 [Mip-Home-Agent-Host] MANDATORY>")

    def test_mip_home_agent_host_avp__diameter_avp_convert_classmethod(self):
        destination_realm_avp = DestinationRealmAVP("epc.mncXXX.mccYYY.3gppnetwork.org")
        destination_host_avp = DestinationHostAVP("topon.s5pgw.node.epc.mncXXX.mccYYY.3gppnetwork.org")

        avps = [destination_realm_avp, destination_host_avp]
        avp = MipHomeAgentHostAVP(avps)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_mip_home_agent_host_avp__1(self):
        self.maxDiff = None
        ref = "0000015c400000700000011b400000296570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000001254000003a746f706f6e2e73357067772e6e6f64652e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000"
      
        destination_realm_avp = DestinationRealmAVP("epc.mncXXX.mccYYY.3gppnetwork.org")
        destination_host_avp = DestinationHostAVP("topon.s5pgw.node.epc.mncXXX.mccYYY.3gppnetwork.org")

        avps = [destination_realm_avp, destination_host_avp]
        avp = MipHomeAgentHostAVP(avps)
        self.assertEqual(avp.dump().hex(), ref)


class TestMip6AgentInfoAVP(unittest.TestCase):
    def test_mip6_agent_info_host_avp__no_value(self):
        self.assertRaises(TypeError, Mip6AgentInfoAVP)

    def test_mip6_agent_info_avp__repr_dunder(self):
        avp = Mip6AgentInfoAVP([
                                    MipHomeAgentHostAVP([
                                                            DestinationRealmAVP("epc.mncXXX.mccYYY.3gppnetwork.org"), 
                                                            DestinationHostAVP("topon.s5pgw.node.epc.mncXXX.mccYYY.3gppnetwork.org")
                                    ])
        ])
        
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 486 [Mip6-Agent-Info] MANDATORY>")

    def test_mip6_agent_info_avp__mip_home_agent_host_only(self):
        ref = "000001e6400000780000015c400000700000011b400000296570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000001254000003a746f706f6e2e73357067772e6e6f64652e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000"

        destination_realm_avp = DestinationRealmAVP("epc.mncXXX.mccYYY.3gppnetwork.org")
        destination_host_avp = DestinationHostAVP("topon.s5pgw.node.epc.mncXXX.mccYYY.3gppnetwork.org")

        avps = [destination_realm_avp, destination_host_avp]
        mip_home_agent_host_avp = MipHomeAgentHostAVP(avps)

        avps = [mip_home_agent_host_avp]
        avp = Mip6AgentInfoAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)


if __name__ == "__main__":
    unittest.main()