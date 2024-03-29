# -*- coding: utf-8 -*-
"""
    tests.avps.etsi_3gpp.test_ts_129_273
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for ETSI TS 129 273.

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
from bromelia.avps.etsi_3gpp.ts_129_273 import *
from bromelia.avps.ietf.rfc4006 import *


class TestDiameterAVP(unittest.TestCase):
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

    def test_diameter_avp__load_staticmethod__parsing_mip6_feature_vector_avp_stream(self):
        stream = bytes.fromhex("0000007c400000100000400000000000")

        avps = DiameterAVP.load(stream)
        self.assertTrue(isinstance(avps[0], Mip6FeatureVectorAVP))    # it needs to be reviewed
        self.assertEqual(avps[0].code, MIP6_FEATURE_VECTOR_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, bytes.fromhex("0000400000000000"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 124 [Mip6-Feature-Vector] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_non_3gpp_ip_access_apn_avp_stream(self):
        pass

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
        self.assertEqual(avps[0].data.hex(), "000001bb4000002c000001c24000000c00000000000001bc4000001535353131313233343536373839000000000005ddc0000010000028af00000000000005dec0000010000028af000000000000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e8000000000d80000010000028af304230300000058f80000010000028af0000000100000596c00000ac000028af0000058f80000010000028af0000058f000001ed4000000b696d7300000005b080000010000028af0000000200000597c0000038000028af0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af000000080000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e80000000598c0000010000028af00000000")
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
        self.assertTrue(apn_configuration_avp.is_mandatory())
        self.assertFalse(apn_configuration_avp.is_protected())
        self.assertEqual(apn_configuration_avp.get_length(), 172)
        self.assertEqual(apn_configuration_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(apn_configuration_avp.data.hex(), "0000058f80000010000028af0000058f000001ed4000000b696d7300000005b080000010000028af0000000200000597c0000038000028af0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af000000080000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e80000000598c0000010000028af00000000")
        self.assertIsNone(apn_configuration_avp.get_padding_length())
        self.assertEqual(apn_configuration_avp.__repr__(), "<Diameter AVP: 1430 [Apn-Configuration] VENDOR, MANDATORY>")

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
        self.assertTrue(vplmn_dynamic_address_allowed_avp.is_mandatory())
        self.assertFalse(vplmn_dynamic_address_allowed_avp.is_protected())
        self.assertEqual(vplmn_dynamic_address_allowed_avp.get_length(), 16)
        self.assertEqual(vplmn_dynamic_address_allowed_avp.vendor_id, VENDOR_ID_3GPP)
        self.assertEqual(vplmn_dynamic_address_allowed_avp.data, VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED)
        self.assertIsNone(vplmn_dynamic_address_allowed_avp.get_padding_length())
        self.assertEqual(vplmn_dynamic_address_allowed_avp.__repr__(), "<Diameter AVP: 1432 [Vplmn-Dynamic-Address-Allowed] VENDOR, MANDATORY>")

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

        
class TestMobileNodeIdentifierAVP(unittest.TestCase):
    def test_mobile_node_identifier_avp__no_value(self):
        self.assertRaises(TypeError, MobileNodeIdentifierAVP)

    def test_mobile_node_identifier_avp__repr_dunder(self):
        avp = MobileNodeIdentifierAVP("123456789012345@nai.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 506 [Mobile-Node-Identifier] MANDATORY>")

    def test_mobile_node_identifier_avp__diameter_avp_convert_classmethod(self):
        avp = MobileNodeIdentifierAVP("123456789012345@nai.epc.mncXXX.mccYYY.3gppnetwork.org")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_mobile_node_identifier_avp__256kbps(self):
        avp = MobileNodeIdentifierAVP("123456789012345@nai.epc.mncXXX.mccYYY.3gppnetwork.org")
        ref = "000001fa4000003d313233343536373839303132333435406e61692e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"
        self.assertEqual(avp.dump().hex(), ref)


class TestNon3gppIpAccessAVP(unittest.TestCase):
    def test_non_3gpp_ip_access_avp__no_value(self):
        self.assertRaises(TypeError, Non3gppIpAccessAVP)

    def test_non_3gpp_ip_access_avp__repr_dunder(self):
        avp = Non3gppIpAccessAVP(NON_3GPP_SUBSCRIPTION_ALLOWED)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1501 [Non3gpp-Ip-Access] VENDOR, MANDATORY>")

    def test_non_3gpp_ip_access_avp__diameter_avp_convert_classmethod(self):
        avp = Non3gppIpAccessAVP(NON_3GPP_SUBSCRIPTION_ALLOWED)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_non_3gpp_ip_access_avp__non_3gpp_subscription_allowed(self):
        avp = Non3gppIpAccessAVP(NON_3GPP_SUBSCRIPTION_ALLOWED)
        ref = "000005ddc0000010000028af00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_non_3gpp_ip_access_avp__non_3gpp_subscription_barred(self):
        avp = Non3gppIpAccessAVP(NON_3GPP_SUBSCRIPTION_BARRED)
        ref = "000005ddc0000010000028af00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestMip6FeatureVectorAVP(unittest.TestCase):
    def test__mip6_feature_vector_avp__no_value(self):
        self.assertRaises(TypeError, Mip6FeatureVectorAVP)

    def test__mip6_feature_vector_avp__repr_dunder(self):
        value = bytes.fromhex("0000400000000000")
        avp = Mip6FeatureVectorAVP(value)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 124 [Mip6-Feature-Vector] MANDATORY>")

    def test__mip6_feature_vector_avp__diameter_avp_convert_classmethod(self):
        value = bytes.fromhex("0000400000000000")
        avp = Mip6FeatureVectorAVP(value)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test__mip6_feature_vector_avp__1(self):
        value = bytes.fromhex("0000400000000000")
        avp = Mip6FeatureVectorAVP(value)
        ref = "0000007c400000100000400000000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test__mip6_feature_vector_avp__2(self):
        avp = Mip6FeatureVectorAVP(70368744177664)
        ref = "0000007c400000100000400000000000"
        self.assertEqual(avp.dump().hex(), ref)
        

class TestNon3gppIpAccessApnAVP(unittest.TestCase):
    def test__non_3gpp_ip_access_apn_avp__no_value(self):
        self.assertRaises(TypeError, Non3gppIpAccessApnAVP)

    def test__non_3gpp_ip_access_apn_avp__repr_dunder(self):
        avp = Non3gppIpAccessApnAVP(NON_3GPP_APNS_ENABLE)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1502 [Non3gpp-Ip-Access-Apn] VENDOR, MANDATORY>")

    def test__non_3gpp_ip_access_apn_avp__diameter_avp_convert_classmethod(self):
        avp = Non3gppIpAccessApnAVP(NON_3GPP_APNS_ENABLE)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

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

    def test__non_3gpp_user_data_avp__diameter_avp_convert_classmethod(self):
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

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

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

        ref = "000005dcc0000150000028af000001bb4000002c000001c24000000c00000000000001bc4000001535353131313233343536373839000000000005ddc0000010000028af00000000000005dec0000010000028af000000000000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e8000000000d80000010000028af304230300000058f80000010000028af0000000100000596c00000ac000028af0000058f80000010000028af0000058f000001ed4000000b696d7300000005b080000010000028af0000000200000597c0000038000028af0000040480000010000028af000000050000040a8000001c000028af0000041680000010000028af000000080000059bc000002c000028af00000203c0000010000028af0003e80000000204c0000010000028af0003e80000000598c0000010000028af00000000"        
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


if __name__ == "__main__":
    unittest.main()