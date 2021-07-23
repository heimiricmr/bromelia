# -*- coding: utf-8 -*-
"""
    test.etsi_3gpp_swx.test_avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP unittests 
	for 3GPP SWx Diameter Application Id.
    
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

from bromelia.etsi_3gpp_swx.avps import *


class TestDiameterAVP(unittest.TestCase):
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
        self.assertEqual(avps[0].data.hex(), "00000260c0000013000028af4541502d414b410000000261c000002c000028af0d005afac8190f0af480882e1168f5721fd697f6ce41000057bafb6ffd6a720d00000262c0000014000028afb8cfc7056c4891ce00000271c000001c000028afd0916caa8f6008195cbff313d841136900000272c000001c000028af1d9f3aadeef31e24f3ebd7c52eee4d26")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 612 [Sip-Auth-Data-Item] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_non_3gpp_ip_access_avp_stream(self):
        stream = bytes.fromhex("000005ddc0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], Non3gppIpAccessAVP))
        self.assertEqual(avps[0].code, NON_3GPP_IP_ACCESS_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, NON_3GPP_SUBSCRIPTION_ALLOWED)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1501 [Non3gpp-Ip-Access] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_sip_auth_data_item_avp_stream(self):
        stream = bytes.fromhex("000005dec0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], Non3gppIpAccessApnAVP))
        self.assertEqual(avps[0].code, NON_3GPP_IP_ACCESS_APN_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, NON_3GPP_APNS_ENABLE)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1502 [Non3gpp-Ip-Access-Apn] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_non_3gpp_user_data_avp_stream(self):
        stream = bytes.fromhex("000005dcc0000150000028af000001bb4000002c000001c24000000c00000000000001bc4000001535353131313233343536373839000000000005ddc0000010000028af00000000000005dec0000010000028af000000000000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e8000000000d80000010000028af304230300000058f80000010000028af0000000100000596800000ac000028af0000058f80000010000028af0000058f000001ed4000000b696d7300000005b080000010000028af000000020000059780000038000028af0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af000000080000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e8000000059880000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], Non3gppUserDataAVP))
        self.assertEqual(avps[0].code, NON_3GPP_USER_DATA_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 336)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "000001bb4000002c000001c24000000c00000000000001bc4000001535353131313233343536373839000000000005ddc0000010000028af00000000000005dec0000010000028af000000000000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e8000000000d80000010000028af304230300000058f80000010000028af0000000100000596800000ac000028af0000058f80000010000028af0000058f000001ed4000000b696d7300000005b080000010000028af000000020000059780000038000028af0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af000000080000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e8000000059880000010000028af00000000")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1500 [Non3gpp-User-Data] VENDOR, MANDATORY>")

        subscription_id_avp = avps[0].subscription_id_avp
        non3gpp_ip_access_avp = avps[0].non3gpp_ip_access_avp
        non3gpp_ip_access_apn_avp = avps[0].non3gpp_ip_access_apn_avp
        ambr_avp = avps[0].ambr_avp
        x3gpp_charging_characteristics_avp = avps[0].x3gpp_charging_characteristics_avp
        context_identifier_avp = avps[0].context_identifier_avp
        apn_configuration_avp = avps[0].apn_configuration_avp
        
        #: Non-3GPP-User-Data > Subscription-Id AVP
        self.assertTrue(isinstance(subscription_id_avp, SubscriptionIdAVP))
        self.assertEqual(subscription_id_avp.code, SUBSCRIPTION_ID_AVP_CODE)
        self.assertFalse(subscription_id_avp.is_vendor_id())
        self.assertTrue(subscription_id_avp.is_mandatory())
        self.assertFalse(subscription_id_avp.is_protected())
        self.assertEqual(subscription_id_avp.get_length(), 44)
        self.assertIsNone(subscription_id_avp.vendor_id)
        self.assertEqual(subscription_id_avp.data.hex(), "000001c24000000c00000000000001bc4000001535353131313233343536373839000000")
        self.assertIsNone(subscription_id_avp.get_padding_length())
        self.assertEqual(subscription_id_avp.__repr__(), "<Diameter AVP: 443 [Subscription-Id] MANDATORY>")

        subscription_id_type_avp = subscription_id_avp.subscription_id_type_avp
        subscription_id_data_avp = subscription_id_avp.subscription_id_data_avp

        # self.assertTrue(isinstance(subscription_id_type_avp, SubscriptionIdTypeAVP))
        self.assertEqual(subscription_id_type_avp.code, SUBSCRIPTION_ID_TYPE_AVP_CODE)
        self.assertFalse(subscription_id_type_avp.is_vendor_id())
        self.assertTrue(subscription_id_type_avp.is_mandatory())
        self.assertFalse(subscription_id_type_avp.is_protected())
        self.assertEqual(subscription_id_type_avp.get_length(), 12)
        self.assertIsNone(subscription_id_type_avp.vendor_id)
        self.assertEqual(subscription_id_type_avp.data, END_USER_E164)
        self.assertIsNone(subscription_id_type_avp.get_padding_length())
        self.assertEqual(subscription_id_type_avp.__repr__(), "<Diameter AVP: 450 [Subscription-Id-Type] MANDATORY>")

        # self.assertTrue(isinstance(subscription_id_data_avp, SubscriptionIdDataAVP))
        self.assertEqual(subscription_id_data_avp.code, SUBSCRIPTION_ID_DATA_AVP_CODE)
        self.assertFalse(subscription_id_data_avp.is_vendor_id())
        self.assertTrue(subscription_id_data_avp.is_mandatory())
        self.assertFalse(subscription_id_data_avp.is_protected())
        self.assertEqual(subscription_id_data_avp.get_length(), 21)
        self.assertIsNone(subscription_id_data_avp.vendor_id)
        self.assertEqual(subscription_id_data_avp.data, b"5511123456789")
        self.assertEqual(subscription_id_data_avp.get_padding_length(), 3)
        self.assertEqual(subscription_id_data_avp.__repr__(), "<Diameter AVP: 444 [Subscription-Id-Data] MANDATORY>")

        #: Non-3GPP-User-Data > Non-3GPP-IP-Access AVP
        self.assertTrue(isinstance(non3gpp_ip_access_avp, Non3gppIpAccessAVP))
        self.assertEqual(non3gpp_ip_access_avp.code, NON_3GPP_IP_ACCESS_AVP_CODE)
        self.assertTrue(non3gpp_ip_access_avp.is_vendor_id())
        self.assertTrue(non3gpp_ip_access_avp.is_mandatory())
        self.assertFalse(non3gpp_ip_access_avp.is_protected())
        self.assertEqual(non3gpp_ip_access_avp.get_length(), 16)
        self.assertEqual(non3gpp_ip_access_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(non3gpp_ip_access_avp.data, NON_3GPP_SUBSCRIPTION_ALLOWED)
        self.assertIsNone(non3gpp_ip_access_avp.get_padding_length())
        self.assertEqual(non3gpp_ip_access_avp.__repr__(), "<Diameter AVP: 1501 [Non3gpp-Ip-Access] VENDOR, MANDATORY>")

        #: Non-3GPP-User-Data > Non-3GPP-IP-Access-APN AVP
        self.assertTrue(isinstance(non3gpp_ip_access_apn_avp, Non3gppIpAccessApnAVP))
        self.assertEqual(non3gpp_ip_access_apn_avp.code, NON_3GPP_IP_ACCESS_APN_AVP_CODE)
        self.assertTrue(non3gpp_ip_access_apn_avp.is_vendor_id())
        self.assertTrue(non3gpp_ip_access_apn_avp.is_mandatory())
        self.assertFalse(non3gpp_ip_access_apn_avp.is_protected())
        self.assertEqual(non3gpp_ip_access_apn_avp.get_length(), 16)
        self.assertEqual(non3gpp_ip_access_apn_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(non3gpp_ip_access_apn_avp.data, NON_3GPP_APNS_ENABLE)
        self.assertIsNone(non3gpp_ip_access_apn_avp.get_padding_length())
        self.assertEqual(non3gpp_ip_access_apn_avp.__repr__(), "<Diameter AVP: 1502 [Non3gpp-Ip-Access-Apn] VENDOR, MANDATORY>")

        #: Non-3GPP-User-Data > AMBR AVP
        self.assertTrue(isinstance(ambr_avp, AmbrAVP))
        self.assertEqual(ambr_avp.code, AMBR_AVP_CODE)
        self.assertTrue(ambr_avp.is_vendor_id())
        self.assertTrue(ambr_avp.is_mandatory())
        self.assertFalse(ambr_avp.is_protected())
        self.assertEqual(ambr_avp.get_length(), 44)
        self.assertEqual(ambr_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(ambr_avp.data.hex(), "00000203c0000010000028af0003e80000000204c0000010000028af0003e800")
        self.assertIsNone(ambr_avp.get_padding_length())
        self.assertEqual(ambr_avp.__repr__(), "<Diameter AVP: 1435 [Ambr] VENDOR, MANDATORY>")

        max_requested_bandwidth_dl_avp = ambr_avp.max_requested_bandwidth_dl_avp
        max_requested_bandwidth_ul_avp = ambr_avp.max_requested_bandwidth_ul_avp

        self.assertTrue(isinstance(max_requested_bandwidth_dl_avp, MaxRequestedBandwidthDlAVP))
        self.assertEqual(max_requested_bandwidth_dl_avp.code, MAX_REQUESTED_BANDWIDTH_DL_AVP_CODE)
        self.assertTrue(max_requested_bandwidth_dl_avp.is_vendor_id())
        self.assertTrue(max_requested_bandwidth_dl_avp.is_mandatory())
        self.assertFalse(max_requested_bandwidth_dl_avp.is_protected())
        self.assertEqual(max_requested_bandwidth_dl_avp.get_length(), 16)
        self.assertEqual(max_requested_bandwidth_dl_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(max_requested_bandwidth_dl_avp.data.hex(), "0003e800")
        self.assertIsNone(max_requested_bandwidth_dl_avp.get_padding_length())
        self.assertEqual(max_requested_bandwidth_dl_avp.__repr__(), "<Diameter AVP: 515 [Max-Requested-Bandwidth-Dl] VENDOR, MANDATORY>")

        self.assertTrue(isinstance(max_requested_bandwidth_ul_avp, MaxRequestedBandwidthUlAVP))
        self.assertEqual(max_requested_bandwidth_ul_avp.code, MAX_REQUESTED_BANDWIDTH_UL_AVP_CODE)
        self.assertTrue(max_requested_bandwidth_ul_avp.is_vendor_id())
        self.assertTrue(max_requested_bandwidth_ul_avp.is_mandatory())
        self.assertFalse(max_requested_bandwidth_ul_avp.is_protected())
        self.assertEqual(max_requested_bandwidth_ul_avp.get_length(), 16)
        self.assertEqual(max_requested_bandwidth_ul_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(max_requested_bandwidth_ul_avp.data.hex(), "0003e800")
        self.assertIsNone(max_requested_bandwidth_ul_avp.get_padding_length())
        self.assertEqual(max_requested_bandwidth_ul_avp.__repr__(), "<Diameter AVP: 516 [Max-Requested-Bandwidth-Ul] VENDOR, MANDATORY>")

        #: Non-3GPP-User-Data > 3GPP-Charging-Characteristics AVP
        self.assertTrue(isinstance(x3gpp_charging_characteristics_avp, X3gppChargingCharacteristicsAVP))
        self.assertEqual(x3gpp_charging_characteristics_avp.code, X_3GPP_CHARGING_CHARACTERISTICS_AVP_CODE)
        self.assertTrue(x3gpp_charging_characteristics_avp.is_vendor_id())
        self.assertFalse(x3gpp_charging_characteristics_avp.is_mandatory())
        self.assertFalse(x3gpp_charging_characteristics_avp.is_protected())
        self.assertEqual(x3gpp_charging_characteristics_avp.get_length(), 16)
        self.assertEqual(x3gpp_charging_characteristics_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(x3gpp_charging_characteristics_avp.data.hex(), "30423030")
        self.assertIsNone(x3gpp_charging_characteristics_avp.get_padding_length())
        self.assertEqual(x3gpp_charging_characteristics_avp.__repr__(), "<Diameter AVP: 13 [X3gpp-Charging-Characteristics] VENDOR>")

        #: Non-3GPP-User-Data > Context-Identifier AVP
        self.assertTrue(isinstance(context_identifier_avp, ContextIdentifierAVP))
        self.assertEqual(context_identifier_avp.code, CONTEXT_IDENTIFIER_AVP_CODE)
        self.assertTrue(context_identifier_avp.is_vendor_id())
        self.assertFalse(context_identifier_avp.is_mandatory())
        self.assertFalse(context_identifier_avp.is_protected())
        self.assertEqual(context_identifier_avp.get_length(), 16)
        self.assertEqual(context_identifier_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(context_identifier_avp.data.hex(), "00000001")
        self.assertIsNone(context_identifier_avp.get_padding_length())
        self.assertEqual(context_identifier_avp.__repr__(), "<Diameter AVP: 1423 [Context-Identifier] VENDOR>")

        #: Non-3GPP-User-Data > APN-Configuration AVP
        self.assertTrue(isinstance(apn_configuration_avp, ApnConfigurationAVP))
        self.assertEqual(apn_configuration_avp.code, APN_CONFIGURATION_AVP_CODE)
        self.assertTrue(apn_configuration_avp.is_vendor_id())
        self.assertFalse(apn_configuration_avp.is_mandatory())
        self.assertFalse(apn_configuration_avp.is_protected())
        self.assertEqual(apn_configuration_avp.get_length(), 172)
        self.assertEqual(apn_configuration_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(apn_configuration_avp.data.hex(), "0000058f80000010000028af0000058f000001ed4000000b696d7300000005b080000010000028af000000020000059780000038000028af0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af000000080000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e8000000059880000010000028af00000000")
        self.assertIsNone(apn_configuration_avp.get_padding_length())
        self.assertEqual(apn_configuration_avp.__repr__(), "<Diameter AVP: 1430 [Apn-Configuration] VENDOR>")

        context_identifier_avp = apn_configuration_avp.context_identifier_avp
        service_selection_avp = apn_configuration_avp.service_selection_avp
        pdn_type_avp = apn_configuration_avp.pdn_type_avp
        eps_subscribed_qos_profile_avp = apn_configuration_avp.eps_subscribed_qos_profile_avp
        ambr_avp = apn_configuration_avp.ambr_avp
        vplmn_dynamic_address_allowed_avp = apn_configuration_avp.vplmn_dynamic_address_allowed_avp

        #: Non-3GPP-User-Data > APN-Configuration AVP > Context-Identifier AVP
        self.assertTrue(isinstance(context_identifier_avp, ContextIdentifierAVP))
        self.assertEqual(context_identifier_avp.code, CONTEXT_IDENTIFIER_AVP_CODE)
        self.assertTrue(context_identifier_avp.is_vendor_id())
        self.assertFalse(context_identifier_avp.is_mandatory())
        self.assertFalse(context_identifier_avp.is_protected())
        self.assertEqual(context_identifier_avp.get_length(), 16)
        self.assertEqual(context_identifier_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(context_identifier_avp.data.hex(), "0000058f")
        self.assertIsNone(context_identifier_avp.get_padding_length())
        self.assertEqual(context_identifier_avp.__repr__(), "<Diameter AVP: 1423 [Context-Identifier] VENDOR>")

        #: Non-3GPP-User-Data > APN-Configuration AVP > Service-Selection AVP
        self.assertTrue(isinstance(service_selection_avp, ServiceSelectionAVP))
        self.assertEqual(service_selection_avp.code, SERVICE_SELECTION_AVP_CODE)
        self.assertFalse(service_selection_avp.is_vendor_id())
        self.assertTrue(service_selection_avp.is_mandatory())
        self.assertFalse(service_selection_avp.is_protected())
        self.assertEqual(service_selection_avp.get_length(), 11)
        self.assertIsNone(service_selection_avp.vendor_id)
        self.assertEqual(service_selection_avp.data, b"ims")
        self.assertEqual(service_selection_avp.get_padding_length(), 1)
        self.assertEqual(service_selection_avp.__repr__(), "<Diameter AVP: 493 [Service-Selection] MANDATORY>")

        #: Non-3GPP-User-Data > APN-Configuration AVP > PDN-Type AVP
        self.assertTrue(isinstance(pdn_type_avp, PdnTypeAVP))
        self.assertEqual(pdn_type_avp.code, PDN_TYPE_AVP_CODE)
        self.assertTrue(pdn_type_avp.is_vendor_id())
        self.assertFalse(pdn_type_avp.is_mandatory())
        self.assertFalse(pdn_type_avp.is_protected())
        self.assertEqual(pdn_type_avp.get_length(), 16)
        self.assertEqual(pdn_type_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(pdn_type_avp.data, PDN_TYPE_IPV4V6)
        self.assertIsNone(pdn_type_avp.get_padding_length())
        self.assertEqual(pdn_type_avp.__repr__(), "<Diameter AVP: 1456 [Pdn-Type] VENDOR>")

        #: Non-3GPP-User-Data > APN-Configuration AVP > EPS-Subscribed-QoS-Profile AVP
        self.assertTrue(isinstance(eps_subscribed_qos_profile_avp, EpsSubscribedQosProfileAVP))
        self.assertEqual(eps_subscribed_qos_profile_avp.code, EPS_SUBSCRIBED_QOS_PROFILE_AVP_CODE)
        self.assertTrue(eps_subscribed_qos_profile_avp.is_vendor_id())
        self.assertFalse(eps_subscribed_qos_profile_avp.is_mandatory())
        self.assertFalse(eps_subscribed_qos_profile_avp.is_protected())
        self.assertEqual(eps_subscribed_qos_profile_avp.get_length(), 56)
        self.assertEqual(eps_subscribed_qos_profile_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(eps_subscribed_qos_profile_avp.data.hex(), "0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af00000008")
        self.assertIsNone(eps_subscribed_qos_profile_avp.get_padding_length())
        self.assertEqual(eps_subscribed_qos_profile_avp.__repr__(), "<Diameter AVP: 1431 [Eps-Subscribed-Qos-Profile] VENDOR>")

        qos_class_identifier_avp = eps_subscribed_qos_profile_avp.qos_class_identifier_avp
        allocation_retention_priority_avp = eps_subscribed_qos_profile_avp.allocation_retention_priority_avp

        #: Non-3GPP-User-Data > APN-Configuration AVP > EPS-Subscribed-QoS-Profile AVP > QoS-Class-Identifier AVP
        self.assertTrue(isinstance(qos_class_identifier_avp, QosClassIdentifierAVP))
        self.assertEqual(qos_class_identifier_avp.code, QOS_CLASS_IDENTIFIER_AVP_CODE)
        self.assertTrue(qos_class_identifier_avp.is_vendor_id())
        self.assertFalse(qos_class_identifier_avp.is_mandatory())
        self.assertFalse(qos_class_identifier_avp.is_protected())
        self.assertEqual(qos_class_identifier_avp.get_length(), 16)
        self.assertEqual(qos_class_identifier_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(qos_class_identifier_avp.data, QCI_5)
        self.assertIsNone(qos_class_identifier_avp.get_padding_length())
        self.assertEqual(qos_class_identifier_avp.__repr__(), "<Diameter AVP: 1028 [Qos-Class-Identifier] VENDOR>")

        #: Non-3GPP-User-Data > APN-Configuration AVP > EPS-Subscribed-QoS-Profile AVP > Allocation-Retention-Priority AVP
        self.assertTrue(isinstance(allocation_retention_priority_avp, AllocationRetentionPriorityAVP))
        self.assertEqual(allocation_retention_priority_avp.code, ALLOCATION_RETENTION_PRIORITY_AVP_CODE)
        self.assertTrue(allocation_retention_priority_avp.is_vendor_id())
        self.assertFalse(allocation_retention_priority_avp.is_mandatory())
        self.assertFalse(allocation_retention_priority_avp.is_protected())
        self.assertEqual(allocation_retention_priority_avp.get_length(), 28)
        self.assertEqual(allocation_retention_priority_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(allocation_retention_priority_avp.data.hex(), "0000041680000010000028af00000008")
        self.assertIsNone(allocation_retention_priority_avp.get_padding_length())
        self.assertEqual(allocation_retention_priority_avp.__repr__(), "<Diameter AVP: 1034 [Allocation-Retention-Priority] VENDOR>")

        priority_level_avp = allocation_retention_priority_avp.priority_level_avp

        #: Non-3GPP-User-Data > APN-Configuration AVP > EPS-Subscribed-QoS-Profile AVP > Allocation-Retention-Priority AVP > Priority-Level AVP
        self.assertTrue(isinstance(priority_level_avp, PriorityLevelAVP))
        self.assertEqual(priority_level_avp.code, PRIORITY_LEVEL_AVP_CODE)
        self.assertTrue(priority_level_avp.is_vendor_id())
        self.assertFalse(priority_level_avp.is_mandatory())
        self.assertFalse(priority_level_avp.is_protected())
        self.assertEqual(priority_level_avp.get_length(), 16)
        self.assertEqual(priority_level_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(priority_level_avp.data.hex(), "00000008")
        self.assertIsNone(priority_level_avp.get_padding_length())
        self.assertEqual(priority_level_avp.__repr__(), "<Diameter AVP: 1046 [Priority-Level] VENDOR>")

        #: Non-3GPP-User-Data > APN-Configuration AVP > AMBR AVP
        ambr_avp = apn_configuration_avp.ambr_avp

        self.assertTrue(isinstance(ambr_avp, AmbrAVP))
        self.assertEqual(ambr_avp.code, AMBR_AVP_CODE)
        self.assertTrue(ambr_avp.is_vendor_id())
        self.assertTrue(ambr_avp.is_mandatory())
        self.assertFalse(ambr_avp.is_protected())
        self.assertEqual(ambr_avp.get_length(), 44)
        self.assertEqual(ambr_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(ambr_avp.data.hex(), "00000203c0000010000028af0003e80000000204c0000010000028af0003e800")
        self.assertIsNone(ambr_avp.get_padding_length())
        self.assertEqual(ambr_avp.__repr__(), "<Diameter AVP: 1435 [Ambr] VENDOR, MANDATORY>")

        max_requested_bandwidth_dl_avp = ambr_avp.max_requested_bandwidth_dl_avp
        max_requested_bandwidth_ul_avp = ambr_avp.max_requested_bandwidth_ul_avp

        #: Non-3GPP-User-Data > APN-Configuration AVP > AMBR AVP > Max-Requested-Bandwidth-DL AVP
        self.assertTrue(isinstance(max_requested_bandwidth_dl_avp, MaxRequestedBandwidthDlAVP))
        self.assertEqual(max_requested_bandwidth_dl_avp.code, MAX_REQUESTED_BANDWIDTH_DL_AVP_CODE)
        self.assertTrue(max_requested_bandwidth_dl_avp.is_vendor_id())
        self.assertTrue(max_requested_bandwidth_dl_avp.is_mandatory())
        self.assertFalse(max_requested_bandwidth_dl_avp.is_protected())
        self.assertEqual(max_requested_bandwidth_dl_avp.get_length(), 16)
        self.assertEqual(max_requested_bandwidth_dl_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(max_requested_bandwidth_dl_avp.data.hex(), "0003e800")
        self.assertIsNone(max_requested_bandwidth_dl_avp.get_padding_length())
        self.assertEqual(max_requested_bandwidth_dl_avp.__repr__(), "<Diameter AVP: 515 [Max-Requested-Bandwidth-Dl] VENDOR, MANDATORY>")

        #: Non-3GPP-User-Data > APN-Configuration AVP > AMBR AVP > Max-Requested-Bandwidth-UL AVP
        self.assertTrue(isinstance(max_requested_bandwidth_ul_avp, MaxRequestedBandwidthUlAVP))
        self.assertEqual(max_requested_bandwidth_ul_avp.code, MAX_REQUESTED_BANDWIDTH_UL_AVP_CODE)
        self.assertTrue(max_requested_bandwidth_ul_avp.is_vendor_id())
        self.assertTrue(max_requested_bandwidth_ul_avp.is_mandatory())
        self.assertFalse(max_requested_bandwidth_ul_avp.is_protected())
        self.assertEqual(max_requested_bandwidth_ul_avp.get_length(), 16)
        self.assertEqual(max_requested_bandwidth_ul_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(max_requested_bandwidth_ul_avp.data.hex(), "0003e800")
        self.assertIsNone(max_requested_bandwidth_ul_avp.get_padding_length())
        self.assertEqual(max_requested_bandwidth_ul_avp.__repr__(), "<Diameter AVP: 516 [Max-Requested-Bandwidth-Ul] VENDOR, MANDATORY>")

        #: Non-3GPP-User-Data > APN-Configuration AVP > AMBR AVP > VPLMN-Dynamic-Address-Allowed AVP
        self.assertTrue(isinstance(vplmn_dynamic_address_allowed_avp, VplmnDynamicAddressAllowedAVP))
        self.assertEqual(vplmn_dynamic_address_allowed_avp.code, VPLMN_DYNAMIC_ADDRESS_ALLOWED_AVP_CODE)
        self.assertTrue(vplmn_dynamic_address_allowed_avp.is_vendor_id())
        self.assertFalse(vplmn_dynamic_address_allowed_avp.is_mandatory())
        self.assertFalse(vplmn_dynamic_address_allowed_avp.is_protected())
        self.assertEqual(vplmn_dynamic_address_allowed_avp.get_length(), 16)
        self.assertEqual(vplmn_dynamic_address_allowed_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(vplmn_dynamic_address_allowed_avp.data, VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED)
        self.assertIsNone(vplmn_dynamic_address_allowed_avp.get_padding_length())
        self.assertEqual(vplmn_dynamic_address_allowed_avp.__repr__(), "<Diameter AVP: 1432 [Vplmn-Dynamic-Address-Allowed] VENDOR>")

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


class TestNon3gppIpAccessAVP(unittest.TestCase):
    def test__non_3gpp_ip_access_avp__no_value(self):
        self.assertRaises(TypeError, Non3gppIpAccessAVP)

    def test__non_3gpp_ip_access_avp__repr_dunder(self):
        avp = Non3gppIpAccessAVP(NON_3GPP_SUBSCRIPTION_ALLOWED)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1501 [Non3gpp-Ip-Access] VENDOR, MANDATORY>")

    def test__non_3gpp_ip_access_avp__allowed(self):
        avp = Non3gppIpAccessAVP(NON_3GPP_SUBSCRIPTION_ALLOWED)
        ref = "000005ddc0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__non_3gpp_ip_access_avp__barred(self):
        avp = Non3gppIpAccessAVP(NON_3GPP_SUBSCRIPTION_BARRED)
        ref = "000005ddc0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestNon3gppIpAccessApnAVP(unittest.TestCase):
    def test__non_3gpp_ip_access_apn_avp__no_value(self):
        self.assertRaises(TypeError, Non3gppIpAccessApnAVP)

    def test__non_3gpp_ip_access_apn_avp__repr_dunder(self):
        avp = Non3gppIpAccessApnAVP(NON_3GPP_APNS_ENABLE)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1502 [Non3gpp-Ip-Access-Apn] VENDOR, MANDATORY>")

    def test__non_3gpp_ip_access_apn_avp__enable(self):
        avp = Non3gppIpAccessApnAVP(NON_3GPP_APNS_ENABLE)
        ref = "000005dec0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__non_3gpp_ip_access_apn_avp__disable(self):
        avp = Non3gppIpAccessApnAVP(NON_3GPP_APNS_DISABLE)
        ref = "000005dec0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestNon3gppUserDataAVP(unittest.TestCase):
    def test__non_3gpp_user_data_avp__no_value(self):
        self.assertRaises(TypeError, Non3gppUserDataAVP)

    def test__non_3gpp_user_data_avp__repr_dunder(self):
        avps = [
                 SubscriptionIdAVP([
                                        SubscriptionIdTypeAVP(END_USER_E164),
                                        SubscriptionIdDataAVP("5511123456789")
                 ]), 
                 Non3gppIpAccessAVP(NON_3GPP_SUBSCRIPTION_ALLOWED), 
                 Non3gppIpAccessApnAVP(NON_3GPP_APNS_ENABLE), 
                 AmbrAVP([
                                        MaxRequestedBandwidthDlAVP(256000),
                                        MaxRequestedBandwidthUlAVP(256000)
                 ]),
                 X3gppChargingCharacteristicsAVP("0B00"),
                 ContextIdentifierAVP(1),
                 ApnConfigurationAVP([
                                        ContextIdentifierAVP(1423),
                                        ServiceSelectionAVP("ims"),
                                        PdnTypeAVP(PDN_TYPE_IPV4V6),
                                        EpsSubscribedQosProfileAVP([
                                                                        QosClassIdentifierAVP(QCI_5),
                                                                        AllocationRetentionPriorityAVP([PriorityLevelAVP(8)])
                                        ]),
                                        AmbrAVP([
                                                    MaxRequestedBandwidthDlAVP(256000),
                                                    MaxRequestedBandwidthUlAVP(256000)
                                        ]),
                                        VplmnDynamicAddressAllowedAVP(VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED)
                 ])


        ]
        avp = Non3gppUserDataAVP(avps)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1500 [Non3gpp-User-Data] VENDOR, MANDATORY>")

    def test__non_3gpp_user_data_avp__1(self):
        avps = [
                 SubscriptionIdAVP([
                                        SubscriptionIdTypeAVP(END_USER_E164),
                                        SubscriptionIdDataAVP("5511123456789")
                 ]), 
                 Non3gppIpAccessAVP(NON_3GPP_SUBSCRIPTION_ALLOWED), 
                 Non3gppIpAccessApnAVP(NON_3GPP_APNS_ENABLE), 
                 AmbrAVP([
                                        MaxRequestedBandwidthDlAVP(256000),
                                        MaxRequestedBandwidthUlAVP(256000)
                 ]),
                 X3gppChargingCharacteristicsAVP("0B00"),
                 ContextIdentifierAVP(1),
                 ApnConfigurationAVP([
                                        ContextIdentifierAVP(1423),
                                        ServiceSelectionAVP("ims"),
                                        PdnTypeAVP(PDN_TYPE_IPV4V6),
                                        EpsSubscribedQosProfileAVP([
                                                                        QosClassIdentifierAVP(QCI_5),
                                                                        AllocationRetentionPriorityAVP([PriorityLevelAVP(8)])
                                        ]),
                                        AmbrAVP([
                                                    MaxRequestedBandwidthDlAVP(256000),
                                                    MaxRequestedBandwidthUlAVP(256000)
                                        ]),
                                        VplmnDynamicAddressAllowedAVP(VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED)
                 ])


        ]
        avp = Non3gppUserDataAVP(avps)

        ref = "000005dcc0000150000028af000001bb4000002c000001c24000000c00000000000001bc4000001535353131313233343536373839000000000005ddc0000010000028af00000000000005dec0000010000028af000000000000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e8000000000d80000010000028af304230300000058f80000010000028af0000000100000596800000ac000028af0000058f80000010000028af0000058f000001ed4000000b696d7300000005b080000010000028af000000020000059780000038000028af0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af000000080000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e8000000059880000010000028af00000000"
        
        self.maxDiff = None
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