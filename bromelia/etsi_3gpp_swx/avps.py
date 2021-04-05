# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_swx.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP SWs Application Id.
    
    :copyright: (c) 2020 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..etsi_3gpp_s6b.avps import Mip6FeatureVectorAVP
from ..etsi_3gpp_swm.avps import *

from ..avps import *
from ..constants import *
from ..types import *


class SipNumberAuthItemsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of SIP-Number-Auth-Items AVP in Section 6.3.8 
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The SIP-Number-Auth-Items AVP (AVP Code 607) is of type Unsigned32.
    """
    code = SIP_NUMBER_AUTH_ITEMS_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, SipNumberAuthItemsAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SipAuthenticationSchemeAVP(DiameterAVP, UTF8StringType):
    """Implementation of Authentication-Scheme AVP in Section 6.3.9 
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The Authentication-Scheme AVP (AVP Code 608) is of type UTF8String.
    """
    code = SIP_AUTHENTICATION_SCHEME_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, SipAuthenticationSchemeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SipAuthenticateAVP(DiameterAVP, OctetStringType):
    """Implementation of SIP-Authenticate AVP in Section 6.3.10 
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The SIP-Authenticate AVP (AVP Code 609) is of type OctetString.
    """
    code = SIP_AUTHENTICATE_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, SipAuthenticateAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SipAuthorizationAVP(DiameterAVP, OctetStringType):
    """Implementation of SIP-Authorization AVP in Section 6.3.11 
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The SIP-Authorization AVP (AVP Code 610) is of type OctetString.
    """
    code = SIP_AUTHORIZATION_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, SipAuthorizationAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ConfidentialityKeyAVP(DiameterAVP, OctetStringType):
    """Implementation of Confidentiality-Key AVP in Section 6.3.27 
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The Confidentiality-Key AVP (AVP Code 625) is of type OctetString.
    """
    code = CONFIDENTIALITY_KEY_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, ConfidentialityKeyAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class IntegrityKeyAVP(DiameterAVP, OctetStringType):
    """Implementation of Integrity-Key AVP in Section 6.3.28
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The Integrity-Key AVP (AVP Code 626) is of type OctetString.
    """
    code = INTEGRITY_KEY_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, IntegrityKeyAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SipAuthDataItemAVP(DiameterAVP, GroupedType):
    """Implementation of SIP-Auth-Data-Item AVP in Section 6.3.13 
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The SIP-Auth-Data-Item AVP (AVP Code 612) is of type Grouped.
    """
    code = SIP_AUTH_DATA_ITEM_AVP_CODE

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
        DiameterAVP.__init__(self, SipAuthDataItemAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.run(self, data=data, vendor_id=VENDOR_ID_3GPP)


class Non3gppIpAccessAVP(DiameterAVP, EnumeratedType):
    """Implementation of Non-3GPP-Ip-Access AVP in Section 8.2.3.3 
    of ETSI TS 129 273 V14.3.0 (2017-07).

    The Non-3GPP-Ip-Access AVP (AVP Code 1501) is of type Enumerated.
    """
    code = NON_3GPP_IP_ACCESS_AVP_CODE
    values = [
                NON_3GPP_SUBSCRIPTION_ALLOWED,
                NON_3GPP_SUBSCRIPTION_BARRED,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, Non3gppIpAccessAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class Non3gppIpAccessApnAVP(DiameterAVP, EnumeratedType):
    """Implementation of Non-3GPP-Ip-Access-APN AVP in Section 8.2.3.4
    of ETSI TS 129 273 V14.3.0 (2017-07).

    The Non-3GPP-Ip-Access-APN AVP (AVP Code 1502) is of type Enumerated.
    """
    code = NON_3GPP_IP_ACCESS_APN_AVP_CODE
    values = [
                NON_3GPP_APNS_ENABLE,
                NON_3GPP_APNS_DISABLE,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, Non3gppIpAccessApnAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class Non3gppUserDataAVP(DiameterAVP, GroupedType):
    """Implementation of Non-3GPP-User-Data AVP in Section 8.2.3.1 
    of ETSI TS 129 273 V14.3.0 (2017-07).

    The Non-3GPP-User-Data AVP (AVP Code 1500) is of type Grouped.
    """
    code = NON_3GPP_USER_DATA_AVP_CODE

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
        DiameterAVP.__init__(self, Non3gppUserDataAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.run(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ServerAssignmentTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Server-Assignment-Type AVP in Section 6.3.15 
    of ETSI TS 129 229 V16.2.0 (2020-11).

    The Server-Assignment-Type AVP (AVP Code 614) is of type Enumerated.
    """
    code = SERVER_ASSIGNMENT_TYPE_AVP_CODE
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
        DiameterAVP.__init__(self, ServerAssignmentTypeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ReasonCodeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Reason-Code AVP in Section 6.3.17 
    of ETSI TS 129 229 V11.3.0 (2013-04).

    The Reason-Code AVP (AVP Code 616) is of type Enumerated.
    """
    code = REASON_CODE_AVP_CODE
    values = [
                REASON_CODE_PERMANENT_TERMINATION,
                REASON_CODE_NEW_SERVER_ASSIGNED,
                REASON_CODE_SERVER_CHANGE,
                REASON_CODE_REMOVE_CHANGE,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, ReasonCodeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ReasonInfoAVP(DiameterAVP, UTF8StringType):
    """Implementation of Reason-Info AVP in Section 6.3.18
    of ETSI TS 129 229 V11.3.0 (2013-04).

    The Reason-Info AVP (AVP Code 617) is of type UTF8String.
    """
    code = REASON_INFO_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, ReasonInfoAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class DeregistrationReasonAVP(DiameterAVP, GroupedType):
    """Implementation of Deregistration-Reason AVP in Section 6.3.16 
    of ETSI TS 129 229 V11.3.0 (2013-04).

    The Server-Assignment-Type AVP (AVP Code 615) is of type Grouped.
    """
    code = DE_REGISTRATION_REASON_AVP_CODE

    mandatory = {
                    "reason_code": ReasonCodeAVP,
    }
    optionals = {
                    "reason_info": ReasonInfoAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, DeregistrationReasonAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.run(self, data=data, vendor_id=VENDOR_ID_3GPP)
