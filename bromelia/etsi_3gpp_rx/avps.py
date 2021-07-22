# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_rx.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP Rx Application Id.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..base import *
from ..constants import *
from ..types import *


class FramedIpAddressAVP(DiameterAVP, AddressType):
    """Implementation of Framed-IP-Address AVP in Section 4.4.10.5.1 of 
    IETF RFC 7155.

    The Framed-IP-Address AVP (AVP Code 8) is of type Address.
    """
    code = FRAMED_IP_ADDRESS_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, FramedIpAddressAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        AddressType.__init__(self, data=data)


    def parser_data(self, data):
        if isinstance(data, str):
            ip_address = ipaddress.ip_address(data)

            if isinstance(ip_address, ipaddress.IPv4Address):
                self._data = ip_address.packed

            else:
                raise DataTypeError("AddressType MUST have data argument "\
                                    "of 'str' with IPv4 address format value")

        elif isinstance(data, bytes):
            self._data = data
    

class CalledStationIdAVP(DiameterAVP, UTF8StringType):
    """Implementation of Called-Station-Id AVP in Section 4.2.5 of RFC 7155.

    The Called-Station-Id AVP (AVP Code 30) is of type UTF8String.
    """
    code = CALLED_STATION_ID_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, CalledStationIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


class FramedIpv6PrefixAVP(DiameterAVP, OctetStringType):
    """Implementation of Framed-IPv6-Prefix AVP in Section 4.4.10.5.6 of 
    IETF RFC 7155.

    The Framed-IPv6-Prefix AVP (AVP Code 97) is of type OctetString.
    """
    code = FRAMED_IPV6_PREFIX_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, FramedIpv6PrefixAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        OctetStringType.__init__(self, data=data)


class AuthorizationLifetimeAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Authorization-Lifetime AVP in Section 8.9 of 
    IETF RFC 6733.

    The Authorization-Lifetime AVP (AVP Code 291) is of type Unsigned32.
    """
    code = AUTHORIZATION_LIFETIME_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, AuthorizationLifetimeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class SubscriptionIdDataAVP(DiameterAVP, UTF8StringType):
    """Implementation of Subscription-Id-Data AVP in Section 8.48 of 
    IETF RFC 4006.

    The Subscription-Id-Data AVP (AVP Code 444) is of type UTF8String.
    """
    code = SUBSCRIPTION_ID_DATA_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, SubscriptionIdDataAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


class SubscriptionIdTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Subscription-Id-Type AVP in Section 8.47 of 
    IETF RFC 4006.

    The Subscription-Id-Type AVP (AVP Code 450) is of type Enumerated.
    """
    code = SUBSCRIPTION_ID_TYPE_AVP_CODE
    vendor_id = None

    values = [
                END_USER_E164,
                END_USER_IMSI,
                END_USER_SIP_URI,
                END_USER_NAI,
                END_USER_PRIVATE
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, SubscriptionIdTypeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class ReservationPriorityAVP(DiameterAVP, EnumeratedType):
    """Implementation of Reservation-Priority AVP in Section 7.3.9 of 
    ETSI TS 183 017 V2.3.1 (2008-09).

    The Reservation-Priority AVP (AVP Code 458) is of type Enumerated.
    """
    code = RESERVATION_PRIORITY_AVP_CODE
    vendor_id = VENDOR_ID_ETSI

    values = [
                PRIORITY_DEFAULT,
                PRIORITY_ONE,
                PRIORITY_TWO,
                PRIORITY_THREE,
                PRIORITY_FOUR,
                PRIORITY_FIVE,
                PRIORITY_SIX,
                PRIORITY_SEVEN
    ]

    def __init__(self, data=PRIORITY_DEFAULT):
        DiameterAVP.__init__(self, 
                             ReservationPriorityAVP.code,
                             ReservationPriorityAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_ETSI)


class AbortCauseAVP(DiameterAVP, EnumeratedType):
    """Implementation of Abort-Cause AVP in Section 5.3.1 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Abort-Cause AVP (AVP Code 500) is of type Enumerated.
    """
    code = ABORT_CAUSE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                ABORT_CAUSE_BEARER_RELEASED,
                ABORT_CAUSE_INSUFFICIENT_SERVER_RESOURCES,
                ABORT_CAUSE_INSUFFICIENT_BEARER_RESOURCES,
                ABORT_CAUSE_PS_TO_CS_HANDOVER,
                ABORT_CAUSE_SPONSORED_DATA_CONNECTIVITY_DISALLOWED,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AbortCauseAVP.code,
                             AbortCauseAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AccessNetworkChargingAddressAVP(DiameterAVP, AddressType):
    """Implementation of Access-Network-Charging-Address AVP in Section 5.3.2 of 
    ETSI 3GPP TS 29.214 V8.14.0 (2012-12).

    The Access-Network-Charging-Address AVP (AVP Code 501) is of type Address.
    """
    code = ACCESS_NETWORK_CHARGING_ADDRESS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AccessNetworkChargingAddressAVP.code,
                             AccessNetworkChargingAddressAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        AddressType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AfApplicationIdentifierAVP(DiameterAVP, OctetStringType):
    """Implementation of AF-Application-identifier AVP in Section 5.3.5  
    of ETSI TS 129 214 V15.4.0 (2018-07).

    The AF-Application-identifier AVP (AVP Code 504) is of type OctetString.
    """
    code = AF_APPLICATION_IDENTIFIER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AfApplicationIdentifierAVP.code,
                             AfApplicationIdentifierAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AfChargingIdentifierAVP(DiameterAVP, OctetStringType):
    """Implementation of AF-Charging-identifier AVP in Section 5.3.6  
    of ETSI TS 129 214 V15.4.0 (2018-07).

    The AF-Charging-identifier AVP (AVP Code 505) is of type OctetString.
    """
    code = AF_CHARGING_IDENTIFIER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AfChargingIdentifierAVP.code,
                             AfChargingIdentifierAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class FlowDescriptionAVP(DiameterAVP, OctetStringType):
    """Implementation of Flow-Description AVP in Section 5.38 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Flow-Description AVP (AVP Code 507) is of type IPFilterRule.
    """
    code = FLOW_DESCRIPTION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             FlowDescriptionAVP.code,
                             FlowDescriptionAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class FlowNumberAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Flow-Number AVP in Section 5.3.9 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Flow-Number AVP (AVP Code 509) is of type Unsigned32.
    """
    code = FLOW_NUMBER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             FlowNumberAVP.code,
                             FlowNumberAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)
 

class FlowStatusAVP(DiameterAVP, EnumeratedType):
    """Implementation of Flow-Status AVP in Section 5.3.11 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Flow-Status AVP (AVP Code 511) is of type Enumerated.
    """
    code = FLOW_STATUS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                FLOW_STATUS_ENABLED_UPLINK,
                FLOW_STATUS_ENABLED_DOWNLINK,
                FLOW_STATUS_ENABLED,
                FLOW_STATUS_DISABLED,
                FLOW_STATUS_REMOVED,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             FlowStatusAVP.code,
                             FlowStatusAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class FlowUsageAVP(DiameterAVP, EnumeratedType):
    """Implementation of Flow-Usage AVP in Section 5.3.12 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Flow-Usage AVP (AVP Code 512) is of type Enumerated.
    """
    code = FLOW_USAGE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                FLOW_USAGE_NO_INFORMATION,
                FLOW_USAGE_RTCP,
                FLOW_USAGE_AF_SIGNALLING,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             FlowUsageAVP.code,
                             FlowUsageAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SpecificActionAVP(DiameterAVP, EnumeratedType):
    """Implementation of Specific-Action AVP in Section 5.3.13 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Specific-Action AVP (AVP Code 513) is of type Enumerated.
    """
    code = SPECIFIC_ACTION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                SPECIFIC_ACTION_CHARGING_CORRELATION_EXCHANGE,
                SPECIFIC_ACTION_INDICATION_OF_LOSS_OF_BEARER,
                SPECIFIC_ACTION_INDICATION_OF_RECOVERY_OF_BEARER,
                SPECIFIC_ACTION_INDICATION_OF_RELEASE_OF_BEARER,
                SPECIFIC_ACTION_IP_CAN_CHANGE,
                SPECIFIC_ACTION_INDICATION_OF_OUT_OF_CREDIT,
                SPECIFIC_ACTION_INDICATION_OF_SUCCESSFUL_RESOURCES_ALLOCATION,
                SPECIFIC_ACTION_INDICATION_OF_FAILED_RESOURCES_ALLOCATION,
                SPECIFIC_ACTION_INDICATION_OF_LIMITED_PCC_DEPLOYMENT,
                SPECIFIC_ACTION_USAGE_REPORT,
                SPECIFIC_ACTION_ACCESS_NETWORK_INFO_REPORT,
                SPECIFIC_ACTION_INDICATION_OF_RECOVERY_FROM_LIMITED_PCC_DEPLOYMENT,
                SPECIFIC_ACTION_INDICATION_OF_ACCESS_NETWORK_INFO_REPORTING_FAILURE,
                SPECIFIC_ACTION_INDICATION_OF_TRANSFER_POLICY_EXPIRED,
                SPECIFIC_ACTION_PLMN_CHANGE,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SpecificActionAVP.code,
                             SpecificActionAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


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


class MediaComponentDescriptionAVP(DiameterAVP, GroupedType):
    """Implementation of Media-Component-Description AVP in Section 5.3.16 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Media-Component-Description AVP (AVP Code 517) is of type Grouped.
    """
    code = MEDIA_COMPONENT_DESCRIPTION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):        
        DiameterAVP.__init__(self, 
                             MediaComponentDescriptionAVP.code,
                             MediaComponentDescriptionAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class MediaComponentNumberAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Media-Component-Number AVP in Section 5.3.17 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Media-Component-Number AVP (AVP Code 518) is of type Unsigned32.
    """
    code = MEDIA_COMPONENT_NUMBER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             MediaComponentNumberAVP.code,
                             MediaComponentNumberAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class MediaSubComponentAVP(DiameterAVP, GroupedType):
    """Implementation of Media-Sub-Component AVP in Section 5.3.18 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Media-Sub-Component AVP (AVP Code 519) is of type Grouped.
    """
    code = MEDIA_SUB_COMPONENT_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):        
        DiameterAVP.__init__(self, 
                             MediaSubComponentAVP.code,
                             MediaSubComponentAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class MediaTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Media-Type AVP in Section 5.3.19 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Media-Type AVP (AVP Code 520) is of type Enumerated.
    """
    code = MEDIA_TYPE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP
 
    values = [
                MEDIA_TYPE_AUDIO,
                MEDIA_TYPE_VIDEO,
                MEDIA_TYPE_DATA,
                MEDIA_TYPE_APPLICATION,
                MEDIA_TYPE_CONTROL,
                MEDIA_TYPE_TEXT,
                MEDIA_TYPE_MESSAGE,
                MEDIA_TYPE_OTHER,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             MediaTypeAVP.code,
                             MediaTypeAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ServiceInfoStatusAVP(DiameterAVP, EnumeratedType):
    """Implementation of Service-Info-Status AVP in Section 5.3.25 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Service-Info-Status AVP (AVP Code 527) is of type Enumerated.
    """
    code = SERVICE_INFO_STATUS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP
 
    values = [
                SERVICE_INFO_STATUS_FINAL_SERVICE_INFORMATION,
                SERVICE_INFO_STATUS_PRELIMINARY_SERVICE_INFORMATION,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ServiceInfoStatusAVP.code,
                             ServiceInfoStatusAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SupportedFeaturesAVP(DiameterAVP, GroupedType):
    """Implementation of Supported-Features AVP in Section 6.3.29 of 
    ETSI TS 129 229 V14.3.0 (2019-10).

    The Supported-Features AVP (AVP Code 628) is of type Grouped.
    """
    code = SUPPORTED_FEATURES_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SupportedFeaturesAVP.code,
                             SupportedFeaturesAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)
        
        GroupedType.__init__(self, data=self.data, vendor_id=VENDOR_ID_3GPP)


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


class AnTrustedAVP(DiameterAVP, EnumeratedType):
    """Implementation of AN-Trusted AVP in Section 5.2.3.9 of
    ETSI TS 129 273 V12.5.0 (2014-10).

    The AN-Trusted AVP (AVP Code 1503) is of type Enumerated.
    """
    code = AN_TRUSTED_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                AN_TRUSTED_TRUSTED,
                AN_TRUSTED_UNTRUSTED,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AnTrustedAVP.code,
                             AnTrustedAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


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

