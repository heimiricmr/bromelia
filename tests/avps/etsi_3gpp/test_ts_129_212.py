# -*- coding: utf-8 -*-
"""
    tests.avps.etsi_3gpp.test_ts_129_212
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for ETSI TS 129 212.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(testing_dir))

sys.path.insert(0, base_dir)

from bromelia.avps.etsi_3gpp.ts_129_212 import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_priority_level_avp_stream(self):
        stream = bytes.fromhex("0000041680000010000028af00000008")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], PriorityLevelAVP))
        self.assertEqual(avps[0].code, PRIORITY_LEVEL_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "00000008")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1046 [Priority-Level] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_qos_class_identifier_avp_stream(self):
        stream = bytes.fromhex("0000040480000010000028af00000001")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], QosClassIdentifierAVP))
        self.assertEqual(avps[0].code, QOS_CLASS_IDENTIFIER_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, QCI_1)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1028 [Qos-Class-Identifier] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_pre_emption_capability_avp_stream(self):
        stream = bytes.fromhex("00000417c0000010000028af00000000")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], PreEmptionCapabilityAVP))
        self.assertEqual(avps[0].code, PRE_EMPTION_CAPABILITY_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, PRE_EMPTION_CAPABILITY_ENABLED)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1047 [Pre-Emption-Capability] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_pre_emption_vulnerability_avp_stream(self):
        stream = bytes.fromhex("00000418c0000010000028af00000000")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], PreEmptionVulnerabilityAVP))
        self.assertEqual(avps[0].code, PRE_EMPTION_VULNERABILITY_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, PRE_EMPTION_VULNERABILITY_ENABLED)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1048 [Pre-Emption-Vulnerability] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_rat_type_avp_stream(self):
        stream = bytes.fromhex("00000408c0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], RatTypeAVP))
        self.assertEqual(avps[0].code, RAT_TYPE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, RAT_TYPE_WLAN)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1032 [Rat-Type] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_ue_local_ip_address_avp_stream(self):
        stream = bytes.fromhex("00000af580000012000028af0001bd3f4b020000")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], UeLocalIpAddressAVP))
        self.assertEqual(avps[0].code, UE_LOCAL_IP_ADDRESS_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 18)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "0001bd3f4b02")
        self.assertEqual(avps[0].get_ip_address(), "189.63.75.2")
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 2805 [Ue-Local-Ip-Address] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_precedence_avp_stream(self):
        stream = bytes.fromhex("000003f2c0000010000028af00000400")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], PrecedenceAVP))
        self.assertEqual(avps[0].code, PRECEDENCE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("00000400"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1010 [Precedence] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_reporting_level_avp_stream(self):
        stream = bytes.fromhex("000003f3c0000010000028af00000002")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ReportingLevelAVP))
        self.assertEqual(avps[0].code, REPORTING_LEVEL_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, REPORTING_LEVEL_SPONSORED_CONNECTIVITY_LEVEL)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1011 [Reporting-Level] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_ip_can_type_avp_stream(self):
        stream = bytes.fromhex("00000403c0000010000028af00000009")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], IpCanTypeAVP))
        self.assertEqual(avps[0].code, IP_CAN_TYPE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, IP_CAN_TYPE_NON_3GPP_5GS)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1027 [Ip-Can-Type] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_an_gw_address_avp_stream(self):
        stream = bytes.fromhex("0000041a80000012000028af00010a81f1d60000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], AnGwAddressAVP))
        self.assertEqual(avps[0].code, AN_GW_ADDRESS_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 18)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("00010a81f1d6"))
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1050 [An-Gw-Address] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_charging_correlation_indicator_avp_stream(self):
        stream = bytes.fromhex("0000043180000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ChargingCorrelationIndicatorAVP))
        self.assertEqual(avps[0].code, CHARGING_CORRELATION_INDICATOR_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, CHARGING_CORRELATION_INDICATOR_CHARGING_IDENTIFIER_REQUIRED)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1073 [Charging-Correlation-Indicator] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_bearer_usage_avp_stream(self):
        stream = bytes.fromhex("000003e8c0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], BearerUsageAVP))
        self.assertEqual(avps[0].code, BEARER_USAGE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, BEARER_USAGE_GENERAL)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1000 [Bearer-Usage] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_charging_rule_install_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_charging_rule_definition_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_charging_rule_name_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_event_trigger_avp_stream(self):
        stream = bytes.fromhex("000003eec0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], EventTriggerAVP))
        self.assertEqual(avps[0].code, EVENT_TRIGGER_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, EVENT_TRIGGER_SGSN_CHANGE)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1006 [Event-Trigger] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_metering_method_avp_stream(self):
        stream = bytes.fromhex("000003efc0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], MeteringMethodAVP))
        self.assertEqual(avps[0].code, METERING_METHOD_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, METERING_METHOD_DURATION)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1007 [Metering-Method] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_offline_avp_stream(self):
        stream = bytes.fromhex("000003f0c0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], OfflineAVP))
        self.assertEqual(avps[0].code, OFFLINE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, OFFLINE_DISABLE_OFFLINE)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1008 [Offline] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_online_avp_stream(self):
        stream = bytes.fromhex("000003f1c0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], OnlineAVP))
        self.assertEqual(avps[0].code, ONLINE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, ONLINE_DISABLE_ONLINE)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1009 [Online] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_qos_information_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_charging_rule_report_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_pcc_rule_status_avp_stream(self):
        stream = bytes.fromhex("000003fbc0000010000028af00000001")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], PccRuleStatusAVP))
        self.assertEqual(avps[0].code, PCC_RULE_STATUS_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, PCC_RULE_STATUS_INACTIVE)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1019 [Pcc-Rule-Status] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_access_network_charging_identifier_gx_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_network_request_support_avp_stream(self):
        stream = bytes.fromhex("00000400c0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], NetworkRequestSupportAVP))
        self.assertEqual(avps[0].code, NETWORK_REQUEST_SUPPORT_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, NETWORK_REQUEST_NOT_SUPPORTED)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1024 [Network-Request-Support] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_guaranteed_bitrate_dl_avp_stream(self):
        stream = bytes.fromhex("00000401c0000010000028af00000100")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], GuaranteedBitrateDlAVP))
        self.assertEqual(avps[0].code, GUARANTEED_BITRATE_DL_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("00000100"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1025 [Guaranteed-Bitrate-Dl] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_guaranteed_bitrate_ul_avp_stream(self):
        stream = bytes.fromhex("00000402c0000010000028af00000008")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], GuaranteedBitrateUlAVP))
        self.assertEqual(avps[0].code, GUARANTEED_BITRATE_UL_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("00000008"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1026 [Guaranteed-Bitrate-Ul] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_rule_failure_code_avp_stream(self):
        stream = bytes.fromhex("00000407c0000010000028af00000001")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], RuleFailureCodeAVP))
        self.assertEqual(avps[0].code, RULE_FAILURE_CODE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, RULE_FAILURE_CODE_UNKNOWN_RULE_NAME)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1031 [Rule-Failure-Code] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_apn_aggregate_max_bitrate_dl_avp_stream(self):
        stream = bytes.fromhex("0000041080000010000028af00000008")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ApnAggregateMaxBitrateDlAVP))
        self.assertEqual(avps[0].code, APN_AGGREGATE_MAX_BITRATE_DL_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "00000008")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1040 [Apn-Aggregate-Max-Bitrate-Dl] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_apn_aggregate_max_bitrate_ul_avp_stream(self):
        stream = bytes.fromhex("0000041180000010000028af00000008")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ApnAggregateMaxBitrateUlAVP))
        self.assertEqual(avps[0].code, APN_AGGREGATE_MAX_BITRATE_UL_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "00000008")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1041 [Apn-Aggregate-Max-Bitrate-Ul] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_default_eps_bearer_qos_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_flow_information_avp_stream(self):
        pass


class TestPriorityLevelAVP(unittest.TestCase):
    def test_priority_level_avp__no_value(self):
        self.assertRaises(TypeError, PriorityLevelAVP)

    def test_priority_level_avp__repr_dunder(self):
        avp = PriorityLevelAVP(convert_to_4_bytes(8))
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1046 [Priority-Level] VENDOR>")

    def test_priority_level_avp__diameter_avp_convert_classmethod(self):
        avp = PriorityLevelAVP(convert_to_4_bytes(8))

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_priority_level_avp__8(self):
        value = convert_to_4_bytes(8)

        avp = PriorityLevelAVP(value)
        ref = "0000041680000010000028af00000008"
        self.assertEqual(avp.dump().hex(), ref)


class TestPreEmptionCapabilityAVP(unittest.TestCase):
    def test_pre_emption_capability_avp__no_value(self):
        self.assertRaises(TypeError, PreEmptionCapabilityAVP)

    def test_pre_emption_capability_avp__repr_dunder(self):
        avp = PreEmptionCapabilityAVP(PRE_EMPTION_CAPABILITY_ENABLED)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1047 [Pre-Emption-Capability] VENDOR, MANDATORY>")

    def test_pre_emption_capability_avp__diameter_avp_convert_classmethod(self):
        avp = PreEmptionCapabilityAVP(PRE_EMPTION_CAPABILITY_ENABLED)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_pre_emption_capability_avp__enabled(self):
        avp = PreEmptionCapabilityAVP(PRE_EMPTION_CAPABILITY_ENABLED)
        ref = "00000417c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_pre_emption_capability_avp__disabled(self):
        avp = PreEmptionCapabilityAVP(PRE_EMPTION_CAPABILITY_DISABLED)
        ref = "00000417c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestPreEmptionVulnerabilityAVP(unittest.TestCase):
    def test_pre_emption_vulnerability_avp__no_value(self):
        self.assertRaises(TypeError, PreEmptionVulnerabilityAVP)

    def test_pre_emption_vulnerability_avp__repr_dunder(self):
        avp = PreEmptionVulnerabilityAVP(PRE_EMPTION_VULNERABILITY_ENABLED)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1048 [Pre-Emption-Vulnerability] VENDOR, MANDATORY>")

    def test_pre_emption_vulnerability_avp__diameter_avp_convert_classmethod(self):
        avp = PreEmptionVulnerabilityAVP(PRE_EMPTION_VULNERABILITY_ENABLED)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_pre_emption_vulnerability_avp__enabled(self):
        avp = PreEmptionVulnerabilityAVP(PRE_EMPTION_VULNERABILITY_ENABLED)
        ref = "00000418c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_pre_emption_vulnerability_avp__disabled(self):
        avp = PreEmptionVulnerabilityAVP(PRE_EMPTION_VULNERABILITY_DISABLED)
        ref = "00000418c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestQosClassIdentifierAVP(unittest.TestCase):
    def test_qos_class_identifier_avp__no_value(self):
        self.assertRaises(TypeError, QosClassIdentifierAVP)

    def test_qos_class_identifier_avp__repr_dunder(self):
        avp = QosClassIdentifierAVP(QCI_1)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1028 [Qos-Class-Identifier] VENDOR>")

    def test_qos_class_identifier_avp__diameter_avp_convert_classmethod(self):
        avp = QosClassIdentifierAVP(QCI_1)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_qos_class_identifier_avp__qci1(self):
        avp = QosClassIdentifierAVP(QCI_1)
        ref = "0000040480000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci2(self):
        avp = QosClassIdentifierAVP(QCI_2)
        ref = "0000040480000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci3(self):
        avp = QosClassIdentifierAVP(QCI_3)
        ref = "0000040480000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci4(self):
        avp = QosClassIdentifierAVP(QCI_4)
        ref = "0000040480000010000028af00000004"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci5(self):
        avp = QosClassIdentifierAVP(QCI_5)
        ref = "0000040480000010000028af00000005"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci6(self):
        avp = QosClassIdentifierAVP(QCI_6)
        ref = "0000040480000010000028af00000006"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci7(self):
        avp = QosClassIdentifierAVP(QCI_7)
        ref = "0000040480000010000028af00000007"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci8(self):
        avp = QosClassIdentifierAVP(QCI_8)
        ref = "0000040480000010000028af00000008"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci9(self):
        avp = QosClassIdentifierAVP(QCI_9)
        ref = "0000040480000010000028af00000009"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci65(self):
        avp = QosClassIdentifierAVP(QCI_65)
        ref = "0000040480000010000028af00000041"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci66(self):
        avp = QosClassIdentifierAVP(QCI_66)
        ref = "0000040480000010000028af00000042"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci69(self):
        avp = QosClassIdentifierAVP(QCI_69)
        ref = "0000040480000010000028af00000045"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci70(self):
        avp = QosClassIdentifierAVP(QCI_70)
        ref = "0000040480000010000028af00000046"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci75(self):
        avp = QosClassIdentifierAVP(QCI_75)
        ref = "0000040480000010000028af0000004b"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci79(self):
        avp = QosClassIdentifierAVP(QCI_79)
        ref = "0000040480000010000028af0000004f"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci80(self):
        avp = QosClassIdentifierAVP(QCI_80)
        ref = "0000040480000010000028af00000050"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci82(self):
        avp = QosClassIdentifierAVP(QCI_82)
        ref = "0000040480000010000028af00000052"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci83(self):
        avp = QosClassIdentifierAVP(QCI_83)
        ref = "0000040480000010000028af00000053"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci84(self):
        avp = QosClassIdentifierAVP(QCI_84)
        ref = "0000040480000010000028af00000054"
        self.assertEqual(avp.dump().hex(), ref)

    def test_qos_class_identifier_avp__qci85(self):
        avp = QosClassIdentifierAVP(QCI_85)
        ref = "0000040480000010000028af00000055"
        self.assertEqual(avp.dump().hex(), ref)


class TestRatTypeAVP(unittest.TestCase):
    def test_rat_type_avp__no_value(self):
        self.assertRaises(TypeError, RatTypeAVP)

    def test_rat_type_avp__repr_dunder(self):
        avp = RatTypeAVP(RAT_TYPE_WLAN)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1032 [Rat-Type] VENDOR, MANDATORY>")

    def test_rat_type_avp__diameter_avp_convert_classmethod(self):
        avp = RatTypeAVP(RAT_TYPE_WLAN)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_rat_type_avp__wlan(self):
        avp = RatTypeAVP(RAT_TYPE_WLAN)
        ref = "00000408c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_rat_type_avp__virtual(self):
        avp = RatTypeAVP(RAT_TYPE_VIRTUAL)
        ref = "00000408c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_rat_type_avp__utran(self):
        avp = RatTypeAVP(RAT_TYPE_UTRAN)
        ref = "00000408c0000010000028af000003e8"
        self.assertEqual(avp.dump().hex(), ref)

    def test_rat_type_avp__geran(self):
        avp = RatTypeAVP(RAT_TYPE_GERAN)
        ref = "00000408c0000010000028af000003e9"
        self.assertEqual(avp.dump().hex(), ref)

    def test_rat_type_avp__gan(self):
        avp = RatTypeAVP(RAT_TYPE_GAN)
        ref = "00000408c0000010000028af000003ea"
        self.assertEqual(avp.dump().hex(), ref)

    def test_rat_type_avp__hspa_evolution(self):
        avp = RatTypeAVP(RAT_TYPE_HSPA_EVOLUTION)
        ref = "00000408c0000010000028af000003eb"
        self.assertEqual(avp.dump().hex(), ref)

    def test_rat_type_avp__eutran(self):
        avp = RatTypeAVP(RAT_TYPE_EUTRAN)
        ref = "00000408c0000010000028af000003ec"
        self.assertEqual(avp.dump().hex(), ref)

    def test_rat_type_avp__cdma2000_1x(self):
        avp = RatTypeAVP(RAT_TYPE_CDMA2000_1X)
        ref = "00000408c0000010000028af000007d0"
        self.assertEqual(avp.dump().hex(), ref)

    def test_rat_type_avp__hrpd(self):
        avp = RatTypeAVP(RAT_TYPE_HRPD)
        ref = "00000408c0000010000028af000007d1"
        self.assertEqual(avp.dump().hex(), ref)

    def test_rat_type_avp__umb(self):
        avp = RatTypeAVP(RAT_TYPE_UMB)
        ref = "00000408c0000010000028af000007d2"
        self.assertEqual(avp.dump().hex(), ref)

    def test_rat_type_avp__ehrpd(self):
        avp = RatTypeAVP(RAT_TYPE_EHRPD)
        ref = "00000408c0000010000028af000007d3"
        self.assertEqual(avp.dump().hex(), ref)


class TestUeLocalIpAddressAVP(unittest.TestCase):
    def test_ue_local_ip_address_avp__no_value(self):
        self.assertRaises(TypeError, UeLocalIpAddressAVP)

    def test_ue_local_ip_address_avp__repr_dunder(self):
        avp = UeLocalIpAddressAVP("127.0.0.1")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 2805 [Ue-Local-Ip-Address] VENDOR>")

    def test_ue_local_ip_address_avp__diameter_avp_convert_classmethod(self):
        avp = UeLocalIpAddressAVP("127.0.0.1")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_ue_local_ip_address_avp__1(self):
        avp = UeLocalIpAddressAVP("189.63.75.2")
        ref = "00000af580000012000028af0001bd3f4b020000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_ue_local_ip_address_avp__2(self):
        avp = UeLocalIpAddressAVP("191.189.14.239")
        ref = "00000af580000012000028af0001bfbd0eef0000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_ue_local_ip_address_avp__3(self):
        avp = UeLocalIpAddressAVP("187.122.124.174")
        ref = "00000af580000012000028af0001bb7a7cae0000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_ue_local_ip_address_avp__4(self):
        avp = UeLocalIpAddressAVP("187.64.214.67")
        ref = "00000af580000012000028af0001bb40d6430000"
        self.assertEqual(avp.dump().hex(), ref)


class TestPrecedenceAVPAVP(unittest.TestCase):
    def test__precedence_avp__no_value(self):
        self.assertRaises(TypeError, PrecedenceAVP)

    def test__precedence_avp__repr_dunder(self):
        avp = PrecedenceAVP(256)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1010 [Precedence] VENDOR, MANDATORY>")

    def test__precedence_avp__diameter_avp_convert_classmethod(self):
        avp = PrecedenceAVP(256)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__precedence_avp__1(self):
        avp = PrecedenceAVP(256)
        ref = "000003f2c0000010000028af00000100"
        self.assertEqual(avp.dump().hex(), ref)

    def test__precedence_avp__2(self):
        avp = PrecedenceAVP(1024)
        ref = "000003f2c0000010000028af00000400"
        self.assertEqual(avp.dump().hex(), ref)


class TestReportingLevelAVPAVP(unittest.TestCase):
    def test__reporting_level_avp__no_value(self):
        self.assertRaises(TypeError, ReportingLevelAVP)

    def test__reporting_level_avp__repr_dunder(self):
        avp = ReportingLevelAVP(REPORTING_LEVEL_SERVICE_IDENTIFIER_LEVEL)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1011 [Reporting-Level] VENDOR, MANDATORY>")

    def test__reporting_level_avp__diameter_avp_convert_classmethod(self):
        avp = ReportingLevelAVP(REPORTING_LEVEL_SERVICE_IDENTIFIER_LEVEL)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__reporting_level_avp__1(self):
        avp = ReportingLevelAVP(REPORTING_LEVEL_SERVICE_IDENTIFIER_LEVEL)
        ref = "000003f3c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reporting_level_avp__2(self):
        avp = ReportingLevelAVP(REPORTING_LEVEL_RATING_GROUP_LEVEL)
        ref = "000003f3c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reporting_level_avp__3(self):
        avp = ReportingLevelAVP(REPORTING_LEVEL_SPONSORED_CONNECTIVITY_LEVEL)
        ref = "000003f3c0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)


class TestIpCanTypeAVPAVP(unittest.TestCase):
    def test__ip_can_type_avp__no_value(self):
        self.assertRaises(TypeError, IpCanTypeAVP)

    def test__ip_can_type_avp__repr_dunder(self):
        avp = IpCanTypeAVP(IP_CAN_TYPE_3GPP_GPRS)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1027 [Ip-Can-Type] VENDOR, MANDATORY>")

    def test__ip_can_type_avp__diameter_avp_convert_classmethod(self):
        avp = IpCanTypeAVP(IP_CAN_TYPE_DOCSIS)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__ip_can_type_avp__1(self):
        avp = IpCanTypeAVP(IP_CAN_TYPE_3GPP_GPRS)
        ref = "00000403c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__ip_can_type_avp__2(self):
        avp = IpCanTypeAVP(IP_CAN_TYPE_DOCSIS)
        ref = "00000403c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__ip_can_type_avp__3(self):
        avp = IpCanTypeAVP(IP_CAN_TYPE_XDSL)
        ref = "00000403c0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test__ip_can_type_avp__4(self):
        avp = IpCanTypeAVP(IP_CAN_TYPE_WIMAX)
        ref = "00000403c0000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test__ip_can_type_avp__5(self):
        avp = IpCanTypeAVP(IP_CAN_TYPE_3GPP2)
        ref = "00000403c0000010000028af00000004"
        self.assertEqual(avp.dump().hex(), ref)

    def test__ip_can_type_avp__6(self):
        avp = IpCanTypeAVP(IP_CAN_TYPE_3GPP_EPS)
        ref = "00000403c0000010000028af00000005"
        self.assertEqual(avp.dump().hex(), ref)

    def test__ip_can_type_avp__7(self):
        avp = IpCanTypeAVP(IP_CAN_TYPE_NON_3GPP_EPS)
        ref = "00000403c0000010000028af00000006"
        self.assertEqual(avp.dump().hex(), ref)

    def test__ip_can_type_avp__8(self):
        avp = IpCanTypeAVP(IP_CAN_TYPE_FBA)
        ref = "00000403c0000010000028af00000007"
        self.assertEqual(avp.dump().hex(), ref)

    def test__ip_can_type_avp__9(self):
        avp = IpCanTypeAVP(IP_CAN_TYPE_3GPP_5GS)
        ref = "00000403c0000010000028af00000008"
        self.assertEqual(avp.dump().hex(), ref)

    def test__ip_can_type_avp__10(self):
        avp = IpCanTypeAVP(IP_CAN_TYPE_NON_3GPP_5GS)
        ref = "00000403c0000010000028af00000009"
        self.assertEqual(avp.dump().hex(), ref)


class TestAnGwAddressAVP(unittest.TestCase):
    def test__an_gw_address_avp__no_value(self):
        self.assertRaises(TypeError, AnGwAddressAVP)

    def test__an_gw_address_avp__repr_dunder(self):
        avp = AnGwAddressAVP("10.129.241.214")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1050 [An-Gw-Address] VENDOR>")

    def test__an_gw_address_avp__diameter_avp_convert_classmethod(self):
        avp = AnGwAddressAVP("10.129.241.214")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__an_gw_address_avp__1(self):
        avp = AnGwAddressAVP("10.129.241.214")
        ref = "0000041a80000012000028af00010a81f1d60000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__an_gw_address_avp__2(self):
        avp = AnGwAddressAVP("10.129.241.235")
        ref = "0000041a80000012000028af00010a81f1eb0000"
        self.assertEqual(avp.dump().hex(), ref)


class TestChargingCorrelationIndicatorAVP(unittest.TestCase):
    def test__charging_correlation_indicator_avp__no_value(self):
        self.assertRaises(TypeError, ChargingCorrelationIndicatorAVP)

    def test__charging_correlation_indicator_avp__repr_dunder(self):
        avp = ChargingCorrelationIndicatorAVP(CHARGING_CORRELATION_INDICATOR_CHARGING_IDENTIFIER_REQUIRED)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1073 [Charging-Correlation-Indicator] VENDOR>")

    def test__charging_correlation_indicator_avp__diameter_avp_convert_classmethod(self):
        avp = ChargingCorrelationIndicatorAVP(CHARGING_CORRELATION_INDICATOR_CHARGING_IDENTIFIER_REQUIRED)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__charging_correlation_indicator_avp__1(self):
        avp = ChargingCorrelationIndicatorAVP(CHARGING_CORRELATION_INDICATOR_CHARGING_IDENTIFIER_REQUIRED)
        ref = "0000043180000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)


class TestBearerUsageAVP(unittest.TestCase):
    def test__bearer_usage_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = BearerUsageAVP()
    
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test__bearer_usage_avp__repr_dunder(self):
        avp = BearerUsageAVP(BEARER_USAGE_GENERAL)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1000 [Bearer-Usage] VENDOR, MANDATORY>")

    def test__bearer_usage_avp__diameter_avp_convert_classmethod(self):
        avp = BearerUsageAVP(BEARER_USAGE_GENERAL)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__bearer_usage_avp__general(self):
        avp = BearerUsageAVP(BEARER_USAGE_GENERAL)
        ref = "000003e8c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__bearer_usage_avp__signalling(self):
        avp = BearerUsageAVP(BEARER_USAGE_SIGNALLING)
        ref = "000003e8c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestSupportedFeaturesAVP(unittest.TestCase):
    pass


class TestChargingRuleInstallAVP(unittest.TestCase):
    pass


class TestChargingRuleDefinitionAVP(unittest.TestCase):
    pass


class TestChargingRuleNameAVP(unittest.TestCase):
    pass


class TestEventTriggerAVP(unittest.TestCase):
    def test__event_trigger_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = EventTriggerAVP()
    
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test__event_trigger_avp__repr_dunder(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_SGSN_CHANGE)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1006 [Event-Trigger] VENDOR, MANDATORY>")

    def test__event_trigger_avp__diameter_avp_convert_classmethod(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_SGSN_CHANGE)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__event_trigger_avp__sgsn_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_SGSN_CHANGE)
        ref = "000003eec0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__qos_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_QOS_CHANGE)
        ref = "000003eec0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__rat_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_RAT_CHANGE)
        ref = "000003eec0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__tft_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_TFT_CHANGE)
        ref = "000003eec0000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__plmn_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_PLMN_CHANGE)
        ref = "000003eec0000010000028af00000004"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__plmn_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_LOSS_OF_BEARER)
        ref = "000003eec0000010000028af00000005"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__recovery_of_bearer(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_RECOVERY_OF_BEARER)
        ref = "000003eec0000010000028af00000006"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__ip_can_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_IP_CAN_CHANGE)
        ref = "000003eec0000010000028af00000007"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__exceeding_authorization(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_QOS_CHANGE_EXCEEDING_AUTHORIZATION)
        ref = "000003eec0000010000028af0000000b"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__rai_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_RAI_CHANGE)
        ref = "000003eec0000010000028af0000000c"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__user_location_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_USER_LOCATION_CHANGE)
        ref = "000003eec0000010000028af0000000d"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__no_event_triggers(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_NO_EVENT_TRIGGERS)
        ref = "000003eec0000010000028af0000000e"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__out_of_credit(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_OUT_OF_CREDIT)
        ref = "000003eec0000010000028af0000000f"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__reallocation_of_credit(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_REALLOCATION_OF_CREDIT)
        ref = "000003eec0000010000028af00000010"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__revalidation_timeout(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_REVALIDATION_TIMEOUT)
        ref = "000003eec0000010000028af00000011"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__ue_ip_address_allocate(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_UE_IP_ADDRESS_ALLOCATE)
        ref = "000003eec0000010000028af00000012"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__ue_ip_address_release(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_UE_IP_ADDRESS_RELEASE)
        ref = "000003eec0000010000028af00000013"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__default_eps_bearer_qos_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_DEFAULT_EPS_BEARER_QOS_CHANGE)
        ref = "000003eec0000010000028af00000014"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__an_gw_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_AN_GW_CHANGE)
        ref = "000003eec0000010000028af00000015"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__successful_resource_allocation(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_SUCCESSFUL_RESOURCE_ALLOCATION)
        ref = "000003eec0000010000028af00000016"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__resource_modification_request(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_RESOURCE_MODIFICATION_REQUEST)
        ref = "000003eec0000010000028af00000017"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__pgw_trace_control(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_PGW_TRACE_CONTROL)
        ref = "000003eec0000010000028af00000018"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__ue_time_zone_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_UE_TIME_ZONE_CHANGE)
        ref = "000003eec0000010000028af00000019"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__tai_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_TAI_CHANGE)
        ref = "000003eec0000010000028af0000001a"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__ecgi_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_ECGI_CHANGE)
        ref = "000003eec0000010000028af0000001b"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__charging_correlation_exchange(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_CHARGING_CORRELATION_EXCHANGE)
        ref = "000003eec0000010000028af0000001c"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__apn_ambr_modification_failure(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_APN_AMBR_MODIFICATION_FAILURE)
        ref = "000003eec0000010000028af0000001d"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__user_csg_information_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_USER_CSG_INFORMATION_CHANGE)
        ref = "000003eec0000010000028af0000001e"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__usage_report(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_USAGE_REPORT)
        ref = "000003eec0000010000028af00000021"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__default_eps_bearer_qos_modification_failure(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_DEFAULT_EPS_BEARER_QOS_MODIFICATION_FAILURE)
        ref = "000003eec0000010000028af00000022"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__user_csg_hybrid_subscribed_information_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_USER_CSG_HYBRID_SUBSCRIBED_INFORMATION_CHANGE)
        ref = "000003eec0000010000028af00000023"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__user_csg_hybrid_unsubscribed_information_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_USER_CSG_HYBRID_UNSUBSCRIBED_INFORMATION_CHANGE)
        ref = "000003eec0000010000028af00000024"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__routing_rule_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_ROUTING_RULE_CHANGE)
        ref = "000003eec0000010000028af00000025"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__application_start(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_APPLICATION_START)
        ref = "000003eec0000010000028af00000027"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__application_stop(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_APPLICATION_STOP)
        ref = "000003eec0000010000028af00000028"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__cs_to_ps_handover(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_CS_TO_PS_HANDOVER)
        ref = "000003eec0000010000028af0000002a"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__ue_local_ip_address_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_UE_LOCAL_IP_ADDRESS_CHANGE)
        ref = "000003eec0000010000028af0000002b"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__henb_local_ip_address_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_HENB_LOCAL_IP_ADDRESS_CHANGE)
        ref = "000003eec0000010000028af0000002c"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__access_network_info_report(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_ACCESS_NETWORK_INFO_REPORT)
        ref = "000003eec0000010000028af0000002d"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__credit_management_session_failure(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_CREDIT_MANAGEMENT_SESSION_FAILURE)
        ref = "000003eec0000010000028af0000002e"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__default_qos_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_DEFAULT_QOS_CHANGE)
        ref = "000003eec0000010000028af0000002f"
        self.assertEqual(avp.dump().hex(), ref)
 
    def test__event_trigger_avp__change_of_ue_presence_in_presence_reporting_area_report(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_CHANGE_OF_UE_PRESENCE_IN_PRESENCE_REPORTING_AREA_REPORT)
        ref = "000003eec0000010000028af00000030"
        self.assertEqual(avp.dump().hex(), ref)
 
    def test__event_trigger_avp__addition_of_access(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_ADDITION_OF_ACCESS)
        ref = "000003eec0000010000028af00000031"
        self.assertEqual(avp.dump().hex(), ref)
 
    def test__event_trigger_avp__removal_of_access(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_REMOVAL_OF_ACCESS)
        ref = "000003eec0000010000028af00000032"
        self.assertEqual(avp.dump().hex(), ref)
 
    def test__event_trigger_avp__unavailability_of_access(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_UNAVAILABILITY_OF_ACCESS)
        ref = "000003eec0000010000028af00000033"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__availability_of_access(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_AVAILABILITY_OF_ACCESS)
        ref = "000003eec0000010000028af00000034"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__resource_release(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_RESOURCE_RELEASE)
        ref = "000003eec0000010000028af00000035"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__enodeb_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_ENODEB_CHANGE)
        ref = "000003eec0000010000028af00000036"
        self.assertEqual(avp.dump().hex(), ref)

    def test__event_trigger_avp__3gpp_ps_data_off_change(self):
        avp = EventTriggerAVP(EVENT_TRIGGER_3GPP_PS_DATA_OFF_CHANGE)
        ref = "000003eec0000010000028af00000037"
        self.assertEqual(avp.dump().hex(), ref)


class TestMeteringMethodAVP(unittest.TestCase):
    def test__metering_method_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = MeteringMethodAVP()
    
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test__metering_method_avp__repr_dunder(self):
        avp = MeteringMethodAVP(METERING_METHOD_DURATION)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1007 [Metering-Method] VENDOR, MANDATORY>")

    def test__metering_method_avp__diameter_avp_convert_classmethod(self):
        avp = MeteringMethodAVP(METERING_METHOD_DURATION)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__metering_method_avp__duration(self):
        avp = MeteringMethodAVP(METERING_METHOD_DURATION)
        ref = "000003efc0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__metering_method_avp__volume(self):
        avp = MeteringMethodAVP(METERING_METHOD_VOLUME)
        ref = "000003efc0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__metering_method_avp__duration_volume(self):
        avp = MeteringMethodAVP(METERING_METHOD_DURATION_VOLUME)
        ref = "000003efc0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test__metering_method_avp__event(self):
        avp = MeteringMethodAVP(METERING_METHOD_EVENT)
        ref = "000003efc0000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)


class TestOfflineAVP(unittest.TestCase):
    def test__offline_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = OfflineAVP()
    
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test__offline_avp__repr_dunder(self):
        avp = OfflineAVP(OFFLINE_DISABLE_OFFLINE)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1008 [Offline] VENDOR, MANDATORY>")

    def test__offline_avp__diameter_avp_convert_classmethod(self):
        avp = OfflineAVP(OFFLINE_DISABLE_OFFLINE)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__offline_avp__disable_offline(self):
        avp = OfflineAVP(OFFLINE_DISABLE_OFFLINE)
        ref = "000003f0c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__offline_avp__enable_offline(self):
        avp = OfflineAVP(OFFLINE_ENABLE_OFFLINE)
        ref = "000003f0c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestOnlineAVP(unittest.TestCase):
    def test__online_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = OnlineAVP()
    
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test__online_avp__repr_dunder(self):
        avp = OnlineAVP(ONLINE_DISABLE_ONLINE)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1009 [Online] VENDOR, MANDATORY>")

    def test__online_avp__diameter_avp_convert_classmethod(self):
        avp = OnlineAVP(ONLINE_DISABLE_ONLINE)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__online_avp__disable_online(self):
        avp = OnlineAVP(ONLINE_DISABLE_ONLINE)
        ref = "000003f1c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__online_avp__enable_online(self):
        avp = OnlineAVP(ONLINE_ENABLE_ONLINE)
        ref = "000003f1c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestQosInformationAVP(unittest.TestCase):
    pass


class TestChargingRuleReportAVP(unittest.TestCase):
    pass


class TestPccRuleStatusAVP(unittest.TestCase):
    def test__pcc_rule_status_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = PccRuleStatusAVP()
    
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test__pcc_rule_status_avp__repr_dunder(self):
        avp = PccRuleStatusAVP(PCC_RULE_STATUS_ACTIVE)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1019 [Pcc-Rule-Status] VENDOR, MANDATORY>")

    def test__pcc_rule_status_avp__diameter_avp_convert_classmethod(self):
        avp = PccRuleStatusAVP(PCC_RULE_STATUS_ACTIVE)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__pcc_rule_status_avp__active(self):
        avp = PccRuleStatusAVP(PCC_RULE_STATUS_ACTIVE)
        ref = "000003fbc0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__pcc_rule_status_avp__inactive(self):
        avp = PccRuleStatusAVP(PCC_RULE_STATUS_INACTIVE)
        ref = "000003fbc0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__pcc_rule_status_avp__temporarily_inactive(self):
        avp = PccRuleStatusAVP(PCC_RULE_STATUS_TEMPORARILY_INACTIVE)
        ref = "000003fbc0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)                


class TestAccessNetworkChargingIdentifierGxAVP(unittest.TestCase):
    pass


class TestNetworkRequestSupportAVP(unittest.TestCase):
    def test__network_request_support_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = NetworkRequestSupportAVP()
    
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test__network_request_support_avp__repr_dunder(self):
        avp = NetworkRequestSupportAVP(NETWORK_REQUEST_NOT_SUPPORTED)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1024 [Network-Request-Support] VENDOR, MANDATORY>")

    def test__network_request_support_avp__diameter_avp_convert_classmethod(self):
        avp = NetworkRequestSupportAVP(NETWORK_REQUEST_NOT_SUPPORTED)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__network_request_support_avp__not_supported(self):
        avp = NetworkRequestSupportAVP(NETWORK_REQUEST_NOT_SUPPORTED)
        ref = "00000400c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__network_request_support_avp__supported(self):
        avp = NetworkRequestSupportAVP(NETWORK_REQUEST_SUPPORTED)
        ref = "00000400c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestGuaranteedBitrateDlAVP(unittest.TestCase):
    def test_guaranteed_bitrate_dl_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = GuaranteedBitrateDlAVP()
    
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")
        
    def test_guaranteed_bitrate_dl_avp__repr_dunder(self):
        avp = GuaranteedBitrateDlAVP(convert_to_4_bytes(8))
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1025 [Guaranteed-Bitrate-Dl] VENDOR, MANDATORY>")

    def test_guaranteed_bitrate_dl_avp__diameter_avp_convert_classmethod(self):
        avp = GuaranteedBitrateDlAVP(convert_to_4_bytes(8))

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_guaranteed_bitrate_dl_avp__8(self):
        avp = GuaranteedBitrateDlAVP(convert_to_4_bytes(8))
        ref = "00000401c0000010000028af00000008"
        self.assertEqual(avp.dump().hex(), ref)

    def test_guaranteed_bitrate_dl_avp__256(self):
        avp = GuaranteedBitrateDlAVP(convert_to_4_bytes(256))
        ref = "00000401c0000010000028af00000100"
        self.assertEqual(avp.dump().hex(), ref)


class TestGuaranteedBitrateUlAVP(unittest.TestCase):
    def test_guaranteed_bitrate_ul_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = GuaranteedBitrateUlAVP()
    
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")
        
    def test_guaranteed_bitrate_ul_avp__repr_dunder(self):
        avp = GuaranteedBitrateUlAVP(convert_to_4_bytes(8))
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1026 [Guaranteed-Bitrate-Ul] VENDOR, MANDATORY>")

    def test_guaranteed_bitrate_ul_avp__diameter_avp_convert_classmethod(self):
        avp = GuaranteedBitrateUlAVP(convert_to_4_bytes(8))

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_guaranteed_bitrate_ul_avp__8(self):
        avp = GuaranteedBitrateUlAVP(convert_to_4_bytes(8))
        ref = "00000402c0000010000028af00000008"
        self.assertEqual(avp.dump().hex(), ref)

    def test_guaranteed_bitrate_ul_avp__256(self):
        avp = GuaranteedBitrateUlAVP(convert_to_4_bytes(256))
        ref = "00000402c0000010000028af00000100"
        self.assertEqual(avp.dump().hex(), ref)


class TestRuleFailureCodeAVP(unittest.TestCase):
    def test__rule_failure_code_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = RuleFailureCodeAVP()
    
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")

    def test__rule_failure_code_avp__repr_dunder(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_UNKNOWN_RULE_NAME)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1031 [Rule-Failure-Code] VENDOR, MANDATORY>")

    def test__rule_failure_code_avp__diameter_avp_convert_classmethod(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_UNKNOWN_RULE_NAME)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__rule_failure_code_avp__unknown_rule_name(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_UNKNOWN_RULE_NAME)
        ref = "00000407c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__rating_group_error(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_RATING_GROUP_ERROR)
        ref = "00000407c0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__service_identifier_error(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_SERVICE_IDENTIFIER_ERROR)
        ref = "00000407c0000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__gw_pcef_malfunction(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_GW_PCEF_MALFUNCTION)
        ref = "00000407c0000010000028af00000004"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__resources_limitation(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_RESOURCES_LIMITATION)
        ref = "00000407c0000010000028af00000005"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__max_nr_bearers_reached(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_MAX_NR_BEARERS_REACHED)
        ref = "00000407c0000010000028af00000006"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__unknown_bearer_id(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_UNKNOWN_BEARER_ID)
        ref = "00000407c0000010000028af00000007"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__missing_bearer_id(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_MISSING_BEARER_ID)
        ref = "00000407c0000010000028af00000008"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__missing_flow_information(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_MISSING_FLOW_INFORMATION)
        ref = "00000407c0000010000028af00000009"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__resource_allocation_failure(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_RESOURCE_ALLOCATION_FAILURE)
        ref = "00000407c0000010000028af0000000a"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__unsuccessful_qos_validation(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_UNSUCCESSFUL_QOS_VALIDATION)
        ref = "00000407c0000010000028af0000000b"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__incorrect_flow_information(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_INCORRECT_FLOW_INFORMATION)
        ref = "00000407c0000010000028af0000000c"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__ps_to_cs_handover(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_PS_TO_CS_HANDOVER)
        ref = "00000407c0000010000028af0000000d"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__tdf_application_identifier_error(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_TDF_APPLICATION_IDENTIFIER_ERROR)
        ref = "00000407c0000010000028af0000000e"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__no_bearer_bound(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_NO_BEARER_BOUND)
        ref = "00000407c0000010000028af0000000f"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__filter_restrictions(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_FILTER_RESTRICTIONS)
        ref = "00000407c0000010000028af00000010"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__an_gw_failed(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_AN_GW_FAILED)
        ref = "00000407c0000010000028af00000011"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__missing_redirect_server_address(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_MISSING_REDIRECT_SERVER_ADDRESS)
        ref = "00000407c0000010000028af00000012"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__cm_end_user_service_denied(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_CM_END_USER_SERVICE_DENIED)
        ref = "00000407c0000010000028af00000013"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__cm_credit_control_not_applicable(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_CM_CREDIT_CONTROL_NOT_APPLICABLE)
        ref = "00000407c0000010000028af00000014"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__cm_authorization_rejected(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_CM_AUTHORIZATION_REJECTED)
        ref = "00000407c0000010000028af00000015"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__cm_user_unknown(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_CM_USER_UNKNOWN)
        ref = "00000407c0000010000028af00000016"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__cm_rating_failed(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_CM_RATING_FAILED)
        ref = "00000407c0000010000028af00000017"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__routing_rule_rejection(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_ROUTING_RULE_REJECTION)
        ref = "00000407c0000010000028af00000018"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__unknown_routing_access_information(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_UNKNOWN_ROUTING_ACCESS_INFORMATION)
        ref = "00000407c0000010000028af00000019"
        self.assertEqual(avp.dump().hex(), ref)

    def test__rule_failure_code_avp__no_nbifom_support(self):
        avp = RuleFailureCodeAVP(RULE_FAILURE_CODE_NO_NBIFOM_SUPPORT)
        ref = "00000407c0000010000028af0000001a"
        self.assertEqual(avp.dump().hex(), ref)


class TestApnAggregateMaxBitrateDlAVP(unittest.TestCase):
    def test_apn_aggregate_max_bitrate_dl_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = ApnAggregateMaxBitrateDlAVP()
    
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")
        
    def test_apn_aggregate_max_bitrate_dl_avp__repr_dunder(self):
        avp = ApnAggregateMaxBitrateDlAVP(convert_to_4_bytes(8))
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1040 [Apn-Aggregate-Max-Bitrate-Dl] VENDOR>")

    def test_apn_aggregate_max_bitrate_dl_avp__diameter_avp_convert_classmethod(self):
        avp = ApnAggregateMaxBitrateDlAVP(convert_to_4_bytes(8))

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_apn_aggregate_max_bitrate_dl_avp__8(self):
        avp = ApnAggregateMaxBitrateDlAVP(convert_to_4_bytes(8))
        ref = "0000041080000010000028af00000008"
        self.assertEqual(avp.dump().hex(), ref)

    def test_apn_aggregate_max_bitrate_dl_avp__256(self):
        avp = ApnAggregateMaxBitrateDlAVP(convert_to_4_bytes(256))
        ref = "0000041080000010000028af00000100"
        self.assertEqual(avp.dump().hex(), ref)


class TestApnAggregateMaxBitrateUlAVP(unittest.TestCase):
    def test_apn_aggregate_max_bitrate_ul_avp__no_value(self):
        with self.assertRaises(TypeError) as cm: 
            avp = ApnAggregateMaxBitrateUlAVP()
    
        self.assertEqual(cm.exception.args[0], "__init__() missing 1 required positional argument: 'data'")
        
    def test_apn_aggregate_max_bitrate_ul_avp__repr_dunder(self):
        avp = ApnAggregateMaxBitrateUlAVP(convert_to_4_bytes(8))
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1041 [Apn-Aggregate-Max-Bitrate-Ul] VENDOR>")

    def test_apn_aggregate_max_bitrate_ul_avp__diameter_avp_convert_classmethod(self):
        avp = ApnAggregateMaxBitrateUlAVP(convert_to_4_bytes(8))

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_apn_aggregate_max_bitrate_ul_avp__8(self):
        avp = ApnAggregateMaxBitrateUlAVP(convert_to_4_bytes(8))
        ref = "0000041180000010000028af00000008"
        self.assertEqual(avp.dump().hex(), ref)

    def test_apn_aggregate_max_bitrate_ul_avp__256(self):
        avp = ApnAggregateMaxBitrateUlAVP(convert_to_4_bytes(256))
        ref = "0000041180000010000028af00000100"
        self.assertEqual(avp.dump().hex(), ref)


class TestDefaultEpsBearerQosAVP(unittest.TestCase):
    pass


class TestFlowInformationAVP(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()