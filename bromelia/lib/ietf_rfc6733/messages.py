# -*- coding: utf-8 -*-
"""
    bromelia.lib.ietf_rfc6733.messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol base messages.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import platform
import socket

from ...avps import *
from ...base import DiameterRequest, DiameterAnswer
from ...constants import *
from ...exceptions import DiameterMessageError


class AbortSessionAnswer(DiameterAnswer):
    """Implementation of Abort-Session-Answer (ASA) in Section 8.5.2 of 
    IETF RFC 6733.

    The Abort-Session-Answer is indicated by the Command Code 274 and the 
    Command Flags' 'R' bit cleared.

    Usage::

        >>> from bromelia.messages import ASA
        >>> from bromelia import DIAMETER_APPLICATION_Rx
        >>> asa = ASA()
        >>> asa.header.application_id = DIAMETER_APPLICATION_Rx
        >>> asa
        <Diameter Message: 274 [ASA] PXY 3GPP Rx, 4 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "result_code": ResultCodeAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }
    optionals = {
                    "user_name": UserNameAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "error_message": ErrorMessageAVP,
                    "error_reporting_host": ErrorReportingHostAVP,
                    "failed_avp": FailedAvpAVP,
                    "redirect_host": RedirectHostAVP,
                    "redirect_host_usage": RedirectHostUsageAVP,
                    "redirect_max_cache_time": RedirectMaxCacheTimeAVP,
                    "proxy_info": ProxyInfoAVP
    }

    def __init__(self, 
                session_id=platform.node(), 
                result_code=DIAMETER_SUCCESS,
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                user_name=None,
                origin_state_id=None,
                error_message=None,
                error_reporting_host=None,
                failed_avp=None,
                redirect_host=None,
                redirect_host_usage=None,
                redirect_max_cache_time=None,
                proxy_info=None,
                **kwargs):
        
        DiameterAnswer.__init__(self, 
                                command_code=ABORT_SESSION_MESSAGE, 
                                application_id=None)

        DiameterAnswer._load(self, locals())


class AbortSessionRequest(DiameterRequest):
    """Implementation of Abort-Session-Request (ASR) in Section 8.5.1 of 
    IETF RFC 6733.

    The Abort-Session-Request is indicated by the Command Code 274 and the 
    Command Flags' 'R' bit set.

    Usage::

        >>> from bromelia.messages import ASR
        >>> from bromelia import DIAMETER_APPLICATION_Rx
        >>> asr_avps = {
        ...     "auth_application_id": DIAMETER_APPLICATION_Rx,
        ...     "destination_realm": "example.com",
        ...     "destination_host": "host.example.com"
        ... }
        >>> asr = ASR(**asr_avps)
        >>> asr
        <Diameter Message: 274 [ASR] REQ, PXY 3GPP Rx, 6 AVP(s)>
    """

    mandatory = { 
                    "session_id": SessionIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "destination_host": DestinationHostAVP,
                    "auth_application_id": AuthApplicationIdAVP
    }
    optionals = { 
                    "user_name": UserNameAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP
    }
    
    def __init__(self,
                session_id=platform.node(), 
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                destination_realm=socket.gethostbyname(platform.node()),
                destination_host=None,
                auth_application_id=None,
                user_name=None,
                origin_state_id=None,
                proxy_info=None,
                route_record=None,
                **kwargs):

        if not auth_application_id:
            raise DiameterMessageError("invalid auth_application_id value. "\
                                    "It needs to include a valid Auth "\
                                    "Application Id")

        DiameterRequest.__init__(self, 
                                 command_code=ABORT_SESSION_MESSAGE,
                                 application_id=auth_application_id)

        DiameterRequest._load(self, locals())


class CapabilitiesExchangeAnswer(DiameterAnswer):
    """Implementation of Capabilities-Exchange-Answer (CEA) in Section 5.3.2 
    of IETF RFC 6733.

    The Capabilities-Exchange-Answer is indicated by the Command Code 257 and
    the Command Flags' 'R' bit cleared.

    Usage::

        >>> from bromelia.messages import CEA
        >>> cea = CEA()
        >>> cea
        <Diameter Message: 257 [CEA], Default, 6 AVP(s)>
    """

    mandatory = {
                    "result_code": ResultCodeAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "host_ip_address": HostIpAddressAVP,
                    "vendor_id": VendorIdAVP,
                    "product_name": ProductNameAVP
    }
    optionals = {
                    "origin_state_id": OriginStateIdAVP,
                    "error_message": ErrorMessageAVP,
                    "failed_avp": FailedAvpAVP,
                    "supported_vendor_id": SupportedVendorIdAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "inband_security_id": InbandSecurityIdAVP,
                    "acct_application_id": AcctApplicationIdAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "firmware_revision": FirmwareRevisionAVP
    }

    def __init__(self, 
                result_code=DIAMETER_SUCCESS,
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                host_ip_address=socket.gethostbyname(platform.node()),
                vendor_id=0,
                product_name=PRODUCT_NAME,
                origin_state_id=None,
                error_message=None,
                failed_avp=None,
                supported_vendor_id=None,
                auth_application_id=DIAMETER_APPLICATION_DEFAULT,
                inband_security_id=None,
                acct_application_id=None,
                vendor_specific_application_id=None, 
                firmware_revision=None,
                **kwargs):

        DiameterAnswer.__init__(self,
                                command_code=CAPABILITIES_EXCHANGE_MESSAGE,
                                application_id=DIAMETER_APPLICATION_DEFAULT)

        DiameterAnswer._load(self, locals())


class CapabilitiesExchangeRequest(DiameterRequest):
    """Implementation of Capabilities-Exchange-Request (CER) in Section 5.3.1 
    of IETF RFC 6733.

    The Capabilities-Exchange-Request is indicated by the Command Code 257 and
    the Command Flags' 'R' bit set.

    Usage::

        >>> from bromelia.messages import CER
        >>> cer = CER()
        >>> cer
        <Diameter Message: 257 [CER], REQ Default, 6 AVP(s)>
    """

    mandatory = { 
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "host_ip_address": HostIpAddressAVP,
                    "vendor_id": VendorIdAVP,
                    "product_name": ProductNameAVP
    }
    optionals = { 
                    "origin_state_id": OriginStateIdAVP,
                    "supported_vendor_id": SupportedVendorIdAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "inband_security_id": InbandSecurityIdAVP,
                    "acct_application_id": AcctApplicationIdAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "firmware_revision": FirmwareRevisionAVP
    }
    
    def __init__(self, 
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                host_ip_address=socket.gethostbyname(platform.node()),
                vendor_id=VENDOR_ID_DEFAULT,
                product_name=PRODUCT_NAME,
                origin_state_id=None,
                supported_vendor_id=None,
                auth_application_id=None,
                inband_security_id=None,
                acct_application_id=None,
                vendor_specific_application_id=None, 
                firmware_revision=FIRMWARE_VERSION,
                **kwargs):

        DiameterRequest.__init__(self, 
                                command_code=CAPABILITIES_EXCHANGE_MESSAGE,
                                application_id=DIAMETER_APPLICATION_DEFAULT)

        DiameterRequest._load(self, locals())


class DeviceWatchdogAnswer(DiameterAnswer):
    """Implementation of Device-Watchdog-Answer (DWA) in Section 5.5.2 
    of IETF RFC 6733.

    The Device-Watchdog-Answer is indicated by the Command Code 280 and the
    Command Flags' 'R' bit cleared.

    Usage::

        >>> from bromelia.messages import DWA
        >>> dwa = DWA()
        >>> dwa
        <Diameter Message: 280 [DWA], Default, 3 AVP(s)>
    """

    mandatory = {
                    "result_code": ResultCodeAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP
    }
    optionals = {
                    "error_message": ErrorMessageAVP,
                    "failed_avp": FailedAvpAVP,
                    "origin_state_id": OriginStateIdAVP
    }

    def __init__(self,
                result_code=DIAMETER_SUCCESS,
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(),
                error_message=None,
                failed_avp=None,
                origin_state_id=None,
                **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=DEVICE_WATCHDOG_MESSAGE,
                                application_id=DIAMETER_APPLICATION_DEFAULT)

        DiameterAnswer._load(self, locals())


class DeviceWatchdogRequest(DiameterRequest):
    """Implementation of Device-Watchdog-Request (DWR) in Section 5.5.1 
    of IETF RFC 6733.

    The Device-Watchdog-Request is indicated by the Command Code 280 and the
    Command Flags' 'R' bit set.

    Usage::

        >>> from bromelia.messages import DWR
        >>> dwr = DWR()
        >>> dwr
        <Diameter Message: 280 [DWR], REQ Default, 2 AVP(s)>
    """

    mandatory = {
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }
    optionals = {
                    "origin_state_id": OriginStateIdAVP
    }
    
    def __init__(self,
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                origin_state_id=None,
                **kwargs):

        DiameterRequest.__init__(self, 
                                command_code=DEVICE_WATCHDOG_MESSAGE,
                                application_id=DIAMETER_APPLICATION_DEFAULT)

        DiameterRequest._load(self, locals())


class DisconnectPeerAnswer(DiameterAnswer):
    """Implementation of Disconnect-Peer-Answer (DPA) in Section 5.4.2 
    of IETF RFC 6733.

    The Disconnect-Peer-Answer is indicated by the Command Code 282 and
    the Command Flags' 'R' bit cleared.

    Usage::

        >>> from bromelia.messages import DPA
        >>> dpa = DPA()
        >>> dpa
        <Diameter Message: 282 [DPA], Default, 3 AVP(s)>
    """
    mandatory = {
                    "result_code": ResultCodeAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }
    optionals = {
                    "error_message": ErrorMessageAVP,
                    "failed_avp": FailedAvpAVP
    }

    def __init__(self,
                result_code=DIAMETER_SUCCESS,
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                error_message=None,
                failed_avp=None,
                **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=DISCONNECT_PEER_MESSAGE,
                                application_id=DIAMETER_APPLICATION_DEFAULT)

        DiameterAnswer._load(self, locals())


class DisconnectPeerRequest(DiameterRequest):
    """Implementation of Disconnect-Peer-Request (DPR) in Section 5.4.1 
    of IETF RFC 6733.

    The Disconnect-Peer-Request is indicated by the Command Code 282 and
    the Command Flags' 'R' bit set.

    Usage::

        >>> from bromelia.messages import DPR
        >>> dpr = DPR()
        >>> dpr
        <Diameter Message: 282 [DPR], REQ Default, 3 AVP(s)>
    """

    mandatory = {
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "disconnect_cause": DisconnectCauseAVP,
    }
    optionals = {}

    def __init__(self,
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                disconnect_cause=DISCONNECT_CAUSE_REBOOTING,
                **kwargs):

        DiameterRequest.__init__(self, 
                                command_code=DISCONNECT_PEER_MESSAGE,
                                application_id=DIAMETER_APPLICATION_DEFAULT)

        DiameterRequest._load(self, locals())


class ReAuthAnswer(DiameterAnswer):
    """Implementation of Re-Auth-Answer (RAA) in Section 8.3.2 of 
    IETF RFC 6733.

    The Re-Auth-Answer is indicated by the Command Code 258 and the Command 
    Flags' 'R' bit cleared.

    Usage::

        >>> from bromelia.messages import RAA
        >>> from bromelia import DIAMETER_APPLICATION_Rx
        >>> raa = RAA()
        >>> raa.header.application_id = DIAMETER_APPLICATION_Rx
        >>> raa
        <Diameter Message: 258 [RAA] PXY 3GPP Rx, 4 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "result_code": ResultCodeAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }
    optionals = {
                    "user_name": UserNameAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "error_message": ErrorMessageAVP,
                    "error_reporting_host": ErrorReportingHostAVP,
                    "failed_avp": FailedAvpAVP,
                    "redirect_host": RedirectHostAVP,
                    "redirect_host_usage": RedirectHostUsageAVP,
                    "redirect_max_cache_time": RedirectMaxCacheTimeAVP,
                    "proxy_info": ProxyInfoAVP
    }

    def __init__(self, 
                session_id=platform.node(), 
                result_code=DIAMETER_SUCCESS,
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                user_name=None,
                origin_state_id=None,
                error_message=None,
                error_reporting_host=None,
                failed_avp=None,
                redirect_host=None,
                redirect_host_usage=None,
                redirect_max_cache_time=None,
                proxy_info=None,
                **kwargs):
        
        DiameterAnswer.__init__(self, 
                                command_code=RE_AUTH_MESSAGE, 
                                application_id=None)

        DiameterAnswer._load(self, locals())


class ReAuthRequest(DiameterRequest):
    """Implementation of Re-Auth-Request (RAR) in Section 8.3.1 of 
    IETF RFC 6733.

    The Re-Auth-Request is indicated by the Command Code 258 and the 
    Command Flags' 'R' bit set.

    Usage::

        >>> from bromelia.messages import RAR
        >>> from bromelia import DIAMETER_APPLICATION_Gx
        >>> from bromelia import AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY
        >>> rar_avps = {
        ...     "auth_application_id": DIAMETER_APPLICATION_Gx,
        ...     "destination_realm": "example.com",
        ...     "destination_host": "host.example.com",
        ...     "re_auth_request_type": AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY
        ... }
        >>> rar = RAR(**rar_avps)
        >>> rar
        <Diameter Message: 258 [RAR] REQ, PXY 3GPP Gx, 7 AVP(s)>
    """

    mandatory = { 
                    "session_id": SessionIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "destination_host": DestinationHostAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "re_auth_request_type": ReAuthRequestTypeAVP
    }
    optionals = { 
                    "user_name": UserNameAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP
    }
    
    def __init__(self,
                session_id=platform.node(), 
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                destination_realm=socket.gethostbyname(platform.node()),
                destination_host=None,
                auth_application_id=None,
                re_auth_request_type=None,
                user_name=None,
                origin_state_id=None,
                proxy_info=None,
                route_record=None,
                **kwargs):

        if not auth_application_id:
            raise DiameterMessageError("invalid auth_application_id value. "\
                                    "It needs to include a valid Auth "\
                                    "Application Id")

        DiameterRequest.__init__(self, 
                                 command_code=RE_AUTH_MESSAGE, 
                                 application_id=auth_application_id)

        DiameterRequest._load(self, locals())


class SessionTerminationAnswer(DiameterAnswer):
    """Implementation of Session-Termination-Answer (STA) in Section 8.4.2 
    of IETF RFC 6733.

    The Session-Termination-Answer is indicated by the Command Code 275 and
    the Command Flags' 'R' bit cleared.

    Usage::

        >>> from bromelia.messages import SessionTerminationAnswer as STA
        >>> sta = STA()
        >>> sta
        <Diameter Message: 275 [STA], Default, 4 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "result_code": ResultCodeAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }
    optionals = {
                    "user_name": UserNameAVP,
                    "_class": ClassAVP,
                    "error_message": ErrorMessageAVP,
                    "error_reporting_host": ErrorReportingHostAVP,
                    "failed_avp": FailedAvpAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "redirect_host": RedirectHostAVP,
                    "redirect_host_usage": RedirectHostUsageAVP,
                    "redirect_max_cache_time": RedirectMaxCacheTimeAVP,
                    "proxy_info": ProxyInfoAVP
    }

    def __init__(self,
                session_id=platform.node(), 
                result_code=DIAMETER_SUCCESS, 
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                user_name=None,
                _class=None,
                error_message=None,
                error_reporting_host=None,
                failed_avp=None,
                origin_state_id=None,
                redirect_host=None,
                redirect_host_usage=None,
                redirect_max_cache_time=None,
                proxy_info=None,
                **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=SESSION_TERMINATION_MESSAGE,
                                application_id=DIAMETER_APPLICATION_DEFAULT)

        DiameterAnswer._load(self, locals())


class SessionTerminationRequest(DiameterRequest):
    """Implementation of Session-Termination-Request (STR) in Section 8.4.1 
    of IETF RFC 6733.

    The Session-Termination-Request is indicated by the Command Code 275 and
    the Command Flags' 'R' bit set.

    Usage::

        >>> from bromelia.messages import SessionTerminationRequest as STR
        >>> _str = STR()
        >>> _str
        <Diameter Message: 275 [STR], REQ Default, 6 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "termination_cause": TerminationCauseAVP,
    }
    optionals = {
                    "user_name": UserNameAVP,
                    "destination_host": DestinationHostAVP,
                    "_class": ClassAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP
    }

    def __init__(self,
                session_id=platform.node(), 
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                destination_realm=socket.gethostbyname(platform.node()),
                auth_application_id=DIAMETER_APPLICATION_DEFAULT,
                termination_cause=DIAMETER_LOGOUT,
                user_name=None,
                destination_host=None,
                _class=None,
                origin_state_id=None,
                proxy_info=None,
                route_record=None,
                **kwargs):

        DiameterRequest.__init__(self, 
                                command_code=SESSION_TERMINATION_MESSAGE,
                                application_id=DIAMETER_APPLICATION_DEFAULT)

        DiameterRequest._load(self, locals())