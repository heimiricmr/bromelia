# -*- coding: utf-8 -*-
"""
    test.etsi_3gpp_s6a_6d.test_avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP unittests 
	for 3GPP S6a/S6d Diameter Application Id.
    
    :copyright: (c) 2020 Henrique Marques Ribeiro.
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

from bromelia.etsi_3gpp_s6a_s6d.avps import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_supported_features_avp_stream(self):
        stream = bytes.fromhex("0000027480000038000028af0000010a4000000c000028af0000027580000010000028af000000010000027680000010000028afdc000201")
        avps = DiameterAVP.load(stream)

        supported_features_avp = avps[0]
        self.assertTrue(isinstance(supported_features_avp, SupportedFeaturesAVP))
        self.assertEqual(supported_features_avp.code, SUPPORTED_FEATURES_AVP_CODE)
        self.assertTrue(supported_features_avp.is_vendor_id())
        self.assertFalse(supported_features_avp.is_mandatory())
        self.assertFalse(supported_features_avp.is_protected())
        self.assertEqual(supported_features_avp.get_length(), 56)
        self.assertEqual(supported_features_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(supported_features_avp.data.hex(), "0000010a4000000c000028af0000027580000010000028af000000010000027680000010000028afdc000201")
        self.assertEqual(supported_features_avp.__repr__(), "<Diameter AVP: 628 [Supported-Features] VENDOR>")

        vendor_id_avp = supported_features_avp.avps[0]
        feature_list_id_avp = supported_features_avp.avps[1]
        feature_list_avp = supported_features_avp.avps[2]

        self.assertTrue(isinstance(vendor_id_avp, VendorIdAVP))
        self.assertEqual(vendor_id_avp.code, VENDOR_ID_AVP_CODE)
        self.assertFalse(vendor_id_avp.is_vendor_id())
        self.assertTrue(vendor_id_avp.is_mandatory())
        self.assertFalse(vendor_id_avp.is_protected())
        self.assertEqual(vendor_id_avp.get_length(), 12)
        self.assertIsNone(vendor_id_avp.vendor_id)
        self.assertEqual(vendor_id_avp.data.hex(), "000028af")
        self.assertEqual(vendor_id_avp.__repr__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")

        self.assertTrue(isinstance(feature_list_id_avp, FeatureListIdAVP))
        self.assertEqual(feature_list_id_avp.code, FEATURE_LIST_ID_AVP_CODE)
        self.assertTrue(feature_list_id_avp.is_vendor_id())
        self.assertFalse(feature_list_id_avp.is_mandatory())
        self.assertFalse(feature_list_id_avp.is_protected())
        self.assertEqual(feature_list_id_avp.get_length(), 16)
        self.assertEqual(feature_list_id_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(feature_list_id_avp.data.hex(), "00000001")
        self.assertEqual(feature_list_id_avp.__repr__(), "<Diameter AVP: 629 [Feature-List-Id] VENDOR>")

        self.assertTrue(isinstance(feature_list_avp, FeatureListAVP))
        self.assertEqual(feature_list_avp.code, FEATURE_LIST_AVP_CODE)
        self.assertTrue(feature_list_avp.is_vendor_id())
        self.assertFalse(feature_list_avp.is_mandatory())
        self.assertFalse(feature_list_avp.is_protected())
        self.assertEqual(feature_list_avp.get_length(), 16)
        self.assertEqual(feature_list_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(feature_list_avp.data.hex(), "dc000201")
        self.assertEqual(feature_list_avp.__repr__(), "<Diameter AVP: 630 [Feature-List] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_feature_list_id_avp_stream(self):
        stream = bytes.fromhex("0000027580000010000028af00000001")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], FeatureListIdAVP))
        self.assertEqual(avps[0].code, FEATURE_LIST_ID_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, FEATURE_LIST_ID_1)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 629 [Feature-List-Id] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_feature_list_avp_stream(self):
        stream = bytes.fromhex("0000027680000010000028afdc000201")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], FeatureListAVP))
        self.assertEqual(avps[0].code, FEATURE_LIST_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("dc000201"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 630 [Feature-List] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_terminal_information_avp_stream(self):
        stream = bytes.fromhex("00000579c0000038000028af0000057ac000001a000028af333533353835313130303334313700000000057bc000000e000028af30350000")
        avps = DiameterAVP.load(stream)

        terminal_information_avp = avps[0]
        self.assertTrue(isinstance(terminal_information_avp, TerminalInformationAVP))
        self.assertEqual(terminal_information_avp.code, TERMINAL_INFORMATION_AVP_CODE)
        self.assertTrue(terminal_information_avp.is_vendor_id())
        self.assertTrue(terminal_information_avp.is_mandatory())
        self.assertFalse(terminal_information_avp.is_protected())
        self.assertEqual(terminal_information_avp.get_length(), 56)
        self.assertEqual(terminal_information_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(terminal_information_avp.data.hex(), "0000057ac000001a000028af333533353835313130303334313700000000057bc000000e000028af30350000")
        self.assertEqual(terminal_information_avp.__repr__(), "<Diameter AVP: 1401 [Terminal-Information] VENDOR, MANDATORY>")

        imei_avp = terminal_information_avp.avps[0]
        software_version_avp = terminal_information_avp.avps[1]

        self.assertTrue(isinstance(imei_avp, ImeiAVP))
        self.assertEqual(imei_avp.code, IMEI_AVP_CODE)
        self.assertTrue(imei_avp.is_vendor_id())
        self.assertTrue(imei_avp.is_mandatory())
        self.assertFalse(imei_avp.is_protected())
        self.assertEqual(imei_avp.get_length(), 26)
        self.assertEqual(imei_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(imei_avp.data.hex(), "3335333538353131303033343137")
        self.assertEqual(imei_avp.__repr__(), "<Diameter AVP: 1402 [Imei] VENDOR, MANDATORY>")

        self.assertTrue(isinstance(software_version_avp, SoftwareVersionAVP))
        self.assertEqual(software_version_avp.code, SOFTWARE_VERSION_AVP_CODE)
        self.assertTrue(software_version_avp.is_vendor_id())
        self.assertTrue(software_version_avp.is_mandatory())
        self.assertFalse(software_version_avp.is_protected())
        self.assertEqual(software_version_avp.get_length(), 14)
        self.assertEqual(software_version_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(software_version_avp.data.hex(), "3035")
        self.assertEqual(software_version_avp.__repr__(), "<Diameter AVP: 1403 [Software-Version] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_operator_determined_barring_avp_stream(self):
        stream = bytes.fromhex("00000591c0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], OperatorDeterminedBarringAVP))
        self.assertEqual(avps[0].code, OPERATOR_DETERMINED_BARRING_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("00000000"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1425 [Operator-Determined-Barring] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_imei_avp_stream(self):
        stream = bytes.fromhex("0000057ac000001a000028af33353335383531313030333431370000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ImeiAVP))
        self.assertEqual(avps[0].code, IMEI_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 26)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, b"35358511003417")
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1402 [Imei] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_software_version_avp_stream(self):
        stream = bytes.fromhex("0000057bc000000e000028af30350000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], SoftwareVersionAVP))
        self.assertEqual(avps[0].code, SOFTWARE_VERSION_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 14)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, b"05")
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1403 [Software-Version] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_ulr_flags_avp_stream(self):
        stream = bytes.fromhex("0000057dc0000010000028af00000003")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], UlrFlagsAVP))
        self.assertEqual(avps[0].code, ULR_FLAGS_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("00000003"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1405 [Ulr-Flags] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_visited_plmn_id_avp_stream(self):
        stream = bytes.fromhex("0000057fc000000f000028af27f45000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], VisitedPlmnIdAVP))
        self.assertEqual(avps[0].code, VISITED_PLMN_ID_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 15)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("27f450"))
        self.assertEqual(avps[0].get_padding_length(), 1)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1407 [Visited-Plmn-Id] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_ue_srvcc_capability_avp_stream(self):
        stream = bytes.fromhex("0000064f80000010000028af00000001")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], UeSrvccCapabilityAVP))
        self.assertEqual(avps[0].code, UE_SRVCC_CAPABILITY_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, UE_SRVCC_SUPPORTED)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1615 [Ue-Srvcc-Capability] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_supported_services_avp_stream(self):
        stream = bytes.fromhex("00000c4780000020000028af00000c4880000014000028af000000000000001a")
        avps = DiameterAVP.load(stream)

        supported_services_avp = avps[0]
        self.assertTrue(isinstance(supported_services_avp, SupportedServicesAVP))
        self.assertEqual(supported_services_avp.code, SUPPORTED_SERVICES_AVP_CODE)
        self.assertTrue(supported_services_avp.is_vendor_id())
        self.assertFalse(supported_services_avp.is_mandatory())
        self.assertFalse(supported_services_avp.is_protected())
        self.assertEqual(supported_services_avp.get_length(), 32)
        self.assertEqual(supported_services_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(supported_services_avp.data.hex(), "00000c4880000014000028af000000000000001a")
        self.assertEqual(supported_services_avp.__repr__(), "<Diameter AVP: 3143 [Supported-Services] VENDOR>")

        supported_monitoring_events_avp = supported_services_avp.avps[0]

        self.assertTrue(isinstance(supported_monitoring_events_avp, SupportedMonitoringEventsAVP))
        self.assertEqual(supported_monitoring_events_avp.code, SUPPORTED_MONITORING_EVENTS_AVP_CODE)
        self.assertTrue(supported_monitoring_events_avp.is_vendor_id())
        self.assertFalse(supported_monitoring_events_avp.is_mandatory())
        self.assertFalse(supported_monitoring_events_avp.is_protected())
        self.assertEqual(supported_monitoring_events_avp.get_length(), 20)
        self.assertEqual(supported_monitoring_events_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(supported_monitoring_events_avp.data.hex(), "000000000000001a")
        self.assertEqual(supported_monitoring_events_avp.__repr__(), "<Diameter AVP: 3144 [Supported-Monitoring-Events] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_supported_monitoring_events_avp_stream(self):
        stream = bytes.fromhex("00000c4880000014000028af000000000000001a")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], SupportedMonitoringEventsAVP))
        self.assertEqual(avps[0].code, SUPPORTED_MONITORING_EVENTS_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 20)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("000000000000001a"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 3144 [Supported-Monitoring-Events] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_cancellation_type_avp_stream(self):
        stream = bytes.fromhex("0000058cc0000010000028af00000004")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], CancellationTypeAVP))
        self.assertEqual(avps[0].code, CANCELLATION_TYPE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, CANCELLATION_TYPE_INITIAL_ATTACH_PROCEDURE)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1420 [Cancellation-Type] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_clr_flags_avp_stream(self):
        stream = bytes.fromhex("0000066680000010000028af00000002")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ClrFlagsAVP))
        self.assertEqual(avps[0].code, CLR_FLAGS_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "00000002")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1638 [Clr-Flags] VENDOR>")


class TestSupportedFeaturesAVP(unittest.TestCase):
    def test_supported_features_avp__no_value(self):
        self.assertRaises(TypeError, SupportedFeaturesAVP)

    def test_supported_features_avp__repr_dunder(self):
        vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)
        feature_list_id_avp = FeatureListIdAVP(1)
        feature_list_avp = FeatureListAVP(3690988033)

        avps = [vendor_id_avp, feature_list_id_avp, feature_list_avp]
        avp = SupportedFeaturesAVP(avps)

        self.assertEqual(avp.__repr__(), "<Diameter AVP: 628 [Supported-Features] VENDOR>")

    def test_supported_features_avp__1(self):
        ref = "0000027480000038000028af0000010a4000000c000028af0000027580000010000028af000000010000027680000010000028afdc000201"

        vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)
        feature_list_id_avp = FeatureListIdAVP(1)
        feature_list_avp = FeatureListAVP(3690988033)

        avps = [vendor_id_avp, feature_list_id_avp, feature_list_avp]
        avp = SupportedFeaturesAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)

    def test_supported_features_avp__2(self):
        ref = "0000027480000038000028af0000010a4000000c000028af0000027580000010000028af000000020000027680000010000028af092a0000"

        vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)
        feature_list_id_avp = FeatureListIdAVP(2)
        feature_list_avp = FeatureListAVP(153747456)

        avps = [vendor_id_avp, feature_list_id_avp, feature_list_avp]
        avp = SupportedFeaturesAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)


class TestFeatureListIdAVP(unittest.TestCase):
    def test_feature_list_id_avp__no_value(self):
        self.assertRaises(TypeError, FeatureListIdAVP)

    def test_feature_list_id_avp__repr_dunder(self):
        avp = FeatureListIdAVP(1)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 629 [Feature-List-Id] VENDOR>")

    def test_feature_list_id_avp__1(self):
        avp = FeatureListIdAVP(1)
        ref = "0000027580000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_feature_list_id_avp__2(self):
        avp = FeatureListIdAVP(2)
        ref = "0000027580000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)


class TestFeatureListAVP(unittest.TestCase):
    def test_feature_list_avp__no_value(self):
        avp = FeatureListAVP()
        ref = "0000027680000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_feature_list_avp__repr_dunder(self):
        avp = FeatureListAVP(3690988033)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 630 [Feature-List] VENDOR>")

    def test_feature_list_avp__1(self):
        avp = FeatureListAVP(3690988033)
        ref = "0000027680000010000028afdc000201"
        self.assertEqual(avp.dump().hex(), ref)

    def test_feature_list_avp__2(self):
        avp = FeatureListAVP(153747456)
        ref = "0000027680000010000028af092a0000"
        self.assertEqual(avp.dump().hex(), ref)


class TestOperatorDeterminedBarringAVP(unittest.TestCase):
    def test_operator_determined_barring_avp__no_value(self):
        avp = OperatorDeterminedBarringAVP()
        ref = "00000591c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_operator_determined_barring_avp__repr_dunder(self):
        avp = OperatorDeterminedBarringAVP()
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1425 [Operator-Determined-Barring] VENDOR, MANDATORY>")

    def test_operator_determined_barring_avp__set_bit_0(self):
        avp = OperatorDeterminedBarringAVP()
        self.assertEqual(avp.dump().hex(), "00000591c0000010000028af00000000")

        avp.set_bit(0)
        self.assertEqual(avp.dump().hex(), "00000591c0000010000028af00000001")

        avp.unset_bit(0)
        self.assertEqual(avp.dump().hex(), "00000591c0000010000028af00000000")

    def test_operator_determined_barring_avp__set_bit_31(self):
        avp = OperatorDeterminedBarringAVP()
        self.assertEqual(avp.dump().hex(), "00000591c0000010000028af00000000")

        avp.set_bit(31)
        self.assertEqual(avp.dump().hex(), "00000591c0000010000028af80000000")

        avp.unset_bit(31)
        self.assertEqual(avp.dump().hex(), "00000591c0000010000028af00000000")


class TestTerminalInformationAVP(unittest.TestCase):
    def test_terminal_information_avp__no_value(self):
        self.assertRaises(TypeError, TerminalInformationAVP)

    def test_terminal_information_avp__repr_dunder(self):
        imei_avp = ImeiAVP("35358511003417")
        software_version_avp = SoftwareVersionAVP("05")

        avps = [imei_avp, software_version_avp]
        avp = TerminalInformationAVP(avps)

        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1401 [Terminal-Information] VENDOR, MANDATORY>")

    def test_terminal_information_avp__1(self):
        ref = "00000579c0000038000028af0000057ac000001a000028af333533353835313130303334313700000000057bc000000e000028af30350000"

        imei_avp = ImeiAVP("35358511003417")
        software_version_avp = SoftwareVersionAVP("05")

        avps = [imei_avp, software_version_avp]
        avp = TerminalInformationAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)

    def test_terminal_information_avp__2(self):
        ref = "00000579c0000038000028af0000057ac000001b000028af333533393837313030313530383632000000057bc000000f000028af32353500"

        imei_avp = ImeiAVP("353987100150862")
        software_version_avp = SoftwareVersionAVP("255")

        avps = [imei_avp, software_version_avp]
        avp = TerminalInformationAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)


class TestImeiAVP(unittest.TestCase):
    def test_imei_avp__no_value(self):
        self.assertRaises(TypeError, ImeiAVP)

    def test_imei_avp__repr_dunder(self):
        avp = ImeiAVP("35358511003417")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1402 [Imei] VENDOR, MANDATORY>")

    def test_imei_avp__1(self):
        avp = ImeiAVP("35358511003417")
        ref = "0000057ac000001a000028af33353335383531313030333431370000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_imei_avp__2(self):
        avp = ImeiAVP("353987100150862")
        ref = "0000057ac000001b000028af33353339383731303031353038363200"
        self.assertEqual(avp.dump().hex(), ref)

    def test_imei_avp__3(self):
        avp = ImeiAVP("359440080055416")
        ref = "0000057ac000001b000028af33353934343030383030353534313600"
        self.assertEqual(avp.dump().hex(), ref)


class TestSoftwareVersionAVP(unittest.TestCase):
    def test_software_version_avp__no_value(self):
        self.assertRaises(TypeError, SoftwareVersionAVP)

    def test_software_version_avp__repr_dunder(self):
        avp = SoftwareVersionAVP("05")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1403 [Software-Version] VENDOR, MANDATORY>")

    def test_software_version_avp__1(self):
        avp = SoftwareVersionAVP("05")
        ref = "0000057bc000000e000028af30350000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_software_version_avp__2(self):
        avp = SoftwareVersionAVP("255")
        ref = "0000057bc000000f000028af32353500"
        self.assertEqual(avp.dump().hex(), ref)


class TestUlrFlagsAVP(unittest.TestCase):
    def test_ulr_flags_avp__no_value(self):
        self.assertRaises(TypeError, UlrFlagsAVP)

    def test_ulr_flags_avp__repr_dunder(self):
        avp = UlrFlagsAVP(3)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1405 [Ulr-Flags] VENDOR, MANDATORY>")

    def test_ulr_flags_avp__1(self):
        avp = UlrFlagsAVP(3)
        ref = "0000057dc0000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test_ulr_flags_avp__2(self):
        avp = UlrFlagsAVP(255)
        ref = "0000057dc0000010000028af000000ff"
        self.assertEqual(avp.dump().hex(), ref)


class TestVisitedPlmnIdAVP(unittest.TestCase):
    def test_visited_plmn_id_avp__no_value(self):
        self.assertRaises(TypeError, VisitedPlmnIdAVP)

    def test_visited_plmn_id_avp__repr_dunder(self):
        avp = VisitedPlmnIdAVP(bytes.fromhex("27f450"))
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1407 [Visited-Plmn-Id] VENDOR, MANDATORY>")

    def test_visited_plmn_id_avp__1(self):
        avp = VisitedPlmnIdAVP(bytes.fromhex("27f450"))
        ref = "0000057fc000000f000028af27f45000"
        self.assertEqual(avp.dump().hex(), ref)


class TestUeSrvccCapabilityAVP(unittest.TestCase):
    def test_ue_srvcc_capability_avp__no_value(self):
        self.assertRaises(TypeError, UeSrvccCapabilityAVP)

    def test_ue_srvcc_capability_avp__repr_dunder(self):
        avp = UeSrvccCapabilityAVP(UE_SRVCC_NOT_SUPPORTED)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1615 [Ue-Srvcc-Capability] VENDOR>")

    def test_ue_srvcc_capability_avp__ue_srvcc_not_supported(self):
        avp = UeSrvccCapabilityAVP(UE_SRVCC_NOT_SUPPORTED)
        ref = "0000064f80000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_ue_srvcc_capability_avp__ue_srvcc_supported(self):
        avp = UeSrvccCapabilityAVP(UE_SRVCC_SUPPORTED)
        ref = "0000064f80000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestSupportedServicesAVP(unittest.TestCase):
    def test_supported_services_avp__no_value(self):
        self.assertRaises(TypeError, SupportedServicesAVP)

    def test_supported_services_avp__repr_dunder(self):
        supported_monitoring_events_avp = SupportedMonitoringEventsAVP(bytes.fromhex("000000000000001a"))

        avps = [supported_monitoring_events_avp]
        avp = SupportedServicesAVP(avps)

        self.assertEqual(avp.__repr__(), "<Diameter AVP: 3143 [Supported-Services] VENDOR>")

    def test_supported_services_avp__1(self):
        ref = "00000c4780000020000028af00000c4880000014000028af000000000000001a"

        supported_monitoring_events_avp = SupportedMonitoringEventsAVP(bytes.fromhex("000000000000001a"))

        avps = [supported_monitoring_events_avp]
        avp = SupportedServicesAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)


class TestSupportedMonitoringEventsAVP(unittest.TestCase):
    def test_supported_monitoring_events_avp__no_value(self):
        self.assertRaises(TypeError, SupportedMonitoringEventsAVP)

    def test_supported_monitoring_events_avp__repr_dunder(self):
        avp = SupportedMonitoringEventsAVP(bytes.fromhex("000000000000001a"))
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 3144 [Supported-Monitoring-Events] VENDOR>")

    def test_supported_monitoring_events_avp__1(self):
        avp = SupportedMonitoringEventsAVP(bytes.fromhex("000000000000001a"))
        ref = "00000c4880000014000028af000000000000001a"
        self.assertEqual(avp.dump().hex(), ref)


class TestCancellationTypeAVP(unittest.TestCase):
    def test_cancellation_type_avp__no_value(self):
        self.assertRaises(TypeError, CancellationTypeAVP)

    def test_cancellation_type_avp__repr_dunder(self):
        avp = CancellationTypeAVP(CANCELLATION_TYPE_MME_UPDATE_PROCEDURE)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1420 [Cancellation-Type] VENDOR, MANDATORY>")

    def test_cancellation_type_avp__mme_update_procedure(self):
        avp = CancellationTypeAVP(CANCELLATION_TYPE_MME_UPDATE_PROCEDURE)
        ref = "0000058cc0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_cancellation_type_avp__sgsn_update_procedure(self):
        avp = CancellationTypeAVP(CANCELLATION_TYPE_SGSN_UPDATE_PROCEDURE)
        ref = "0000058cc0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_cancellation_type_avp__subscription_withdrawal(self):
        avp = CancellationTypeAVP(CANCELLATION_TYPE_SUBSCRIPTION_WITHDRAWAL)
        ref = "0000058cc0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_cancellation_type_avp__update_procedure_iwf(self):
        avp = CancellationTypeAVP(CANCELLATION_TYPE_UPDATE_PROCEDURE_IWF)
        ref = "0000058cc0000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test_cancellation_type_avp__initial_attach_procedure(self):
        avp = CancellationTypeAVP(CANCELLATION_TYPE_INITIAL_ATTACH_PROCEDURE)
        ref = "0000058cc0000010000028af00000004"
        self.assertEqual(avp.dump().hex(), ref)


class TestClrFlagsAVP(unittest.TestCase):
    def test_clr_flags_avp__no_value(self):
        self.assertRaises(TypeError, ClrFlagsAVP)

    def test_clr_flags_avp__repr_dunder(self):
        avp = ClrFlagsAVP(2)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1638 [Clr-Flags] VENDOR>")

    def test_clr_flags_avp__1(self):
        avp = ClrFlagsAVP(2)
        ref = "0000066680000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)


if __name__ == "__main__":
    unittest.main()

    