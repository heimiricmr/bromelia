# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_gy.messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages for 3GPP Gy
    Application Id.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import platform
import socket

from .avps import *

from ...base import DiameterRequest, DiameterAnswer
from ...constants import *


class CreditControlAnswer(DiameterAnswer):
    """Implementation of CC-Answer (CCA) command as per clause 6.4.3 of 
    ETSI TS 132 299 V14.3.0 (2017-04).

    The CC-Answer is indicated by the Command Code field set to 272 and 
    Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_gy.messages import CreditControlAnswer as CCA
        >>> cca = CCA()
        >>> cca
        <Diameter Message: 272 [CCA] PXY, 4 [3GPP Gy], W AVP(s)>    
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "result_code": ResultCodeAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "cc_request_type": CcRequestTypeAVP,
                    "cc_request_number": CcRequestNumberAVP,
    }
    optionals = { 
                    "cc_session_failover": CcSessionFailoverAVP,
                    "multiple_services_credit_control": MultipleServicesCreditControlAVP,
                    "cost_information": CostInformationAVP,
                    "low_balance_indication": LowBalanceIndicationAVP,
                    "remaining_balance": RemainingBalanceAVP,
                    "credit_control_failure_handling": CreditControlFailureHandlingAVP,
                    "direct_debiting_failure_handling": DirectDebitingFailureHandlingAVP,
                    "redirect_host": RedirectHostAVP,
                    "redirect_host_usage": RedirectHostUsageAVP,
                    "redirect_max_cache_time": RedirectMaxCacheTimeAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
                    "failed_avp": FailedAvpAVP,
                    # "service_information": ServiceInformationAVP
    }

    def __init__(self,
                 session_id=platform.node(),
                 result_code=DIAMETER_SUCCESS,
                 origin_host=platform.node(),
                 origin_realm=socket.getfqdn(),
                 auth_application_id=DIAMETER_APPLICATION_Gy,
                 cc_request_type=CC_REQUEST_TYPE_INITIAL_REQUEST,
                 cc_request_number=0,
                 cc_session_failover=None,
                 multiple_services_credit_control=None,
                 cost_information=None,
                 low_balance_indication=None,
                 remaining_balance=None,
                 credit_control_failure_handling=None,
                 direct_debiting_failure_handling=None,
                 redirect_host=None,
                 redirect_host_usage=None,
                 redirect_max_cache_time=None,
                 proxy_info=None,
                 route_record=None,
                 failed_avp=None,
                 service_information=None,
                 **kwargs):

        DiameterAnswer.__init__(self,
                                command_code=CC_MESSAGE,
                                application_id=DIAMETER_APPLICATION_Gy)

        DiameterAnswer._load(self, locals())


class CreditControlRequest(DiameterRequest):
    """Implementation of CC-Request (CCR) command as per clause 6.4.2 of 
    ETSI TS 132 299 V14.3.0 (2017-04).

    The CC-Request is indicated by the Command Code field set to 272 and 
    the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.lib.etsi_3gpp_gy import CCR
        >>> from bromelia.constants import *
        >>> ccr_avps = {
        ...     "destination_realm": "remote",
        ...     "cc_request_type": CC_REQUEST_TYPE_INITIAL_REQUEST,
        ...     "cc_request_number": 1,
        ... }
        >>> ccr = CCR(**ccr_avps)
        >>> ccr
        <Diameter Message: 272 [CCR] REQ|PXY, 16777238 [3GPP Gy], 7 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    # "service_context_id": ServiceContextIdAVP,
                    "cc_request_type": CcRequestTypeAVP,
                    "cc_request_number": CcRequestNumberAVP,
    }
    optionals = {
                    "destination_host": DestinationHostAVP,
                    "user_name": UserNameAVP,
                    # "cc_sub_session_id_avp": CcSubSessionIdAVP,
                    "acct_multi_session_id_avp": AcctMultiSessionIdAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "event_timestamp": EventTimestampAVP,
                    "subscription_id": SubscriptionIdAVP,
                    "service_identifier": ServiceIdentifierAVP,
                    "termination_cause": TerminationCauseAVP,
                    "requested_service_unit": RequestedServiceUnitAVP,
                    # "requested_action": RequestedActionAVP,
                    # "used_service_unit": UsedServiceUnitAVP,
                    # "aoc_request_type": AocRequestTypeAVP,
                    # "multiple_services_indicator": MultipleServicesIndicatorAVP,
                    "multiple_services_credit_control": MultipleServicesCreditControlAVP,
                    # "service_parameter_info": ServiceParameterInfoAVP,
                    # "cc_correlation_id": CcCorrelationIdAVP,
                    "user_equipment_info": UserEquipmentInfoAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
                    # "service_information": ServiceInformationAVP
    }

    def __init__(self,
                 session_id=platform.node(),
                 origin_host=platform.node(),
                 origin_realm=socket.getfqdn(),
                 destination_realm=None,
                 auth_application_id=DIAMETER_APPLICATION_Gy,
                 service_context_id=None,
                 cc_request_type=CC_REQUEST_TYPE_INITIAL_REQUEST,
                 cc_request_number=0,
                 destination_host=None,
                 user_name=None,
                 cc_sub_session_id=None,
                 acct_multi_session_id=None,
                 origin_state_id=None,
                 event_timestamp=None,
                 subscription_id=None,
                 service_identifier=None,
                 termination_cause=None,
                 requested_service_unit=None,
                 requested_action=None,
                 used_service_unit=None,
                 aoc_request_type=None,
                 multiple_services_indicator=None,
                 multiple_services_credit_control=None,
                 service_parameter_info=None,
                 cc_correlation_id=None,
                 user_equipment_info=None,
                 proxy_info=None,
                 route_record=None,
                 service_information=None,
                 **kwargs):

        DiameterRequest.__init__(self,
                                 command_code=CC_MESSAGE,
                                 application_id=DIAMETER_APPLICATION_Gy)

        DiameterRequest._load(self, locals())
