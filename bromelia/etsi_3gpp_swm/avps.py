# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_swm.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP SWm Application Id.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..avps import Mip6AgentInfoAVP
from ..base import *
from ..constants import *
from ..types import *


class X3gppChargingCharacteristicsAVP(DiameterAVP, UTF8StringType):
    """Implementation of 3GPP-Charging-Characteristics AVP in Section 16.4.7.2 
    of ETSI TS 129 061 V10.11.0 (2014-10).

    The 3GPP-Charging-Characteristics AVP (AVP Code 13) is of type UTF8String.
    """
    code = X_3GPP_CHARGING_CHARACTERISTICS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             X3gppChargingCharacteristicsAVP.code,
                             X3gppChargingCharacteristicsAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ServiceSelectionAVP(DiameterAVP, UTF8StringType):
    """Implementation of Service-Selection AVP in Section 7.3.36
    of ETSI TS 129 272 V15.10.0 (2020-01).

    The Service-Selection AVP (AVP Code 493) is of type UTF8String.
    """
    code = SERVICE_SELECTION_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ServiceSelectionAVP.code,
                             ServiceSelectionAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


class MobileNodeIdentifierAVP(DiameterAVP, UTF8StringType):
    """Implementation of Mobile-Node-Identifier AVP in Section 5.2.3.2  
    of ETSI TS 129 273 V15.4.0 (2019-10).

    The Mobile-Node-Identifier AVP (AVP Code 506) is of type UTF8String.
    """
    code = MOBILE_NODE_IDENTIFIER_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             MobileNodeIdentifierAVP.code,
                             MobileNodeIdentifierAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


class MaxRequestedBandwidthDlAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Max-Requested-Bandwidth-DL AVP in Section 5.3.14 
    of ETSI TS 129 214 V15.4.0 (2018-07).

    The Max-Requested-Bandwidth-DL AVP (AVP Code 515) is of type Unsigned32.
    """
    code = MAX_REQUESTED_BANDWIDTH_DL_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             MaxRequestedBandwidthDlAVP.code,
                             MaxRequestedBandwidthDlAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class MaxRequestedBandwidthUlAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Max-Requested-Bandwidth-UL AVP in Section 5.3.15 
    of ETSI TS 129 214 V15.4.0 (2018-07).

    The Max-Requested-Bandwidth-UL AVP (AVP Code 516) is of type Unsigned32.
    """
    code = MAX_REQUESTED_BANDWIDTH_UL_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             MaxRequestedBandwidthUlAVP.code,
                             MaxRequestedBandwidthUlAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class VisitedNetworkIdentifierAVP(DiameterAVP, OctetStringType):
    """Implementation of Visited-Network-Identifier AVP in Section 6.3.1  
    of ETSI TS 129 229 V15.2.0 (2019-10).

    The Visited-Network-Identifier AVP (AVP Code 600) is of type OctetString.
    """
    code = VISITED_NETWORK_IDENTIFIER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             VisitedNetworkIdentifierAVP.code,
                             VisitedNetworkIdentifierAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class QosClassIdentifierAVP(DiameterAVP, EnumeratedType):
    """Implementation of QoS-Class-Identifier AVP in Section 5.3.17
    of ETSI TS 129 212 V12.6.0 (2014-10)

    The QoS-Class-Identifier AVP (AVP Code 1028) is of type Enumerated.
    """
    code = QOS_CLASS_IDENTIFIER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

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
        DiameterAVP.__init__(self, 
                             QosClassIdentifierAVP.code,
                             QosClassIdentifierAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class RatTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of RAT-Type AVP in Section 5.3.31 of 3GPP TS 29.212.

    The RAT-Type AVP (AVP code 1032) is of type Enumerated.
    """
    code = RAT_TYPE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

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
        DiameterAVP.__init__(self, 
                             RatTypeAVP.code,
                             RatTypeAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class PriorityLevelAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Priority-Level AVP in Section 5.3.45
    of ETSI TS 129 212 V12.6.0 (2014-10)

    The Priority-Level AVP (AVP Code 1406) is of type Unsigned32.
    """
    code = PRIORITY_LEVEL_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             PriorityLevelAVP.code,
                             PriorityLevelAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class PreEmptionCapabilityAVP(DiameterAVP, EnumeratedType):
    """Implementation of Pre-emption-Capability AVP in Section 5.3.46 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Pre-emption-Capability AVP (AVP code 1047) is of type Enumerated.
    """
    code = PRE_EMPTION_CAPABILITY_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                 PRE_EMPTION_CAPABILITY_ENABLED,
                 PRE_EMPTION_CAPABILITY_DISABLED,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             PreEmptionCapabilityAVP.code,
                             PreEmptionCapabilityAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class PreEmptionVulnerabilityAVP(DiameterAVP, EnumeratedType):
    """Implementation of Pre-emption-Capability AVP in Section 5.3.47 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Pre-emption-Capability AVP (AVP code 1048) is of type Enumerated.
    """
    code = PRE_EMPTION_VULNERABILITY_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                 PRE_EMPTION_VULNERABILITY_ENABLED,
                 PRE_EMPTION_VULNERABILITY_DISABLED,
     ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             PreEmptionVulnerabilityAVP.code,
                             PreEmptionVulnerabilityAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AllocationRetentionPriorityAVP(DiameterAVP, GroupedType):
    """Implementation of Allocation-Retention-Priority AVP in Section 7.3.40 
    of ETSI TS 129 272 V15.10.0 (2020-01).

    The Allocation-Retention-Priority AVP (AVP Code 1034) is of type Grouped.
    """
    code = ALLOCATION_RETENTION_PRIORITY_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "priority_level": PriorityLevelAVP
    }
    optionals = {
                    "pre_emption_capability": PreEmptionCapabilityAVP,
                    "pre_emption_vulnerability": PreEmptionVulnerabilityAVP

    }

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             AllocationRetentionPriorityAVP.code,
                             AllocationRetentionPriorityAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ContextIdentifierAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Context-Identifier AVP in Section 7.3.27
    of ETSI TS 129 272 V15.10.0 (2020-01).

    The Context-Identifier AVP (AVP Code 1423) is of type Unsigned32.
    """
    code = CONTEXT_IDENTIFIER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ContextIdentifierAVP.code,
                             ContextIdentifierAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class PdnTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of PDN-Type AVP in Section 7.3.62 of
    ETSI TS 129 272 V15.10.0 (2020-01).

    The PDN-Type AVP (AVP Code 1456) is of type Enumerated.
    """
    code = PDN_TYPE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                PDN_TYPE_IPV4,
                PDN_TYPE_IPV6,
                PDN_TYPE_IPV4V6,
                PDN_TYPE_IPV4_OR_IPV6
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             PdnTypeAVP.code,
                             PdnTypeAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)    
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class EpsSubscribedQosProfileAVP(DiameterAVP, GroupedType):
    """Implementation of EPS-Subscribed-QoS-Profile AVP in Section 7.3.37 
    of ETSI TS 129 272 V15.10.0 (2020-01)

    The EPS-Subscribed-QoS-Profile AVP (AVP Code 1431) is of type Grouped.
    """
    code = EPS_SUBSCRIBED_QOS_PROFILE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "qos_class_identifier": QosClassIdentifierAVP,
                    "allocation_retention_priority": AllocationRetentionPriorityAVP
    }
    optionals = {}

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             EpsSubscribedQosProfileAVP.code,
                             EpsSubscribedQosProfileAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class VplmnDynamicAddressAllowedAVP(DiameterAVP, EnumeratedType):
    """Implementation of VPLMN-Dynamic-Address-Allowed AVP in Section 7.3.38 
    of ETSI TS 129 272 V15.10.0 (2020-01).

    The VPLMN-Dynamic-Address-Allowed AVP (AVP Code 1432) is of type 
    Enumerated.
    """
    code = VPLMN_DYNAMIC_ADDRESS_ALLOWED_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED,
                VPLMN_DYNAMIC_ADDRESS_ALLOWED_ALLOWED
    ]


    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             VplmnDynamicAddressAllowedAVP.code,
                             VplmnDynamicAddressAllowedAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)    
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AmbrAVP(DiameterAVP, GroupedType):
    """Implementation of AMBR AVP in Section 7.3.41 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The AMBR AVP (AVP Code 1435) is of type Grouped.
    """
    code = AMBR_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "max_requested_bandwidth_ul": MaxRequestedBandwidthUlAVP,
                    "max_requested_bandwidth_dl": MaxRequestedBandwidthDlAVP,
    }
    optionals = {
                    # "extended_max_requested_bw_ul": ExtendedMaxRequestedBwUlAVP,
                    # "extended_max_requested_bw_dl": ExtendedMaxRequestedBwDlAVP,
    }

    def __init__(self, data):        
        DiameterAVP.__init__(self, 
                             AmbrAVP.code,
                             AmbrAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class PdnGwAllocationTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of PDN-GW-Allocation-Type AVP in Section 7.3.44 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The PDN-GW-Allocation-Type AVP (AVP Code 1438) is of type Enumerated.
    """
    code = PDN_GW_ALLOCATION_TYPE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                PDN_GW_ALLOCATION_TYPE_STATIC,
                PDN_GW_ALLOCATION_TYPE_DYNAMIC
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             PdnGwAllocationTypeAVP.code,
                             PdnGwAllocationTypeAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)    
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ApnConfigurationAVP(DiameterAVP, GroupedType):
    """Implementation of APN-Configuration AVP in Section 7.3.35 of
    ETSI TS 129 272 V15.10.0 (2020-01).

    The APN-Configuration AVP (AVP Code 1430) is of type Grouped.
    """
    code = APN_CONFIGURATION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "context_identifier": ContextIdentifierAVP,
                    "pdn_type": PdnTypeAVP,
                    "service_selection": ServiceSelectionAVP,
    }
    optionals = {
                    "eps_subscribed_qos_profile": EpsSubscribedQosProfileAVP,
                    "vplmn_dynamic_address_allowed": VplmnDynamicAddressAllowedAVP,
                    "mip6_agent_info": Mip6AgentInfoAVP,
                    "visited_network_identifier": VisitedNetworkIdentifierAVP,
                    "pdn_gw_allocation_type": PdnGwAllocationTypeAVP,
                    "x3gpp_charging_characteristics": X3gppChargingCharacteristicsAVP,
                    "ambr": AmbrAVP,
                    # "specific_apn_info": SpecificApnInfoAVP,
                    # "apn_oi_replacement": ApnOiReplacementAVP,
                    # "sipto_permission": SiptoPermissionAVP,
                    # "lipa_permission": LipaPermissionAVP,
                    # "restoration_priority": RestorationPriorityAVP,
                    # "sipto_local_network_permission": SiptoLocalNetworkPermissionAVP,
                    # "wlan_offloadability": WlanOffloadabilityAVP,
                    # "non_ip_pdn_type_indicator": NonIpPdnTypeIndicatorAVP,
                    # "non_ip_data_delivery_mechanism": NonIpDataDeliveryMechanismAVP,
                    # "scef_id": ScefIdAVP,
                    # "scef_realm": ScefRealmAVP,
                    # "preferred_data_mode": PreferredDataModeAVP,
                    # "pdn_connectivity_continuity": PdnConnectivityContinuityAVP,
                    # "rds_indicator": RdsIndicatorAVP,
    }

    def __init__(self, data):        
        DiameterAVP.__init__(self, 
                             ApnConfigurationAVP.code,
                             ApnConfigurationAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class Non3gppIpAccessAVP(DiameterAVP, EnumeratedType):
    """Implementation of Non-3GPP-IP-Access AVP in Section 8.2.3.3 
    of ETSI TS 129 273 V14.5.0 (2019-10).

    The Non-3GPP-IP-Access AVP (AVP Code 1501) is of type Enumerated.
    """
    code = NON_3GPP_IP_ACCESS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                NON_3GPP_SUBSCRIPTION_ALLOWED,
                NON_3GPP_SUBSCRIPTION_BARRED
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             Non3gppIpAccessAVP.code,
                             Non3gppIpAccessAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)    
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class UeLocalIpAddressAVP(DiameterAVP, AddressType):
    """Implementation of UE-Local-IP-Address AVP AVP in Section 5.3.5 of 
    ETSI TS 129 212 V15.9.0 (2020-01).

    The UE-Local-IP-Address AVP AVP (AVP Code 2805) is of type Address.
    """
    code = UE_LOCAL_IP_ADDRESS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             UeLocalIpAddressAVP.code,
                             UeLocalIpAddressAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)        
        AddressType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)