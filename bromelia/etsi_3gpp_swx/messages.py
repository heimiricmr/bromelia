# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_swx.messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages for 3GPP SWx
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

show_warn("messages", "etsi_3gpp_swx")


class MultimediaAuthRequest(DiameterRequest):
    """Implementation of Multimedia-Auth-Request (MAR) command as per 
    clause 8.2.2.1 of ETSI TS 129.273 V14.3.0 (2017-07).

    The Multimedia-Auth-Request is indicated by the Command Code field set to 
    303 and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.etsi_3gpp_swx.messages import MultimediaAuthRequest as MAR
        >>> mar = MAR()
        >>> mar
        <Diameter Message: 303 [MAR], REQ, PXY SWx, 10 AVP(s)>
    """    

    mandatory = {
                    "session_id": SessionIdAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "user_name": UserNameAVP,
                    "sip_auth_data_item": SipAuthDataItemAVP,
                    "sip_number_auth_items": SipNumberAuthItemsAVP
    }
    optionals = {
                    #"drmp": DrmpAVP,
                    "destination_host": DestinationHostAVP,
                    "rat_type": RatTypeAVP,
                    #"anid": AnidAVP,
                    "visited_network_identifier": VisitedNetworkIdentifierAVP,
                    "terminal_information": TerminalInformationAVP,
                    #"aaa_failure_indication": AaaFailureIndicationAVP,
                    #"oc_supported_features": OcSupportedFeaturesAVP,
                    "supported_features": SupportedFeaturesAVP
    }

    def __init__(self,
                 session_id=platform.node(), 
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_SWx)],
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 destination_realm=None,
                 destination_host=None,
                 user_name=None,
                 rat_type=None,
                 anid=None,
                 visited_network_identifier=None,
                 terminal_information=None,
                 sip_auth_data_item=[SipAuthenticationSchemeAVP("EAP-AKA")],
                 sip_number_auth_items=5,
                 aaa_failure_indication=None,
                 oc_supported_features=None,
                 supported_features=None,
                 **kwargs):

        DiameterRequest.__init__(self,
                                command_code=MULTIMEDIA_AUTH_MESSAGE, 
                                application_id=DIAMETER_APPLICATION_SWx)

        DiameterRequest._load(self, locals())


class MultimediaAuthAnswer(DiameterAnswer):
    """Implementation of Multimedia-Auth-Answer (MAA) command as per 
    clause 8.2.2.2 of ETSI TS 129.273 V14.3.0 (2017-07).

    The Multimedia-Auth-Answer is indicated by the Command Code field set to 
    303 and Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_swx.messages import MultimediaAuthAnswer as MAA
        >>> maa = MAA()
        >>> maa
        <Diameter Message: 303 [MAA], PXY SWx, 9 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "user_name": UserNameAVP,
    }
    optionals = { 
                    #"drmp": DrmpAVP,
                    "result_code": ResultCodeAVP,
                    "experimental_result": ExperimentalResultAVP,
                    "sip_number_auth_items": SipNumberAuthItemsAVP,
                    "sip_auth_data_item": SipAuthDataItemAVP,
                    #"x3gpp_aaa_server_name": X3gppAaaServerNameAVP,
                    #"oc_supported_features": OcSupportedFeaturesAVP,
                    #"oc_olr": OcOlrAVP,
                    #"load": LoadAVP,
                    "supported_features": SupportedFeaturesAVP,
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_SWx)],
                 result_code=None,
                 experimental_result=None,
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 user_name=None,
                 sip_number_auth_items=None,
                 sip_auth_data_item=None,
                 x3gpp_aaa_server_name=None,
                 oc_supported_features=None,
                 oc_olr=None,
                 load=None,
                 supported_features=None,
                 **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=MULTIMEDIA_AUTH_MESSAGE, 
                                application_id=DIAMETER_APPLICATION_SWx)

        DiameterAnswer._load(self, locals())


class RegistrationTerminationRequest(DiameterRequest):
    """Implementation of Registration-Termination-Request (RTR) command as per 
    clause 8.2.2.4 of ETSI TS 129.273 V14.3.0 (2017-07).

    The Registration-Termination-Request is indicated by the Command Code 
    field set to 304 and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.etsi_3gpp_swx.messages import RegistrationTerminationRequest as RTR
        >>> rtr_avps = {
        ...     "destination_realm": "example.com",
        ...     "user_name": "frodo"
        ...     "destination_host": "host.example.com",
        ... }
        >>> rtr = RTR(**rtr_avps)
        >>> rtr
        <Diameter Message: 304 [RTR] REQ|PXY, 16777265 [3GPP SWx], 9 AVP(s)>
    """    

    mandatory = {
                    "session_id": SessionIdAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_host": DestinationHostAVP,
                    "destination_realm": DestinationRealmAVP,
                    "user_name": UserNameAVP,
                    "deregistration_reason": DeregistrationReasonAVP
    }
    optionals = {
                    #"drmp": DrmpAVP,
                    "supported_features": SupportedFeaturesAVP,
    }

    def __init__(self, 
                 session_id=platform.node(), 
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_SWx)],
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 destination_host=None,
                 destination_realm=None,
                 user_name=None,
                 deregistration_reason=[ReasonCodeAVP(REASON_CODE_PERMANENT_TERMINATION)],
                 supported_features=None,
                 **kwargs):

        DiameterRequest.__init__(self, 
                                 command_code=REGISTRATION_TERMINATION_MESSAGE, 
                                 application_id=DIAMETER_APPLICATION_SWx)

        DiameterRequest._load(self, locals())


class RegistrationTerminationAnswer(DiameterAnswer):
    """Implementation of Registration-Termination-Answer (RTA) command as per 
    clause 8.2.2.4 of ETSI TS 129.273 V14.3.0 (2017-07).

    The Server-Assignment-Answer is indicated by the Command Code field set to 
    304 and Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_swx.messages import RegistrationTerminationAnswer as RTA
        >>>
        >>> rta_avps = {
        ...     "user_name": "frodo"
        ... }
        >>> rta = RTA(**rta_avps)
        <Diameter Message: 304 [RTA], PXY, 16777265 [3GPP SWx], 6 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }
    optionals = { 
                    #"drmp": DrmpAVP,
                    "result_code": ResultCodeAVP,
                    "experimental_result": ExperimentalResultAVP,
                    "supported_features": SupportedFeaturesAVP,
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_SWx)],
                 result_code=None,
                 experimental_result=None,
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 supported_features=None,
                 **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=REGISTRATION_TERMINATION_MESSAGE, 
                                application_id=DIAMETER_APPLICATION_SWx)

        DiameterAnswer._load(self, locals())


class ServerAssignmentRequest(DiameterRequest):
    """Implementation of Server-Assignment-Request (MAR) command as per 
    clause 8.2.2.3 of ETSI TS 129.273 V14.3.0 (2017-07).

    The Server-Assignment-Request is indicated by the Command Code field set to
    301 and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.etsi_3gpp_swx.messages import ServerAssignmentRequest as SAR
        >>> sar_avps = {
        ...     "destination_realm": "example.com",
        ...     "user_name": "frodo"
        ...     "destination_host": "host.example.com",
        ... }
        >>> sar = SAR(**sar_avps)
        >>> sar
        <Diameter Message: 301 [SAR], REQ, PXY SWx, 9 AVP(s)>
    """    

    mandatory = {
                    "session_id": SessionIdAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "user_name": UserNameAVP,
                    "server_assignment_type": ServerAssignmentTypeAVP
    }
    optionals = {
                    #"drmp": DrmpAVP,
                    "destination_host": DestinationHostAVP,
                    "service_selection": ServiceSelectionAVP,
                    "context_identifier": ContextIdentifierAVP,
                    "mip6_agent_info": Mip6AgentInfoAVP,
                    "visited_network_identifier": VisitedNetworkIdentifierAVP,
                    #"active_apn": ActiveApnAVP,
                    #"oc_supported_features": OcSupportedFeaturesAVP,
                    "supported_features": SupportedFeaturesAVP,
                    "terminal_information": TerminalInformationAVP,
                    #"emergency_services": EmergencyServicesAVP
    }

    def __init__(self, 
                 session_id=platform.node(), 
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_SWx)],
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 destination_host=None,
                 destination_realm=None,
                 service_selection=None,
                 context_identifier=None,
                 mip6_agent_info=None,
                 visited_network_identifier=None,
                 user_name=None,
                 server_assignment_type=SERVER_ASSIGNMENT_TYPE_NO_ASSIGNMENT,
                 active_apn=None,
                 oc_supported_features=None,
                 terminal_information=None,
                 emergency_services=None,
                 **kwargs):

        DiameterRequest.__init__(self, 
                                 command_code=SERVER_ASSIGNMENT_MESSAGE, 
                                 application_id=DIAMETER_APPLICATION_SWx)

        DiameterRequest._load(self, locals())


class ServerAssignmentAnswer(DiameterAnswer):
    """Implementation of Server-Assignment-Answer (SAA) command as per 
    clause 8.2.2.3 of ETSI TS 129.273 V14.3.0 (2017-07).

    The Server-Assignment-Answer is indicated by the Command Code field set to 
    301 and Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_swx.messages import ServerAssignmentAnswer as SAA
        >>> saa_avps = {
        ...     "user_name": "frodo"
        ... }
        >>> saa = SAA(**sar_avps)
        >>> saa
        <Diameter Message: 301 [SAA], PXY SWx, 8 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "user_name": UserNameAVP,
    }
    optionals = { 
                    #"drmp": DrmpAVP,
                    "result_code": ResultCodeAVP,
                    "experimental_result": ExperimentalResultAVP,
                    "non3gpp_user_data": Non3gppUserDataAVP,
                    #"x3gpp_aaa_server_name": X3gppAaaServerNameAVP,
                    #"oc_supported_features": OcSupportedFeaturesAVP,
                    #"oc_olr": OcOlrAVP,
                    #"load": LoadAVP,
                    "supported_features": SupportedFeaturesAVP,
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_SWx)],
                 result_code=None,
                 experimental_result=None,
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 user_name=None,
                 non3gpp_user_data=None,
                 x3gpp_aaa_server_name=None,
                 oc_supported_features=None,
                 oc_olr=None,
                 load=None,
                 supported_features=None,
                 **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=SERVER_ASSIGNMENT_MESSAGE, 
                                application_id=DIAMETER_APPLICATION_SWx)

        DiameterAnswer._load(self, locals())

