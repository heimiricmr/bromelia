# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_swm.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP SWm Application Id.
    
    :copyright: (c) 2020 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import base64

from ..avps import *
from ..constants import *
from ..exceptions import AVPAttributeValueError
from ..types import *


class X3gppChargingCharacteristicsAVP(DiameterAVP, UTF8StringType):
    """Implementation of 3GPP-Charging-Characteristics AVP in Section 16.4.7.2 
    of ETSI TS 129 061 V10.11.0 (2014-10).

    The 3GPP-Charging-Characteristics AVP (AVP Code 13) is of type UTF8String.
    """
    code = X_3GPP_CHARGING_CHARACTERISTICS_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, X3gppChargingCharacteristicsAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ServiceSelectionAVP(DiameterAVP, UTF8StringType):
    """Implementation of Service-Selection AVP in Section 7.3.36
    of ETSI TS 129 272 V15.10.0 (2020-01).

    The Service-Selection AVP (AVP Code 493) is of type UTF8String.
    """
    code = SERVICE_SELECTION_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, ServiceSelectionAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


class MobileNodeIdentifierAVP(DiameterAVP, UTF8StringType):
    """Implementation of Mobile-Node-Identifier AVP in Section 5.2.3.2  
    of ETSI TS 129 273 V15.4.0 (2019-10).

    The Mobile-Node-Identifier AVP (AVP Code 506) is of type UTF8String.
    """
    code = MOBILE_NODE_IDENTIFIER_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, MobileNodeIdentifierAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


class MaxRequestedBandwidthDlAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Max-Requested-Bandwidth-DL AVP in Section 5.3.14 
    of ETSI TS 129 214 V15.4.0 (2018-07).

    The Max-Requested-Bandwidth-DL AVP (AVP Code 515) is of type Unsigned32.
    """
    code = MAX_REQUESTED_BANDWIDTH_DL_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, MaxRequestedBandwidthDlAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class MaxRequestedBandwidthUlAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Max-Requested-Bandwidth-UL AVP in Section 5.3.15 
    of ETSI TS 129 214 V15.4.0 (2018-07).

    The Max-Requested-Bandwidth-UL AVP (AVP Code 516) is of type Unsigned32.
    """
    code = MAX_REQUESTED_BANDWIDTH_UL_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, MaxRequestedBandwidthUlAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class VisitedNetworkIdentifierAVP(DiameterAVP, OctetStringType):
    """Implementation of Visited-Network-Identifier AVP in Section 6.3.1  
    of ETSI TS 129 229 V15.2.0 (2019-10).

    The Visited-Network-Identifier AVP (AVP Code 600) is of type OctetString.
    """
    code = VISITED_NETWORK_IDENTIFIER_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, VisitedNetworkIdentifierAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class QosClassIdentifierAVP(DiameterAVP, EnumeratedType):
    """Implementation of QoS-Class-Identifier AVP in Section 5.3.17
    of ETSI TS 129 212 V12.6.0 (2014-10)

    The QoS-Class-Identifier AVP (AVP Code 1028) is of type Enumerated.
    """
    code = QOS_CLASS_IDENTIFIER_AVP_CODE

    values = [
                QCI_1,
                QCI_2,
                QCI_3,
                QCI_4,
                QCI_5,
                QCI_6,
                QCI_7,
                QCI_8,
                QCI_9,
                QCI_65,
                QCI_66,
                QCI_69,
                QCI_70
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, QosClassIdentifierAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class RatTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of RAT-Type AVP in Section 5.3.31 of 3GPP TS 29.212.

    The RAT-Type AVP (AVP code 1032) is of type Enumerated.
    """
    code = RAT_TYPE_AVP_CODE

    values = [
                 RAT_TYPE_WLAN,
                 RAT_TYPE_VIRTUAL,
                 RAT_TYPE_UTRAN,
                 RAT_TYPE_GERAN,
                 RAT_TYPE_GAN,
                 RAT_TYPE_HSPA_EVOLUTION,
                 RAT_TYPE_EUTRAN,
                 RAT_TYPE_CDMA2000_1X,
                 RAT_TYPE_HRPD,
                 RAT_TYPE_UMB,
                 RAT_TYPE_EHRPD
     ]

    def __init__(self, data):
        DiameterAVP.__init__(self, RatTypeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AllocationRetentionPriorityAVP(DiameterAVP, GroupedType):
    """Implementation of Allocation-Retention-Priority AVP in Section 7.3.40 
    of ETSI TS 129 272 V15.10.0 (2020-01).

    The Allocation-Retention-Priority AVP (AVP Code 1034) is of type Grouped.
    """
    code = ALLOCATION_RETENTION_PRIORITY_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self)
        self.code = AllocationRetentionPriorityAVP.code
        DiameterAVP.set_vendor_id_bit(self, True)

        if isinstance(data, bytes):
            data = DiameterAVP.load(data)
            self.avps = data

        if not isinstance(data, list):
                raise DataTypeError("GroupedType MUST have data argument "\
                                "of 'list'")

        self.data = b""

        mandatory_avps_count = 0
        secondary_avps_count = 0
        for avp in data:
            if isinstance(avp, PriorityLevelAVP):
                self.priority_level_avp = avp
                self.data += avp.dump()
                mandatory_avps_count += 1


        if mandatory_avps_count == 0:
            raise AVPAttributeValueError("invalid input argument for "\
                                    "AllocationRetentionPriorityAVP. It "\
                                    "MUST contain one PriorityLevelAVP "\
                                    "object",
                                    DIAMETER_MISSING_AVP)

        if mandatory_avps_count > 1:
            raise AVPAttributeValueError("invalid input argument for "\
                                    "AllocationRetentionPriorityAVP. It "\
                                    "MUST contain only one PriorityLevelAVP "\
                                    "object",
                                    DIAMETER_AVP_OCCURS_TOO_MANY_TIMES)

        GroupedType.__init__(self, data=self.data, vendor_id=VENDOR_ID_3GPP)


class PriorityLevelAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Priority-Level AVP in Section 5.3.45
    of ETSI TS 129 212 V12.6.0 (2014-10)

    The Priority-Level AVP (AVP Code 1406) is of type Unsigned32.
    """
    code = PRIORITY_LEVEL_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, PriorityLevelAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self,data=data, vendor_id=VENDOR_ID_3GPP)


class ContextIdentifierAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Context-Identifier AVP in Section 7.3.27
    of ETSI TS 129 272 V15.10.0 (2020-01).

    The Context-Identifier AVP (AVP Code 1423) is of type Unsigned32.
    """
    code = CONTEXT_IDENTIFIER_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, ContextIdentifierAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ApnConfigurationAVP(DiameterAVP, GroupedType):
    """Implementation of APN-Configuration AVP in Section 7.3.35 of
    ETSI TS 129 272 V15.10.0 (2020-01).

    The APN-Configuration AVP (AVP Code 1430) is of type Grouped.
    """
    code = APN_CONFIGURATION_AVP_CODE

    def __init__(self, data):        
        DiameterAVP.__init__(self, ApnConfigurationAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)

        if isinstance(data, bytes):
            data = DiameterAVP.load(data)
            self.avps = data

        if not isinstance(data, list):
            raise DataTypeError("GroupedType MUST have data argument "\
                                "of 'list'")

        self.data = b""

        mandatory_avps_count = 0
        secondary_avps_count = 0
        for avp in data:
            if isinstance(avp, DiameterAVP):
                self.data += avp.dump()
            else:
                raise AVPAttributeValueError("TO DO")

            if isinstance(avp, ContextIdentifierAVP):
                self.context_identifier_avp = avp
                mandatory_avps_count += 1

            elif isinstance(avp, PdnTypeAVP):
                self.pdn__type_avp = avp
                mandatory_avps_count += 1
            
            elif isinstance(avp, ServiceSelectionAVP):
                self.service_selection_avp = avp
                mandatory_avps_count += 1
            
            elif isinstance(avp, EpsSubscribedQosProfileAVP):
                self.eps_subscribed_qos_profile_avp = avp
                secondary_avps_count += 1

            elif isinstance(avp, Mip6AgentInfoAVP):
                self.mip6_agent_info_avp = avp
                secondary_avps_count += 1

            elif isinstance(avp, VplmnDynamicAddressAllowedAVP):
                self.vplmn_dynamic_address_allowed_avp = avp
                secondary_avps_count += 1

            elif isinstance(avp, PdnGwAllocationTypeAVP):
                self.pdn_gw_allocation_type_avp = avp
                secondary_avps_count += 1
            
            elif isinstance(avp, AmbrAVP):
                self.ambr_avp = avp
                secondary_avps_count += 1

        if mandatory_avps_count < 3:
            raise AVPAttributeValueError("invalid input argument for "\
                                    "ApnConfigurationAVP. It MUST contain "\
                                    "one ContextIdentifierAVP object, one "\
                                    "PdnTypeAVP object and one "\
                                    "ServiceSelectionAVP object",
                                    DIAMETER_MISSING_AVP)

        if mandatory_avps_count > 3:
            raise AVPAttributeValueError("invalid input argument for "\
                                    "ApnConfigurationAVP. It MUST contain "\
                                    "only one ContextIdentifierAVP object, "\
                                    "only one PdnTypeAVP object and only "\
                                    "one ServiceSelectionAVP object",
                                    DIAMETER_AVP_OCCURS_TOO_MANY_TIMES)

        GroupedType.__init__(self, data=self.data, vendor_id=VENDOR_ID_3GPP)


class EpsSubscribedQosProfileAVP(DiameterAVP, GroupedType):
    """Implementation of EPS-Subscribed-QoS-Profile AVP in Section 7.3.37 
    of ETSI TS 129 272 V15.10.0 (2020-01)

    The EPS-Subscribed-QoS-Profile AVP (AVP Code 1431) is of type Grouped.
    """
    code = EPS_SUBSCRIBED_QOS_PROFILE_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, EpsSubscribedQosProfileAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)

        if isinstance(data, bytes):
            data = DiameterAVP.load(data)
            self.avps = data

        if not isinstance(data, list):
                raise DataTypeError("GroupedType MUST have data argument "\
                                "of 'list'")

        self.data = b""

        qos_class_id_count = 0
        allocation_retention_priority_count = 0
        for avp in data:
            if isinstance(avp, QosClassIdentifierAVP):
                self.priority_level_avp = avp
                self.data += avp.dump()
                qos_class_id_count += 1

            elif isinstance(avp, AllocationRetentionPriorityAVP):
                self.priority_level_avp = avp
                self.data += avp.dump()
                allocation_retention_priority_count += 1


        if qos_class_id_count == 0 or allocation_retention_priority_count == 0:
            raise AVPAttributeValueError("invalid input argument for "\
                                    "EpsSubscribedQosProfileAVP. It "\
                                    "MUST contain one QosClassIdentifierAVP "\
                                    "object and one "\
                                    "AllocationRetentionPriorityAVP object",
                                    DIAMETER_MISSING_AVP)

        if qos_class_id_count > 1 or allocation_retention_priority_count > 1:
            raise AVPAttributeValueError("invalid input argument for "\
                                    "EpsSubscribedQosProfileAVP. It "\
                                    "MUST contain only one "\
                                    "QosClassIdentifierAVP object and only "\
                                    "one AllocationRetentionPriorityAVP "\
                                    "object",
                                    DIAMETER_AVP_OCCURS_TOO_MANY_TIMES)

        GroupedType.__init__(self, data=self.data, vendor_id=VENDOR_ID_3GPP)


class VplmnDynamicAddressAllowedAVP(DiameterAVP, EnumeratedType):
    """Implementation of VPLMN-Dynamic-Address-Allowed AVP in Section 7.3.38 
    of ETSI TS 129 272 V15.10.0 (2020-01).

    The VPLMN-Dynamic-Address-Allowed AVP (AVP Code 1432) is of type 
    Enumerated.
    """
    code = VPLMN_DYNAMIC_ADDRESS_ALLOWED_AVP_CODE

    values = [
                VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED,
                VPLMN_DYNAMIC_ADDRESS_ALLOWED_ALLOWED
    ]


    def __init__(self, data):
        DiameterAVP.__init__(self, VplmnDynamicAddressAllowedAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)    
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AmbrAVP(DiameterAVP, GroupedType):
    """Implementation of AMBR AVP in Section 7.3.41 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The AMBR AVP (AVP Code 1435) is of type Grouped.
    """
    code = AMBR_AVP_CODE

    def __init__(self, data):        
        DiameterAVP.__init__(self, AmbrAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)

        if isinstance(data, bytes):
            data = DiameterAVP.load(data)
            self.avps = data

        if not isinstance(data, list):
            raise DataTypeError("GroupedType MUST have data argument "\
                                "of 'list'")

        self.data = b""

        mandatory_avps_count = 0
        secondary_avps_count = 0
        for avp in data:
            if isinstance(avp, MaxRequestedBandwidthUlAVP):
                self.max_requested_bandwidth_ul_avp = avp
                self.data += avp.dump()
                mandatory_avps_count += 1

            elif isinstance(avp, MaxRequestedBandwidthDlAVP):
                self.max_requested_bandwidth_dl_avp = avp
                self.data += avp.dump()
                mandatory_avps_count += 1
        
        if mandatory_avps_count == 0:
            raise AVPAttributeValueError("invalid input argument for "\
                                    "AmbrAVP. It MUST contain one "\
                                    "MaxRequestedBandwidthUlAVP object and "\
                                    "one MaxRequestedBandwidthDlAVP object",
                                    DIAMETER_MISSING_AVP)

        if mandatory_avps_count > 2:
            raise AVPAttributeValueError("invalid input argument for "\
                                    "AmbrAVP. It MUST contain only one "
                                    "MaxRequestedBandwidthUlAVP object and "\
                                    "only one MaxRequestedBandwidthDlAVP "\
                                    "object",
                                    DIAMETER_AVP_OCCURS_TOO_MANY_TIMES)

        GroupedType.__init__(self, data=self.data, vendor_id=VENDOR_ID_3GPP)


class PdnGwAllocationTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of PDN-GW-Allocation-Type AVP in Section 7.3.44 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The PDN-GW-Allocation-Type AVP (AVP Code 1438) is of type Enumerated.
    """
    code = PDN_GW_ALLOCATION_TYPE_AVP_CODE

    values = [
                PDN_GW_ALLOCATION_TYPE_STATIC,
                PDN_GW_ALLOCATION_TYPE_DYNAMIC
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, PdnGwAllocationTypeAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)    
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class PdnTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of PDN-Type AVP in Section 7.3.62 of
    ETSI TS 129 272 V15.10.0 (2020-01).

    The PDN-Type AVP (AVP Code 1456) is of type Enumerated.
    """
    code = PDN_TYPE_AVP_CODE

    values = [
                PDN_TYPE_IPV4,
                PDN_TYPE_IPV6,
                PDN_TYPE_IPV4V6,
                PDN_TYPE_IPV4_OR_IPV6
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, PdnTypeAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)    
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class Non3gppIpAccessAVP(DiameterAVP, EnumeratedType):
    """Implementation of Non-3GPP-IP-Access AVP in Section 8.2.3.3 
    of ETSI TS 129 273 V14.5.0 (2019-10).

    The Non-3GPP-IP-Access AVP (AVP Code 1501) is of type Enumerated.
    """
    code = NON_3GPP_IP_ACCESS_AVP_CODE

    values = [
                NON_3GPP_SUBSCRIPTION_ALLOWED,
                NON_3GPP_SUBSCRIPTION_BARRED
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, Non3gppIpAccessAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)    
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class UeLocalIpAddressAVP(DiameterAVP, AddressType):
    """Implementation of UE-Local-IP-Address AVP AVP in Section 5.3.5 of 
    ETSI TS 129 212 V15.9.0 (2020-01).

    The UE-Local-IP-Address AVP AVP (AVP Code 2805) is of type Address.
    """
    code = UE_LOCAL_IP_ADDRESS_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, UeLocalIpAddressAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)        
        AddressType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)