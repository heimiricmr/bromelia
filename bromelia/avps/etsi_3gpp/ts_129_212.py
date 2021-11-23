# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp.ts_129_212
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in ETSI TS 129 212.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ...base import DiameterAVP
from ...constants.etsi_3gpp.ts_129_212 import *
from ...types import *


class PriorityLevelAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Priority-Level AVP in Section 5.3.45
    of ETSI TS 129 212 V12.6.0 (2014-10).

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
    """Implementation of Pre-emption-Vulnerability AVP in Section 5.3.47 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Pre-emption-Vulnerability AVP (AVP code 1048) is of type Enumerated.
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


class QosClassIdentifierAVP(DiameterAVP, EnumeratedType):
    """Implementation of QoS-Class-Identifier AVP in Section 5.3.17
    of ETSI TS 129 212 V15.3.0 (2018-07).

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
                QCI_70,
                QCI_75,
                QCI_79,
                QCI_80,
                QCI_82,
                QCI_83,
                QCI_84,
                QCI_85,
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


class PrecedenceAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Precedence AVP in Section 5.3.11 of
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Precedence AVP (AVP Code 1010) is of type Unsigned32.
    """
    code = PRECEDENCE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             PrecedenceAVP.code,
                             PrecedenceAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ReportingLevelAVP(DiameterAVP, EnumeratedType):
    """Implementation of Reporting-Level AVP in Section 5.3.12 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Reporting-Level AVP (AVP Code 1011) is of type Enumerated.
    """
    code = REPORTING_LEVEL_AVP_CODE
    vendor_id = VENDOR_ID_3GPP
  
    values = [
                REPORTING_LEVEL_SERVICE_IDENTIFIER_LEVEL,
                REPORTING_LEVEL_RATING_GROUP_LEVEL,
                REPORTING_LEVEL_SPONSORED_CONNECTIVITY_LEVEL,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ReportingLevelAVP.code,
                             ReportingLevelAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class IpCanTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of IP-CAN-Type AVP in Section 5.3.27 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The IP-CAN-Type AVP (AVP Code 1027) is of type Enumerated.
    """
    code = IP_CAN_TYPE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP
 
    values = [
                IP_CAN_TYPE_3GPP_GPRS,
                IP_CAN_TYPE_DOCSIS,
                IP_CAN_TYPE_XDSL,
                IP_CAN_TYPE_WIMAX,
                IP_CAN_TYPE_3GPP2,
                IP_CAN_TYPE_3GPP_EPS,
                IP_CAN_TYPE_NON_3GPP_EPS,
                IP_CAN_TYPE_FBA,
                IP_CAN_TYPE_3GPP_5GS,
                IP_CAN_TYPE_NON_3GPP_5GS,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             IpCanTypeAVP.code,
                             IpCanTypeAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AnGwAddressAVP(DiameterAVP, AddressType):
    """Implementation of AN-GW-Address AVP in Section 5.3.49 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The AN-GW-Address AVP (AVP Code 1050) is of type Address.
    """
    code = AN_GW_ADDRESS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AnGwAddressAVP.code,
                             AnGwAddressAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        AddressType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ChargingCorrelationIndicatorAVP(DiameterAVP, EnumeratedType):
    """Implementation of Charging-Correlation-Indicator AVP in Section 5.3.67 of
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Charging-Correlation-Indicator AVP (AVP Code 1073) is of type Enumerated.
    """
    code = CHARGING_CORRELATION_INDICATOR_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                CHARGING_CORRELATION_INDICATOR_CHARGING_IDENTIFIER_REQUIRED,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ChargingCorrelationIndicatorAVP.code,
                             ChargingCorrelationIndicatorAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class BearerUsageAVP(DiameterAVP, EnumeratedType):
    """Implementation of Bearer-Usage AVP in Section 5.3.1 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Bearer-Usage AVP (AVP Code 1000) is of type Enumerated.
    """
    code = BEARER_USAGE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                BEARER_USAGE_GENERAL,
                BEARER_USAGE_SIGNALLING,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             BearerUsageAVP.code,
                             BearerUsageAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ChargingRuleInstallAVP(DiameterAVP, GroupedType):
    """Implementation of Charging-Rule-Install AVP in Section 5.3.2 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Charging-Rule-Install AVP (AVP Code 1001) is of type Grouped.
    """
    code = CHARGING_RULE_INSTALL_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ChargingRuleInstallAVP.code,
                             ChargingRuleInstallAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ChargingRuleDefinitionAVP(DiameterAVP, GroupedType):
    """Implementation of Charging-Rule-Definition AVP in Section 5.3.4 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Charging-Rule-Definition AVP (AVP Code 1003) is of type Grouped.
    """
    code = CHARGING_RULE_DEFINITION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ChargingRuleDefinitionAVP.code,
                             ChargingRuleDefinitionAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ChargingRuleNameAVP(DiameterAVP, OctetStringType):
    """Implementation of Charging-Rule-Name AVP in Section 5.3.6 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Charging-Rule-Name AVP (AVP Code 1005) is of type OctetString.
    """
    code = CHARGING_RULE_NAME_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ChargingRuleNameAVP.code,
                             ChargingRuleNameAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class EventTriggerAVP(DiameterAVP, EnumeratedType):
    """Implementation of Event-Trigger AVP in Section 5.3.7 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Event-Trigger AVP (AVP Code 1006) is of type Enumerated.
    """
    code = EVENT_TRIGGER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP
 
    values = [
                EVENT_TRIGGER_SGSN_CHANGE,
                EVENT_TRIGGER_QOS_CHANGE,
                EVENT_TRIGGER_RAT_CHANGE,
                EVENT_TRIGGER_TFT_CHANGE,
                EVENT_TRIGGER_PLMN_CHANGE,
                EVENT_TRIGGER_LOSS_OF_BEARER,
                EVENT_TRIGGER_RECOVERY_OF_BEARER,
                EVENT_TRIGGER_IP_CAN_CHANGE,
                EVENT_TRIGGER_QOS_CHANGE_EXCEEDING_AUTHORIZATION,
                EVENT_TRIGGER_RAI_CHANGE,
                EVENT_TRIGGER_USER_LOCATION_CHANGE,
                EVENT_TRIGGER_NO_EVENT_TRIGGERS,
                EVENT_TRIGGER_OUT_OF_CREDIT,
                EVENT_TRIGGER_REALLOCATION_OF_CREDIT,
                EVENT_TRIGGER_REVALIDATION_TIMEOUT,
                EVENT_TRIGGER_UE_IP_ADDRESS_ALLOCATE,
                EVENT_TRIGGER_UE_IP_ADDRESS_RELEASE,
                EVENT_TRIGGER_DEFAULT_EPS_BEARER_QOS_CHANGE,
                EVENT_TRIGGER_AN_GW_CHANGE,
                EVENT_TRIGGER_SUCCESSFUL_RESOURCE_ALLOCATION,
                EVENT_TRIGGER_RESOURCE_MODIFICATION_REQUEST,
                EVENT_TRIGGER_PGW_TRACE_CONTROL,
                EVENT_TRIGGER_UE_TIME_ZONE_CHANGE,
                EVENT_TRIGGER_TAI_CHANGE,
                EVENT_TRIGGER_ECGI_CHANGE,
                EVENT_TRIGGER_CHARGING_CORRELATION_EXCHANGE,
                EVENT_TRIGGER_APN_AMBR_MODIFICATION_FAILURE,
                EVENT_TRIGGER_USER_CSG_INFORMATION_CHANGE,
                EVENT_TRIGGER_USAGE_REPORT,
                EVENT_TRIGGER_DEFAULT_EPS_BEARER_QOS_MODIFICATION_FAILURE,
                EVENT_TRIGGER_USER_CSG_HYBRID_SUBSCRIBED_INFORMATION_CHANGE,
                EVENT_TRIGGER_USER_CSG_HYBRID_UNSUBSCRIBED_INFORMATION_CHANGE,
                EVENT_TRIGGER_ROUTING_RULE_CHANGE,
                EVENT_TRIGGER_APPLICATION_START,
                EVENT_TRIGGER_APPLICATION_STOP,
                EVENT_TRIGGER_CS_TO_PS_HANDOVER,
                EVENT_TRIGGER_UE_LOCAL_IP_ADDRESS_CHANGE,
                EVENT_TRIGGER_HENB_LOCAL_IP_ADDRESS_CHANGE,
                EVENT_TRIGGER_ACCESS_NETWORK_INFO_REPORT,
                EVENT_TRIGGER_CREDIT_MANAGEMENT_SESSION_FAILURE,
                EVENT_TRIGGER_DEFAULT_QOS_CHANGE,
                EVENT_TRIGGER_CHANGE_OF_UE_PRESENCE_IN_PRESENCE_REPORTING_AREA_REPORT,
                EVENT_TRIGGER_ADDITION_OF_ACCESS,
                EVENT_TRIGGER_REMOVAL_OF_ACCESS,
                EVENT_TRIGGER_UNAVAILABILITY_OF_ACCESS,
                EVENT_TRIGGER_AVAILABILITY_OF_ACCESS,
                EVENT_TRIGGER_RESOURCE_RELEASE,
                EVENT_TRIGGER_ENODEB_CHANGE,
                EVENT_TRIGGER_3GPP_PS_DATA_OFF_CHANGE
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             EventTriggerAVP.code,
                             EventTriggerAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class MeteringMethodAVP(DiameterAVP, EnumeratedType):
    """Implementation of Metering-Method AVP in Section 5.3.8 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Metering-Method AVP (AVP Code 1007) is of type Enumerated.
    """
    code = METERING_METHOD_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                METERING_METHOD_DURATION,
                METERING_METHOD_VOLUME,
                METERING_METHOD_DURATION_VOLUME,
                METERING_METHOD_EVENT
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             MeteringMethodAVP.code,
                             MeteringMethodAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)

 
class OfflineAVP(DiameterAVP, EnumeratedType):
    """Implementation of Offline AVP in Section 5.3.9 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Offline AVP (AVP Code 1008) is of type Enumerated.
    """
    code = OFFLINE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                OFFLINE_DISABLE_OFFLINE,
                OFFLINE_ENABLE_OFFLINE
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             OfflineAVP.code,
                             OfflineAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class OnlineAVP(DiameterAVP, EnumeratedType):
    """Implementation of Online AVP in Section 5.3.10 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Online AVP (AVP Code 1009) is of type Enumerated.
    """
    code = ONLINE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                ONLINE_DISABLE_ONLINE,
                ONLINE_ENABLE_ONLINE
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             OnlineAVP.code,
                             OnlineAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class QosInformationAVP(DiameterAVP, GroupedType):
    """Implementation of QoS-Information AVP in Section 5.3.16 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The QoS-Information AVP (AVP Code 1016) is of type Grouped.
    """
    code = QOS_INFORMATION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             QosInformationAVP.code,
                             QosInformationAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ChargingRuleReportAVP(DiameterAVP, GroupedType):
    """Implementation of Charging-Rule-Report AVP in Section 5.3.18 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Charging-Rule-Report AVP (AVP Code 1018) is of type Grouped.
    """
    code = CHARGING_RULE_REPORT_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ChargingRuleReportAVP.code,
                             ChargingRuleReportAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class PccRuleStatusAVP(DiameterAVP, EnumeratedType):
    """Implementation of PCC-Rule-Status AVP in Section 5.3.19 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The PCC-Rule-Status AVP (AVP Code 1019) is of type Enumerated.
    """
    code = PCC_RULE_STATUS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                PCC_RULE_STATUS_ACTIVE,
                PCC_RULE_STATUS_INACTIVE,
                PCC_RULE_STATUS_TEMPORARILY_INACTIVE
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             PccRuleStatusAVP.code,
                             PccRuleStatusAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AccessNetworkChargingIdentifierGxAVP(DiameterAVP, GroupedType):
    """Implementation of Access-Network-Charging-Identifier-Gx AVP in 
    Section 5.3.22 of ETSI TS 129 212 V15.3.0 (2018-07).

    The Access-Network-Charging-Identifier-Gx AVP (AVP Code 1022) is 
    of type Grouped.
    """
    code = ACCESS_NETWORK_CHARGING_IDENTIFIER_GX_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AccessNetworkChargingIdentifierGxAVP.code,
                             AccessNetworkChargingIdentifierGxAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class NetworkRequestSupportAVP(DiameterAVP, EnumeratedType):
    """Implementation of Network-Request-Support AVP in Section 5.3.24 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Network-Request-Support AVP (AVP Code 1024) is of type Enumerated.
    """
    code = NETWORK_REQUEST_SUPPORT_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                NETWORK_REQUEST_NOT_SUPPORTED,
                NETWORK_REQUEST_SUPPORTED
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             NetworkRequestSupportAVP.code,
                             NetworkRequestSupportAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class GuaranteedBitrateDlAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Guaranteed-Bitrate-DL AVP in Section 5.3.25 of
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Guaranteed-Bitrate-DL AVP (AVP Code 1025) is of type Unsigned32.
    """
    code = GUARANTEED_BITRATE_DL_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             GuaranteedBitrateDlAVP.code,
                             GuaranteedBitrateDlAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class GuaranteedBitrateUlAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Guaranteed-Bitrate-UL AVP in Section 5.3.26 of
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Guaranteed-Bitrate-UL AVP (AVP Code 1026) is of type Unsigned32.
    """
    code = GUARANTEED_BITRATE_UL_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             GuaranteedBitrateUlAVP.code,
                             GuaranteedBitrateUlAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class RuleFailureCodeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Rule-Failure-Code AVP in Section 5.3.38 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Rule-Failure-Code AVP (AVP Code 1031) is of type Enumerated.
    """
    code = RULE_FAILURE_CODE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                RULE_FAILURE_CODE_UNKNOWN_RULE_NAME,
                RULE_FAILURE_CODE_RATING_GROUP_ERROR,
                RULE_FAILURE_CODE_SERVICE_IDENTIFIER_ERROR,
                RULE_FAILURE_CODE_GW_PCEF_MALFUNCTION,
                RULE_FAILURE_CODE_RESOURCES_LIMITATION,
                RULE_FAILURE_CODE_MAX_NR_BEARERS_REACHED,
                RULE_FAILURE_CODE_UNKNOWN_BEARER_ID,
                RULE_FAILURE_CODE_MISSING_BEARER_ID,
                RULE_FAILURE_CODE_MISSING_FLOW_INFORMATION,
                RULE_FAILURE_CODE_RESOURCE_ALLOCATION_FAILURE,
                RULE_FAILURE_CODE_UNSUCCESSFUL_QOS_VALIDATION,
                RULE_FAILURE_CODE_INCORRECT_FLOW_INFORMATION,
                RULE_FAILURE_CODE_PS_TO_CS_HANDOVER,
                RULE_FAILURE_CODE_TDF_APPLICATION_IDENTIFIER_ERROR,
                RULE_FAILURE_CODE_NO_BEARER_BOUND,
                RULE_FAILURE_CODE_FILTER_RESTRICTIONS,
                RULE_FAILURE_CODE_AN_GW_FAILED,
                RULE_FAILURE_CODE_MISSING_REDIRECT_SERVER_ADDRESS,
                RULE_FAILURE_CODE_CM_END_USER_SERVICE_DENIED,
                RULE_FAILURE_CODE_CM_CREDIT_CONTROL_NOT_APPLICABLE,
                RULE_FAILURE_CODE_CM_AUTHORIZATION_REJECTED,
                RULE_FAILURE_CODE_CM_USER_UNKNOWN,
                RULE_FAILURE_CODE_CM_RATING_FAILED,
                RULE_FAILURE_CODE_ROUTING_RULE_REJECTION,
                RULE_FAILURE_CODE_UNKNOWN_ROUTING_ACCESS_INFORMATION,
                RULE_FAILURE_CODE_NO_NBIFOM_SUPPORT,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             RuleFailureCodeAVP.code,
                             RuleFailureCodeAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ApnAggregateMaxBitrateDlAVP(DiameterAVP, Unsigned32Type):
    """Implementation of APN-Aggregate-Max-Bitrate-DL AVP in Section 5.3.39 of
    ETSI TS 129 212 V15.3.0 (2018-07).

    The APN-Aggregate-Max-Bitrate-DL AVP (AVP Code 1040) is of type Unsigned32.
    """
    code = APN_AGGREGATE_MAX_BITRATE_DL_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ApnAggregateMaxBitrateDlAVP.code,
                             ApnAggregateMaxBitrateDlAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ApnAggregateMaxBitrateUlAVP(DiameterAVP, Unsigned32Type):
    """Implementation of APN-Aggregate-Max-Bitrate-UL AVP in Section 5.3.40 of
    ETSI TS 129 212 V15.3.0 (2018-07).

    The APN-Aggregate-Max-Bitrate-UL AVP (AVP Code 1041) is of type Unsigned32.
    """
    code = APN_AGGREGATE_MAX_BITRATE_UL_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ApnAggregateMaxBitrateUlAVP.code,
                             ApnAggregateMaxBitrateUlAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class DefaultEpsBearerQosAVP(DiameterAVP, GroupedType):
    """Implementation of Default-EPS-Bearer-QoS AVP in Section 5.3.48 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Default-EPS-Bearer-QoS AVP (AVP Code 1049) is of type Grouped.
    """
    code = DEFAULT_EPS_BEARER_QOS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             DefaultEpsBearerQosAVP.code,
                             DefaultEpsBearerQosAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class FlowInformationAVP(DiameterAVP, GroupedType):
    """Implementation of Flow-Information AVP in Section 5.3.53 of 
    ETSI TS 129 212 V15.3.0 (2018-07).

    The Flow-Information AVP (AVP Code 1058) is of type Grouped.
    """
    code = FLOW_INFORMATION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             FlowInformationAVP.code,
                             FlowInformationAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)