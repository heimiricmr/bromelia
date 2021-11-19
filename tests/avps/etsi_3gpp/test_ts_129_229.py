# -*- coding: utf-8 -*-
"""
    tests.avps.etsi_3gpp.test_ts_129_229
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for ETSI TS 129 229.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(testing_dir))

sys.path.insert(0, base_dir)

from bromelia.avps.etsi_3gpp.ts_129_229 import *


class TestDiameterAVP(unittest.TestCase):
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

    def test_diameter_avp__load_staticmethod__parsing_visited_network_identifier_avp_stream(self):
        stream = bytes.fromhex("00000258c0000029000028af6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], VisitedNetworkIdentifierAVP))
        self.assertEqual(avps[0].code, VISITED_NETWORK_IDENTIFIER_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 41)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, b"mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avps[0].get_padding_length(), 3)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 600 [Visited-Network-Identifier] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_sip_number_auth_items_avp_stream(self):
        stream = bytes.fromhex("0000025fc0000010000028af00000001")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], SipNumberAuthItemsAVP))
        self.assertEqual(avps[0].code, SIP_NUMBER_AUTH_ITEMS_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("00000001"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 607 [Sip-Number-Auth-Items] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_sip_authentication_scheme_avp_stream(self):
        stream = bytes.fromhex("00000260c0000013000028af4541502d414b4100")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], SipAuthenticationSchemeAVP))
        self.assertEqual(avps[0].code, SIP_AUTHENTICATION_SCHEME_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 19)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, b"EAP-AKA")
        self.assertEqual(avps[0].get_padding_length(), 1)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 608 [Sip-Authentication-Scheme] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_sip_authenticate_avp_stream(self):
        stream = bytes.fromhex("00000261c000002c000028af0d005afac8190f0af480882e1168f5721fd697f6ce41000057bafb6ffd6a720d")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], SipAuthenticateAVP))
        self.assertEqual(avps[0].code, SIP_AUTHENTICATE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 44)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("0d005afac8190f0af480882e1168f5721fd697f6ce41000057bafb6ffd6a720d"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 609 [Sip-Authenticate] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_sip_authorization_avp_stream(self):
        stream = bytes.fromhex("00000262c0000014000028afb8cfc7056c4891ce")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], SipAuthorizationAVP))
        self.assertEqual(avps[0].code, SIP_AUTHORIZATION_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 20)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "b8cfc7056c4891ce")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 610 [Sip-Authorization] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_confidentiality_key_avp_stream(self):
        stream = bytes.fromhex("00000271c000001c000028afd0916caa8f6008195cbff313d8411369")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ConfidentialityKeyAVP))
        self.assertEqual(avps[0].code, CONFIDENTIALITY_KEY_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 28)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "d0916caa8f6008195cbff313d8411369")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 625 [Confidentiality-Key] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_integrity_key_avp_stream(self):
        stream = bytes.fromhex("00000272c000001c000028af1d9f3aadeef31e24f3ebd7c52eee4d26")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], IntegrityKeyAVP))
        self.assertEqual(avps[0].code, INTEGRITY_KEY_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 28)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "1d9f3aadeef31e24f3ebd7c52eee4d26")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 626 [Integrity-Key] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_sip_auth_data_item_avp_stream(self):
        stream = bytes.fromhex("00000264c0000098000028af00000260c0000013000028af4541502d414b410000000261c000002c000028af0d005afac8190f0af480882e1168f5721fd697f6ce41000057bafb6ffd6a720d00000262c0000014000028afb8cfc7056c4891ce00000271c000001c000028afd0916caa8f6008195cbff313d841136900000272c000001c000028af1d9f3aadeef31e24f3ebd7c52eee4d26")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], SipAuthDataItemAVP))
        self.assertEqual(avps[0].code, SIP_AUTH_DATA_ITEM_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 152)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.maxDiff = None
        self.assertEqual(avps[0].data, bytes.fromhex("00000260c0000013000028af4541502d414b410000000261c000002c000028af0d005afac8190f0af480882e1168f5721fd697f6ce41000057bafb6ffd6a720d00000262c0000014000028afb8cfc7056c4891ce00000271c000001c000028afd0916caa8f6008195cbff313d841136900000272c000001c000028af1d9f3aadeef31e24f3ebd7c52eee4d26"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 612 [Sip-Auth-Data-Item] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_server_assignment_type_avp_stream(self):
        stream = bytes.fromhex("00000266c0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ServerAssignmentTypeAVP))
        self.assertEqual(avps[0].code, SERVER_ASSIGNMENT_TYPE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, SERVER_ASSIGNMENT_TYPE_NO_ASSIGNMENT)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 614 [Server-Assignment-Type] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_reason_code_avp_stream(self):
        stream = bytes.fromhex("00000268c0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ReasonCodeAVP))
        self.assertEqual(avps[0].code, REASON_CODE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, REASON_CODE_PERMANENT_TERMINATION)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 616 [Reason-Code] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_reason_info_avp_stream(self):
        stream = bytes.fromhex("00000269c0000030000028af5375627363726962657220686173206265656e2072656d6f7665642066726f6d204e572e")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ReasonInfoAVP))
        self.assertEqual(avps[0].code, REASON_INFO_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 48)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, b"Subscriber has been removed from NW.")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 617 [Reason-Info] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_de_registration_reason_avp_stream(self):
        stream = bytes.fromhex("00000267c000001c000028af00000268c0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], DeregistrationReasonAVP))
        self.assertEqual(avps[0].code, DE_REGISTRATION_REASON_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 28)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "00000268c0000010000028af00000000")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 615 [Deregistration-Reason] VENDOR, MANDATORY>")

        reason_code_avp = avps[0].reason_code_avp

        self.assertTrue(isinstance(reason_code_avp, ReasonCodeAVP))
        self.assertEqual(reason_code_avp.code, REASON_CODE_AVP_CODE)
        self.assertTrue(reason_code_avp.is_vendor_id())
        self.assertTrue(reason_code_avp.is_mandatory())
        self.assertFalse(reason_code_avp.is_protected())
        self.assertEqual(reason_code_avp.get_length(), 16)
        self.assertEqual(reason_code_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(reason_code_avp.data, REASON_CODE_PERMANENT_TERMINATION)
        self.assertIsNone(reason_code_avp.get_padding_length())
        self.assertEqual(reason_code_avp.__repr__(), "<Diameter AVP: 616 [Reason-Code] VENDOR, MANDATORY>")


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


class TestVisitedNetworkIdentifierAVP(unittest.TestCase):
    def test_visited_network_identifier_avp__no_value(self):
        self.assertRaises(TypeError, VisitedNetworkIdentifierAVP)

    def test_visited_network_identifier_avp__repr_dunder(self):
        avp = VisitedNetworkIdentifierAVP("mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 600 [Visited-Network-Identifier] VENDOR, MANDATORY>")

    def test_visited_network_identifier_avp__mncXXX_mccYYY(self):
        avp = VisitedNetworkIdentifierAVP("mncXXX.mccYYY.3gppnetwork.org")
        ref = "00000258c0000029000028af6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"
        self.assertEqual(avp.dump().hex(), ref)


class TestSipNumberAuthItemsAVP(unittest.TestCase):
    def test__sip_number_auth_items_avp__no_value(self):
        self.assertRaises(TypeError, SipNumberAuthItemsAVP)

    def test__sip_number_auth_items_avp__repr_dunder(self):
        avp = SipNumberAuthItemsAVP(0)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 607 [Sip-Number-Auth-Items] VENDOR, MANDATORY>")

    def test__sip_number_auth_items_avp__1(self):
        avp = SipNumberAuthItemsAVP(1)
        ref = "0000025fc0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__sip_number_auth_items_avp__2(self):
        avp = SipNumberAuthItemsAVP(2)
        ref = "0000025fc0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)


class TestSipAuthenticationSchemeAVP(unittest.TestCase):
    def test__sip_authentication_scheme_avp__no_value(self):
        self.assertRaises(TypeError, SipAuthenticationSchemeAVP)

    def test__sip_authentication_scheme_avp__repr_dunder(self):
        avp = SipAuthenticationSchemeAVP("SIP Digest")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 608 [Sip-Authentication-Scheme] VENDOR, MANDATORY>")

    def test__sip_authentication_scheme_avp__1(self):
        avp = SipAuthenticationSchemeAVP("SIP Digest")
        ref = "00000260c0000016000028af534950204469676573740000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__sip_authentication_scheme_avp__2(self):
        avp = SipAuthenticationSchemeAVP("NASS-Bundled")
        ref = "00000260c0000018000028af4e4153532d42756e646c6564"
        self.assertEqual(avp.dump().hex(), ref)

    def test__sip_authentication_scheme_avp__3(self):
        avp = SipAuthenticationSchemeAVP("Early-IMS-Security")
        ref = "00000260c000001e000028af4561726c792d494d532d53656375726974790000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__sip_authentication_scheme_avp__4(self):
        avp = SipAuthenticationSchemeAVP("Unknown")
        ref = "00000260c0000013000028af556e6b6e6f776e00"
        self.assertEqual(avp.dump().hex(), ref)

    def test__sip_authentication_scheme_avp__5(self):
        avp = SipAuthenticationSchemeAVP("EAP-AKA")
        ref = "00000260c0000013000028af4541502d414b4100"
        self.assertEqual(avp.dump().hex(), ref)


class TestSipAuthenticateAVP(unittest.TestCase):
    def test__sip_authenticate_avp__no_value(self):
        self.assertRaises(TypeError, SipAuthenticateAVP)

    def test__sip_authenticate_avp__repr_dunder(self):
        data = bytes.fromhex("0d005afac8190f0af480882e1168f5721fd697f6ce41000057bafb6ffd6a720d")
        avp = SipAuthenticateAVP(data)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 609 [Sip-Authenticate] VENDOR, MANDATORY>")

    def test__sip_authenticate_avp__1(self):
        data = bytes.fromhex("0d005afac8190f0af480882e1168f5721fd697f6ce41000057bafb6ffd6a720d")
        avp = SipAuthenticateAVP(data)
        ref = "00000261c000002c000028af0d005afac8190f0af480882e1168f5721fd697f6ce41000057bafb6ffd6a720d"
        self.assertEqual(avp.dump().hex(), ref)


class TestSipAuthorizationAVP(unittest.TestCase):
    def test__sip_authorization_avp__no_value(self):
        self.assertRaises(TypeError, SipAuthorizationAVP)

    def test__sip_authorization_avp__repr_dunder(self):
        avp = SipAuthorizationAVP(bytes.fromhex("b8cfc7056c4891ce"))
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 610 [Sip-Authorization] VENDOR, MANDATORY>")

    def test__sip_authorization_avp__1(self):
        avp = SipAuthorizationAVP(bytes.fromhex("b8cfc7056c4891ce"))
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 610 [Sip-Authorization] VENDOR, MANDATORY>")


class TestConfidentialityKeyAVP(unittest.TestCase):
    def test__confidentiality_key_avp__no_value(self):
        self.assertRaises(TypeError, ConfidentialityKeyAVP)

    def test__confidentiality_key_avp__repr_dunder(self):
        data = bytes.fromhex("d0916caa8f6008195cbff313d8411369")
        avp = ConfidentialityKeyAVP(data)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 625 [Confidentiality-Key] VENDOR, MANDATORY>")

    def test__confidentiality_key_avp__1(self):
        data = bytes.fromhex("d0916caa8f6008195cbff313d8411369")
        avp = ConfidentialityKeyAVP(data)
        ref = "00000271c000001c000028afd0916caa8f6008195cbff313d8411369"
        self.assertEqual(avp.dump().hex(), ref)


class TestIntegrityKeyAVP(unittest.TestCase):
    def test__integrity_key_avp__no_value(self):
        self.assertRaises(TypeError, IntegrityKeyAVP)

    def test__integrity_key_avp__repr_dunder(self):
        avp = IntegrityKeyAVP("1d9f3aadeef31e24f3ebd7c52eee4d26")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 626 [Integrity-Key] VENDOR, MANDATORY>")

    def test__integrity_key_avp__1(self):
        data = bytes.fromhex("1d9f3aadeef31e24f3ebd7c52eee4d26")
        avp = IntegrityKeyAVP(data)
        ref = "00000272c000001c000028af1d9f3aadeef31e24f3ebd7c52eee4d26"
        self.assertEqual(avp.dump().hex(), ref)


class TestSipAuthDataItemAVP(unittest.TestCase):
    def test__sip_auth_data_item_avp__no_value(self):
        self.assertRaises(TypeError, SipAuthDataItemAVP)

    def test__sip_auth_data_item_avp__repr_dunder(self):
        sip_authentication_scheme_avp = SipAuthenticationSchemeAVP("EAP-AKA")
        sip_authenticate_avp = SipAuthenticateAVP(bytes.fromhex("0d005afac8190f0af480882e1168f5721fd697f6ce41000057bafb6ffd6a720d"))
        sip_authorization_avp = SipAuthorizationAVP(bytes.fromhex("b8cfc7056c4891ce"))
        confidentiality_key_avp = ConfidentialityKeyAVP(bytes.fromhex("d0916caa8f6008195cbff313d8411369"))
        integrity_key_avp = IntegrityKeyAVP(bytes.fromhex("1d9f3aadeef31e24f3ebd7c52eee4d26"))

        avps = [sip_authentication_scheme_avp, sip_authenticate_avp, sip_authorization_avp, confidentiality_key_avp, integrity_key_avp]
        avp = SipAuthDataItemAVP(avps)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 612 [Sip-Auth-Data-Item] VENDOR, MANDATORY>")

    def test__sip_auth_data_item_avp__1(self):
        sip_authentication_scheme_avp = SipAuthenticationSchemeAVP("EAP-AKA")
        sip_authenticate_avp = SipAuthenticateAVP(bytes.fromhex("0d005afac8190f0af480882e1168f5721fd697f6ce41000057bafb6ffd6a720d"))
        sip_authorization_avp = SipAuthorizationAVP(bytes.fromhex("b8cfc7056c4891ce"))
        confidentiality_key_avp = ConfidentialityKeyAVP(bytes.fromhex("d0916caa8f6008195cbff313d8411369"))
        integrity_key_avp = IntegrityKeyAVP(bytes.fromhex("1d9f3aadeef31e24f3ebd7c52eee4d26"))

        avps = [sip_authentication_scheme_avp, sip_authenticate_avp, sip_authorization_avp, confidentiality_key_avp, integrity_key_avp]
        avp = SipAuthDataItemAVP(avps)

        ref = "00000264c0000098000028af00000260c0000013000028af4541502d414b410000000261c000002c000028af0d005afac8190f0af480882e1168f5721fd697f6ce41000057bafb6ffd6a720d00000262c0000014000028afb8cfc7056c4891ce00000271c000001c000028afd0916caa8f6008195cbff313d841136900000272c000001c000028af1d9f3aadeef31e24f3ebd7c52eee4d26"
        self.assertEqual(avp.dump().hex(), ref)


class TestServerAssignmentTypeAVP(unittest.TestCase):
    def test__server_assignment_type_avp__no_value(self):
        self.assertRaises(TypeError, ServerAssignmentTypeAVP)

    def test__server_assignment_type_avp__repr_dunder(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_NO_ASSIGNMENT)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 614 [Server-Assignment-Type] VENDOR, MANDATORY>")

    def test__server_assignment_type_avp__no_assignment(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_NO_ASSIGNMENT)
        ref = "00000266c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__server_assignment_type_avp__registration(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_REGISTRATION)
        ref = "00000266c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__server_assignment_type_avp__re_registration(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_RE_REGISTRATION)
        ref = "00000266c0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test__server_assignment_type_avp__unregistered_user(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_UNREGISTERED_USER)
        ref = "00000266c0000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test__server_assignment_type_avp__timeout_deregistration(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_TIMEOUT_DEREGISTRATION)
        ref = "00000266c0000010000028af00000004"
        self.assertEqual(avp.dump().hex(), ref)

    def test__server_assignment_type_avp__user_deregistration(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_USER_DEREGISTRATION)
        ref = "00000266c0000010000028af00000005"
        self.assertEqual(avp.dump().hex(), ref)

    def test__server_assignment_type_avp__deregistration_store_server_name(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_DEREGISTRATION_STORE_SERVER_NAME)
        ref = "00000266c0000010000028af00000006"
        self.assertEqual(avp.dump().hex(), ref)

    def test__server_assignment_type_avp__user_deregistration_store_server_name(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_USER_DEREGISTRATION_STORE_SERVER_NAME)
        ref = "00000266c0000010000028af00000007"
        self.assertEqual(avp.dump().hex(), ref)

    def test__server_assignment_type_avp__administrative_deregistration(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_ADMINISTRATIVE_DEREGISTRATION)
        ref = "00000266c0000010000028af00000008"
        self.assertEqual(avp.dump().hex(), ref)

    def test__server_assignment_type_avp__authentication_failure(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_AUTHENTICATION_FAILURE)
        ref = "00000266c0000010000028af00000009"
        self.assertEqual(avp.dump().hex(), ref)

    def test__server_assignment_type_avp__authentication_timeout(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_AUTHENTICATION_TIMEOUT)
        ref = "00000266c0000010000028af0000000a"
        self.assertEqual(avp.dump().hex(), ref)

    def test__server_assignment_type_avp__deregistration_too_much_data(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_DEREGISTRATION_TOO_MUCH_DATA)
        ref = "00000266c0000010000028af0000000b"
        self.assertEqual(avp.dump().hex(), ref)

    def test__server_assignment_type_avp__aaa_user_data_request(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_AAA_USER_DATA_REQUEST)
        ref = "00000266c0000010000028af0000000c"
        self.assertEqual(avp.dump().hex(), ref)

    def test__server_assignment_type_avp__pgw_update(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_PGW_UPDATE)
        ref = "00000266c0000010000028af0000000d"
        self.assertEqual(avp.dump().hex(), ref)

    def test__server_assignment_type_avp__restoration(self):
        avp = ServerAssignmentTypeAVP(SERVER_ASSIGNMENT_TYPE_RESTORATION)
        ref = "00000266c0000010000028af0000000e"
        self.assertEqual(avp.dump().hex(), ref)   


class TestReasonCodeAVP(unittest.TestCase):
    def test__reason_code_avp__no_value(self):
        self.assertRaises(TypeError, ReasonCodeAVP)

    def test__reason_code_avp__repr_dunder(self):
        avp = ReasonCodeAVP(REASON_CODE_PERMANENT_TERMINATION)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 616 [Reason-Code] VENDOR, MANDATORY>")

    def test__reason_code_avp__permanent_termination(self):
        avp = ReasonCodeAVP(REASON_CODE_PERMANENT_TERMINATION)
        ref = "00000268c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reason_code_avp__new_server_assigned(self):
        avp = ReasonCodeAVP(REASON_CODE_NEW_SERVER_ASSIGNED)
        ref = "00000268c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reason_code_avp__server_change(self):
        avp = ReasonCodeAVP(REASON_CODE_SERVER_CHANGE)
        ref = "00000268c0000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reason_code_avp__remove_change(self):
        avp = ReasonCodeAVP(REASON_CODE_REMOVE_CHANGE)
        ref = "00000268c0000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)


class TestReasonInfoAVP(unittest.TestCase):
    def test__reason_info_avp__no_value(self):
        self.assertRaises(TypeError, ReasonInfoAVP)

    def test__reason_info_avp__repr_dunder(self):
        avp = ReasonInfoAVP("Subscriber has been removed from NW.")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 617 [Reason-Info] VENDOR, MANDATORY>")

    def test__reason_info_avp__1(self):
        avp = ReasonInfoAVP("Subscriber has been removed from NW.")
        ref = "00000269c0000030000028af5375627363726962657220686173206265656e2072656d6f7665642066726f6d204e572e"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reason_info_avp__2(self):
        avp = ReasonInfoAVP("Subscriber registration refreshed.")
        ref = "00000269c000002e000028af5375627363726962657220726567697374726174696f6e207265667265736865642e0000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reason_info_avp__3(self):
        avp = ReasonInfoAVP("Subscriber profile updated.")
        ref = "00000269c0000027000028af537562736372696265722070726f66696c6520757064617465642e00"
        self.assertEqual(avp.dump().hex(), ref)


class TestDeregistrationReasonAVP(unittest.TestCase):
    def test__de_registration_reason_avp__no_value(self):
        self.assertRaises(TypeError, DeregistrationReasonAVP)

    def test__de_registration_reason_avp__repr_dunder(self):
        avps = [
                    ReasonCodeAVP(REASON_CODE_PERMANENT_TERMINATION)
        ]
        avp = DeregistrationReasonAVP(avps)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 615 [Deregistration-Reason] VENDOR, MANDATORY>")

    def test__de_registration_reason_avp__reason_code_1(self):
        ref = "00000267c000001c000028af00000268c0000010000028af00000000"

        avps = [
                    ReasonCodeAVP(REASON_CODE_PERMANENT_TERMINATION)
        ]
        avp = DeregistrationReasonAVP(avps)
        self.assertEqual(avp.dump().hex(), ref)

    def test__de_registration_reason_avp__reason_code_2(self):
        ref = "00000267c000001c000028af00000268c0000010000028af00000001"

        avps = [
                    ReasonCodeAVP(REASON_CODE_NEW_SERVER_ASSIGNED)
        ]
        avp = DeregistrationReasonAVP(avps)
        self.assertEqual(avp.dump().hex(), ref)

    def test__de_registration_reason_avp__reason_code_3(self):
        ref = "00000267c000001c000028af00000268c0000010000028af00000002"

        avps = [
                    ReasonCodeAVP(REASON_CODE_SERVER_CHANGE)
        ]
        avp = DeregistrationReasonAVP(avps)
        self.assertEqual(avp.dump().hex(), ref)

    def test__de_registration_reason_avp__reason_code_4(self):
        ref = "00000267c000001c000028af00000268c0000010000028af00000003"

        avps = [
                    ReasonCodeAVP(REASON_CODE_REMOVE_CHANGE)
        ]
        avp = DeregistrationReasonAVP(avps)
        self.assertEqual(avp.dump().hex(), ref)

    def test__de_registration_reason_avp__reason_code_5(self):
        ref = "00000267c000004c000028af00000268c0000010000028af0000000000000269c0000030000028af5375627363726962657220686173206265656e2072656d6f7665642066726f6d204e572e"

        avps = [
                    ReasonCodeAVP(REASON_CODE_PERMANENT_TERMINATION),
                    ReasonInfoAVP("Subscriber has been removed from NW.")
        ]
        avp = DeregistrationReasonAVP(avps)
        self.assertEqual(avp.dump().hex(), ref)


if __name__ == "__main__":
    unittest.main()