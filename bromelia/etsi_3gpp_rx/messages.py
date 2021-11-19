# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_rx.messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages for 3GPP Rx
    Application Id.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import platform
import socket

from .avps import *

from .._internal_utils import show_warn
from ..base import DiameterRequest, DiameterAnswer
from ..constants import *

show_warn("messages", "etsi_3gpp_rx")


class AAAnswer(DiameterAnswer):
    """Implementation of AA-Answer (CCA) command as per clause 5.6.2 
    of ETSI TS 129 214 V15.4.0 (2018-07).

    The AA-Answer is indicated by the Command Code field 
    set to 265 and Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_rx.messages import AAAnswer as AAA
        >>> aaa = AAA()
        >>> aaa
        <Diameter Message: 265 [AAA] PXY, 16777236 [3GPP Rx], 5 AVP(s)>   
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }
    optionals = { 
                    #"drmp": DrmpAVP,
                    "result_code": ResultCodeAVP,
                    "experimental_result": ExperimentalResultAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    # "access_network_charging_identifier": AccessNetworkChargingIdentifierAVP,
                    "access_network_charging_address": AccessNetworkChargingAddressAVP,
                    # "acceptable_service_info": AcceptableServiceInfoAVP,
                    "an_gw_address": AnGwAddressAVP,
                    "an_trusted": AnTrustedAVP,
                    # "service_authorization_info": ServiceAuthorizationInfoAVP,
                    "ip_can_type": IpCanTypeAVP,
                    # "netloc_access_support": NetlocAccessSupportAVP,
                    "rat_type": RatTypeAVP,
                    # "flows": FlowsAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    # "oc_olr": OcOlrAVP,
                    "supported_features": SupportedFeaturesAVP,
                    "subscription_id": SubscriptionIdAVP,
                    "user_equipment_info": UserEquipmentInfoAVP,
                    # "x3gpp_sgsn_mcc_mnc": X3gppSgsnMccMncAVP,
                    "_class": ClassAVP,
                    "error_message": ErrorMessageAVP,
                    # "error_reporting": ErrorReportingAVP,
                    "failed_avp": FailedAvpAVP,
                    # "retry_interval": RetryIntervalAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "redirect_host": RedirectHostAVP,
                    "redirect_host_usage": RedirectHostUsageAVP,
                    "redirect_max_cache_time": RedirectMaxCacheTimeAVP,
                    "proxy_info": ProxyInfoAVP,
                    # "load": LoadAVP
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 auth_application_id=DIAMETER_APPLICATION_Rx,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 result_code=DIAMETER_SUCCESS,
                 experimental_result=None,
                 auth_session_state=None,
                 access_network_charging_identifier=None,
                 access_network_charging_address=None,
                 acceptable_service_info=None,
                 an_gw_address=None,
                 an_trusted=None,
                 service_authorization_info=None,
                 ip_can_type=None,
                 netloc_access_support=None,
                 rat_type=None,
                 flows=None,
                 oc_supported_features=None,
                 oc_olr=None,
                 supported_features=None,
                 subscription_id=None,
                 user_equipment_info=None,
                 x3gpp_sgsn_mcc_mnc=None,
                 _class=None,
                 error_message=None,
                 error_reporting=None,
                 failed_avp=None,
                 retry_interval=None,
                 origin_state_id=None,
                 redirect_host=None,
                 redirect_host_usage=None,
                 redirect_max_cache_time=None,
                 proxy_info=None,
                 load=None,
                 **kwargs):

        DiameterAnswer.__init__(self,
                                 command_code=AA_MESSAGE, 
                                 application_id=DIAMETER_APPLICATION_Rx)

        DiameterAnswer._load(self, locals())


class AARequest(DiameterRequest):
    """Implementation of AA-Request (AAR) command as per clause 5.6.1 
    of ETSI TS 129 214 V15.4.0 (2018-07).

    The AA-Request is indicated by the Command Code field 
    set to 265 and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.etsi_3gpp_rx.messages import AARequest as AAR
        >>> aar_avps = {
        ...     "destination_realm": "remote",
        ... }
        >>> aar = AAR(**aar_avps)
        >>> aar
        <Diameter Message: 265 [AAR] REQ|PXY, 16777236 [3GPP Rx], 5 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
    }
    optionals = {
                    #"drmp": DrmpAVP,
                    "destination_host": DestinationHostAVP,
                    # "ip_domain_id": IpDomainIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "af_application_identifier": AfApplicationIdentifierAVP,
                    "media_component_description": MediaComponentDescriptionAVP,
                    "service_info_status": ServiceInfoStatusAVP,
                    "af_charging_identifier": AfChargingIdentifierAVP,
                    # "sip_forking_indication": SipForkingIndicationAVP,
                    "specific_action": SpecificActionAVP,
                    "subscription_id": SubscriptionIdAVP,
                    # "oc_supported_features": OcSupportedAVP,
                    "supported_features": SupportedFeaturesAVP,
                    "reservation_priority": ReservationPriorityAVP,
                    "framed_ip_address": FramedIpAddressAVP,
                    "framed_ipv6_prefix": FramedIpv6PrefixAVP,
                    "called_station_id": CalledStationIdAVP,
                    # "service_urn": ServiceUrnAVP,
                    # "sponsored_connectivity_data": SponsoredConnectivityDataAVP,
                    # "mps_identifier": MpsIdentifierAVP,
                    # "gcs_identifier": GcsIdentifierAVP,
                    # "mcptt_identifier": McpttIdentifierAVP,
                    # "mcvideo_identifier": McvideoIdentifierAVP,
                    # "ims_content_identifier": ImsContentIdentifierAVP,
                    # "ims_content_type": ImsContentTypeAVP,
                    # "rx_request_type": RxRequestTypeAVP,
                    # "required_access_info": RequiredAccessInfoAVP,
                    # "af_requested_data": AfRequestedDataAVP,
                    # "reference_id": ReferenceIdAVP,
                    # "pre_emption_control_info": PreEmptionControlInfoAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self,
                 session_id=platform.node(), 
                 drmp=None,
                 auth_application_id=DIAMETER_APPLICATION_Rx,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 destination_realm=None,
                 destination_host=None,
                 ip_domain_id=None,
                 auth_session_state=None,
                 af_application_identifier=None,
                 media_component_description=None,
                 service_info_status=None,
                 af_charging_identifier=None,
                 sip_forking_indication=None,
                 specific_action=None,
                 subscription_id=None,
                 oc_supported_features=None,
                 supported_features=None,
                 reservation_priority=None,
                 framed_ip_address=None,
                 framed_ipv6_prefix=None,
                 called_station_id=None,
                 service_urn=None,
                 sponsored_connectivity_data=None,
                 mps_identifier=None,
                 gcs_identifier=None,
                 mcptt_identifier=None,
                 mcvideo_identifier=None,
                 ims_content_identifier=None,
                 ims_content_type=None,
                 rx_request_type=None,
                 required_access_info=None,
                 af_requested_data=None,
                 reference_id=None,
                 pre_emption_control_info=None,
                 origin_state_id=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterRequest.__init__(self,
                                 command_code=AA_MESSAGE, 
                                 application_id=DIAMETER_APPLICATION_Rx)

        DiameterRequest._load(self, locals())


class AbortSessionAnswer(DiameterAnswer):
    """Implementation of Abort-Session-Answer (ASA) command as per clause 5.6.8 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Abort-Session-Answer is indicated by the Command Code 274 and the 
    Command Flags' 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_rx.messages import AbortSessionAnswer as ASA
        >>> asa = ASA()
        >>> asa
        <Diameter Message: 274 [ASA] PXY, 16777236 [3GPP Rx], 4 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }
    optionals = {
                    # "drmp": DrmpAVP,
                    "result_code": ResultCodeAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    # "oc_olr": OcOlrAVP,
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
                 drmp=None,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 result_code=DIAMETER_SUCCESS,
                 oc_supported_features=None,
                 oc_olr=None,
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
                                application_id=DIAMETER_APPLICATION_Rx)

        DiameterAnswer._load(self, locals())


class AbortSessionRequest(DiameterRequest):
    """Implementation of Abort-Session-Request (ASR) command as per clause 5.6.7 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Abort-Session-Request is indicated by the Command Code 274 and the 
    Command Flags' 'R' bit set.

    Usage::

        >>> from bromelia.etsi_3gpp_rx.messages import AbortSessionRequest as ASR
        >>> asr_avps = {
        ...     "destination_host": "host.example.com"
        ... }
        >>> asr = ASR(**asr_avps)
        >>> asr
        <Diameter Message: 274 [ASR] REQ|PXY, 16777236 [3GPP Rx], 7 AVP(s)>
    """

    mandatory = { 
                    "session_id": SessionIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "destination_host": DestinationHostAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "abort_cause": AbortCauseAVP,
    }
    optionals = { 
                    # "drmp": DrmpAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP
    }
    
    def __init__(self,
                session_id=platform.node(), 
                drmp=None,
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                destination_realm=socket.gethostbyname(platform.node()),
                destination_host=None,
                auth_application_id=DIAMETER_APPLICATION_Rx,
                oc_supported_features=None,
                abort_cause=ABORT_CAUSE_BEARER_RELEASED,
                origin_state_id=None,
                proxy_info=None,
                route_record=None,
                **kwargs):

        DiameterRequest.__init__(self, 
                                 command_code=ABORT_SESSION_MESSAGE,
                                 application_id=DIAMETER_APPLICATION_Rx)

        DiameterRequest._load(self, locals())


class ReAuthAnswer(DiameterAnswer):
    """Implementation of Re-Auth-Answer (RAA) command as per clause 5.6.4 
    of ETSI TS 129 214 V15.4.0 (2018-07).

    The Re-Auth-Answer is indicated by the Command Code field 
    set to 258 and Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_rx.messages import ReAuthAnswer as RAA
        >>> raa = RAA()
        >>> raa
        <Diameter Message: 258 [RAA] PXY, 16777236 [3GPP Rx], 4 AVP(s)>   
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }
    optionals = { 
                    #"drmp": DrmpAVP,
                    "result_code": ResultCodeAVP,
                    "experimental_result": ExperimentalResultAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    # "oc_olr": OcOlrAVP,
                    "media_component_description": MediaComponentDescriptionAVP,
                    # "service_urn": ServiceUrnAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "_class": ClassAVP,
                    "error_message": ErrorMessageAVP,
                    "error_reporting_host": ErrorReportingHostAVP,
                    "redirect_host": RedirectHostAVP,
                    "redirect_host_usage": RedirectHostUsageAVP,
                    "redirect_max_cache_time": RedirectMaxCacheTimeAVP,
                    "failed_avp": FailedAvpAVP,
                    "proxy_info": ProxyInfoAVP
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 result_code=DIAMETER_SUCCESS,
                 experimental_result=None,
                 oc_supported_features=None,
                 oc_olr=None,
                 media_component_description=None,
                 service_urn=None,
                 origin_state_id=None,
                 _class=None,
                 error_message=None,
                 error_reporting_host=None,
                 redirect_host=None,
                 redirect_host_usage=None,
                 redirect_max_cache_time=None,
                 failed_avp=None,
                 proxy_info=None,
                 **kwargs):

        DiameterAnswer.__init__(self,
                                 command_code=RE_AUTH_MESSAGE, 
                                 application_id=DIAMETER_APPLICATION_Rx)

        DiameterAnswer._load(self, locals())


class ReAuthRequest(DiameterRequest):
    """Implementation of Re-Auth-Request (RAR) command as per clause 5.6.3 
    of ETSI TS 129 214 V15.4.0 (2018-07).

    The Re-Auth-Request is indicated by the Command Code field 
    set to 258 and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.etsi_3gpp_rx.messages import ReAuthRequest as RAR
        >>> rar_avps = {
        ...     "destination_realm": "remote",
        ...     "destination_host": "remote"
        ... }
        >>> rar = RAR(**rar_avps)
        >>> rar
        <Diameter Message: 258 [RAR] REQ|PXY, 16777236 [3GPP Rx], 6 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "destination_host": DestinationHostAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "specific_action": SpecificActionAVP,
    }
    optionals = {
                    #"drmp": DrmpAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    # "access_network_charging_identifier": AccessNetworkChargingIdentifierAVP,
                    "access_network_charging_address": AccessNetworkChargingAddressAVP,
                    "an_gw_address": AnGwAddressAVP,
                    "an_trusted": AnTrustedAVP,
                    # "flows": FlowsAVP,
                    "subscription_id": SubscriptionIdAVP,
                    # "abort_cause": AbortCauseAVP,
                    "ip_can_type": IpCanTypeAVP,
                    # "netloc_access_support": NetlocAccessSupportAVP,
                    "rat_type": RatTypeAVP,
                    # "sponsored_connectivity_data": SponsoredConnectivityDataAVP,
                    # "x3gpp_user_location_info": X3gppUserLocationInfoAVP,
                    # "user_location_info_time": UserLocationInfoTimeAVP,
                    # "x3gpp_ms_timezone": X3gppMsTimezoneAVP,
                    # "ran_nas_release_cause": RanNasReleaseCauseAVP,
                    # "x3gpp_sgsn_mcc_mnc": X3gppSgsnMccMncAVP,
                    # "twan_identifier": TwanIdentifierAVP,
                    # "tcp_source_port": TcpSourcePortAVP,
                    # "udp_source_port": UdpSourcePortAVP,
                    "ue_local_ip_address": UeLocalIpAddressAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "_class": ClassAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self,
                 session_id=platform.node(), 
                 drmp=None,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 destination_realm=None,
                 destination_host=None,
                 auth_application_id=DIAMETER_APPLICATION_Rx,
                 specific_action=None,
                 oc_supported_features=None,
                 access_network_charging_identifier=None,
                 access_network_charging_address=None,
                 an_gw_address=None,
                 an_trusted=None,
                 flows=None,
                 subscription_id=None,
                 abort_cause=None,
                 ip_can_type=None,
                 netloc_access_support=None,
                 rat_type=None,
                 sponsored_connectivity_data=None,
                 x3gpp_user_location_info=None,
                 user_location_info_time=None,
                 x3gpp_ms_timezone=None,
                 ran_nas_release_cause=None,
                 x3gpp_sgsn_mcc_mnc=None,
                 twan_identifier=None,
                 tcp_source_port=None,
                 udp_source_port=None,
                 ue_local_ip_address=None,
                 origin_state_id=None,
                 _class=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterRequest.__init__(self,
                                 command_code=RE_AUTH_MESSAGE, 
                                 application_id=DIAMETER_APPLICATION_Rx)

        DiameterRequest._load(self, locals())


class SessionTerminationAnswer(DiameterAnswer):
    """Implementation of Session-Termination-Answer (STA) command as per 
    clause 5.6.6 of ETSI TS 129 214 V15.4.0 (2018-07).

    The Session-Termination-Answer is indicated by the Command Code 275 and
    the Command Flags' 'R' bit cleared.

    Usage::
        >>> from bromelia.etsi_3gpp_rx.messages import SessionTerminationAnswer as STA
        >>> sta = STA()
        >>> sta
        <Diameter Message: 275 [STA] PXY, 16777236 [3GPP Rx], 4 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }
    optionals = {
                    # "drmp": DrmpAVP,
                    "result_code": ResultCodeAVP,
                    "error_message": ErrorMessageAVP,
                    "error_reporting_host": ErrorReportingHostAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    # "oc_olr": OcOlrAVP,
                    "failed_avp": FailedAvpAVP,
                    # "sponsored_connectivity_data": SponsoredConnectivityDataAVP,
                    "origin_state_id": OriginStateIdAVP,
                    # "x3gpp_user_location_info": X3gppUserLocationInfoAVP,
                    # "user_location_info_time": UserLocationInfoTimeAVP,
                    # "x3gpp_ms_timezone": X3gppMsTimezoneAVP,
                    # "ran_nas_release_cause": RanNasReleaseCauseAVP,
                    # "x3gpp_sgsn_mcc_mnc": X3gppSgsnMccMncAVP,
                    # "twan_identifier": TwanIdentifierAVP,
                    # "tcp_source_port": TcpSourcePortAVP,
                    # "udp_source_port": UdpSourcePortAVP,
                    "ue_local_ip_address": UeLocalIpAddressAVP,
                    # "netloc_access_support": NetlocAccessSupportAVP,
                    "_class": ClassAVP,
                    "redirect_host": RedirectHostAVP,
                    "redirect_host_usage": RedirectHostUsageAVP,
                    "redirect_max_cache_time": RedirectMaxCacheTimeAVP,
                    "proxy_info": ProxyInfoAVP,
                    # "load": LoadAVP
    }

    def __init__(self,
                session_id=platform.node(), 
                drmp=None,
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                result_code=DIAMETER_SUCCESS, 
                error_message=None,
                error_reporting_host=None,
                oc_supported_features=None,
                oc_olr=None,
                failed_avp=None,
                sponsored_connectivity_data=None,
                origin_state_id=None,
                x3gpp_user_location_info=None,
                user_location_info_time=None,
                x3gpp_ms_timezone=None,
                ran_nas_release_cause=None,
                x3gpp_sgsn_mcc_mnc=None,
                twan_identifier=None,
                tcp_source_port=None,
                udp_source_port=None,
                ue_local_ip_address=None,
                netloc_access_support=None,
                _class=None,
                redirect_host=None,
                redirect_host_usage=None,
                redirect_max_cache_time=None,
                proxy_info=None,
                load=None,
                **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=SESSION_TERMINATION_MESSAGE,
                                application_id=DIAMETER_APPLICATION_Rx)

        DiameterAnswer._load(self, locals())


class SessionTerminationRequest(DiameterRequest):
    """Implementation of Session-Termination-Request (STR) command as per 
    clause 5.6.5 of ETSI TS 129 214 V15.4.0 (2018-07).

    The Session-Termination-Request is indicated by the Command Code 275 and
    the Command Flags' 'R' bit set.

    Usage::

        >>> from bromelia.etsi_3gpp_rx.messages import SessionTerminationRequest as STR
        >>> _str = STR()
        >>> _str
        <Diameter Message: 275 [STR] REQ|PXY, 16777236 [3GPP Rx], 6 AVP(s)>
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
                    # "drmp": DrmpAVP,
                    "destination_host": DestinationHostAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    # "required_access_info": RequiredAccessInfoAVP,
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
                                application_id=DIAMETER_APPLICATION_Rx)

        DiameterRequest._load(self, locals())
