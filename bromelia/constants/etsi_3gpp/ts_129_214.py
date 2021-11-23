# -*- coding: utf-8 -*-
"""
    bromelia.constants.etsi_3gpp.ts_129_214
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains constants defined in ETSI TS 129 214.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_4_bytes


#: Diameter AVPs
ABORT_CAUSE_AVP_CODE = convert_to_4_bytes(500)
ACCESS_NETWORK_CHARGING_ADDRESS_AVP_CODE = convert_to_4_bytes(501)
ACCESS_NETWORK_CHARGING_IDENTIFIER_VALUE_AVP_CODE = convert_to_4_bytes(503)
AF_APPLICATION_IDENTIFIER_AVP_CODE = convert_to_4_bytes(504)
AF_CHARGING_IDENTIFIER_AVP_CODE = convert_to_4_bytes(505)
FLOW_DESCRIPTION_AVP_CODE = convert_to_4_bytes(507)
FLOW_NUMBER_AVP_CODE = convert_to_4_bytes(509)
FLOW_STATUS_AVP_CODE = convert_to_4_bytes(511)
FLOW_USAGE_AVP_CODE = convert_to_4_bytes(512)
SPECIFIC_ACTION_AVP_CODE = convert_to_4_bytes(513)
MAX_REQUESTED_BANDWIDTH_DL_AVP_CODE = convert_to_4_bytes(515)
MAX_REQUESTED_BANDWIDTH_UL_AVP_CODE = convert_to_4_bytes(516)
MEDIA_COMPONENT_DESCRIPTION_AVP_CODE = convert_to_4_bytes(517)
MEDIA_COMPONENT_NUMBER_AVP_CODE = convert_to_4_bytes(518) 
MEDIA_SUB_COMPONENT_AVP_CODE = convert_to_4_bytes(519)
MEDIA_TYPE_AVP_CODE = convert_to_4_bytes(520)
SERVICE_INFO_STATUS_AVP_CODE = convert_to_4_bytes(527)

#: List of Abort-Cause AVP values.
#: For more information, please refer to Section 5.3.1 of 
#: ETSI TS 129 214 V15.4.0 (2018-07).
ABORT_CAUSE_BEARER_RELEASED = convert_to_4_bytes(0)
ABORT_CAUSE_INSUFFICIENT_SERVER_RESOURCES = convert_to_4_bytes(1)
ABORT_CAUSE_INSUFFICIENT_BEARER_RESOURCES = convert_to_4_bytes(2)
ABORT_CAUSE_PS_TO_CS_HANDOVER = convert_to_4_bytes(3)
ABORT_CAUSE_SPONSORED_DATA_CONNECTIVITY_DISALLOWED = convert_to_4_bytes(4)

#: List of Flow-Status AVP values.
#: For more information, please refer to Section 5.3.11 of 
#: ETSI TS 129 214 V15.4.0 (2018-07).
FLOW_STATUS_ENABLED_UPLINK = convert_to_4_bytes(0)
FLOW_STATUS_ENABLED_DOWNLINK = convert_to_4_bytes(1)
FLOW_STATUS_ENABLED = convert_to_4_bytes(2)
FLOW_STATUS_DISABLED = convert_to_4_bytes(3)
FLOW_STATUS_REMOVED = convert_to_4_bytes(4)

#: List of Flow-Usage AVP values.
#: For more information, please refer to Section 5.3.12 of 
#: ETSI TS 129 214 V15.4.0 (2018-07).
FLOW_USAGE_NO_INFORMATION = convert_to_4_bytes(0)
FLOW_USAGE_RTCP = convert_to_4_bytes(1)
FLOW_USAGE_AF_SIGNALLING = convert_to_4_bytes(2)

#: List of Specific-Action AVP values.
#: For more information, please refer to Section 5.3.13 of 
#: ETSI TS 129 214 V15.4.0 (2018-07).
SPECIFIC_ACTION_CHARGING_CORRELATION_EXCHANGE = convert_to_4_bytes(1)
SPECIFIC_ACTION_INDICATION_OF_LOSS_OF_BEARER = convert_to_4_bytes(2)
SPECIFIC_ACTION_INDICATION_OF_RECOVERY_OF_BEARER = convert_to_4_bytes(3)
SPECIFIC_ACTION_INDICATION_OF_RELEASE_OF_BEARER = convert_to_4_bytes(4)
SPECIFIC_ACTION_IP_CAN_CHANGE = convert_to_4_bytes(6)
SPECIFIC_ACTION_INDICATION_OF_OUT_OF_CREDIT = convert_to_4_bytes(7)
SPECIFIC_ACTION_INDICATION_OF_SUCCESSFUL_RESOURCES_ALLOCATION = convert_to_4_bytes(8)
SPECIFIC_ACTION_INDICATION_OF_FAILED_RESOURCES_ALLOCATION = convert_to_4_bytes(9)
SPECIFIC_ACTION_INDICATION_OF_LIMITED_PCC_DEPLOYMENT = convert_to_4_bytes(10)
SPECIFIC_ACTION_USAGE_REPORT = convert_to_4_bytes(11)
SPECIFIC_ACTION_ACCESS_NETWORK_INFO_REPORT = convert_to_4_bytes(12)
SPECIFIC_ACTION_INDICATION_OF_RECOVERY_FROM_LIMITED_PCC_DEPLOYMENT = convert_to_4_bytes(13)
SPECIFIC_ACTION_INDICATION_OF_ACCESS_NETWORK_INFO_REPORTING_FAILURE = convert_to_4_bytes(14)
SPECIFIC_ACTION_INDICATION_OF_TRANSFER_POLICY_EXPIRED = convert_to_4_bytes(15)
SPECIFIC_ACTION_PLMN_CHANGE = convert_to_4_bytes(16)

#: List of Media-Type AVP values.
#: For more information, please refer to Section 5.3.19 of 
#: ETSI TS 129 214 V15.4.0 (2018-07).
MEDIA_TYPE_AUDIO = convert_to_4_bytes(0)
MEDIA_TYPE_VIDEO = convert_to_4_bytes(1)
MEDIA_TYPE_DATA = convert_to_4_bytes(2)
MEDIA_TYPE_APPLICATION = convert_to_4_bytes(3)
MEDIA_TYPE_CONTROL = convert_to_4_bytes(4)
MEDIA_TYPE_TEXT = convert_to_4_bytes(5)
MEDIA_TYPE_MESSAGE = convert_to_4_bytes(6)
MEDIA_TYPE_OTHER = convert_to_4_bytes(7)

#: List of Service-Info-Status AVP values.
#: For more information, please refer to Section 5.3.25 of 
#: ETSI TS 129 214 V15.4.0 (2018-07).
SERVICE_INFO_STATUS_FINAL_SERVICE_INFORMATION = convert_to_4_bytes(0)
SERVICE_INFO_STATUS_PRELIMINARY_SERVICE_INFORMATION = convert_to_4_bytes(1)
