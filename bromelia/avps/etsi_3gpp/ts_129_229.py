# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp.ts_129_229
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in ETSI TS 129 229.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..ietf.rfc6733 import VendorIdAVP

from ...base import DiameterAVP
from ...constants.etsi_3gpp.ts_129_229 import *
from ...types import *


class FeatureListIdAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Feature-List-ID AVP in Section 6.3.30 of
    ETSI TS 129 229 V14.3.0 (2019-10).

    The Feature-List-ID AVP (AVP Code 629) is of type Unsigned32.
    """
    code = FEATURE_LIST_ID_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             FeatureListIdAVP.code,
                             FeatureListIdAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class FeatureListAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Feature-List AVP in Section 6.3.31 of 
    ETSI TS 129 229 V14.3.0 (2019-10).

    The Feature-List AVP (AVP Code 630) is of type Unsigned32.
    """
    code = FEATURE_LIST_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data=convert_to_4_bytes(0)):
        DiameterAVP.__init__(self, 
                             FeatureListAVP.code,
                             FeatureListAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SupportedFeaturesAVP(DiameterAVP, GroupedType):
    """Implementation of Supported-Features AVP in Section 6.3.29 of 
    ETSI TS 129 229 V14.3.0 (2019-10).

    The Supported-Features AVP (AVP Code 628) is of type Grouped.
    """
    code = SUPPORTED_FEATURES_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "vendor_id": VendorIdAVP,
                    "feature_list_id": FeatureListIdAVP,
                    "feature_list": FeatureListAVP
    }
    optionals = {}

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SupportedFeaturesAVP.code,
                             SupportedFeaturesAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


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