# -*- coding: utf-8 -*-
"""
    test.etsi_3gpp_rx.test_avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP unittests 
	for 3GPP Rx Diameter Application Id.
    
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

from bromelia.etsi_3gpp_rx.avps import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_framed_ip_address_avp_stream(self):
        stream = bytes.fromhex("000000084000000c0a2d000c")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], FramedIpAddressAVP))
        self.assertEqual(avps[0].code, FRAMED_IP_ADDRESS_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, bytes.fromhex("0a2d000c"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 8 [Framed-Ip-Address] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_called_station_id_avp_stream(self):
        stream = bytes.fromhex("0000001e4000000931000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], CalledStationIdAVP))
        self.assertEqual(avps[0].code, CALLED_STATION_ID_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 9)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"1")
        self.assertEqual(avps[0].get_padding_length(), 3)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 30 [Called-Station-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_framed_ipv6_prefix_avp_stream(self):
        stream = bytes.fromhex("000000614000001a0080280403886010041200b1d8508280babe0000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], FramedIpv6PrefixAVP))
        self.assertEqual(avps[0].code, FRAMED_IPV6_PREFIX_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 26)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, bytes.fromhex("0080280403886010041200b1d8508280babe"))
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 97 [Framed-Ipv6-Prefix] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_authorization_life_time_avp_stream(self):
        stream = bytes.fromhex("000001234000000c00001c20")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], AuthorizationLifetimeAVP))
        self.assertEqual(avps[0].code, AUTHORIZATION_LIFETIME_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, bytes.fromhex("00001c20"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 291 [Authorization-Lifetime] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_subscription_id_data_avp_stream(self):
        stream = bytes.fromhex("000001bc4000001535353131313233343536373839000000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], SubscriptionIdDataAVP))
        self.assertEqual(avps[0].code, SUBSCRIPTION_ID_DATA_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 21)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"5511123456789")
        self.assertEqual(avps[0].get_padding_length(), 3)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 444 [Subscription-Id-Data] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_subscription_id_type_avp_stream(self):
        stream = bytes.fromhex("000001c24000000c00000001")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], SubscriptionIdTypeAVP))
        self.assertEqual(avps[0].code, SUBSCRIPTION_ID_TYPE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, END_USER_IMSI)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 450 [Subscription-Id-Type] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_reservation_priority_avp_stream(self):
        stream = bytes.fromhex("000001ca80000010000032db00000005")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ReservationPriorityAVP))
        self.assertEqual(avps[0].code, RESERVATION_PRIORITY_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_ETSI)
        self.assertEqual(avps[0].data, PRIORITY_FIVE)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 458 [Reservation-Priority] VENDOR>")

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

    def test_diameter_avp__load_staticmethod__parsing_max_requested_bandwidth_dl_avp_stream(self):
        stream = bytes.fromhex("00000203c0000010000028af00000400")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], MaxRequestedBandwidthDlAVP))
        self.assertEqual(avps[0].code, MAX_REQUESTED_BANDWIDTH_DL_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("00000400"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 515 [Max-Requested-Bandwidth-Dl] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_max_requested_bandwidth_ul_avp_stream(self):
        stream = bytes.fromhex("00000204c0000010000028af00000400")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], MaxRequestedBandwidthUlAVP))
        self.assertEqual(avps[0].code, MAX_REQUESTED_BANDWIDTH_UL_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("00000400"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 516 [Max-Requested-Bandwidth-Ul] VENDOR, MANDATORY>")

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
        stream = bytes.fromhex("00000208c0000010000028af00000007")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], MediaTypeAVP))
        self.assertEqual(avps[0].code, MEDIA_TYPE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, MEDIA_TYPE_OTHER)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 520 [Media-Type] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_service_info_status_avp_stream(self):
        stream = bytes.fromhex("0000020fc0000010000028af00000001")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ServiceInfoStatusAVP))
        self.assertEqual(avps[0].code, SERVICE_INFO_STATUS_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, SERVICE_INFO_STATUS_PRELIMINARY_SERVICE_INFORMATION)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 527 [Service-Info-Status] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_supported_features_avp_stream(self):
        pass

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

    def test_diameter_avp__load_staticmethod__parsing_an_trusted_avp_stream(self):
        stream = bytes.fromhex("000005dfc0000010000028af00000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], AnTrustedAVP))
        self.assertEqual(avps[0].code, AN_TRUSTED_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, AN_TRUSTED_TRUSTED)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1503 [An-Trusted] VENDOR, MANDATORY>")

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

    def test_diameter_avp__load_staticmethod__parsing_ue_local_ip_address_avp_stream(self):
        stream = bytes.fromhex("00000af580000012000028af00010a2d00010000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], UeLocalIpAddressAVP))
        self.assertEqual(avps[0].code, UE_LOCAL_IP_ADDRESS_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 18)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, bytes.fromhex("00010a2d0001"))
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 2805 [Ue-Local-Ip-Address] VENDOR>")


class TestFramedIpAddressAVP(unittest.TestCase):
    def test__framed_ip_address_avp__no_value(self):
        self.assertRaises(TypeError, FramedIpAddressAVP)

    def test__framed_ip_address_avp__repr_dunder(self):
        value = bytes.fromhex("0a2d0012")
        avp = FramedIpAddressAVP(value)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 8 [Framed-Ip-Address] MANDATORY>")

    def test__framed_ip_address_avp__diameter_avp_convert_classmethod(self):
        value = bytes.fromhex("0a2d0012")
        avp = FramedIpAddressAVP(value)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__framed_ip_address_avp__1(self):
        value = bytes.fromhex("0a2d000c")
        avp = FramedIpAddressAVP(value)
        ref = "000000084000000c0a2d000c"
        self.assertEqual(avp.dump().hex(), ref)

    def test__framed_ip_address_avp__2(self):
        avp = FramedIpAddressAVP("10.45.0.12")
        ref = "000000084000000c0a2d000c"
        self.assertEqual(avp.dump().hex(), ref)


class TestCalledStationIdAVP(unittest.TestCase):
    def test__called_station_id_avp__no_value(self):
        self.assertRaises(TypeError, CalledStationIdAVP)

    def test__called_station_id_avp__repr_dunder(self):
        avp = CalledStationIdAVP("1")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 30 [Called-Station-Id] MANDATORY>")

    def test__called_station_id_avp__diameter_avp_convert_classmethod(self):
        avp = CalledStationIdAVP("1")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__called_station_id_avp__1(self):
        avp = CalledStationIdAVP("1")
        ref = "0000001e4000000931000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__called_station_id_avp__2(self):
        avp = CalledStationIdAVP("2")
        ref = "0000001e4000000932000000"
        self.assertEqual(avp.dump().hex(), ref)


class TestFramedIpv6PrefixAVP(unittest.TestCase):
    def test__framed_ipv6_prefix_avp__no_value(self):
        self.assertRaises(TypeError, FramedIpv6PrefixAVP)

    def test__framed_ipv6_prefix_avp__repr_dunder(self):
        avp = FramedIpv6PrefixAVP(bytes.fromhex("0080280403886010041200b1d8508280babe"))
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 97 [Framed-Ipv6-Prefix] MANDATORY>")

    def test__framed_ipv6_prefix_avp__diameter_avp_convert_classmethod(self):
        avp = FramedIpv6PrefixAVP(bytes.fromhex("0080280403886010041200b1d8508280babe"))

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__framed_ipv6_prefix_avp__1(self):
        avp = FramedIpv6PrefixAVP(bytes.fromhex("0080280403886010041200b1d8508280babe"))
        ref = "000000614000001a0080280403886010041200b1d8508280babe0000"
        self.assertEqual(avp.dump().hex(), ref)


class TestAuthorizationLifetimeAVP(unittest.TestCase):
    def test__authorization_life_time_avp__no_value(self):
        self.assertRaises(TypeError, AuthorizationLifetimeAVP)

    def test__authorization_life_time_avp__repr_dunder(self):
        avp = AuthorizationLifetimeAVP(7200)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 291 [Authorization-Lifetime] MANDATORY>")

    def test__authorization_life_time_avp__diameter_avp_convert_classmethod(self):
        avp = AuthorizationLifetimeAVP(7200)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__authorization_life_time_avp__1(self):
        avp = AuthorizationLifetimeAVP(7200)
        ref = "000001234000000c00001c20"
        self.assertEqual(avp.dump().hex(), ref)


class TestSubscriptionIdDataAVP(unittest.TestCase):
    def test_subscription_id_data_avp__no_value(self):
        self.assertRaises(TypeError, SubscriptionIdDataAVP)

    def test_subscription_id_data_avp__repr_dunder(self):
        avp = SubscriptionIdDataAVP("5522123456789")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 444 [Subscription-Id-Data] MANDATORY>")

    def test_subscription_id_data_avp__diameter_avp_convert_classmethod(self):
        avp = SubscriptionIdDataAVP("5511123456789")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_subscription_id_data_avp__1(self):
        avp = SubscriptionIdDataAVP("5511123456789")
        ref = "000001bc4000001535353131313233343536373839000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_subscription_id_data_avp__2(self):
        avp = SubscriptionIdDataAVP("5522123456789")
        ref = "000001bc4000001535353232313233343536373839000000"
        self.assertEqual(avp.dump().hex(), ref)
      

class TestSubscriptionIdTypeAVP(unittest.TestCase):
    def test_subscription_id_type_avp__no_value(self):
        self.assertRaises(TypeError, SubscriptionIdTypeAVP)

    def test_subscription_id_type_avp__repr_dunder(self):
        avp = SubscriptionIdTypeAVP(END_USER_E164)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 450 [Subscription-Id-Type] MANDATORY>")

    def test_subscription_id_type_avp__diameter_avp_convert_classmethod(self):
        avp = SubscriptionIdTypeAVP(END_USER_PRIVATE)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_subscription_id_type_avp__end_user_e164(self):
        avp = SubscriptionIdTypeAVP(END_USER_E164)
        ref = "000001c24000000c00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_subscription_id_type_avp__end_user_imsi(self):
        avp = SubscriptionIdTypeAVP(END_USER_IMSI)
        ref = "000001c24000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_subscription_id_type_avp__end_user_sip_uri(self):
        avp = SubscriptionIdTypeAVP(END_USER_SIP_URI)
        ref = "000001c24000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_subscription_id_type_avp__end_user_nai(self):
        avp = SubscriptionIdTypeAVP(END_USER_NAI)
        ref = "000001c24000000c00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test_subscription_id_type_avp__end_user_private(self):
        avp = SubscriptionIdTypeAVP(END_USER_PRIVATE)
        ref = "000001c24000000c00000004"
        self.assertEqual(avp.dump().hex(), ref)


class TestReservationPriorityAVP(unittest.TestCase):
    def test__reservation_priority_avp__no_value(self):
        avp = ReservationPriorityAVP()

    def test__reservation_priority_avp__repr_dunder(self):
        avp = ReservationPriorityAVP()
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 458 [Reservation-Priority] VENDOR>")

    def test__reservation_priority_avp__diameter_avp_convert_classmethod(self):
        avp = ReservationPriorityAVP()

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__reservation_priority_avp__1(self):
        avp = ReservationPriorityAVP()
        ref = "000001ca80000010000032db00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reservation_priority_avp__2(self):
        avp = ReservationPriorityAVP(PRIORITY_ONE)
        ref = "000001ca80000010000032db00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reservation_priority_avp__3(self):
        avp = ReservationPriorityAVP(PRIORITY_TWO)
        ref = "000001ca80000010000032db00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reservation_priority_avp__4(self):
        avp = ReservationPriorityAVP(PRIORITY_THREE)
        ref = "000001ca80000010000032db00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reservation_priority_avp__5(self):
        avp = ReservationPriorityAVP(PRIORITY_FOUR)
        ref = "000001ca80000010000032db00000004"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reservation_priority_avp__6(self):
        avp = ReservationPriorityAVP(PRIORITY_FIVE)
        ref = "000001ca80000010000032db00000005"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reservation_priority_avp__7(self):
        avp = ReservationPriorityAVP(PRIORITY_SIX)
        ref = "000001ca80000010000032db00000006"
        self.assertEqual(avp.dump().hex(), ref)

    def test__reservation_priority_avp__8(self):
        avp = ReservationPriorityAVP(PRIORITY_SEVEN)
        ref = "000001ca80000010000032db00000007"
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


class TestMaxRequestedBandwidthDlAVP(unittest.TestCase):
    def test__max_requested_bandwidth_dl_avp__no_value(self):
        self.assertRaises(TypeError, MaxRequestedBandwidthDlAVP)

    def test__max_requested_bandwidth_dl_avp__repr_dunder(self):
        avp = MaxRequestedBandwidthDlAVP(256)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 515 [Max-Requested-Bandwidth-Dl] VENDOR, MANDATORY>")

    def test__max_requested_bandwidth_dl_avp__diameter_avp_convert_classmethod(self):
        avp = MaxRequestedBandwidthDlAVP(256)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__max_requested_bandwidth_dl_avp__1(self):
        avp = MaxRequestedBandwidthDlAVP(256)
        ref = "00000203c0000010000028af00000100"
        self.assertEqual(avp.dump().hex(), ref)

    def test__max_requested_bandwidth_dl_avp__2(self):
        avp = MaxRequestedBandwidthDlAVP(1024)
        ref = "00000203c0000010000028af00000400"
        self.assertEqual(avp.dump().hex(), ref)


class TestMaxRequestedBandwidthUlAVPAVP(unittest.TestCase):
    def test__max_requested_bandwidth_ul_avp__no_value(self):
        self.assertRaises(TypeError, MaxRequestedBandwidthUlAVP)

    def test__max_requested_bandwidth_ul_avp__repr_dunder(self):
        avp = MaxRequestedBandwidthUlAVP(256)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 516 [Max-Requested-Bandwidth-Ul] VENDOR, MANDATORY>")

    def test__max_requested_bandwidth_ul_avp__diameter_avp_convert_classmethod(self):
        avp = MaxRequestedBandwidthUlAVP(256)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__max_requested_bandwidth_ul_avp__1(self):
        avp = MaxRequestedBandwidthUlAVP(256)
        ref = "00000204c0000010000028af00000100"
        self.assertEqual(avp.dump().hex(), ref)

    def test__max_requested_bandwidth_ul_avp__2(self):
        avp = MaxRequestedBandwidthUlAVP(1024)
        ref = "00000204c0000010000028af00000400"
        self.assertEqual(avp.dump().hex(), ref)


class TestMediaComponentDescriptionAVP(unittest.TestCase):
    pass


class TestMediaComponentNumberAVPAVP(unittest.TestCase):
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


class TestSupportedFeaturesAVP(unittest.TestCase):
    pass


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


class TestRatTypeAVP(unittest.TestCase):
    def test_rat_type_avp__no_value(self):
        self.assertRaises(TypeError, RatTypeAVP)

    def test_rat_type_avp__repr_dunder(self):
        avp = RatTypeAVP(RAT_TYPE_WLAN)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1032 [Rat-Type] VENDOR, MANDATORY>")

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


class TestAnTrustedAVP(unittest.TestCase):
    def test__an_trusted_avp__no_value(self):
        self.assertRaises(TypeError, AnTrustedAVP)

    def test__an_trusted_avp__repr_dunder(self):
        avp = AnTrustedAVP(AN_TRUSTED_TRUSTED)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1503 [An-Trusted] VENDOR, MANDATORY>")

    def test__an_trusted_avp__diameter_avp_convert_classmethod(self):
        avp = AnTrustedAVP(AN_TRUSTED_TRUSTED)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__an_trusted_avp__1(self):
        avp = AnTrustedAVP(AN_TRUSTED_TRUSTED)
        ref = "000005dfc0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__an_trusted_avp__2(self):
        avp = AnTrustedAVP(AN_TRUSTED_UNTRUSTED)
        ref = "000005dfc0000010000028af00000001"
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


class TestUeLocalIpAddressAVP(unittest.TestCase):
    def test__ue_local_ip_address_avp__no_value(self):
        self.assertRaises(TypeError, UeLocalIpAddressAVP)

    def test__ue_local_ip_address_avp__repr_dunder(self):
        avp = UeLocalIpAddressAVP("10.45.0.1")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 2805 [Ue-Local-Ip-Address] VENDOR>")

    def test__ue_local_ip_address_avp__diameter_avp_convert_classmethod(self):
        avp = UeLocalIpAddressAVP("10.45.0.1")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__ue_local_ip_address_avp__1(self):
        avp = UeLocalIpAddressAVP("10.45.0.1")
        ref = "00000af580000012000028af00010a2d00010000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__ue_local_ip_address_avp__2(self):
        avp = UeLocalIpAddressAVP("10.45.0.2")
        ref = "00000af580000012000028af00010a2d00020000"
        self.assertEqual(avp.dump().hex(), ref)
