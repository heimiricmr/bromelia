# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_s6a_s6d.messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages for 3GPP S6a/S6d 
    Application Id.

    :copyright: (c) 2020 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import platform
import socket

from .avps import *

from ..avps import *
from ..etsi_3gpp_s6a_s6d.avps import *
from ..base import DiameterAnswer
from ..base import DiameterRequest 
from ..constants import *


class CancelLocationRequest(DiameterRequest):
    """Implementation of Cancel-Location-Request (CLR) command as per 
    clause 7.2.7 of ETSI TS 129 272 V15.4.0 (2018-07).

    The Cancel-Location-Request is indicated by the Command Code field set to 
    317 and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.etsi_3gpp_s6a_s6d.messages import CancelLocationRequest as CLR
        >>>
        >>> clr_avps = {
        ...     "destination_realm": "example.com",
        ...     "destination_host": "host.example.com",
        ...     "user_name": "frodo"
        ... }
        >>> clr = CLR(**clr_avps)
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
                    #"drmp": DrmpAVP,
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
        >>>
        >>> cla = CLA()
        <Diameter Message: 317 [CLA] PXY, 16777251 [3GPP S6a], 5 AVP(s)>
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
