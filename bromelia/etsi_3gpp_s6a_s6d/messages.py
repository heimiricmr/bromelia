# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_s6a_s6d.messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages for 3GPP S6a/S6d 
    Application Id.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import platform
import socket

from .avps import *

from .._internal_utils import show_warn
from ..base import DiameterAnswer, DiameterRequest 
from ..constants import *

show_warn("messages", "etsi_3gpp_s6a_s6d", "etsi_3gpp_s6a")


class AuthenticationInformationRequest(DiameterRequest):
    """Implementation of Authentication-Information-Request (AIR) command as per 
    clause 7.2.5 of ETSI TS 129 272 V15.4.0 (2018-07).

    The Authentication-Information-Request is indicated by the Command Code 
    field set to 318 and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.etsi_3gpp_s6a_s6d.messages import AuthenticationInformationRequest as AIR
        >>> air_avps = {
        ...     "destination_realm": "example.com",
        ...     "user_name": "frodo",
        ...     "visited_plmn_id": bytes.fromhex("ffffff")
        ... }
        >>> air = AIR(**air_avps)
        >>> air
        <Diameter Message: 318 [AIR] REQ|PXY, 16777251 [3GPP S6a], 8 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "user_name": UserNameAVP,
                    "visited_plmn_id": VisitedPlmnIdAVP,
    }

    optionals = {
                    # "drmp": DrmpAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "destination_host": DestinationHostAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    "supported_features": SupportedFeaturesAVP,
                    "requested_eutran_authentication_info": RequestedEutranAuthenticationInfoAVP,
                    # "requested_utran_geran_authentication_info": RequestedUtranGeranAuthenticationInfoAVP,
                    "air_flags": AirFlagsAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self, 
                 session_id=platform.node(), 
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)],
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 destination_host=None,
                 destination_realm=None,
                 user_name=None,
                 oc_supported_features=None,
                 supported_features=None,
                 requested_eutran_authentication_info=None,
                 requested_utran_geran_authentication_info=None,
                 visited_plmn_id=None,
                 air_flags=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterRequest.__init__(self, 
                                 command_code=AUTHENTICATION_INFORMATION_MESSAGE, 
                                 application_id=DIAMETER_APPLICATION_S6a_S6d)

        DiameterRequest._load(self, locals())


class AuthenticationInformationAnswer(DiameterAnswer):
    """Implementation of Authentication-Information-Answer (AIA) command as per 
    clause 7.2.6 of ETSI TS 129 272 V15.4.0 (2018-07).

    The Authentication-Information-Answer is indicated by the Command Code field
    set to 318 and Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_s6a_s6d.messages import AuthenticationInformationAnswer as AIA
        >>> aia = AIA()
        >>> aia
        <Diameter Message: 318 [AIA] PXY, 16777251 [3GPP S6a], 5 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }

    optionals = { 
                    # "drmp": DrmpAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "result_code": ResultCodeAVP,
                    "experimental_result": ExperimentalResultAVP,
                    "error_diagnostic": ErrorDiagnosticAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    # "oc_olr": OcOlrAVP,
                    # "load": LoadAVP,
                    "supported_features": SupportedFeaturesAVP,
                    "authentication_info": AuthenticationInfoAVP,
                    "ue_usage_type": UeUsageTypeAVP,
                    "failed_avp": FailedAvpAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)],
                 result_code=None,
                 experimental_result=None,
                 error_diagnostic=None,
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 oc_supported_features=None,
                 oc_olr=None,
                 load=None,
                 supported_features=None,
                 authentication_info=None,
                 ue_usage_type=None,
                 failed_avp=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=AUTHENTICATION_INFORMATION_MESSAGE, 
                                application_id=DIAMETER_APPLICATION_S6a_S6d)

        DiameterAnswer._load(self, locals())


class CancelLocationRequest(DiameterRequest):
    """Implementation of Cancel-Location-Request (CLR) command as per 
    clause 7.2.7 of ETSI TS 129 272 V15.4.0 (2018-07).

    The Cancel-Location-Request is indicated by the Command Code field set to 
    317 and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.etsi_3gpp_s6a_s6d.messages import CancelLocationRequest as CLR
        >>> clr_avps = {
        ...     "destination_realm": "example.com",
        ...     "destination_host": "host.example.com",
        ...     "user_name": "frodo"
        ... }
        >>> clr = CLR(**clr_avps)
        >>> clr
        <Diameter Message: 317 [CLR] REQ|PXY, 16777251 [3GPP S6a], 9 AVP(s)>
    """    

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_host": DestinationHostAVP,
                    "destination_realm": DestinationRealmAVP,
                    "user_name": UserNameAVP,
                    "cancellation_type": CancellationTypeAVP,
    }

    optionals = {
                    # "drmp": DrmpAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "supported_features": SupportedFeaturesAVP,
                    "clr_flags": ClrFlagsAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self, 
                 session_id=platform.node(), 
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)],
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 destination_host=None,
                 destination_realm=None,
                 user_name=None,
                 supported_features=None,
                 cancellation_type=CANCELLATION_TYPE_SUBSCRIPTION_WITHDRAWAL,
                 clr_flags=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterRequest.__init__(self, 
                                 command_code=CANCEL_LOCATION_MESSAGE, 
                                 application_id=DIAMETER_APPLICATION_S6a_S6d)

        DiameterRequest._load(self, locals())


class CancelLocationAnswer(DiameterAnswer):
    """Implementation of Cancel-Location-Answer (CLA) command as per 
    clause 7.2.8 of ETSI TS 129 272 V15.4.0 (2018-07).

    The Cancel-Location-Answer is indicated by the Command Code field set to 
    317 and Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_s6a_s6d.messages import CancelLocationAnswer as CLA
        >>> cla = CLA()
        >>> cla
        <Diameter Message: 317 [CLA] PXY, 16777251 [3GPP S6a], 5 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }

    optionals = { 
                    # "drmp": DrmpAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "supported_features": SupportedFeaturesAVP,
                    "result_code": ResultCodeAVP,
                    "experimental_result": ExperimentalResultAVP,
                    "failed_avp": FailedAvpAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)],
                 supported_features=None,
                 result_code=None,
                 experimental_result=None,
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 failed_avp=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=CANCEL_LOCATION_MESSAGE, 
                                application_id=DIAMETER_APPLICATION_S6a_S6d)

        DiameterAnswer._load(self, locals())


class NotifyRequest(DiameterRequest):
    """Implementation of Notify-Request (NOR) command as per clause 7.2.17 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The Notify-Request is indicated by the Command Code field set to 323 and 
    the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.etsi_3gpp_s6a_s6d.messages import NotifyRequest as NOR
        >>> nor_avps = {
        ...     "destination_realm": "example.com",
        ...     "user_name": "frodo",
        ... }
        >>> nor = NOR(**nor_avps)
        >>> nor
        <Diameter Message: 323 [NOR] REQ|PXY, 16777251 [3GPP S6a], 8 AVP(s)>
    """    

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "user_name": UserNameAVP,
    }

    optionals = {
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    # "drmp": DrmpAVP,
                    "destination_host": DestinationHostAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    "supported_features": SupportedFeaturesAVP,
                    "terminal_information": TerminalInformationAVP,
                    "mip6_agent_info": Mip6AgentInfoAVP,
                    "visited_network_identifier": VisitedNetworkIdentifierAVP,
                    "context_identifier": ContextIdentifierAVP,
                    "service_selection": ServiceSelectionAVP,
                    "alert_reason": AlertReasonAVP,
                    "ue_srvcc_capability": UeSrvccCapabilityAVP,
                    "nor_flags": NorFlagsAVP,
                    "homogeneous_support_of_ims_voice_over_ps_sessions": HomogeneousSupportOfImsVoiceOverPsSessionsAVP,
                    # "maximum_ue_availability_time": MaximumUeAvailabilityTimeAVP,
                    # "monitoring_event_config_status": MonitoringEventConfigStatusAVP,
                    # "emergency_services": EmergencyServicesAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self, 
                 session_id=platform.node(), 
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)],
                 drmp=None,
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 destination_host=None,
                 destination_realm=None,
                 user_name=None,
                 oc_supported_features=None,
                 supported_features=None,
                 terminal_information=None,
                 mip6_agent_info=None,
                 visited_network_identifier=None,
                 context_identifier=None,
                 service_selection=None,
                 alert_reason=None,
                 ue_srvcc_capability=None,
                 nor_flags=None,
                 homogeneous_support_of_ims_voice_over_ps_sessions=None,
                 maximum_ue_availability_time=None,
                 monitoring_event_config_status=None,
                 emergency_services=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterRequest.__init__(self, 
                                 command_code=NOTIFY_MESSAGE, 
                                 application_id=DIAMETER_APPLICATION_S6a_S6d)

        DiameterRequest._load(self, locals())


class NotifyAnswer(DiameterAnswer):
    """Implementation of Notify-Answer (NOA) command as per clause 7.2.18 of
    ETSI TS 129 272 V15.4.0 (2018-07).

    The Notify-Answer is indicated by the Command Code field set to 323 and
    Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_s6a_s6d.messages import NotifyAnswer as NOA
        >>> noa = NOA()
        >>> noa
        <Diameter Message: 323 [NOA] PXY, 16777251 [3GPP S6a], 5 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }

    optionals = { 
                    # "drmp": DrmpAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "result_code": ResultCodeAVP,
                    "experimental_result": ExperimentalResultAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    # "oc_olr": OcOlrAVP,
                    # "load": LoadAVP,
                    "supported_features": SupportedFeaturesAVP,
                    "failed_avp": FailedAvpAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)],
                 result_code=None,
                 experimental_result=None,
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 oc_supported_features=None,
                 oc_olr=None,
                 load=None,
                 supported_features=None,
                 failed_avp=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=NOTIFY_MESSAGE, 
                                application_id=DIAMETER_APPLICATION_S6a_S6d)

        DiameterAnswer._load(self, locals())


class PurgeUeRequest(DiameterRequest):
    """Implementation of Purge-UE-Request (PUR) command as per clause 7.2.13 of
    ETSI TS 129 272 V15.4.0 (2018-07).

    The Purge-UE-Request is indicated by the Command Code field set to 321 and
    the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.etsi_3gpp_s6a_s6d.messages import PurgeUeRequest as PUR
        >>> pur_avps = {
        ...     "destination_realm": "example.com",
        ...     "user_name": "frodo",
        ... }
        >>> pur = PUR(**pur_avps)
        >>> pur
        <Diameter Message: 321 [PUR] REQ|PXY, 16777251 [3GPP S6a], 8 AVP(s)>
    """    

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "user_name": UserNameAVP,
    }

    optionals = {
                    # "drmp": DrmpAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "destination_host": DestinationHostAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    "pur_flags": PurFlagsAVP,
                    "supported_features": SupportedFeaturesAVP,
                    # "eps_location_information": EpsLocationInformationAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self, 
                 session_id=platform.node(), 
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)],
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 destination_host=None,
                 destination_realm=None,
                 user_name=None,
                 oc_supported_features=None,
                 pur_flags=None,
                 supported_features=None,
                 eps_location_information=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterRequest.__init__(self, 
                                 command_code=PURGE_UE_MESSAGE, 
                                 application_id=DIAMETER_APPLICATION_S6a_S6d)

        DiameterRequest._load(self, locals())


class PurgeUeAnswer(DiameterAnswer):
    """Implementation of Purge-UE-Answer (PUA) command as per clause 7.2.14 of
    ETSI TS 129 272 V15.4.0 (2018-07).

    The Purge-UE-Answer is indicated by the Command Code field set to 321 and
    Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_s6a_s6d.messages import PurgeUeAnswer as PUA
        >>> pua = PUA()
        >>> pua
        <Diameter Message: 321 [PUA] PXY, 16777251 [3GPP S6a], 5 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }

    optionals = { 
                    # "drmp": DrmpAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "result_code": ResultCodeAVP,
                    "experimental_result": ExperimentalResultAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    # "oc_olr": OcOlrAVP,
                    # "load": LoadAVP,
                    "pua_flags": PuaFlagsAVP,
                    "failed_avp": FailedAvpAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)],
                 result_code=None,
                 experimental_result=None,
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 oc_supported_features=None,
                 oc_olr=None,
                 load=None,
                 pua_flags=None,
                 failed_avp=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=PURGE_UE_MESSAGE, 
                                application_id=DIAMETER_APPLICATION_S6a_S6d)

        DiameterAnswer._load(self, locals())


class UpdateLocationRequest(DiameterRequest):
    """Implementation of Update-Location-Request (ULR) command as per 
    clause 7.2.3 of ETSI TS 129 272 V15.4.0 (2018-07).

    The Update-Location-Request is indicated by the Command Code field set to 
    316 and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.etsi_3gpp_s6a_s6d.messages import UpdateLocationRequest as ULR
        >>> ulr_avps = {
        ...     "destination_realm": "example.com",
        ...     "user_name": "frodo",
        ...     "visited_plmn_id": bytes.fromhex("ffffff")
        ... }
        >>> ulr = ULR(**ulr_avps)
        >>> ulr
        <Diameter Message: 316 [ULR] REQ|PXY, 16777251 [3GPP S6a], 10 AVP(s)>
    """    

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "user_name": UserNameAVP,
                    "rat_type": RatTypeAVP,
                    "ulr_flags": UlrFlagsAVP,
                    "visited_plmn_id": VisitedPlmnIdAVP,
    }

    optionals = {
                    # "drmp": DrmpAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "destination_host": DestinationHostAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    "supported_features": SupportedFeaturesAVP,
                    "terminal_information": TerminalInformationAVP,
                    "ue_srvcc_capability": UeSrvccCapabilityAVP,
                    # "sgsn_number": SgsnNumberAVP,
                    "homogeneous_support_of_ims_voice_over_ps_sessions": HomogeneousSupportOfImsVoiceOverPsSessionsAVP,
                    # "gmlc_address": GmlcAddressAVP,
                    # "active_apn": ActiveApnAVP,
                    # "equivalent_plmn_list": EquivalentPlmnListAVP,
                    # "mme_number_for_mt_sms": MmeNumberForMtSmsAVP,
                    # "sms_register_request": SmsRegisterRequestAVP,
                    # "sgs_mme_identity": SgsMmeIdentityAVP,
                    # "copled_node_diameter_id": CopledNodeDiameterIdAVP,
                    # "adjacent_plmns": AdjacentPlmnsAVP,
                    "supported_services": SupportedServicesAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self, 
                 session_id=platform.node(), 
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)],
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 destination_host=None,
                 destination_realm=None,
                 user_name=None,
                 oc_supported_features=None,
                 supported_features=None,
                 terminal_information=None,
                 rat_type=RAT_TYPE_EUTRAN,
                 ulr_flags=3,
                 visited_plmn_id=None,
                 ue_srvcc_capability=None,
                 sgsn_number=None,
                 homogeneous_support_of_ims_voice_over_ps_sessions=None,
                 gmlc_address=None,
                 active_apn=None,
                 equivalent_plmn_list=None,
                 mme_number_for_mt_sms=None,
                 sms_register_request=None,
                 sgs_mme_identity=None,
                 copled_node_diameter_id=None,
                 adjacent_plmns=None,
                 supported_services=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterRequest.__init__(self, 
                                 command_code=UPDATE_LOCATION_MESSAGE, 
                                 application_id=DIAMETER_APPLICATION_S6a_S6d)

        DiameterRequest._load(self, locals())


class UpdateLocationAnswer(DiameterAnswer):
    """Implementation of Update-Location-Answer (ULA) command as per 
    clause 7.2.4 of ETSI TS 129 272 V15.4.0 (2018-07).

    The Update-Location-Answer is indicated by the Command Code field
    set to 316 and Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_s6a_s6d.messages import UpdateLocationAnswer as ULA
        >>> ula = ULA()
        >>> ula
        <Diameter Message: 316 [ULA] PXY, 16777251 [3GPP S6a], 5 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }

    optionals = { 
                    # "drmp": DrmpAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "result_code": ResultCodeAVP,
                    "experimental_result": ExperimentalResultAVP,
                    "error_diagnostic": ErrorDiagnosticAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    # "oc_olr": OcOlrAVP,
                    # "load": LoadAVP,
                    "supported_features": SupportedFeaturesAVP,
                    "ula_flags": UlaFlagsAVP,
                    "subscription_data": SubscriptionDataAVP,
                    # "reset_id": ResetIdAVP,
                    "failed_avp": FailedAvpAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)],
                 result_code=None,
                 experimental_result=None,
                 error_diagnostic=None,
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 oc_supported_features=None,
                 oc_olr=None,
                 load=None,
                 supported_features=None,
                 ula_flags=None,
                 subscription_data=None,
                 reset_id=None,
                 failed_avp=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=UPDATE_LOCATION_MESSAGE, 
                                application_id=DIAMETER_APPLICATION_S6a_S6d)

        DiameterAnswer._load(self, locals())
