# -*- coding: utf-8 -*-
"""
    test.etsi_3gpp_swm.test_avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP unittests 
	for 3GPP SWm Diameter Application Id.
    
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

from bromelia.etsi_3gpp_swm.avps import *
from bromelia.etsi_3gpp_swm.definitions import *
from bromelia.etsi_3gpp_swx.avps import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_3gpp_charging_characteristics_avp_stream(self):
        stream = bytes.fromhex("0000000d80000010000028af30423030")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], X3gppChargingCharacteristicsAVP))
        self.assertEqual(avps[0].code, X_3GPP_CHARGING_CHARACTERISTICS_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "30423030")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 13 [X3gpp-Charging-Characteristics] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_service_selection_avp_stream(self):
        stream = bytes.fromhex("000001ed4000000b696d7300")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ServiceSelectionAVP))
        self.assertEqual(avps[0].code, SERVICE_SELECTION_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 11)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"ims")
        self.assertEqual(avps[0].get_padding_length(), 1)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 493 [Service-Selection] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_mobile_node_identifier_avp_stream(self):
        stream = bytes.fromhex("000001fa4000003d313233343536373839303132333435406e61692e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], MobileNodeIdentifierAVP))
        self.assertEqual(avps[0].code, MOBILE_NODE_IDENTIFIER_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 61)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"123456789012345@nai.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avps[0].get_padding_length(), 3)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 506 [Mobile-Node-Identifier] MANDATORY>")

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

    def test_diameter_avp__load_staticmethod__parsing_qos_class_identifier_avp_stream(self):
        stream = bytes.fromhex("0000040a8000001c000028af0000041680000010000028af00000008")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], AllocationRetentionPriorityAVP))
        self.assertEqual(avps[0].code, ALLOCATION_RETENTION_PRIORITY_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 28)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "0000041680000010000028af00000008")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1034 [Allocation-Retention-Priority] VENDOR>")

        priority_level_avp = avps[0].priority_level_avp
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

    def test_diameter_avp__load_staticmethod__parsing_context_identifier_avp_stream(self):
        stream = bytes.fromhex("0000058f80000010000028af00000001")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], ContextIdentifierAVP))
        self.assertEqual(avps[0].code, CONTEXT_IDENTIFIER_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "00000001")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1423 [Context-Identifier] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_apn_configuration_avp_stream(self):
        stream = bytes.fromhex("00000596800000ac000028af0000058f80000010000028af0000058f000001ed4000000b696d7300000005b080000010000028af000000020000059780000038000028af0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af000000080000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e8000000059880000010000028af00000000")

        avps = DiameterAVP.load(stream)

        #: Non-3GPP-User-Data > APN-Configuration AVP
        self.assertTrue(isinstance(avps[0], ApnConfigurationAVP))
        self.assertEqual(avps[0].code, APN_CONFIGURATION_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 172)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "0000058f80000010000028af0000058f000001ed4000000b696d7300000005b080000010000028af000000020000059780000038000028af0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af000000080000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e8000000059880000010000028af00000000")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1430 [Apn-Configuration] VENDOR>")

        context_identifier_avp = avps[0].context_identifier_avp
        service_selection_avp = avps[0].service_selection_avp
        pdn_type_avp = avps[0].pdn_type_avp
        eps_subscribed_qos_profile_avp = avps[0].eps_subscribed_qos_profile_avp
        ambr_avp = avps[0].ambr_avp
        vplmn_dynamic_address_allowed_avp = avps[0].vplmn_dynamic_address_allowed_avp

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
        ambr_avp = avps[0].ambr_avp

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

    def test_diameter_avp__load_staticmethod__parsing_eps_subscribed_qos_profile_avp_stream(self):
        stream = bytes.fromhex("0000059780000038000028af0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af00000008")
        
        avps = DiameterAVP.load(stream)

        #: Non-3GPP-User-Data > APN-Configuration AVP > EPS-Subscribed-QoS-Profile AVP
        self.assertTrue(isinstance(avps[0], EpsSubscribedQosProfileAVP))
        self.assertEqual(avps[0].code, EPS_SUBSCRIBED_QOS_PROFILE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 56)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af00000008")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1431 [Eps-Subscribed-Qos-Profile] VENDOR>")

        qos_class_identifier_avp = avps[0].qos_class_identifier_avp
        allocation_retention_priority_avp = avps[0].allocation_retention_priority_avp

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

    def test_diameter_avp__load_staticmethod__parsing_vplmn_dynamic_address_allowed_avp_stream(self):
        stream = bytes.fromhex("0000059880000010000028af00000000")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], VplmnDynamicAddressAllowedAVP))
        self.assertEqual(avps[0].code, VPLMN_DYNAMIC_ADDRESS_ALLOWED_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1432 [Vplmn-Dynamic-Address-Allowed] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_ambr_avp_stream(self):
        stream = bytes.fromhex("0000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e800")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], AmbrAVP))
        self.assertEqual(avps[0].code, AMBR_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 44)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "00000203c0000010000028af0003e80000000204c0000010000028af0003e800")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1435 [Ambr] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_pdn_gw_allocation_type_avp_stream(self):
        stream = bytes.fromhex("0000059e80000010000028af00000000")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], PdnGwAllocationTypeAVP))
        self.assertEqual(avps[0].code, PDN_GW_ALLOCATION_TYPE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, PDN_GW_ALLOCATION_TYPE_STATIC)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1438 [Pdn-Gw-Allocation-Type] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_pdn_type_avp_stream(self):
        stream = bytes.fromhex("000005b080000010000028af00000000")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], PdnTypeAVP))
        self.assertEqual(avps[0].code, PDN_TYPE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, PDN_TYPE_IPV4)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1456 [Pdn-Type] VENDOR>")

    def test_diameter_avp__load_staticmethod__parsing_non_3gpp_ip_access_avp_stream(self):
        stream = bytes.fromhex("000005dd80000010000028af00000000")
        
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


class TestX3gppChargingCharacteristicsAVP(unittest.TestCase):
    def test__3gpp_charging_characteristics_avp__no_value(self):
        self.assertRaises(TypeError, X3gppChargingCharacteristicsAVP)

    def test__3gpp_charging_characteristics_avp__repr_dunder(self):
        value = bytes.fromhex("30343030")                #: 0400
        avp = X3gppChargingCharacteristicsAVP(value)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 13 [X3gpp-Charging-Characteristics] VENDOR>")

    def test__3gpp_charging_characteristics_avp__1(self):
        value = bytes.fromhex("30343030")                #: 0400
        avp = X3gppChargingCharacteristicsAVP(value)
        ref = "0000000d80000010000028af30343030"
        self.assertEqual(avp.dump().hex(), ref)

    def test__3gpp_charging_characteristics_avp__2(self):
        value = bytes.fromhex("30323030")                #: 0200
        avp = X3gppChargingCharacteristicsAVP(value)
        ref = "0000000d80000010000028af30323030"
        self.assertEqual(avp.dump().hex(), ref)

    def test__3gpp_charging_characteristics_avp__3(self):
        value = bytes.fromhex("30353030")                #: 0500
        avp = X3gppChargingCharacteristicsAVP(value)
        ref = "0000000d80000010000028af30353030"
        self.assertEqual(avp.dump().hex(), ref)

    def test__3gpp_charging_characteristics_avp__4(self):
        value = bytes.fromhex("30383030")                #: 0800
        avp = X3gppChargingCharacteristicsAVP(value)
        ref = "0000000d80000010000028af30383030"
        self.assertEqual(avp.dump().hex(), ref)

    def test__3gpp_charging_characteristics_avp__5(self):
        value = bytes.fromhex("30413030")                #: 0A00
        avp = X3gppChargingCharacteristicsAVP(value)
        ref = "0000000d80000010000028af30413030"
        self.assertEqual(avp.dump().hex(), ref)

    def test__3gpp_charging_characteristics_avp__6(self):
        value = bytes.fromhex("30423030")                #: 0B00
        avp = X3gppChargingCharacteristicsAVP(value)
        ref = "0000000d80000010000028af30423030"
        self.assertEqual(avp.dump().hex(), ref)

    def test__3gpp_charging_characteristics_avp__7(self):
        value = bytes.fromhex("30453030")                #: 0E00
        avp = X3gppChargingCharacteristicsAVP(value)
        ref = "0000000d80000010000028af30453030"
        self.assertEqual(avp.dump().hex(), ref)


class TestServiceSelectionAVP(unittest.TestCase):
    def test_service_selection_avp__no_value(self):
        self.assertRaises(TypeError, ServiceSelectionAVP)

    def test_service_selection_avp__repr_dunder(self):
        avp = ServiceSelectionAVP("operator.com")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 493 [Service-Selection] MANDATORY>")

    def test_service_selection_avp__apn_1(self):
        avp = ServiceSelectionAVP("operator.com")
        ref = "000001ed400000146f70657261746f722e636f6d"
        self.assertEqual(avp.dump().hex(), ref)

    def test_service_selection_avp__apn_2(self):
        avp = ServiceSelectionAVP("mms.operator.com")
        ref = "000001ed400000186d6d732e6f70657261746f722e636f6d"
        self.assertEqual(avp.dump().hex(), ref)

    def test_service_selection_avp__apn_3(self):
        avp = ServiceSelectionAVP("internet.operator.com")
        ref = "000001ed4000001d696e7465726e65742e6f70657261746f722e636f6d000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_service_selection_avp__apn_4(self):
        avp = ServiceSelectionAVP("xcap")
        ref = "000001ed4000000c78636170"
        self.assertEqual(avp.dump().hex(), ref)

    def test_service_selection_avp__apn_5(self):
        avp = ServiceSelectionAVP("ims")
        ref = "000001ed4000000b696d7300"
        self.assertEqual(avp.dump().hex(), ref)


class TestMobileNodeIdentifierAVP(unittest.TestCase):
    def test_mobile_node_identifier_avp__no_value(self):
        self.assertRaises(TypeError, MobileNodeIdentifierAVP)

    def test_mobile_node_identifier_avp__repr_dunder(self):
        avp = MobileNodeIdentifierAVP("123456789012345@nai.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 506 [Mobile-Node-Identifier] MANDATORY>")

    def test_mobile_node_identifier_avp__256kbps(self):
        avp = MobileNodeIdentifierAVP("123456789012345@nai.epc.mncXXX.mccYYY.3gppnetwork.org")
        ref = "000001fa4000003d313233343536373839303132333435406e61692e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"
        self.assertEqual(avp.dump().hex(), ref)


class TestMaxRequestedBandwidthDlAVP(unittest.TestCase):
    def test_max_requested_bandwidth_dl_avp__no_value(self):
        self.assertRaises(TypeError, MaxRequestedBandwidthDlAVP)

    def test_max_requested_bandwidth_dl_avp__repr_dunder(self):
        MAX_DL = convert_to_4_bytes(256000)
        
        avp = MaxRequestedBandwidthDlAVP(MAX_DL)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 515 [Max-Requested-Bandwidth-Dl] VENDOR, MANDATORY>")

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
        MAX_DL = convert_to_4_bytes(256000)
        
        avp = MaxRequestedBandwidthUlAVP(MAX_DL)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 516 [Max-Requested-Bandwidth-Ul] VENDOR, MANDATORY>")

    def test_max_requested_bandwidth_ul_avp__256kbps(self):
        MAX_DL = convert_to_4_bytes(256000)

        avp = MaxRequestedBandwidthUlAVP(MAX_DL)
        ref = "00000204c0000010000028af0003e800"
        self.assertEqual(avp.dump().hex(), ref)

    def test_max_requested_bandwidth_ul_avp__999Mbps(self):
        MAX_DL = convert_to_4_bytes(999000000)

        avp = MaxRequestedBandwidthUlAVP(MAX_DL)
        ref = "00000204c0000010000028af3b8b87c0"
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


class TestQosClassIdentifierAVP(unittest.TestCase):
    def test_qos_class_identifier_avp__no_value(self):
        self.assertRaises(TypeError, QosClassIdentifierAVP)

    def test_qos_class_identifier_avp__repr_dunder(self):
        avp = QosClassIdentifierAVP(QCI_1)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1028 [Qos-Class-Identifier] VENDOR>")

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


class TestAllocationRetentionPriorityAVP(unittest.TestCase):
    def test_allocation_retention_priority_avp__no_value(self):
        self.assertRaises(TypeError, AllocationRetentionPriorityAVP)

    def test_allocation_retention_priority_avp__repr_dunder(self):
        avp = AllocationRetentionPriorityAVP([PriorityLevelAVP(QCI_8)])
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1034 [Allocation-Retention-Priority] VENDOR>")

    def test_allocation_retention_priority_avp__default(self):
        ref = "0000040a8000001c000028af0000041680000010000028af00000008"

        priority_level_avp = PriorityLevelAVP(QCI_8)

        avps = [priority_level_avp]
        avp = AllocationRetentionPriorityAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)

    def test_vendor_specific_application_id_avp__invalid_avp(self):
        vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)
        avps = [vendor_id_avp]

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp = AllocationRetentionPriorityAVP(avps)
        
        self.assertEqual(cm.exception.args[1], DIAMETER_MISSING_AVP)


class TestPriorityLevelAVP(unittest.TestCase):
    def test_priority_level_avp__no_value(self):
        self.assertRaises(TypeError, PriorityLevelAVP)

    def test_priority_level_avp__repr_dunder(self):
        avp = PriorityLevelAVP(convert_to_4_bytes(8))
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1046 [Priority-Level] VENDOR>")


    def test_priority_level_avp__8(self):
        value = convert_to_4_bytes(8)

        avp = PriorityLevelAVP(value)
        ref = "0000041680000010000028af00000008"
        self.assertEqual(avp.dump().hex(), ref)


class TestContextIdentifierAVP(unittest.TestCase):
    def test_context_identifier_avp__no_value(self):
        self.assertRaises(TypeError, ContextIdentifierAVP)

    def test_context_identifier_avp__repr_dunder(self):
        avp = ContextIdentifierAVP(convert_to_4_bytes(1))
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1423 [Context-Identifier] VENDOR>")

    def test_context_identifier_avp__value1(self):
        VALUE = convert_to_4_bytes(1)
        avp = ContextIdentifierAVP(VALUE)
        ref = "0000058f80000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_context_identifier_avp__value2(self):
        VALUE = convert_to_4_bytes(3)
        avp = ContextIdentifierAVP(VALUE)
        ref = "0000058f80000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test_context_identifier_avp__value3(self):
        VALUE = convert_to_4_bytes(4)
        avp = ContextIdentifierAVP(VALUE)
        ref = "0000058f80000010000028af00000004"
        self.assertEqual(avp.dump().hex(), ref)

    def test_context_identifier_avp__value4(self):
        VALUE = convert_to_4_bytes(824)
        avp = ContextIdentifierAVP(VALUE)
        ref = "0000058f80000010000028af00000338"
        self.assertEqual(avp.dump().hex(), ref)


class TestApnConfigurationAVP(unittest.TestCase):
    def test_apn_configuration_avp__no_value(self):
        self.assertRaises(TypeError, ApnConfigurationAVP)

    def test_apn_configuration_avp__repr_dunder(self):
        avp = ApnConfigurationAVP([
                                    ContextIdentifierAVP(convert_to_4_bytes(3)), 
                                    PdnTypeAVP(PDN_TYPE_IPV4), 
                                    ServiceSelectionAVP("xcap")
        ])
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1430 [Apn-Configuration] VENDOR>")

    def test_apn_configuration_avp__default(self):
        ref = "0000059680000038000028af0000058f80000010000028af00000003000005b080000010000028af00000000000001ed4000000c78636170"
          
        IDENTIFIER = convert_to_4_bytes(3)

        context_identifier_avp = ContextIdentifierAVP(IDENTIFIER)
        pdn__type_avp = PdnTypeAVP(PDN_TYPE_IPV4)
        service_selection_avp = ServiceSelectionAVP("xcap")

        avps = [context_identifier_avp, pdn__type_avp, service_selection_avp]

        avp = ApnConfigurationAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)

    def test_apn_configuration_avp__swm_interface(self):
        self.maxDiff = None
        ref = "000005968000014c000028af0000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e8000000059e80000010000028af00000001000001e6400000900000015c400000880000011b400000296570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000000000012540000054746f706f6e2e73357067772e73616563697330342e6a616730312e73702e636e312e73756c2e6e6f64652e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000058f80000010000028af00000338000001ed4000000b696d73000000059780000038000028af0000040a8000001c000028af0000041680000010000028af000000080000040480000010000028af00000005000005b080000010000028af000000020000059880000010000028af00000000"
          
        MAX_DL = convert_to_4_bytes(256000)
        max_requested_bw_dl_avp = MaxRequestedBandwidthDlAVP(MAX_DL)
        MAX_UL = convert_to_4_bytes(256000)
        max_requested_bw_ul_avp = MaxRequestedBandwidthUlAVP(MAX_UL)

        avps = [max_requested_bw_dl_avp, max_requested_bw_ul_avp]
        ambr_avp = AmbrAVP(avps)


        pdn_gw_allocation_type_avp = PdnGwAllocationTypeAVP(
                                            PDN_GW_ALLOCATION_TYPE_DYNAMIC)


        destination_realm_avp = DestinationRealmAVP("epc.mncXXX.mccYYY.3gppnetwork.org")
        destination_host_avp = DestinationHostAVP("topon.s5pgw.saecis04.jag01.sp.cn1.sul.node.epc.mncXXX.mccYYY.3gppnetwork.org")

        avps = [destination_realm_avp, destination_host_avp]
        mip_home_agent_host_avp = MipHomeAgentHostAVP(avps)

        avps = [mip_home_agent_host_avp]
        mip6_agent_info_avp = Mip6AgentInfoAVP(avps)   


        IDENTIFIER = convert_to_4_bytes(824)
        context_identifier_avp = ContextIdentifierAVP(IDENTIFIER)


        service_selection_avp = ServiceSelectionAVP("ims")


        priority_level_avp = PriorityLevelAVP(QCI_8)
        avps = [priority_level_avp]
        allocation_retention_priority_avp = AllocationRetentionPriorityAVP(
                                                                        avps)

        qos_class_identifier_avp = QosClassIdentifierAVP(QCI_5)

        avps = [allocation_retention_priority_avp, qos_class_identifier_avp]
        eps_subscribed_qos_profile_avp = EpsSubscribedQosProfileAVP(avps)


        pdn_type_avp = PdnTypeAVP(PDN_TYPE_IPV4V6)


        vplmn_dynamic_address_allowed_avp = VplmnDynamicAddressAllowedAVP(
                                    VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED)


        avps = [
                ambr_avp, 
                pdn_gw_allocation_type_avp,
                mip6_agent_info_avp,
                context_identifier_avp,
                service_selection_avp,
                eps_subscribed_qos_profile_avp,
                pdn_type_avp,
                vplmn_dynamic_address_allowed_avp
        ]
        avp = ApnConfigurationAVP(avps)

        self.assertEqual(avp.dump().hex()[:1000], ref[:1000])
        self.assertEqual(avp.dump().hex()[1000:], ref[1000:])


class TestEpsSubscribedQosProfileAVP(unittest.TestCase):
    def test_eps_subscribed_qos_profile_avp__no_value(self):
        self.assertRaises(TypeError, EpsSubscribedQosProfileAVP)

    def test_eps_subscribed_qos_profile_avp__repr_dunder(self):
        avp = EpsSubscribedQosProfileAVP([
                                            AllocationRetentionPriorityAVP([PriorityLevelAVP(QCI_8)]), 
                                            QosClassIdentifierAVP(QCI_9)
        ])
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1431 [Eps-Subscribed-Qos-Profile] VENDOR>")

    def test_eps_subscribed_qos_profile_avp__default(self):
        ref = "0000059780000038000028af0000040a8000001c000028af0000041680000010000028af000000080000040480000010000028af00000009"
      
        priority_level_avp = PriorityLevelAVP(QCI_8)
        avps1 = [priority_level_avp]
        allocation_ret_priority_avp = AllocationRetentionPriorityAVP(avps1)

        qos_class_identifier_avp = QosClassIdentifierAVP(QCI_9)

        avps = [allocation_ret_priority_avp, qos_class_identifier_avp]
        avp = EpsSubscribedQosProfileAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)

    def test_eps_subscribed_qos_profile_avp__invalid_avp(self):
        vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)
        avps = [vendor_id_avp]

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp = EpsSubscribedQosProfileAVP(avps)
        
        self.assertEqual(cm.exception.args[1], DIAMETER_MISSING_AVP)


class TestVplmnDynamicAddressAllowedAVP(unittest.TestCase):
    def test_vplmn_dynamic_address_allowed_avp__no_value(self):
        self.assertRaises(TypeError, VplmnDynamicAddressAllowedAVP)

    def test_eps_subscribed_qos_profile_avp__repr_dunder(self):
        avp = VplmnDynamicAddressAllowedAVP(VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1432 [Vplmn-Dynamic-Address-Allowed] VENDOR>")

    def test_vplmn_dynamic_address_allowed_avp__not_allowed(self):
        avp = VplmnDynamicAddressAllowedAVP(VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED)
        ref = "0000059880000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_vplmn_dynamic_address_allowed_avp__allowed(self):
        avp = VplmnDynamicAddressAllowedAVP(VPLMN_DYNAMIC_ADDRESS_ALLOWED_ALLOWED)
        ref = "0000059880000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestAmbrAVP(unittest.TestCase):
    def test_ambr_avp__no_value(self):
        self.assertRaises(TypeError, AmbrAVP)

    def test_ambr_avp__repr_dunder(self):
        avp = AmbrAVP([
                        MaxRequestedBandwidthDlAVP(convert_to_4_bytes(256000)), 
                        MaxRequestedBandwidthUlAVP(convert_to_4_bytes(256000))
        ])
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1435 [Ambr] VENDOR, MANDATORY>")

    def test_ambr_avp__default_1(self):
        MAX_DL = convert_to_4_bytes(256000)
        max_requested_bw_dl_avp = MaxRequestedBandwidthDlAVP(MAX_DL)
        MAX_UL = convert_to_4_bytes(256000)
        max_requested_bw_ul_avp = MaxRequestedBandwidthUlAVP(MAX_UL)

        avp = AmbrAVP([max_requested_bw_dl_avp, max_requested_bw_ul_avp])

        ref = "0000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e800"
        self.assertEqual(avp.dump().hex(), ref)
      
    def test_ambr_avp__default_2(self):
        MAX_DL = convert_to_4_bytes(999000000)
        max_requested_bw_dl_avp = MaxRequestedBandwidthDlAVP(MAX_DL)
        MAX_UL = convert_to_4_bytes(999000000)
        max_requested_bw_ul_avp = MaxRequestedBandwidthUlAVP(MAX_UL)

        avp = AmbrAVP([max_requested_bw_dl_avp, max_requested_bw_ul_avp])

        ref = "0000059bc000002c000028af00000203c0000010000028af3b8b87c000000204c0000010000028af3b8b87c0"
        self.assertEqual(avp.dump().hex(), ref)


class TestPdnGwAllocationTypeAVP(unittest.TestCase):
    def test_pdn_gw_allocation_type_avp__no_value(self):
        self.assertRaises(TypeError, PdnGwAllocationTypeAVP)

    def test_pdn_gw_allocation_type_avp__repr_dunder(self):
        avp = PdnGwAllocationTypeAVP(PDN_GW_ALLOCATION_TYPE_STATIC)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1438 [Pdn-Gw-Allocation-Type] VENDOR>")

    def test_pdn_gw_allocation_type_avp__static(self):
        avp = PdnGwAllocationTypeAVP(PDN_GW_ALLOCATION_TYPE_STATIC)
        ref = "0000059e80000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)
      
    def test_pdn_gw_allocation_type_avp__dynamic(self):
        avp = PdnGwAllocationTypeAVP(PDN_GW_ALLOCATION_TYPE_DYNAMIC)
        ref = "0000059e80000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestPdnTypeAVP(unittest.TestCase):
    def test_pdn_type_avp__no_value(self):
        self.assertRaises(TypeError, PdnTypeAVP)

    def test_pdn_type_avp__repr_dunder(self):
        avp = PdnTypeAVP(PDN_TYPE_IPV4)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1456 [Pdn-Type] VENDOR>")

    def test_pdn_type_avp__ipv4_only(self):
        avp = PdnTypeAVP(PDN_TYPE_IPV4)
        ref = "000005b080000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_pdn_type_avp__ipv6_only(self):
        avp = PdnTypeAVP(PDN_TYPE_IPV6)
        ref = "000005b080000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_pdn_type_avp__ipv4v6(self):
        avp = PdnTypeAVP(PDN_TYPE_IPV4V6)
        ref = "000005b080000010000028af00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_pdn_type_avp__ipv4_or_ipv6(self):
        avp = PdnTypeAVP(PDN_TYPE_IPV4_OR_IPV6)
        ref = "000005b080000010000028af00000003"
        self.assertEqual(avp.dump().hex(), ref)


class TestNon3gppIpAccessAVP(unittest.TestCase):
    def test_non_3gpp_ip_access_avp__no_value(self):
        self.assertRaises(TypeError, Non3gppIpAccessAVP)

    def test_non_3gpp_ip_access_avp__repr_dunder(self):
        avp = Non3gppIpAccessAVP(NON_3GPP_SUBSCRIPTION_ALLOWED)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1501 [Non3gpp-Ip-Access] VENDOR, MANDATORY>")

    def test_non_3gpp_ip_access_avp__non_3gpp_subscription_allowed(self):
        avp = Non3gppIpAccessAVP(NON_3GPP_SUBSCRIPTION_ALLOWED)
        ref = "000005ddc0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_non_3gpp_ip_access_avp__non_3gpp_subscription_barred(self):
        avp = Non3gppIpAccessAVP(NON_3GPP_SUBSCRIPTION_BARRED)
        ref = "000005ddc0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestUeLocalIpAddressAVP(unittest.TestCase):
    def test_ue_local_ip_address_avp__no_value(self):
        self.assertRaises(TypeError, UeLocalIpAddressAVP)

    def test_ue_local_ip_address_avp__repr_dunder(self):
        avp = UeLocalIpAddressAVP("127.0.0.1")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 2805 [Ue-Local-Ip-Address] VENDOR>")

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


if __name__ == "__main__":
    unittest.main()