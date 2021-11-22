# -*- coding: utf-8 -*-
"""
    tests.avps.etsi_3gpp.test_ts_129_214
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for ETSI TS 129 214.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(testing_dir))

sys.path.insert(0, base_dir)

from bromelia.avps.etsi_3gpp.ts_129_214 import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_max_requested_bandwidth_dl_avp_stream(self):
        stream = bytes.fromhex("00000203c0000010000028af0003e800")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], MaxRequestedBandwidthDlAVP))
        self.assertEqual(avps[0].code, MAX_REQUESTED_BANDWIDTH_DL_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "0003e800")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 515 [Max-Requested-Bandwidth-Dl] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_max_requested_bandwidth_ul_avp_stream(self):
        stream = bytes.fromhex("00000204c0000010000028af0003e800")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], MaxRequestedBandwidthUlAVP))
        self.assertEqual(avps[0].code, MAX_REQUESTED_BANDWIDTH_UL_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "0003e800")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 516 [Max-Requested-Bandwidth-Ul] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_abort_cause_avp_stream(self):
        stream = bytes.fromhex("000001f4c0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], AbortCauseAVP))
        self.assertEqual(avps[0].code, ABORT_CAUSE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, ABORT_CAUSE_BEARER_RELEASED)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 500 [Abort-Cause] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_af_application_identifier_avp_stream(self):
        stream = bytes.fromhex("000001f8c0000018000028af494d53205365727669636573")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], AfApplicationIdentifierAVP))
        self.assertEqual(avps[0].code, AF_APPLICATION_IDENTIFIER_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 24)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, b"IMS Services")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 504 [Af-Application-Identifier] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_af_charging_identifier_avp_stream(self):
        stream = bytes.fromhex("000001f9c0000011000028af7265616c6d000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], AfChargingIdentifierAVP))
        self.assertEqual(avps[0].code, AF_CHARGING_IDENTIFIER_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 17)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, b"realm")
        self.assertEqual(avps[0].get_padding_length(), 3)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 505 [Af-Charging-Identifier] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_flow_description_avp_stream(self):
        stream = bytes.fromhex("000001fbc000004f000028af7065726d6974206f75742031372066726f6d20616e7920746f20323830343a3338383a363031303a3431323a62313a643835303a383238303a6261626520343931323000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], FlowDescriptionAVP))
        self.assertEqual(avps[0].code, FLOW_DESCRIPTION_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 79)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, b"permit out 17 from any to 2804:388:6010:412:b1:d850:8280:babe 49120")
        self.assertEqual(avps[0].get_padding_length(), 1)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 507 [Flow-Description] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_flow_number_avp_stream(self):
        stream = bytes.fromhex("000001fdc0000010000028af00000001")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], FlowNumberAVP))
        self.assertEqual(avps[0].code, FLOW_NUMBER_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("00000001"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 509 [Flow-Number] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_flow_status_avp_stream(self):
        stream = bytes.fromhex("000001ffc0000010000028af00000002")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], FlowStatusAVP))
        self.assertEqual(avps[0].code, FLOW_STATUS_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, FLOW_STATUS_ENABLED)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 511 [Flow-Status] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_flow_usage_avp_stream(self):
        stream = bytes.fromhex("00000200c0000010000028af00000001")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], FlowUsageAVP))
        self.assertEqual(avps[0].code, FLOW_USAGE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, FLOW_USAGE_RTCP)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 512 [Flow-Usage] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_specific_action_avp_stream(self):
        stream = bytes.fromhex("00000201c0000010000028af00000001")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], SpecificActionAVP))
        self.assertEqual(avps[0].code, SPECIFIC_ACTION_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, SPECIFIC_ACTION_CHARGING_CORRELATION_EXCHANGE)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 513 [Specific-Action] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_media_component_description_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_media_component_number_avp_stream(self):
        stream = bytes.fromhex("00000206c0000010000028af00000002")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], MediaComponentNumberAVP))
        self.assertEqual(avps[0].code, MEDIA_COMPONENT_NUMBER_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("00000002"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 518 [Media-Component-Number] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_media_sub_component_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_media_type_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_service_info_status_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_access_network_charging_address_avp_stream(self):
        stream = bytes.fromhex("000001f5c0000012000028af00010a81f1d60000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], AccessNetworkChargingAddressAVP))
        self.assertEqual(avps[0].code, ACCESS_NETWORK_CHARGING_ADDRESS_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 18)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("00010a81f1d6"))
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 501 [Access-Network-Charging-Address] VENDOR, MANDATORY>")
        self.assertTrue(avps[0].is_ipv4())

    def test_diameter_avp__load_staticmethod__parsing_access_network_charging_identifier_value_avp_stream(self):
        pass


class TestMaxRequestedBandwidthDlAVP(unittest.TestCase):
    def test_max_requested_bandwidth_dl_avp__no_value(self):
        self.assertRaises(TypeError, MaxRequestedBandwidthDlAVP)

    def test_max_requested_bandwidth_dl_avp__repr_dunder(self):
        MAX_DL = convert_to_4_bytes(256000)
        
        avp = MaxRequestedBandwidthDlAVP(MAX_DL)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 515 [Max-Requested-Bandwidth-Dl] VENDOR, MANDATORY>")

    def test_max_requested_bandwidth_dl_avp__diameter_avp_convert_classmethod(self):
        MAX_DL = convert_to_4_bytes(256000)
        
        avp = MaxRequestedBandwidthDlAVP(MAX_DL)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_max_requested_bandwidth_dl_avp__256kbps(self):
        MAX_DL = convert_to_4_bytes(256000)

        avp = MaxRequestedBandwidthDlAVP(MAX_DL)
        ref = "00000203c0000010000028af0003e800"
        self.assertEqual(avp.dump().hex(), ref)

    def test_max_requested_bandwidth_dl_avp__999Mbps(self):
        MAX_DL = convert_to_4_bytes(999000000)

        avp = MaxRequestedBandwidthDlAVP(MAX_DL)
        ref = "00000203c0000010000028af3b8b87c0"
        self.assertEqual(avp.dump().hex(), ref)


class TestMaxRequestedBandwidthUlAVP(unittest.TestCase):
    def test_max_requested_bandwidth_ul_avp__no_value(self):
        self.assertRaises(TypeError, MaxRequestedBandwidthUlAVP)

    def test_max_requested_bandwidth_ul_avp__repr_dunder(self):
        MAX_UL = convert_to_4_bytes(256000)
        
        avp = MaxRequestedBandwidthUlAVP(MAX_UL)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 516 [Max-Requested-Bandwidth-Ul] VENDOR, MANDATORY>")

    def test_max_requested_bandwidth_ul_avp__diameter_avp_convert_classmethod(self):
        MAX_UL = convert_to_4_bytes(256000)
        
        avp = MaxRequestedBandwidthUlAVP(MAX_UL)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_max_requested_bandwidth_ul_avp__256kbps(self):
        MAX_UL = convert_to_4_bytes(256000)

        avp = MaxRequestedBandwidthUlAVP(MAX_UL)
        ref = "00000204c0000010000028af0003e800"
        self.assertEqual(avp.dump().hex(), ref)

    def test_max_requested_bandwidth_ul_avp__999Mbps(self):
        MAX_UL = convert_to_4_bytes(999000000)

        avp = MaxRequestedBandwidthUlAVP(MAX_UL)
        ref = "00000204c0000010000028af3b8b87c0"
        self.assertEqual(avp.dump().hex(), ref)


class TestAbortCauseAVP(unittest.TestCase):
    def test__abort_cause_avp__no_value(self):
        self.assertRaises(TypeError, AbortCauseAVP)

    def test__abort_cause_avp__repr_dunder(self):
        avp = AbortCauseAVP(ABORT_CAUSE_BEARER_RELEASED)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 500 [Abort-Cause] VENDOR, MANDATORY>")

    def test__abort_cause_avp__diameter_avp_convert_classmethod(self):
        avp = AbortCauseAVP(ABORT_CAUSE_BEARER_RELEASED)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__abort_cause_avp__1(self):
        avp = AbortCauseAVP(ABORT_CAUSE_BEARER_RELEASED)
        ref = "000001f4c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__abort_cause_avp__2(self):
        avp = AbortCauseAVP(ABORT_CAUSE_INSUFFICIENT_SERVER_RESOURCES)
        ref = "000001f4c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__abort_cause_avp__3(self):
        avp = AbortCauseAVP(ABORT_CAUSE_INSUFFICIENT_BEARER_RESOURCES)
        ref = "000001f4c0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test__abort_cause_avp__4(self):
        avp = AbortCauseAVP(ABORT_CAUSE_PS_TO_CS_HANDOVER)
        ref = "000001f4c0000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test__abort_cause_avp__5(self):
        avp = AbortCauseAVP(ABORT_CAUSE_SPONSORED_DATA_CONNECTIVITY_DISALLOWED)
        ref = "000001f4c0000010000028af00000004"
        self.assertEqual(avp.dump().hex(), ref)


class TestAfApplicationIdentifierAVP(unittest.TestCase):
    def test__af_application_identifier_avp__no_value(self):
        self.assertRaises(TypeError, AfApplicationIdentifierAVP)

    def test__af_application_identifier_avp__repr_dunder(self):
        avp = AfApplicationIdentifierAVP("IMS Services")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 504 [Af-Application-Identifier] VENDOR, MANDATORY>")

    def test__af_application_identifier_avp__diameter_avp_convert_classmethod(self):
        avp = AfApplicationIdentifierAVP("IMS Services")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__af_application_identifier_avp__1(self):
        avp = AfApplicationIdentifierAVP("IMS Services")
        ref = "000001f8c0000018000028af494d53205365727669636573"
        self.assertEqual(avp.dump().hex(), ref)


class TestAfChargingIdentifierAVP(unittest.TestCase):
    def test__af_charging_identifier_avp__no_value(self):
        self.assertRaises(TypeError, AfChargingIdentifierAVP)

    def test__af_charging_identifier_avp__repr_dunder(self):
        avp = AfChargingIdentifierAVP("realm")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 505 [Af-Charging-Identifier] VENDOR, MANDATORY>")

    def test__af_charging_identifier_avp__diameter_avp_convert_classmethod(self):
        avp = AfChargingIdentifierAVP("realm")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__af_charging_identifier_avp__1(self):
        avp = AfChargingIdentifierAVP("realm")
        ref = "000001f9c0000011000028af7265616c6d000000"
        self.assertEqual(avp.dump().hex(), ref)


class TestFlowDescriptionAVP(unittest.TestCase):
    def test__flow_description_avp__no_value(self):
        self.assertRaises(TypeError, FlowDescriptionAVP)

    def test__flow_description_avp__repr_dunder(self):
        avp = FlowDescriptionAVP("permit out 17 from any to 2804:388:6010:412:b1:d850:8280:babe 49120")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 507 [Flow-Description] VENDOR, MANDATORY>")

    def test__flow_description_avp__diameter_avp_convert_classmethod(self):
        avp = FlowDescriptionAVP("permit out 17 from any to 2804:388:6010:412:b1:d850:8280:babe 49120")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__flow_description_avp__1(self):
        avp = FlowDescriptionAVP("permit out 17 from any to 2804:388:6010:412:b1:d850:8280:babe 49120")
        ref = "000001fbc000004f000028af7065726d6974206f75742031372066726f6d20616e7920746f20323830343a3338383a363031303a3431323a62313a643835303a383238303a6261626520343931323000"
        self.assertEqual(avp.dump().hex(), ref)


class TestFlowNumberAVP(unittest.TestCase):
    def test__flow_number_avp__no_value(self):
        self.assertRaises(TypeError, FlowNumberAVP)

    def test__flow_number_avp__repr_dunder(self):
        avp = FlowNumberAVP(1)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 509 [Flow-Number] VENDOR, MANDATORY>")

    def test__flow_number_avp__diameter_avp_convert_classmethod(self):
        avp = FlowNumberAVP(1)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__flow_number_avp__1(self):
        avp = FlowNumberAVP(1)
        ref = "000001fdc0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestFlowStatusAVP(unittest.TestCase):
    def test__flow_status_avp__no_value(self):
        self.assertRaises(TypeError, FlowStatusAVP)

    def test__flow_status_avp__repr_dunder(self):
        avp = FlowStatusAVP(FLOW_STATUS_ENABLED_UPLINK)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 511 [Flow-Status] VENDOR, MANDATORY>")

    def test__flow_status_avp__diameter_avp_convert_classmethod(self):
        avp = FlowStatusAVP(FLOW_STATUS_ENABLED_UPLINK)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__flow_status_avp__1(self):
        avp = FlowStatusAVP(FLOW_STATUS_ENABLED_UPLINK)
        ref = "000001ffc0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__flow_status_avp__2(self):
        avp = FlowStatusAVP(FLOW_STATUS_ENABLED_DOWNLINK)
        ref = "000001ffc0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__flow_status_avp__3(self):
        avp = FlowStatusAVP(FLOW_STATUS_ENABLED)
        ref = "000001ffc0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test__flow_status_avp__4(self):
        avp = FlowStatusAVP(FLOW_STATUS_DISABLED)
        ref = "000001ffc0000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test__flow_status_avp__5(self):
        avp = FlowStatusAVP(FLOW_STATUS_REMOVED)
        ref = "000001ffc0000010000028af00000004"
        self.assertEqual(avp.dump().hex(), ref)


class TestFlowUsageAVP(unittest.TestCase):
    def test__flow_usage_avp__no_value(self):
        self.assertRaises(TypeError, FlowUsageAVP)

    def test__flow_usage_avp__repr_dunder(self):
        avp = FlowUsageAVP(FLOW_USAGE_NO_INFORMATION)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 512 [Flow-Usage] VENDOR, MANDATORY>")

    def test__flow_usage_avp__diameter_avp_convert_classmethod(self):
        avp = FlowUsageAVP(FLOW_USAGE_NO_INFORMATION)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__flow_usage_avp__1(self):
        avp = FlowUsageAVP(FLOW_USAGE_NO_INFORMATION)
        ref = "00000200c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__flow_usage_avp__2(self):
        avp = FlowUsageAVP(FLOW_USAGE_RTCP)
        ref = "00000200c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__flow_usage_avp__3(self):
        avp = FlowUsageAVP(FLOW_USAGE_AF_SIGNALLING)
        ref = "00000200c0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)


class TestSpecificActionAVP(unittest.TestCase):
    def test__specific_action_avp__no_value(self):
        self.assertRaises(TypeError, SpecificActionAVP)

    def test__specific_action_avp__repr_dunder(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_CHARGING_CORRELATION_EXCHANGE)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 513 [Specific-Action] VENDOR, MANDATORY>")

    def test__specific_action_avp__diameter_avp_convert_classmethod(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_CHARGING_CORRELATION_EXCHANGE)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__specific_action_avp__1(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_CHARGING_CORRELATION_EXCHANGE)
        ref = "00000201c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__specific_action_avp__2(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_INDICATION_OF_LOSS_OF_BEARER)
        ref = "00000201c0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test__specific_action_avp__3(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_INDICATION_OF_RECOVERY_OF_BEARER)
        ref = "00000201c0000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test__specific_action_avp__4(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_INDICATION_OF_RELEASE_OF_BEARER)
        ref = "00000201c0000010000028af00000004"
        self.assertEqual(avp.dump().hex(), ref)

    def test__specific_action_avp__5(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_IP_CAN_CHANGE)
        ref = "00000201c0000010000028af00000006"
        self.assertEqual(avp.dump().hex(), ref)

    def test__specific_action_avp__6(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_INDICATION_OF_OUT_OF_CREDIT)
        ref = "00000201c0000010000028af00000007"
        self.assertEqual(avp.dump().hex(), ref)

    def test__specific_action_avp__7(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_INDICATION_OF_SUCCESSFUL_RESOURCES_ALLOCATION)
        ref = "00000201c0000010000028af00000008"
        self.assertEqual(avp.dump().hex(), ref)

    def test__specific_action_avp__8(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_INDICATION_OF_FAILED_RESOURCES_ALLOCATION)
        ref = "00000201c0000010000028af00000009"
        self.assertEqual(avp.dump().hex(), ref)

    def test__specific_action_avp__9(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_INDICATION_OF_LIMITED_PCC_DEPLOYMENT)
        ref = "00000201c0000010000028af0000000a"
        self.assertEqual(avp.dump().hex(), ref)

    def test__specific_action_avp__10(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_USAGE_REPORT)
        ref = "00000201c0000010000028af0000000b"
        self.assertEqual(avp.dump().hex(), ref)

    def test__specific_action_avp__11(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_ACCESS_NETWORK_INFO_REPORT)
        ref = "00000201c0000010000028af0000000c"
        self.assertEqual(avp.dump().hex(), ref)

    def test__specific_action_avp__12(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_INDICATION_OF_RECOVERY_FROM_LIMITED_PCC_DEPLOYMENT)
        ref = "00000201c0000010000028af0000000d"
        self.assertEqual(avp.dump().hex(), ref)

    def test__specific_action_avp__13(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_INDICATION_OF_ACCESS_NETWORK_INFO_REPORTING_FAILURE)
        ref = "00000201c0000010000028af0000000e"
        self.assertEqual(avp.dump().hex(), ref)

    def test__specific_action_avp__14(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_INDICATION_OF_TRANSFER_POLICY_EXPIRED)
        ref = "00000201c0000010000028af0000000f"
        self.assertEqual(avp.dump().hex(), ref)

    def test__specific_action_avp__15(self):
        avp = SpecificActionAVP(SPECIFIC_ACTION_PLMN_CHANGE)
        ref = "00000201c0000010000028af00000010"
        self.assertEqual(avp.dump().hex(), ref)


class TestMediaComponentDescriptionAVP(unittest.TestCase):
    pass


class TestMediaComponentNumberAVP(unittest.TestCase):
    def test__media_component_number_avp__no_value(self):
        self.assertRaises(TypeError, MediaComponentNumberAVP)

    def test__media_component_number_avp__repr_dunder(self):
        avp = MediaComponentNumberAVP(1)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 518 [Media-Component-Number] VENDOR, MANDATORY>")

    def test__media_component_number_avp__diameter_avp_convert_classmethod(self):
        avp = MediaComponentNumberAVP(1)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__media_component_number_avp__1(self):
        avp = MediaComponentNumberAVP(1)
        ref = "00000206c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__media_component_number_avp__2(self):
        avp = MediaComponentNumberAVP(2)
        ref = "00000206c0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)


class TestMediaSubComponentAVP(unittest.TestCase):
    pass


class TestMediaTypeAVPAVP(unittest.TestCase):
    def test__media_type_avp__no_value(self):
        self.assertRaises(TypeError, MediaTypeAVP)

    def test__media_type_avp__repr_dunder(self):
        avp = MediaTypeAVP(MEDIA_TYPE_VIDEO)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 520 [Media-Type] VENDOR, MANDATORY>")

    def test__media_type_avp__diameter_avp_convert_classmethod(self):
        avp = MediaTypeAVP(MEDIA_TYPE_VIDEO)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__media_type_avp__1(self):
        avp = MediaTypeAVP(MEDIA_TYPE_AUDIO)
        ref = "00000208c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__media_type_avp__2(self):
        avp = MediaTypeAVP(MEDIA_TYPE_VIDEO)
        ref = "00000208c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__media_type_avp__3(self):
        avp = MediaTypeAVP(MEDIA_TYPE_DATA)
        ref = "00000208c0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test__media_type_avp__4(self):
        avp = MediaTypeAVP(MEDIA_TYPE_APPLICATION)
        ref = "00000208c0000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test__media_type_avp__5(self):
        avp = MediaTypeAVP(MEDIA_TYPE_CONTROL)
        ref = "00000208c0000010000028af00000004"
        self.assertEqual(avp.dump().hex(), ref)

    def test__media_type_avp__6(self):
        avp = MediaTypeAVP(MEDIA_TYPE_TEXT)
        ref = "00000208c0000010000028af00000005"
        self.assertEqual(avp.dump().hex(), ref)

    def test__media_type_avp__7(self):
        avp = MediaTypeAVP(MEDIA_TYPE_MESSAGE)
        ref = "00000208c0000010000028af00000006"
        self.assertEqual(avp.dump().hex(), ref)

    def test__media_type_avp__8(self):
        avp = MediaTypeAVP(MEDIA_TYPE_OTHER)
        ref = "00000208c0000010000028af00000007"
        self.assertEqual(avp.dump().hex(), ref)


class TestServiceInfoStatusAVPAVP(unittest.TestCase):
    def test__service_info_status__no_value(self):
        self.assertRaises(TypeError, ServiceInfoStatusAVP)

    def test__service_info_status__repr_dunder(self):
        avp = ServiceInfoStatusAVP(SERVICE_INFO_STATUS_FINAL_SERVICE_INFORMATION)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 527 [Service-Info-Status] VENDOR, MANDATORY>")

    def test__service_info_status__diameter_avp_convert_classmethod(self):
        avp = ServiceInfoStatusAVP(SERVICE_INFO_STATUS_FINAL_SERVICE_INFORMATION)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__service_info_status__1(self):
        avp = ServiceInfoStatusAVP(SERVICE_INFO_STATUS_FINAL_SERVICE_INFORMATION)
        ref = "0000020fc0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__service_info_status__2(self):
        avp = ServiceInfoStatusAVP(SERVICE_INFO_STATUS_PRELIMINARY_SERVICE_INFORMATION)
        ref = "0000020fc0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestAccessNetworkChargingAddressAVP(unittest.TestCase):
    def test__access_network_charging_address_avp__no_value(self):
        self.assertRaises(TypeError, AccessNetworkChargingAddressAVP)

    def test__access_network_charging_address_avp__repr_dunder(self):
        avp = AccessNetworkChargingAddressAVP(7200)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 501 [Access-Network-Charging-Address] VENDOR, MANDATORY>")

    def test__access_network_charging_address_avp__diameter_avp_convert_classmethod(self):
        avp = AccessNetworkChargingAddressAVP("10.129.241.214")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__access_network_charging_address_avp__1(self):
        avp = AccessNetworkChargingAddressAVP("10.129.241.214")
        ref = "000001f5c0000012000028af00010a81f1d60000"
        self.assertEqual(avp.dump().hex(), ref)


class TestAccessNetworkChargingIdentifierValueAVP(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()