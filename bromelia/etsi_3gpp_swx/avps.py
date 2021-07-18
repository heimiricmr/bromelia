# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_swx.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP SWs Application Id.
    
    :copyright: (c) 2020 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..etsi_3gpp_swm.avps import *

from ..avps import SubscriptionIdAVP, SessionTimeoutAVP
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


class Mip6FeatureVectorAVP(DiameterAVP, Unsigned64Type):
    """Implementation of MIP6-Feature-Vector AVP in Section 9.2.3.2.3 of 
    ETSI TS 129 273 V14.3.0 (2017-07).

    The MIP6-Feature-Vector AVP (AVP Code 124) is of type Unsigned64.
    """
    code = MIP6_FEATURE_VECTOR_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, Mip6FeatureVectorAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned64Type.__init__(self, data=data)


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


class SipNumberAuthItemsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of SIP-Number-Auth-Items AVP in Section 6.3.8 
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The SIP-Number-Auth-Items AVP (AVP Code 607) is of type Unsigned32.
    """
    code = SIP_NUMBER_AUTH_ITEMS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SipNumberAuthItemsAVP.code,
                             SipNumberAuthItemsAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SipAuthenticationSchemeAVP(DiameterAVP, UTF8StringType):
    """Implementation of Authentication-Scheme AVP in Section 6.3.9 
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The Authentication-Scheme AVP (AVP Code 608) is of type UTF8String.
    """
    code = SIP_AUTHENTICATION_SCHEME_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SipAuthenticationSchemeAVP.code,
                             SipAuthenticationSchemeAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SipAuthenticateAVP(DiameterAVP, OctetStringType):
    """Implementation of SIP-Authenticate AVP in Section 6.3.10 
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The SIP-Authenticate AVP (AVP Code 609) is of type OctetString.
    """
    code = SIP_AUTHENTICATE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SipAuthenticateAVP.code,
                             SipAuthenticateAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SipAuthorizationAVP(DiameterAVP, OctetStringType):
    """Implementation of SIP-Authorization AVP in Section 6.3.11 
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The SIP-Authorization AVP (AVP Code 610) is of type OctetString.
    """
    code = SIP_AUTHORIZATION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SipAuthorizationAVP.code,
                             SipAuthorizationAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ConfidentialityKeyAVP(DiameterAVP, OctetStringType):
    """Implementation of Confidentiality-Key AVP in Section 6.3.27 
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The Confidentiality-Key AVP (AVP Code 625) is of type OctetString.
    """
    code = CONFIDENTIALITY_KEY_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ConfidentialityKeyAVP.code,
                             ConfidentialityKeyAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class IntegrityKeyAVP(DiameterAVP, OctetStringType):
    """Implementation of Integrity-Key AVP in Section 6.3.28
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The Integrity-Key AVP (AVP Code 626) is of type OctetString.
    """
    code = INTEGRITY_KEY_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             IntegrityKeyAVP.code,
                             IntegrityKeyAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SipAuthDataItemAVP(DiameterAVP, GroupedType):
    """Implementation of SIP-Auth-Data-Item AVP in Section 6.3.13 
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The SIP-Auth-Data-Item AVP (AVP Code 612) is of type Grouped.
    """
    code = SIP_AUTH_DATA_ITEM_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    optionals = {
                    #"sip_item_number": SipItemNumberAVP,
                    "sip_authentication_scheme": SipAuthenticationSchemeAVP,
                    "sip_authenticate": SipAuthenticateAVP,
                    "sip_authorization": SipAuthorizationAVP,
                    #"sip_authentication_context": SipAuthenticationContextAVP,
                    "confidentiality_key": ConfidentialityKeyAVP,
                    "integrity_key": IntegrityKeyAVP,
                    #"sip_digest_authenticate": SipDigestAuthenticateAVP,
                    #"framed_ip_address": FramedIpvAddressAVP,
                    #"framed_ipv6_address": FramedIpv6AddressAVP,
                    #"framed_interface_id": FramedInterfaceIdAVP,
                    #"line_identifier": LineIdentifierAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SipAuthDataItemAVP.code,
                             SipAuthDataItemAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


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


class Non3gppIpAccessAVP(DiameterAVP, EnumeratedType):
    """Implementation of Non-3GPP-Ip-Access AVP in Section 8.2.3.3 
    of ETSI TS 129 273 V14.3.0 (2017-07).

    The Non-3GPP-Ip-Access AVP (AVP Code 1501) is of type Enumerated.
    """
    code = NON_3GPP_IP_ACCESS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                NON_3GPP_SUBSCRIPTION_ALLOWED,
                NON_3GPP_SUBSCRIPTION_BARRED,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             Non3gppIpAccessAVP.code,
                             Non3gppIpAccessAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class Non3gppIpAccessApnAVP(DiameterAVP, EnumeratedType):
    """Implementation of Non-3GPP-Ip-Access-APN AVP in Section 8.2.3.4
    of ETSI TS 129 273 V14.3.0 (2017-07).

    The Non-3GPP-Ip-Access-APN AVP (AVP Code 1502) is of type Enumerated.
    """
    code = NON_3GPP_IP_ACCESS_APN_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                NON_3GPP_APNS_ENABLE,
                NON_3GPP_APNS_DISABLE,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             Non3gppIpAccessApnAVP.code,
                             Non3gppIpAccessApnAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class Non3gppUserDataAVP(DiameterAVP, GroupedType):
    """Implementation of Non-3GPP-User-Data AVP in Section 8.2.3.1 
    of ETSI TS 129 273 V14.3.0 (2017-07).

    The Non-3GPP-User-Data AVP (AVP Code 1500) is of type Grouped.
    """
    code = NON_3GPP_USER_DATA_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    optionals = {
                    "subscription_id": SubscriptionIdAVP,
                    "non_3gpp_ip_access": Non3gppIpAccessAVP,
                    "non_3gpp_ip_access_apn": Non3gppIpAccessApnAVP,
                    "rat_type": RatTypeAVP,
                    "session_timeout": SessionTimeoutAVP,
                    "mip6_feature_vector": Mip6FeatureVectorAVP,
                    "ambr": AmbrAVP,
                    "x3gpp_charging_characteristics": X3gppChargingCharacteristicsAVP,
                    "context_identifier": ContextIdentifierAVP,
                    #"apn_oi_replacement": ApnOiReplacementAVP,
                    "apn_configuration": ApnConfigurationAVP,
                    #"trace_info": TraceInfoAVP,
                    #"twan_default_apn_context_id": TwanDefaultApnContextIdAVP,
                    #"twan_access_info": TwanAccessInfoAVP,
                    #"emergency_info": EmergencyInfoAVP,
                    #"erp_authorization": ErpAuthorizationAVP

    }

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             Non3gppUserDataAVP.code,
                             Non3gppUserDataAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ServerAssignmentTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Server-Assignment-Type AVP in Section 6.3.15 
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The Server-Assignment-Type AVP (AVP Code 614) is of type Enumerated.
    """
    code = SERVER_ASSIGNMENT_TYPE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                SERVER_ASSIGNMENT_TYPE_NO_ASSIGNMENT,
                SERVER_ASSIGNMENT_TYPE_REGISTRATION,
                SERVER_ASSIGNMENT_TYPE_RE_REGISTRATION,
                SERVER_ASSIGNMENT_TYPE_UNREGISTERED_USER,
                SERVER_ASSIGNMENT_TYPE_TIMEOUT_DEREGISTRATION,
                SERVER_ASSIGNMENT_TYPE_USER_DEREGISTRATION,
                SERVER_ASSIGNMENT_TYPE_DEREGISTRATION_STORE_SERVER_NAME,
                SERVER_ASSIGNMENT_TYPE_USER_DEREGISTRATION_STORE_SERVER_NAME,
                SERVER_ASSIGNMENT_TYPE_ADMINISTRATIVE_DEREGISTRATION,
                SERVER_ASSIGNMENT_TYPE_AUTHENTICATION_FAILURE,
                SERVER_ASSIGNMENT_TYPE_AUTHENTICATION_TIMEOUT,
                SERVER_ASSIGNMENT_TYPE_DEREGISTRATION_TOO_MUCH_DATA,
                SERVER_ASSIGNMENT_TYPE_AAA_USER_DATA_REQUEST,
                SERVER_ASSIGNMENT_TYPE_PGW_UPDATE,
                SERVER_ASSIGNMENT_TYPE_RESTORATION
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ServerAssignmentTypeAVP.code,
                             ServerAssignmentTypeAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ReasonCodeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Reason-Code AVP in Section 6.3.17 
    of ETSI TS 129 229 V11.3.0 (2013-04).

    The Reason-Code AVP (AVP Code 616) is of type Enumerated.
    """
    code = REASON_CODE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                REASON_CODE_PERMANENT_TERMINATION,
                REASON_CODE_NEW_SERVER_ASSIGNED,
                REASON_CODE_SERVER_CHANGE,
                REASON_CODE_REMOVE_CHANGE,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ReasonCodeAVP.code,
                             ReasonCodeAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ReasonInfoAVP(DiameterAVP, UTF8StringType):
    """Implementation of Reason-Info AVP in Section 6.3.18
    of ETSI TS 129 229 V11.3.0 (2013-04).

    The Reason-Info AVP (AVP Code 617) is of type UTF8String.
    """
    code = REASON_INFO_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ReasonInfoAVP.code,
                             ReasonInfoAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class DeregistrationReasonAVP(DiameterAVP, GroupedType):
    """Implementation of Deregistration-Reason AVP in Section 6.3.16 
    of ETSI TS 129 229 V11.3.0 (2013-04).

    The Server-Assignment-Type AVP (AVP Code 615) is of type Grouped.
    """
    code = DE_REGISTRATION_REASON_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "reason_code": ReasonCodeAVP,
    }
    optionals = {
                    "reason_info": ReasonInfoAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             DeregistrationReasonAVP.code,
                             DeregistrationReasonAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)
