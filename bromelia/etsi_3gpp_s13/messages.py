# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_s13.messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages for 3GPP S13/S13'
    Application Id.

    :copyright: (c) 2021-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import platform
import socket

from .avps import *

from .._internal_utils import show_warn
from ..base import DiameterRequest, DiameterAnswer
from ..constants import *

show_warn("messages", "etsi_3gpp_s13")


class MeIdentityCheckRequest(DiameterRequest):
    """Implementation of ME-Identity-Check-Request (ECR) command as per 
    clause 7.2.19 of ETSI TS 129 272 V15.4.0 (2018-07).

    The ME-Identity-Check-Request is indicated by the Command Code field 
    set to 324 and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.etsi_3gpp_s13.messages import MeIdentityCheckRequest as ECR
        >>> ecr_avps = {
        ...     "destination_realm": "remote",
        ...     "terminal_information": [ImeiAVP("12345678901234"), SoftwareVersionAVP("12")],
        ... }
        >>> ecr = ECR(**ecr_avps)
        >>> ecr
        <Diameter Message: 324 [ECR] REQ|PXY, 16777252 [3GPP S13], 8 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "terminal_information": TerminalInformationAVP,
    }
    optionals = {
                    #"drmp": DrmpAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "destination_host": DestinationHostAVP,
                    "user_name": UserNameAVP, 
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self,
                 session_id=platform.node(), 
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_S13_S13)],
                 auth_session_state=NO_STATE_MAINTAINED, 
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 destination_host=None,
                 destination_realm=None,
                 terminal_information=None,
                 user_name=None,
                 avp=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterRequest.__init__(self,
                                 command_code=EC_MESSAGE, 
                                 application_id=DIAMETER_APPLICATION_S13_S13)

        DiameterRequest._load(self, locals())


class MeIdentityCheckAnswer(DiameterAnswer):
    """Implementation of ME-Identity-Check-Answer (ECA) command as per 
    clause 7.2.20 of ETSI TS 129 272 V15.4.0 (2018-07).

    The ME-Identity-Check-Answer is indicated by the Command Code field 
    set to 324 and Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_s13.messages import MeIdentityCheckAnswer as ECA
        >>> eca = ECA()
        >>> eca
        <Diameter Message: 324 [ECA] PXY, 16777252 [3GPP S13], 6 AVP(s)>    
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }
    optionals = { 
                    #"drmp": DrmpAVP,
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "result_code": ResultCodeAVP,
                    "experimental_result": ExperimentalResultAVP,
                    "equipment_status": EquipmentStatusAVP,
                    "failed_avp": FailedAvpAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_S13_S13)],
                 result_code=DIAMETER_SUCCESS,
                 experimental_result=None,
                 auth_session_state=NO_STATE_MAINTAINED, 
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 equipment_status=None,
                 avp=None,
                 failed_avp=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterAnswer.__init__(self, 
                                command_code=EC_MESSAGE, 
                                application_id=DIAMETER_APPLICATION_S13_S13)

        DiameterAnswer._load(self, locals())
