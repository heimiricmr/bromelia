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
        pass

    def test_diameter_avp__load_staticmethod__parsing_charging_rule_install_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_charging_rule_definition_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_charging_rule_name_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_event_trigger_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_metering_method_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_offline_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_online_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_qos_information_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_charging_rule_report_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_pcc_rule_status_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_access_network_charging_identifier_gx_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_network_request_support_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_guaranteed_bitrate_dl_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_guaranteed_bitrate_ul_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_rule_failure_code_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_apn_aggregate_max_bitrate_dl_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_apn_aggregate_max_bitrate_ul_avp_stream(self):
        pass

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
    pass


class TestSupportedFeaturesAVP(unittest.TestCase):
    pass


class TestChargingRuleInstallAVP(unittest.TestCase):
    pass


class TestChargingRuleDefinitionAVP(unittest.TestCase):
    pass


class TestChargingRuleNameAVP(unittest.TestCase):
    pass


class TestEventTriggerAVP(unittest.TestCase):
    pass


class TestMeteringMethodAVP(unittest.TestCase):
    pass


class TestOfflineAVP(unittest.TestCase):
    pass


class TestOnlineAVP(unittest.TestCase):
    pass


class TestQosInformationAVP(unittest.TestCase):
    pass


class TestChargingRuleReportAVP(unittest.TestCase):
    pass


class TestPccRuleStatusAVP(unittest.TestCase):
    pass


class TestAccessNetworkChargingIdentifierGxAVP(unittest.TestCase):
    pass


class TestNetworkRequestSupportAVP(unittest.TestCase):
    pass


class TestGuaranteedBitrateDlAVP(unittest.TestCase):
    pass


class TestGuaranteedBitrateUlAVP(unittest.TestCase):
    pass


class TestRuleFailureCodeAVP(unittest.TestCase):
    pass


class TestApnAggregateMaxBitrateDlAVP(unittest.TestCase):
    pass


class TestApnAggregateMaxBitrateUlAVP(unittest.TestCase):
    pass


class TestDefaultEpsBearerQosAVP(unittest.TestCase):
    pass


class TestFlowInformationAVP(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()