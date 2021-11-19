# -*- coding: utf-8 -*-
"""
    bromelia.lib.etsi_3gpp_s6b.messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages for 3GPP S6b
    Application Id.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import platform
import socket

from .avps import *

from ...base import DiameterRequest, DiameterAnswer
from ...constants import *


class AAAnswer(DiameterAnswer):
    """Implementation of AA-Answer (MAA) command as per 
    clause 9.2.2.2.2 of ETSI TS 129.273 V14.3.0 (2017-07).

    The AA-Answer is indicated by the Command Code field set to 265
    and Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.lib.etsi_3gpp_s6b import AAA
        >>> aaa_avps = {
        ...     "mip6_feature_vector": 70368744177664,
        ...     "session_timeout": 10800,
        ... }
        >>> aaa = AAA(**aaa_avps)
        >>> aaa
        <Diameter Message: 265 [AAA] PXY, 16777272 [3GPP S6b], 8 AVP(s)>        
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "auth_request_type": AuthRequestTypeAVP,
                    "result_code": ResultCodeAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
    }
    optionals = { 
                    #"drmp": DrmpAVP,
                    "mip6_feature_vector": Mip6FeatureVectorAVP, 
                    "session_timeout": SessionTimeoutAVP,
                    "apn_configuration": ApnConfigurationAVP,
                    #"qos_resources": QosResourcesAVP,
                    #"an_trusted": AnTrustedAVP,
                    "redirect_host": RedirectHostAVP,
                    #"trace_info": TraceInfoAVP,
                    #"oc_supported_features": OcSupportedFeaturesAVP,
                    #"oc_olr": OcOlrAVP,
                    #"load": LoadAVP,
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 auth_application_id=DIAMETER_APPLICATION_S6b,
                 auth_request_type=AUTH_REQUEST_TYPE_AUTHORIZE_ONLY,
                 result_code=DIAMETER_SUCCESS,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 mip6_feature_vector=None,
                 session_timeout=None,
                 apn_configuration=None,
                 qos_resources=None,
                 an_trusted=None,
                 redirect_host=None,
                 trace_info=None,
                 oc_supported_features=None,
                 oc_olr=None,
                 load=None,
                 **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=AA_MESSAGE, 
                                application_id=DIAMETER_APPLICATION_S6b)

        DiameterAnswer._load(self, locals())


class AARequest(DiameterRequest):
    """Implementation of AA-Request (AAR) command as per 
    clause 9.2.2.2.1 of ETSI TS 129.273 V14.3.0 (2017-07).

    The AA-Request is indicated by the Command Code field set to 265
    and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.lib.etsi_3gpp_s6b import AAR
        >>> aar_avps = {
        ...     "destination_realm": "remote",
        ...     "user_name": "frodo",
        ... }
        >>> aar = AAR(**aar_avps)
        >>> aar
        <Diameter Message: 265 [AAR] REQ|PXY, 16777272 [3GPP S6b], 7 AVP(s)>
    """    

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "auth_request_type": AuthRequestTypeAVP,
    }
    optionals = {
                    #"drmp": DrmpAVP,
                    "user_name": UserNameAVP,
                    "mip6_agent_info": Mip6AgentInfoAVP,
                    "mip6_feature_vector": Mip6FeatureVectorAVP, 
                    "visited_network_identifier": VisitedNetworkIdentifierAVP,
                    #"qos_capacity": QosCapacityAVP,
                    "service_selection": ServiceSelectionAVP,
                    #"oc_supported_features": OcSupportedFeaturesAVP,
                    #"origination_time_stamp": OriginationTimeStampAVP,
                    #"maximum_wait_time": MaximumWaitTimeAVP,
                    "supported_features": SupportedFeaturesAVP,
                    #"emergency_services": EmergencyServicesAVP,
    }

    def __init__(self,
                 session_id=platform.node(), 
                 drmp=None,
                 auth_application_id=DIAMETER_APPLICATION_S6b,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 destination_realm=None,
                 auth_request_type=AUTH_REQUEST_TYPE_AUTHORIZE_ONLY,
                 user_name=None,
                 mip6_agent_info=None,
                 mip6_feature_vector=None,
                 visited_network_identifier=None,
                 qos_capacity=None,
                 service_selection=None,
                 oc_supported_features=None,
                 origination_time_stamp=None,
                 maximum_wait_time=None,
                 supported_features=None,
                 emergency_services=None,
                 **kwargs):

        DiameterRequest.__init__(self,
                                 command_code=AA_MESSAGE, 
                                 application_id=DIAMETER_APPLICATION_S6b)

        DiameterRequest._load(self, locals())