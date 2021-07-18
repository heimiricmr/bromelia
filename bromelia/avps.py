# -*- coding: utf-8 -*-
"""
    bromelia.avps
    ~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library 
    that are used to create Diameter messages.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import base64
import datetime

from .__version__ import __version__
from ._internal_utils import convert_to_1_byte
from .base import DiameterAVP
from .constants import *
from .types import *

PRODUCT_NAME = f"Python bromelia v{__version__}"

class UserNameAVP(DiameterAVP, UTF8StringType):
    """Implementation of User-Name AVP in Section 8.14 of IETF RFC 6733.

    The User-Name AVP (AVP Code 1) [RADIUS] is of type UTF8String.
    """
    code = USER_NAME_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, UserNameAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


class ClassAVP(DiameterAVP, OctetStringType):
    """Implementation of Class AVP in Section 8.20 of IETF RFC 6733.

    The Class AVP (AVP Code 25) is of type OctetString.
    """
    code = CLASS_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, ClassAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)

        OctetStringType.__init__(self, data=data)


class SessionTimeoutAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Session-Timeout AVP in Section 8.13 IETF RFC 6733.

    The Session-Timeout AVP (AVP Code 27) is of type Unsigned32.
    """
    code = SESSION_TIMEOUT_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, SessionTimeoutAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class CallingStationIdAVP(DiameterAVP, UTF8StringType):
    """Implementation of Calling-Station-Id AVP in Section 4.2.6 IETF RFC 7155.

    The Calling-Station-Id AVP (AVP Code 31) is of type UTF8String.
    """
    code = CALLING_STATION_ID_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, CallingStationIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


class ProxyStateAVP(DiameterAVP, OctetStringType):
    """Implementation of Proxy-State AVP in Section 6.7.4 of IETF RFC 6733.

    The Proxy-State AVP (AVP Code 33) is of type OctetString.
    """
    code = PROXY_STATE_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, ProxyStateAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)    
        OctetStringType.__init__(self, data=data)


class AcctSessionIdAVP(DiameterAVP, OctetStringType):
    """Implementation of Acct-Session-Id AVP in Section 9.8.4 of IETF RFC 6733.

    The Acct-Session-Id AVP (AVP Code 44) is of type OctetString.
    """
    code = ACCT_SESSION_ID_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, AcctSessionIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)    
        OctetStringType.__init__(self, data=data)


""" REVIEW """
class AcctMultiSessionIdAVP(DiameterAVP, UTF8StringType):
    """Implementation of Acct-Multi-Session-Id AVP in Section 9.8.5 of 
    IETF RFC 6733.

    The Acct-Multi-Session-Id AVP (AVP Code 50) is of type UTF8String.
    """
    code = ACCT_MULTI_SESSION_ID_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        if isinstance(data, str):
            high = "403292"
            low = "403292"
            optional = "403292"
            data = f"{data};{high};{low};{optional}"
        elif isinstance(data, bytes):
            data = data

        DiameterAVP.__init__(self, AcctMultiSessionIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)    
        OctetStringType.__init__(self, data=data)


class EventTimestampAVP(DiameterAVP, TimeType):
    """Implementation of Event-Timestamp AVP in Section 8.21 of IETF RFC 6733.

    The Event-Timestamp AVP (AVP Code 55) is of type Time.
    """
    code = EVENT_TIMESTAMP_AVP_CODE
    vendor_id = None

    def __init__(self, data=datetime.datetime.utcnow()):
        DiameterAVP.__init__(self, EventTimestampAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)    
        TimeType.__init__(self, data=data)


class AcctInterimIntervalAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Acct-Interim-Interval AVP in Section 9.8.2 of 
    IETF RFC 6733.

    The Acct-Interim-Interval AVP (AVP Code 85) is of type Unsigned32.
    """
    code = ACCT_INTERIM_INTERVAL_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, AcctInterimIntervalAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class HostIpAddressAVP(DiameterAVP, AddressType):
    """Implementation of Host-IP-Address AVP in Section 5.3.5 of IETF RFC 3588.

    The Host-IP-Address AVP (AVP Code 257) is of type Address.
    """
    code = HOST_IP_ADDRESS_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, HostIpAddressAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        AddressType.__init__(self, data=data)


class AuthApplicationIdAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Auth-Application-Id AVP in Section 6.8 of 
    IETF RFC 3588.

    The Auth-Application-Id AVP (AVP Code 258) is of type Unsigned32.
    """
    code = AUTH_APPLICATION_ID_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, AuthApplicationIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class AcctApplicationIdAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Acct-Application-Id AVP in Section 6.9 of 
    IETF RFC 6733.

    The Acct-Application-Id AVP (AVP Code 259) is of type Unsigned32.
    """
    code = ACCT_APPLICATION_ID_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, AcctApplicationIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class VendorIdAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Vendor-Id AVP in Section 5.3.3 of IETF RFC 3588.

    The Vendor-Id AVP (AVP Code 266) is of type Unsigned32.

    A Vendor-Id value of zero in the CER or CEA messages is reserved and 
    indicates that this field is ignored.
    """
    code = VENDOR_ID_AVP_CODE
    vendor_id = None

    def __init__(self, data=VENDOR_ID_DEFAULT):
        DiameterAVP.__init__(self, VendorIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class VendorSpecificApplicationIdAVP(DiameterAVP, GroupedType):
    """Implementation of Vendor-Specific-Application-Id AVP in Section 6.11 of
    IETF RFC 6733.

    The Vendor-Specific-Application-Id AVP (AVP Code 260) is of type Grouped.
    """
    code = VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE
    vendor_id = None

    mandatory = {
                    "vendor_id": VendorIdAVP,
    }
    optionals = {
                    "auth_application_id": AuthApplicationIdAVP,
                    "acct_application_id": AcctApplicationIdAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, VendorSpecificApplicationIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)


class RedirectHostUsageAVP(DiameterAVP, EnumeratedType):
    """Implementation of Redirect-Host-Usage AVP in Section 6.13 of 
    IETF RFC 6733.

    The Redirect-Host-Usage AVP (AVP Code 261) is of type Enumerated.
    """
    code = REDIRECT_HOST_USAGE_AVP_CODE
    vendor_id = None

    values = [
                REDIRECT_HOST_USAGE_DONT_CACHE,
                REDIRECT_HOST_USAGE_ALL_SESSION,
                REDIRECT_HOST_USAGE_ALL_REALM,
                REDIRECT_HOST_USAGE_REALM_AND_APPLICATION,
                REDIRECT_HOST_USAGE_ALL_APPLICATION,
                REDIRECT_HOST_USAGE_ALL_HOST,
                REDIRECT_HOST_USAGE_ALL_USER
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, RedirectHostUsageAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class RedirectMaxCacheTimeAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Redirect-Max-Cache-Time AVP in Section 6.14 of 
    IETF RFC 6733.

    The Redirect-Max-Cache-Time AVP (AVP Code 262) is of type Unsigned32.
    """
    code = REDIRECT_MAX_CACHE_TIME_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, RedirectMaxCacheTimeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class SessionIdAVP(DiameterAVP, UTF8StringType):
    """Implementation of Session-Id AVP in Section 8.8 of IETF RFC 3588.

    The Session-Id AVP (AVP Code 263) is of type UTF8String.
    """
    code = SESSION_ID_AVP_CODE
    vendor_id = None

    diff = datetime.datetime.utcnow() - datetime.datetime(1900, 1, 1, 0, 0, 0)
    init = diff.days*24*60*60 + diff.seconds
    id = 0

    def __init__(self, data):
        if isinstance(data, str):
            high = SessionIdAVP.init
            low = SessionIdAVP.id
            optional = "bromelia"
            data = f"{data};{high};{low};{optional}"
            SessionIdAVP.id += 1
            
        elif isinstance(data, bytes):
            data = data

        DiameterAVP.__init__(self, SessionIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


    @staticmethod
    def _init():
        diff = datetime.datetime.utcnow() - datetime.datetime(1900, 1, 1, 0, 0, 0)
        SessionIdAVP.init = diff.days*24*60*60 + diff.seconds



class OriginHostAVP(DiameterAVP, DiameterIdentityType):
    """Implementation of Origin-Host AVP in Section 6.3 of IETF RFC 3588.

    The Origin-Host AVP (AVP Code 264) is of type DiameterIdentity.
    """
    code = ORIGIN_HOST_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, OriginHostAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterIdentityType.__init__(self, data=data)


class SupportedVendorIdAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Supported-Vendor-Id AVP in Section 5.3.6 of 
    IETF RFC 6733.

    The Supported-Vendor-Id AVP (AVP Code 265) is of type Unsigned32.
    """
    code = SUPPORTED_VENDOR_ID_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, SupportedVendorIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class FirmwareRevisionAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Firmware-Revision AVP in Section 5.3.4 of 
    IETF RFC 3588.

    The Firmware-Revision AVP (AVP Code 267) is of type Unsigned32.
    """
    code = FIRMWARE_REVISION_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, FirmwareRevisionAVP.code)
        Unsigned32Type.__init__(self, data=data)


class ResultCodeAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Result-Code AVP in Section 7.1 of IETF RFC 3588.

    The Result-Code AVP (AVP Code 268) is of type Unsigned32.
    """
    code = RESULT_CODE_AVP_CODE
    vendor_id = None

    values = [
                DIAMETER_MULTI_ROUND_AUTH,
                DIAMETER_SUCCESS,
                DIAMETER_LIMITED_SUCCESS,
                DIAMETER_COMMAND_UNSUPPORTED,
                DIAMETER_UNABLE_TO_DELIVER,
                DIAMETER_REALM_NOT_SERVED,
                DIAMETER_TOO_BUSY,
                DIAMETER_LOOP_DETECTED,
                DIAMETER_REDIRECT_INDICATION,
                DIAMETER_APPLICATION_UNSUPPORTED,
                DIAMETER_INVALID_HDR_BITS,
                DIAMETER_INVALID_AVP_BITS,
                DIAMETER_UNKNOWN_PEER,
                DIAMETER_AUTHENTICATION_REJECTED,
                DIAMETER_OUT_OF_SPACE,
                DIAMETER_ELECTION_LOST,
                DIAMETER_AVP_UNSUPPORTED,
                DIAMETER_UNKNOWN_SESSION_ID,
                DIAMETER_AUTHORIZATION_REJECTED,
                DIAMETER_INVALID_AVP_VALUE,
                DIAMETER_MISSING_AVP,
                DIAMETER_RESOURCES_EXCEEDED,
                DIAMETER_CONTRADICTING_AVPS,
                DIAMETER_AVP_NOT_ALLOWED,
                DIAMETER_AVP_OCCURS_TOO_MANY_TIMES,
                DIAMETER_NO_COMMON_APPLICATION,
                DIAMETER_UNSUPPORTED_VERSION,
                DIAMETER_UNABLE_TO_COMPLY,
                DIAMETER_INVALID_BIT_IN_HEADER,
                DIAMETER_INVALID_AVP_LENGTH,
                DIAMETER_INVALID_MESSAGE_LENGTH,
                DIAMETER_INVALID_AVP_BIT_COMBO,
                DIAMETER_NO_COMMON_SECURITY
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, ResultCodeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class ProductNameAVP(DiameterAVP, UTF8StringType):
    """Implementation of Product-Name AVP in Section 5.3.7 of IETF RFC 3588.

    The Product-Name AVP (AVP Code 269) is of type UTF8String.
    """
    code = PRODUCT_NAME_AVP_CODE
    vendor_id = None

    def __init__(self, data=PRODUCT_NAME):
        DiameterAVP.__init__(self, ProductNameAVP.code)
        UTF8StringType.__init__(self, data=data)


class SessionBindingAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Session-Binding AVP in Section 8.17 of IETF RFC 6733.

    The Session-Binding AVP (AVP Code 270) is of type Unsigned32.
    """
    code = SESSION_BINDING_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, SessionBindingAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class SessionServerFailoverAVP(DiameterAVP, EnumeratedType):
    """Implementation of Session-Server-Failover AVP in Section 8.18 of 
    IETF RFC 6733.

    The Session-Server-Failover AVP (AVP Code 271) is of type Enumerated.
    """
    code = SESSION_SERVER_FAILOVER_AVP_CODE
    vendor_id = None
    
    values = [
                SESSION_SERVER_FAILOVER_REFUSE_SERVICE,
                SESSION_SERVER_FAILOVER_TRY_AGAIN,
                SESSION_SERVER_FAILOVER_ALLOW_SERVICE,
                SESSION_SERVER_FAILOVER_TRY_AGAIN_ALLOW_SERVICE
    ]

    def __init__(self, data=SESSION_SERVER_FAILOVER_REFUSE_SERVICE):
        DiameterAVP.__init__(self, SessionServerFailoverAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class MultiRoundTimeOutAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Multi-Round-Time-Out AVP in Section 8.19 of 
    IETF RFC 6733.

    The Multi-Round-Time-Out AVP (AVP Code 272) is of type Unsigned32.
    """
    code = MULTI_ROUND_TIME_OUT_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, MultiRoundTimeOutAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class DisconnectCauseAVP(DiameterAVP, EnumeratedType):
    """Implementation of Disconnect-Cause AVP in Section 5.4.3 of 
    IETF RFC 3588.

    The Disconnect-Cause AVP (AVP Code 273) is of type Enumerated.
    """
    code = DISCONNECT_CAUSE_AVP_CODE
    vendor_id = None
    
    values = [
                DISCONNECT_CAUSE_REBOOTING,
                DISCONNECT_CAUSE_BUSY,
                DISCONNECT_CAUSE_DO_NOT_WANT_TO_TALK_TO_YOU
    ]

    def __init__(self, data=DISCONNECT_CAUSE_REBOOTING):
        DiameterAVP.__init__(self, DisconnectCauseAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class AuthRequestTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Auth-Request-Type AVP in Section 8.7 of IETF RFC 3588.

    The Auth-Request-Type AVP (AVP Code 274) is of type Enumerated.
    """
    code = AUTH_REQUEST_TYPE_AVP_CODE
    vendor_id = None
    
    values = [
                AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY,
                AUTH_REQUEST_TYPE_AUTHORIZE_ONLY,
                AUTH_REQUEST_TYPE_AUTHORIZE_AUTHENTICATE
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, AuthRequestTypeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class AuthGracePeriodAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Auth-Grace-Period AVP in Section 8.10 of 
    IETF RFC 6733.

    The Auth-Grace-Period AVP (AVP Code 276) is of type Unsigned32.
    """
    code = AUTH_GRACE_PERIOD_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, AuthGracePeriodAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class AuthSessionStateAVP(DiameterAVP, EnumeratedType):
    """Implementation of Auth-Session-State AVP in Section 8.11 of 
    IETF RFC 3588.

    The Auth-Session-State AVP (AVP Code 277) is of type Enumerated.
    """
    code = AUTH_SESSION_STATE_AVP_CODE
    vendor_id = None

    values = [
                STATE_MAINTAINED,
                NO_STATE_MAINTAINED
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, AuthSessionStateAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class OriginStateIdAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Origin-State-Id AVP in Section 8.16 of IETF RFC 6733.

    The Origin-State-Id AVP (AVP Code 278) is of type Unsigned32.
    """
    code = ORIGIN_STATE_ID_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, OriginStateIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class FailedAvpAVP(DiameterAVP, GroupedType):
    """Implementation of Failed-AVP AVP in Section 7.5 of IETF RFC 6733.

    The Failed-AVP AVP (AVP Code 279) is of type Grouped.
    """
    code = FAILED_AVP_AVP_CODE
    vendor_id = None

    mandatory = {}
    optionals = {}

    def __init__(self, data):
        DiameterAVP.__init__(self, FailedAvpAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)


class ProxyHostAVP(DiameterAVP, DiameterIdentityType):
    """Implementation of Proxy-Host AVP in Section 6.7.3 of IETF RFC 6733.

    The Proxy-Host AVP (AVP Code 280) is of type DiameterIdentity.
    """
    code = PROXY_HOST_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, ProxyHostAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterIdentityType.__init__(self, data=data)


class ErrorMessageAVP(DiameterAVP, UTF8StringType):
    """Implementation of Error-Message AVP in Section 7.3 of IETF RFC 6733.

    The Error-Message AVP (AVP Code 281) is of type UTF8String.
    """
    code = ERROR_MESSAGE_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, ErrorMessageAVP.code)
        UTF8StringType.__init__(self, data=data)


class RouteRecordAVP(DiameterAVP, DiameterIdentityType):
    """Implementation of Route-Record AVP in Section 6.7.1 of IETF RFC 6733.

    The Route-Record AVP (AVP Code 282) is of type DiameterIdentity.
    """
    code = ROUTE_RECORD_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, RouteRecordAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterIdentityType.__init__(self, data=data)


class DestinationRealmAVP(DiameterAVP, DiameterIdentityType):
    """Implementation of Destination-Realm AVP in Section 6.6 of IETF RFC 3588.

    The Destination-Realm AVP (AVP Code 283) is of type DiameterIdentity.
    """
    code = DESTINATION_REALM_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, DestinationRealmAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterIdentityType.__init__(self, data=data)


class ProxyInfoAVP(DiameterAVP, GroupedType):
    """Implementation of Proxy-Info AVP in Section 6.7.2 of IETF RFC 6733.

    The Proxy-Info AVP (AVP Code 284) is of type Grouped.
    """
    code = PROXY_INFO_AVP_CODE
    vendor_id = None

    mandatory = {
                    "proxy_host": ProxyHostAVP,
                    "proxy_state": ProxyStateAVP,
    }
    optionals = {}

    def __init__(self, data):
        DiameterAVP.__init__(self, ProxyInfoAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)


class ReAuthRequestTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Re-Auth-Request-Type AVP in Section 8.12 of 
    IETF RFC 6733.

    The Re-Auth-Request-Type AVP (AVP Code 285) is of type Enumerated.
    """
    code = RE_AUTH_REQUEST_TYPE_AVP_CODE
    vendor_id = None

    values = [
                RE_AUTH_REQUEST_TYPE_AUTHORIZE_ONLY,
                RE_AUTH_REQUEST_TYPE_AUTHORIZE_AUTHENTICATE
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, ReAuthRequestTypeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class AccountingSubSessionIdAVP(DiameterAVP, Unsigned64Type):
    """Implementation of Accounting-Sub-Session-Id AVP in Section 9.8.6 of 
    IETF RFC 6733.

    The Accounting-Sub-Session-Id AVP (AVP Code 287) is of type Unsigned64.
    """
    code = ACCOUNTING_SUB_SESSION_ID_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, AccountingSubSessionIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned64Type.__init__(self, data=data)


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


class RedirectHostAVP(DiameterAVP, DiameterURIType):
    """Implementation of Redirect-Host AVP in Section 6.12 of IETF RFC 6733.

    The Redirect-Host AVP (AVP Code 292) is of type DiameterURI.
    """
    code = REDIRECT_HOST_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, RedirectHostAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterURIType.__init__(self, data=data)


class DestinationHostAVP(DiameterAVP, DiameterIdentityType):
    """Implementation of Destination-Host AVP in Section 6.5 of IETF RFC 3588.

    The Destination-Host AVP (AVP Code 293) is of type DiameterIdentity.
    """
    code = DESTINATION_HOST_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, DestinationHostAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterIdentityType.__init__(self, data=data)


class ErrorReportingHostAVP(DiameterAVP, DiameterIdentityType):
    """Implementation of Error-Reporting-Host AVP in Section 7.4 of 
    IETF RFC 6733.

    The Error-Reporting-Host AVP (AVP Code 294) is of type DiameterIdentity.
    """
    code = ERROR_REPORTING_HOST_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, ErrorReportingHostAVP.code)
        DiameterIdentityType.__init__(self, data=data)


class TerminationCauseAVP(DiameterAVP, EnumeratedType):
    """Implementation of Termination-Cause AVP in Section 8.47 of 
    IETF RFC 6733.

    The Termination-Cause AVP (AVP Code 295) is of type Enumerated.
    """
    code = TERMINATION_CAUSE_AVP_CODE
    vendor_id = None

    values = [
                DIAMETER_LOGOUT,
                DIAMETER_SERVICE_NOT_PROVIDED,
                DIAMETER_BAD_ANSWER,
                DIAMETER_ADMINISTRATIVE,
                DIAMETER_LINK_BROKEN,
                DIAMETER_AUTH_EXPIRED,
                DIAMETER_USER_MOVED,
                DIAMETER_SESSION_TIMEOUT
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, TerminationCauseAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class OriginRealmAVP(DiameterAVP, DiameterIdentityType):
    """Implementation of Origin-Realm AVP in Section 6.4 of IETF RFC 3588.

    The Origin-Realm AVP (AVP Code 296) is of type DiameterIdentity.
    """
    code = ORIGIN_REALM_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, OriginRealmAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterIdentityType.__init__(self, data=data)


class ExperimentalResultCodeAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Experimental-Result-Code AVP in Section 7.7 of 
    IETF RFC 6733.

    The Experimental-Result-Code AVP (AVP Code 298) is of type Unsigned32.
    """
    code = EXPERIMENTAL_RESULT_CODE_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, ExperimentalResultCodeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class ExperimentalResultAVP(DiameterAVP, GroupedType):
    """Implementation of Experimental-Result AVP in Section 7.6 of 
    IETF RFC 6733.

    The Experimental-Result AVP (AVP Code 297) is of type Grouped.
    """
    code = EXPERIMENTAL_RESULT_AVP_CODE
    vendor_id = None

    mandatory = {
                    "vendor_id": VendorIdAVP,
                    "experimental_result_code": ExperimentalResultCodeAVP,
    }
    optionals = {}

    def __init__(self, data):
        DiameterAVP.__init__(self, ExperimentalResultAVP.code)
        GroupedType.__init__(self, data=data)


class InbandSecurityIdAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Inband-Security-Id AVP in Section 6.10 of 
    IETF RFC 6733.

    The Inband-Security-Id AVP (AVP Code 299) is of type Unsigned32.
    """
    code = INBAND_SECURITY_ID_AVP_CODE
    vendor_id = None

    def __init__(self, data):    
        DiameterAVP.__init__(self, InbandSecurityIdAVP.code)
        Unsigned32Type.__init__(self, data=data)


class MipHomeAgentHostAVP(DiameterAVP, GroupedType):
    """Implementation of MIP-Home-Agent-Host AVP in both Section 7.3.43 of
    ETSI TS 129 272 V15.10.0 (2020-01) and Section 4.2.3 of IETF RFC 5447.

    The MIP-Home-Agent-Host AVP (AVP Code 348) is of type Grouped.
    """
    code = MIP_HOME_AGENT_HOST_AVP_CODE
    vendor_id = None

    mandatory = {
                    "destination_host": DestinationHostAVP,
                    "destination_realm": DestinationRealmAVP,
    }
    optionals = {}

    def __init__(self, data):
        DiameterAVP.__init__(self, MipHomeAgentHostAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)


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


class SubscriptionIdAVP(DiameterAVP, GroupedType):
    """Implementation of Subscription-Id AVP in Section 8.46 of IETF RFC 4006.

    The Subscription-Id AVP (AVP Code 443) is of type Grouped.
    """
    code = SUBSCRIPTION_ID_AVP_CODE
    vendor_id = None

    mandatory = {
                    "subscription_id_data": SubscriptionIdDataAVP,
                    "subscription_id_type": SubscriptionIdTypeAVP,
    }
    optionals = {}

    def __init__(self, data):
        DiameterAVP.__init__(self, SubscriptionIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)


class EapPayloadAVP(DiameterAVP, OctetStringType):
    """Implementation of EAP-Payload AVP in Section 4.1.1 of IETF RFC 4072.

    The EAP-Payload AVP (AVP Code 462) is of type OctetString.
    """
    code = EAP_PAYLOAD_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, EapPayloadAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)    

        EapPayloadAVP.parser_data(self, data)

        OctetStringType.__init__(self, data=self.data)


    def parser_data(self, data):
        if not isinstance(data, bytes):
            if data.eap_type == EAP_TYPE_IDENTITY:
                eap_nai_data = data.content["nai"].encode("utf-8")
                eap_length = convert_to_2_bytes(len(data.eap_code + convert_to_1_byte(data.eap_id) + data.eap_type + eap_nai_data) + 2)
                
                data = data.eap_code + convert_to_1_byte(data.eap_id) + eap_length + data.eap_type + eap_nai_data
                        
            elif data.eap_type == EAP_TYPE_UMTS_AUTHENTICATION_AND_KEY_AGREEMENT_EAP:
                data = base64.b64decode(data.content["payload"])

        self.data = data


class EapMasterSessionKeyAVP(DiameterAVP, OctetStringType):
    """Implementation of EAP-Master-Session-Key AVP in Section 4.1.3
    of IETF RFC 4072.

    The EAP-Master-Session-Key AVP (AVP Code 464) is of type OctetString.
    """
    code = EAP_MASTER_SESSION_KEY_AVP_CODE
    vendor_id = None

    def __init__(self, data): 
        DiameterAVP.__init__(self, EapMasterSessionKeyAVP.code)
        OctetStringType.__init__(self, data=data)


class AccountingRecordTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Accounting-Record-Type AVP in Section 9.8.1 of 
    IETF RFC 6733.

    The Accounting-Record-Type AVP (AVP Code 480) is of type Enumerated.
    """
    code = ACCOUNTING_RECORD_TYPE_AVP_CODE
    vendor_id = None
    
    values = [
                ACCOUNTING_RECORD_TYPE_EVENT_RECORD,
                ACCOUNTING_RECORD_TYPE_START_RECORD,
                ACCOUNTING_RECORD_TYPE_INTERIM_RECORD,
                ACCOUNTING_RECORD_TYPE_STOP_RECORD
    ]

    def __init__(self, data=ACCOUNTING_RECORD_TYPE_EVENT_RECORD):
        DiameterAVP.__init__(self, AccountingRecordTypeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class AccountingRealtimeRequiredAVP(DiameterAVP, EnumeratedType):
    """Implementation of Accounting-Realtime-Required AVP in Section 9.8.7 of 
    IETF RFC 6733.

    The Accounting-Realtime-Required AVP (AVP Code 483) is of type Enumerated.
    """
    code = ACCOUNTING_REALTIME_REQUIRED_AVP_CODE
    vendor_id = None
    
    values = [
                ACCOUNTING_REALTIME_REQUIRED_DELIVER_AND_GRANT,
                ACCOUNTING_REALTIME_REQUIRED_GRANT_AND_STORE,
                ACCOUNTING_REALTIME_REQUIRED_GRAND_AND_LOSE
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, AccountingRealtimeRequiredAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class AccountingRecordNumberAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Accounting-Record-Number AVP in Section 9.8.3 of 
    IETF RFC 6733.

    The Accounting-Record-Number AVP (AVP Code 485) is of type Unsigned32.
    """
    code = ACCOUNTING_RECORD_NUMBER_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, AccountingRecordNumberAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class Mip6AgentInfoAVP(DiameterAVP, GroupedType):
    """Implementation of MIP6-Agent-Info AVP in both Section 7.3.45 of
    ETSI TS 129 272 V15.10.0 (2020-01) and Section 4.2.1 of IETF RFC 5447.

    The MIP6-Agent-Info AVP (AVP Code 486) is of type Grouped.
    """
    code = MIP6_AGENT_INFO_AVP_CODE
    vendor_id = None

    mandatory = {}
    optionals = {
                    # "mip_home_agent_address": MipHomeAgentAddressAVP,
                    "mip_home_agent_host": MipHomeAgentHostAVP,
                    # "mip_home_link_prefix": MipHomeLinkPrefixAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, Mip6AgentInfoAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)
