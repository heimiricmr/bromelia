# -*- coding: utf-8 -*-
"""
    bromelia.lib.etsi_3gpp_swm.messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages for 3GPP SWm 
    Application Id.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import platform
import socket

from .avps import *

from ...base import DiameterRequest, DiameterAnswer
from ...constants import *


class AbortSessionAnswer(DiameterAnswer):
    """Implementation of Abort-Session-Answer (ASA) command as per 
    clause 7.1.2.4 of ETSI TS 129.273 V14.3.0 (2017-07).

    The Abort-Session-Answer is indicated by the Command Code field set to 274
    and Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.lib.etsi_3gpp_swm import ASA
        >>> asa = ASA()
        >>> asa
        <Diameter Message: 274 [ASA] PXY, 16777264 [3GPP SWm], 4 AVP(s)>
    """

    mandatory = { 
                    "session_id": SessionIdAVP,
                    "result_code": ResultCodeAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }
    optionals = { 
                    #"drmp": DrmpAvp,
    }

    def __init__(self,
                session_id=platform.node(),
                drmp=None,
                result_code=DIAMETER_SUCCESS,
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=ABORT_SESSION_MESSAGE, 
                                application_id=DIAMETER_APPLICATION_SWm)

        DiameterAnswer._load(self, locals())


class AbortSessionRequest(DiameterRequest):
    """Implementation of Abort-Session-Request (ASR) command as per 
    clause 7.1.2.4 of ETSI TS 129.273 V14.3.0 (2017-07).

    The Abort-Session-Request is indicated by the Command Code field set to 274
    and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.lib.etsi_3gpp_swm import ASR
        >>> asr_avps = {
        ...     "destination_realm": "remote",
        ...     "destination_host": "peer_node",
        ...     "user_name": "frodo"
        ... }
        >>> asr = ASR(**asr)
        >>> asr
        <Diameter Message: 274 [ASR] REQ|PXY, 16777264 [3GPP SWm], 8 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "destination_host": DestinationHostAVP,
                    "auth_application_id": AuthApplicationIdAVP,
    }
    optionals = {
                    #"drmp": DrmpAVP,
                    "user_name": UserNameAVP,
                    "auth_session_state": AuthSessionStateAVP,
    }

    def __init__(self,
                 session_id=platform.node(), 
                 drmp=None,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 destination_realm=None,
                 destination_host=None,
                 auth_application_id=DIAMETER_APPLICATION_SWm,
                 user_name=None,
                 auth_session_state=NO_STATE_MAINTAINED,
                 **kwargs):

        DiameterRequest.__init__(self,
                                 command_code=ABORT_SESSION_MESSAGE, 
                                 application_id=DIAMETER_APPLICATION_SWm)

        DiameterRequest._load(self, locals())


class DiameterEapAnswer(DiameterAnswer):
    """Implementation of Diameter-EAP-Answer (DEA) command as per 
    clause 7.2.2.1.2 of ETSI TS 129.273 V14.3.0 (2017-07).

    The Diameter-EAP-Answer is indicated by the Command Code field set to 268
    and Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.lib.etsi_3gpp_swm import DEA
        >>> dea = DEA()
        >>> dea
        <Diameter Message: 268 [DEA], PXY SWm, 9 AVP(s)>
    """

    mandatory = { 
                    "session_id": SessionIdAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "auth_request_type": AuthRequestTypeAVP,
                    "result_code": ResultCodeAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }
    optionals = { 
                    #"drmp": DrmpAvp,
                    "eap_payload": EapPayloadAVP,
                    "user_name": UserNameAVP,
                    "eap_master_session_key": EapMasterSessionKeyAVP,
                    #"apn_oi_replacement": ApnOiReplacementAVP,
                    "apn_configuration": ApnConfigurationAVP,
                    "mip6_feature_vector": Mip6FeatureVectorAVP,
                    "mobile_node_identifier": MobileNodeIdentifierAVP,
                    #"trace_info": TraceInfoAVP,
                    "subscription_id": SubscriptionIdAVP,
                    "session_timeout": SessionTimeoutAVP,
                    "mip6_agent_info": Mip6AgentInfoAVP,
                    "x3gpp_charging_characteristics": X3gppChargingCharacteristicsAVP,
                    "redirect_host": RedirectHostAVP,
                    "supported_features": SupportedFeaturesAVP,
                    #"oc_supported_features": OcSupportedFeaturesAVP,
                    #"oc_olr": OcOlrAVP,
                    #"load": LoadAVP,
                    #"access_network_info": AccessNetworkInfoAVP,
                    #"user_location_info_time": UserLocationInfoTime,
                    #"emergency_info": EmergencyInfoAVP,
    }

    def __init__(self,
                session_id=platform.node(),
                drmp=None,
                auth_application_id=DIAMETER_APPLICATION_SWm,
                auth_request_type=AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY,
                result_code=DIAMETER_SUCCESS,
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                eap_payload=None, 
                user_name=None, 
                eap_master_session_key=None,
                apn_oi_replacement=None,
                apn_configuration=None,
                mip6_feature_vector=None,
                mobile_node_identifier=None,
                trace_info=None,
                subscription_id=None,
                session_timeout=None,
                mip6_agent_info=None,
                x3gpp_charging_characteristics=None,
                redirect_host=None,
                supported_features=None,
                oc_supported_features=None,
                oc_olr=None,
                load=None,
                access_network_info=None,
                user_location_info_time=None,
                emergency_info=None,
                **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=DIAMETER_EAP_MESSAGE, 
                                application_id=auth_application_id)

        DiameterAnswer._load(self, locals())


class DiameterEapRequest(DiameterRequest):
    """Implementation of Diameter-EAP-Request (DER) command as per 
    clause 7.2.2.1.1 of ETSI TS 129.273 V14.3.0 (2017-07).

    The Diameter-EAP-Request is indicated by the Command Code field set to 268
    and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.lib.etsi_3gpp_swm import DER
        >>> der = DER()
        >>> der
        <Diameter Message: 268 [DER], REQ, PXY SWm, 7 AVP(s)>
    """    

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "auth_request_type": AuthRequestTypeAVP,
                    "eap_payload": EapPayloadAVP
    }
    optionals = {
                    #"drmp": DrmpAvp,
                    "destination_host": DestinationHostAVP,
                    "user_name": UserNameAVP,
                    "rat_type": RatTypeAVP,
                    "service_selection": ServiceSelectionAVP,
                    "mip6_feature_vector": Mip6FeatureVectorAVP,
                    # "qos_capability": QosCapabilityAVP, 
                    "visited_network_identifier": VisitedNetworkIdentifierAVP,
                    # "aaa_failure_indication": AaaFailureIndicationAVP,
                    # "supported_features": SupportedFeaturesAVP,
                    "ue_local_ip_address": UeLocalIpAddressAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    # "terminal_information": TerminalInformationAVP,
                    # "emergency_services": EmergencyServicesAVP,
    }

    def __init__(self,
                session_id=platform.node(), 
                drmp=None,
                auth_application_id=DIAMETER_APPLICATION_SWm,
                origin_host=platform.node(), 
                origin_realm=socket.getfqdn(), 
                destination_realm=None,
                destination_host=None,
                auth_request_type=AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY,
                eap_payload=None,
                user_name=None,
                rat_type=None,
                service_selection=None,
                mip6_feature_vector=None,
                qos_capability=None, 
                visited_network_identifier=None,
                aaa_failure_indication=None,
                supported_features=None,
                ue_local_ip_address=None,
                oc_supported_features=None,
                terminal_information=None,
                emergency_services=None,
                **kwargs):

        DiameterRequest.__init__(self, 
                                command_code=DIAMETER_EAP_MESSAGE, 
                                application_id=auth_application_id)

        DiameterRequest._load(self, locals())