# -*- coding: utf-8 -*-
"""
    bromelia.constants.etsi_3gpp.ts_129_272
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains constants defined in ETSI TS 129 272.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_3_bytes
from ..._internal_utils import convert_to_4_bytes


#: Diameter Messages
UPDATE_LOCATION_MESSAGE = convert_to_3_bytes(316)
CANCEL_LOCATION_MESSAGE = convert_to_3_bytes(317)
AUTHENTICATION_INFORMATION_MESSAGE = convert_to_3_bytes(318)
PURGE_UE_MESSAGE = convert_to_3_bytes(321)
NOTIFY_MESSAGE = convert_to_3_bytes(323)
EC_MESSAGE = convert_to_3_bytes(324)

#: Diameter AVPs
SERVICE_SELECTION_AVP_CODE = convert_to_4_bytes(493)
ALLOCATION_RETENTION_PRIORITY_AVP_CODE = convert_to_4_bytes(1034)
SUBSCRIPTION_DATA_AVP_CODE = convert_to_4_bytes(1400)
TERMINAL_INFORMATION_AVP_CODE = convert_to_4_bytes(1401)
IMEI_AVP_CODE = convert_to_4_bytes(1402)
SOFTWARE_VERSION_AVP_CODE = convert_to_4_bytes(1403)
ULR_FLAGS_AVP_CODE = convert_to_4_bytes(1405)
ULA_FLAGS_AVP_CODE = convert_to_4_bytes(1406)
VISITED_PLMN_ID_AVP_CODE = convert_to_4_bytes(1407)
REQUESTED_EUTRAN_AUTHENTICATION_INFO_AVP_CODE = convert_to_4_bytes(1408)
NUMBER_OF_REQUESTED_VECTORS_AVP_CODE = convert_to_4_bytes(1410)
RE_SYNCHRONIZATION_INFO_AVP_CODE = convert_to_4_bytes(1411)
IMMEDIATE_RESPONSE_PREFERRED_AVP_CODE = convert_to_4_bytes(1412)
AUTHENTICATION_INFO_AVP_CODE = convert_to_4_bytes(1413)
E_UTRAN_VECTOR_AVP_CODE = convert_to_4_bytes(1414)
ITEM_NUMBER_AVP_CODE = convert_to_4_bytes(1419)
CANCELLATION_TYPE_AVP_CODE = convert_to_4_bytes(1420)
CONTEXT_IDENTIFIER_AVP_CODE = convert_to_4_bytes(1423)
SUBSCRIBER_STATUS_AVP_CODE = convert_to_4_bytes(1424)
OPERATOR_DETERMINED_BARRING_AVP_CODE = convert_to_4_bytes(1425)
ALL_APN_CONFIGURATIONS_INCLUDED_INDICATOR_AVP_CODE = convert_to_4_bytes(1428)
APN_CONFIGURATION_PROFILE_AVP_CODE = convert_to_4_bytes(1429)
APN_CONFIGURATION_AVP_CODE = convert_to_4_bytes(1430)
EPS_SUBSCRIBED_QOS_PROFILE_AVP_CODE = convert_to_4_bytes(1431)
VPLMN_DYNAMIC_ADDRESS_ALLOWED_AVP_CODE = convert_to_4_bytes(1432)
STN_SR_AVP_CODE = convert_to_4_bytes(1433)
ALERT_REASON_AVP_CODE = convert_to_4_bytes(1434)
AMBR_AVP_CODE = convert_to_4_bytes(1435)
PDN_GW_ALLOCATION_TYPE_AVP_CODE = convert_to_4_bytes(1438)
PUA_FLAGS_AVP_CODE = convert_to_4_bytes(1442)
NOR_FLAGS_AVP_CODE = convert_to_4_bytes(1443)
EQUIPMENT_STATUS_AVP_CODE = convert_to_4_bytes(1445)
RAND_AVP_CODE = convert_to_4_bytes(1447)
XRES_AVP_CODE = convert_to_4_bytes(1448)
AUTN_AVP_CODE = convert_to_4_bytes(1449)
KASME_AVP_CODE = convert_to_4_bytes(1450)
PDN_TYPE_AVP_CODE = convert_to_4_bytes(1456)
HOMOGENEOUS_SUPPORT_OF_IMS_VOICE_OVER_PS_SESSION_AVP_CODE = convert_to_4_bytes(1493)
ERROR_DIAGNOSTIC_AVP_CODE = convert_to_4_bytes(1614)
UE_SRVCC_CAPABILITY_AVP_CODE = convert_to_4_bytes(1615)
PUR_FLAGS_AVP_CODE = convert_to_4_bytes(1635)
CLR_FLAGS_AVP_CODE = convert_to_4_bytes(1638)
AIR_FLAGS_AVP_CODE = convert_to_4_bytes(1679)
UE_USAGE_TYPE_AVP_CODE = convert_to_4_bytes(1680)
SUPPORTED_SERVICES_AVP_CODE = convert_to_4_bytes(3143)
SUPPORTED_MONITORING_EVENTS_AVP_CODE = convert_to_4_bytes(3144)

#: List of Cancellation-Type AVP values.
#: For more information, please refer to Section 7.3.24 of 
#: ETSI TS 129 272 V15.4.0 (2018-07).
CANCELLATION_TYPE_MME_UPDATE_PROCEDURE = convert_to_4_bytes(0)
CANCELLATION_TYPE_SGSN_UPDATE_PROCEDURE = convert_to_4_bytes(1)
CANCELLATION_TYPE_SUBSCRIPTION_WITHDRAWAL = convert_to_4_bytes(2)
CANCELLATION_TYPE_UPDATE_PROCEDURE_IWF = convert_to_4_bytes(3)
CANCELLATION_TYPE_INITIAL_ATTACH_PROCEDURE = convert_to_4_bytes(4)

#: List of Subscriber-Status AVP values.
#: For more information, please refer to Section 7.3.29 of
#: ETSI TS 129 272 V15.4.0 (2018-07).
SUBSCRIBER_STATUS_SERVICE_GRANTED = convert_to_4_bytes(0)
SUBSCRIBER_STATUS_OPERATOR_DETERMINED_BARRING = convert_to_4_bytes(1)

#: List of All-APN-Configurations-Included-Indicator AVP values.
#: For more information, please refer to Section 7.3.33 of
#: ETSI TS 129 272 V15.4.0 (2018-07).
ALL_APN_CONFIGURATIONS_INCLUDED = convert_to_4_bytes(0)
MODIFIED_ADDED_APN_CONFIGURATIONS_INCLUDED = convert_to_4_bytes(1)

#: List of VPLMN-Dynamic-Address-Allowed.
#: For more information, please refer to Section 7.3.38 of 
#: ETSI TS 129 272 V12.6.0 (2014-10).
VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED = convert_to_4_bytes(0)
VPLMN_DYNAMIC_ADDRESS_ALLOWED_ALLOWED = convert_to_4_bytes(1)

#: List of PDN-GW-Allocation-Type values.
#: For more information, please refer to Section 7.3.44 of
#  ETSI TS 129 272 V15.10.0 (2020-01).
PDN_GW_ALLOCATION_TYPE_STATIC = convert_to_4_bytes(0)
PDN_GW_ALLOCATION_TYPE_DYNAMIC = convert_to_4_bytes(1)

#: List of Equipment-Status AVP values.
#: For more information, please refer to Section 7.3.51 of 
#: ETSI TS 129 272 V15.4.0 (2018-07).
EQUIPMENT_STATUS_WHITELISTED = convert_to_4_bytes(0)
EQUIPMENT_STATUS_BLACKLISTED = convert_to_4_bytes(1)
EQUIPMENT_STATUS_GREYLISTED = convert_to_4_bytes(2)

#: List of PDN-Type values.
#: For more information, please refer to Section 7.3.62 of
#  ETSI TS 129 272 V15.10.0 (2020-01).
PDN_TYPE_IPV4 = convert_to_4_bytes(0)
PDN_TYPE_IPV6 = convert_to_4_bytes(1)
PDN_TYPE_IPV4V6 = convert_to_4_bytes(2)
PDN_TYPE_IPV4_OR_IPV6 = convert_to_4_bytes(3)

#: List of Alert-Reason AVP values.
#: For more information, please refer to Section 7.3.83 of
#: ETSI TS 129 272 V15.4.0 (2018-07).
ALERT_REASON_UE_PRESET = convert_to_4_bytes(0)
ALERT_REASON_UE_MEMORY_AVAILABLE = convert_to_4_bytes(1)

#: List of Homogeneous-Support-of-IMS-Voice-Over-PS-Sessions AVP values.
#: For more information, please refer to Section 7.3.107 of
#: ETSI TS 129 272 V15.4.0 (2018-07).
IMS_VOICE_OVER_PS_NOT_SUPPORTED = convert_to_4_bytes(0)
IMS_VOICE_OVER_PS_SUPPORTED = convert_to_4_bytes(1)

#: List of Error-Diagnostic AVP values.
#: For more information, please refer to Section 7.3.128 of
#: ETSI TS 129 272 V15.4.0 (2018-07).
ERROR_DIAGNOSTIC_GPRS_DATA_SUBSCRIBED = convert_to_4_bytes(0)
ERROR_DIAGNOSTIC_NO_GPRS_DATA_SUBSCRIBED = convert_to_4_bytes(1)
ERROR_DIAGNOSTIC_ODB_ALL_APN = convert_to_4_bytes(2)
ERROR_DIAGNOSTIC_ODB_HPLMN_APN = convert_to_4_bytes(3)
ERROR_DIAGNOSTIC_ODB_VPLMN_APN = convert_to_4_bytes(4)

#: List of UE-SRVCC-Capability AVP values.
#: For more information, please refer to Section 7.3.130 of 
#: ETSI TS 129 272 V15.10.0 (2020-01).
UE_SRVCC_NOT_SUPPORTED = convert_to_4_bytes(0)
UE_SRVCC_SUPPORTED = convert_to_4_bytes(1)
