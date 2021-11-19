# -*- coding: utf-8 -*-
"""
    tests.avps.etsi_3gpp.test_ts_129_272
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for ETSI TS 129 272.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(testing_dir))

sys.path.insert(0, base_dir)

from bromelia.avps.etsi_3gpp.ts_129_272 import *
from bromelia.avps.ietf.rfc6733 import *
from bromelia.avps.ietf.rfc5447 import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_stn_sr_avp_stream(self):
        pass

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

    def test_diameter_avp__load_staticmethod__parsing_subscriber_status_avp_stream(self):
       pass

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

    def test_diameter_avp__load_staticmethod__parsing_allocation_retention_priority_avp_stream(self):
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

    def test_diameter_avp__load_staticmethod__parsing_eps_subscribed_qos_profile_avp_stream(self):
        stream = bytes.fromhex("0000059780000038000028af0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af00000008")
        
        avps = DiameterAVP.load(stream)

        #: Non-3GPP-User-Data > APN-Configuration AVP > EPS-Subscribed-QoS-Profile AVP
        self.assertTrue(isinstance(avps[0], EpsSubscribedQosProfileAVP))
        self.assertEqual(avps[0].code, EPS_SUBSCRIBED_QOS_PROFILE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 56)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af00000008")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1431 [Eps-Subscribed-Qos-Profile] VENDOR, MANDATORY>")

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
        stream = bytes.fromhex("00000598c0000010000028af00000000")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], VplmnDynamicAddressAllowedAVP))
        self.assertEqual(avps[0].code, VPLMN_DYNAMIC_ADDRESS_ALLOWED_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1432 [Vplmn-Dynamic-Address-Allowed] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_pdn_gw_allocation_type_avp_stream(self):
        stream = bytes.fromhex("0000059e80000010000028af00000000")
        
        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], PdnGwAllocationTypeAVP))
        self.assertEqual(avps[0].code, PDN_GW_ALLOCATION_TYPE_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data, PDN_GW_ALLOCATION_TYPE_STATIC)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1438 [Pdn-Gw-Allocation-Type] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_apn_configuration_avp_stream(self):
        stream = bytes.fromhex("00000596800000ac000028af0000058f80000010000028af0000058f000001ed4000000b696d7300000005b080000010000028af000000020000059780000038000028af0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af000000080000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e8000000059880000010000028af00000000")

        avps = DiameterAVP.load(stream)

        #: Non-3GPP-User-Data > APN-Configuration AVP
        self.assertTrue(isinstance(avps[0], ApnConfigurationAVP))
        self.assertEqual(avps[0].code, APN_CONFIGURATION_AVP_CODE)
        self.assertTrue(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 172)
        self.assertEqual(avps[0].vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(avps[0].data.hex(), "0000058f80000010000028af0000058f000001ed4000000b696d7300000005b080000010000028af0000000200000597c0000038000028af0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af000000080000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e80000000598c0000010000028af00000000")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1430 [Apn-Configuration] VENDOR, MANDATORY>")

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
        self.assertTrue(eps_subscribed_qos_profile_avp.is_mandatory())
        self.assertFalse(eps_subscribed_qos_profile_avp.is_protected())
        self.assertEqual(eps_subscribed_qos_profile_avp.get_length(), 56)
        self.assertEqual(eps_subscribed_qos_profile_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(eps_subscribed_qos_profile_avp.data.hex(), "0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af00000008")
        self.assertIsNone(eps_subscribed_qos_profile_avp.get_padding_length())
        self.assertEqual(eps_subscribed_qos_profile_avp.__repr__(), "<Diameter AVP: 1431 [Eps-Subscribed-Qos-Profile] VENDOR, MANDATORY>")

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
        self.assertTrue(vplmn_dynamic_address_allowed_avp.is_mandatory())
        self.assertFalse(vplmn_dynamic_address_allowed_avp.is_protected())
        self.assertEqual(vplmn_dynamic_address_allowed_avp.get_length(), 16)
        self.assertEqual(vplmn_dynamic_address_allowed_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(vplmn_dynamic_address_allowed_avp.data, VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED)
        self.assertIsNone(vplmn_dynamic_address_allowed_avp.get_padding_length())
        self.assertEqual(vplmn_dynamic_address_allowed_avp.__repr__(), "<Diameter AVP: 1432 [Vplmn-Dynamic-Address-Allowed] VENDOR, MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_all_apn_configurations_included_indicator_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_apn_configuration_profile_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_ue_usage_type_avp_stream(self):
        pass

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

    def test_diameter_avp__load_staticmethod__parsing_subscription_data_avp_stream(self):
        pass

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

    def test_diameter_avp__load_staticmethod__parsing_number_of_requested_vectors_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_re_synchronization_info_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_immediate_response_preferred_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_requested_eutran_authentication_info_avp_stream(self):
        pass

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

    def test_diameter_avp__load_staticmethod__parsing_equipment_status_avp_stream(self):
        pass

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

    def test_diameter_avp__load_staticmethod__parsing_ula_flags_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_air_flags_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_nor_flags_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_pur_flags_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_pua_flags_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_alert_reason_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_error_diagnostic_avp_stream(self):
        pass

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

    def test_diameter_avp__load_staticmethod__parsing_item_number_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_rand_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_xres_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_autn_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_kasme_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_e_utran_vector_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_authentication_info_avp_stream(self):
        pass

    def test_diameter_avp__load_staticmethod__parsing_homogeneous_support_of_ims_voice_over_ps_sessions_avp_stream(self):
        pass

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


class TestStnSrAVP(unittest.TestCase):
    pass


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


class TestSubscriberStatusAVP(unittest.TestCase):
    pass


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


class TestEpsSubscribedQosProfileAVP(unittest.TestCase):
    def test_eps_subscribed_qos_profile_avp__no_value(self):
        self.assertRaises(TypeError, EpsSubscribedQosProfileAVP)

    def test_eps_subscribed_qos_profile_avp__repr_dunder(self):
        avp = EpsSubscribedQosProfileAVP([
                                            AllocationRetentionPriorityAVP([PriorityLevelAVP(QCI_8)]), 
                                            QosClassIdentifierAVP(QCI_9)
        ])
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1431 [Eps-Subscribed-Qos-Profile] VENDOR, MANDATORY>")

    def test_eps_subscribed_qos_profile_avp__default(self):
        ref = "00000597c0000038000028af0000040a8000001c000028af0000041680000010000028af000000080000040480000010000028af00000009"
      
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
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1432 [Vplmn-Dynamic-Address-Allowed] VENDOR, MANDATORY>")

    def test_vplmn_dynamic_address_allowed_avp__not_allowed(self):
        avp = VplmnDynamicAddressAllowedAVP(VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED)
        ref = "00000598c0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_vplmn_dynamic_address_allowed_avp__allowed(self):
        avp = VplmnDynamicAddressAllowedAVP(VPLMN_DYNAMIC_ADDRESS_ALLOWED_ALLOWED)
        ref = "00000598c0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestPdnGwAllocationTypeAVP(unittest.TestCase):
    def test_pdn_gw_allocation_type_avp__no_value(self):
        self.assertRaises(TypeError, PdnGwAllocationTypeAVP)

    def test_pdn_gw_allocation_type_avp__repr_dunder(self):
        avp = PdnGwAllocationTypeAVP(PDN_GW_ALLOCATION_TYPE_STATIC)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1438 [Pdn-Gw-Allocation-Type] VENDOR, MANDATORY>")

    def test_pdn_gw_allocation_type_avp__static(self):
        avp = PdnGwAllocationTypeAVP(PDN_GW_ALLOCATION_TYPE_STATIC)
        ref = "0000059ec0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)
      
    def test_pdn_gw_allocation_type_avp__dynamic(self):
        avp = PdnGwAllocationTypeAVP(PDN_GW_ALLOCATION_TYPE_DYNAMIC)
        ref = "0000059ec0000010000028af00000001"
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
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1430 [Apn-Configuration] VENDOR, MANDATORY>")

    def test_apn_configuration_avp__default(self):
        ref = "00000596c0000038000028af0000058f80000010000028af00000003000005b080000010000028af00000000000001ed4000000c78636170"
          
        IDENTIFIER = convert_to_4_bytes(3)

        context_identifier_avp = ContextIdentifierAVP(IDENTIFIER)
        pdn__type_avp = PdnTypeAVP(PDN_TYPE_IPV4)
        service_selection_avp = ServiceSelectionAVP("xcap")

        avps = [context_identifier_avp, pdn__type_avp, service_selection_avp]

        avp = ApnConfigurationAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)

    def test_apn_configuration_avp__swm_interface(self):
        ref = "00000596c000014c000028af0000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e8000000059ec0000010000028af00000001000001e6400000900000015c400000880000011b400000296570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000000000012540000054746f706f6e2e73357067772e73616563697330342e6a616730312e73702e636e312e73756c2e6e6f64652e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000058f80000010000028af00000338000001ed4000000b696d730000000597c0000038000028af0000040a8000001c000028af0000041680000010000028af000000080000040480000010000028af00000005000005b080000010000028af0000000200000598c0000010000028af00000000"
          
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


class TestAllApnConfigurationsIncludedIndicatorAVP(unittest.TestCase):
    pass


class TestApnConfigurationProfileAVP(unittest.TestCase):
    pass


class TestUeUsageTypeAVP(unittest.TestCase):
    pass


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


class TestSubscriptionDataAVP(unittest.TestCase):
    pass


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


class TestNumberOfRequestedVectorsAVP(unittest.TestCase):
    pass


class TestReSynchronizationInfoAVP(unittest.TestCase):
    pass


class TestImmediateResponsePreferredAVP(unittest.TestCase):
    pass


class TestRequestedEutranAuthenticationInfoAVP(unittest.TestCase):
    pass


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


class TestEquipmentStatusAVP(unittest.TestCase):
    pass


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


class TestUlaFlagsAVP(unittest.TestCase):
    pass


class TestAirFlagsAVP(unittest.TestCase):
    pass


class TestNorFlagsAVP(unittest.TestCase):
    pass


class TestPurFlagsAVP(unittest.TestCase):
    pass


class TestPuaFlagsAVP(unittest.TestCase):
    pass


class TestAlertReasonAVP(unittest.TestCase):
    pass


class TestErrorDiagnosticAVP(unittest.TestCase):
    pass


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


class TestItemNumberAVP(unittest.TestCase):
    pass


class TestRandAVP(unittest.TestCase):
    pass


class TestXresAVP(unittest.TestCase):
    pass


class TestAutnAVP(unittest.TestCase):
    pass


class TestKasmeAVP(unittest.TestCase):
    pass


class TestEUtranVectorAVP(unittest.TestCase):
    pass


class TestAuthenticationInfoAVP(unittest.TestCase):
    pass


class TestHomogeneousSupportOfImsVoiceOverPsSessionsAVP(unittest.TestCase):
    pass


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