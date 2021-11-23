# -*- coding: utf-8 -*-
"""
    bromelia.constants.etsi_3gpp.ts_129_212
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains constants defined in ETSI TS 129 212.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_3_bytes
from ..._internal_utils import convert_to_4_bytes


#: Diameter Messages
CC_MESSAGE = convert_to_3_bytes(272)

#: Diameter AVPs
BEARER_USAGE_AVP_CODE = convert_to_4_bytes(1000)
CHARGING_RULE_INSTALL_AVP_CODE = convert_to_4_bytes(1001)
CHARGING_RULE_DEFINITION_AVP_CODE = convert_to_4_bytes(1003)
CHARGING_RULE_NAME_AVP_CODE = convert_to_4_bytes(1005)
EVENT_TRIGGER_AVP_CODE = convert_to_4_bytes(1006)
METERING_METHOD_AVP_CODE = convert_to_4_bytes(1007)
OFFLINE_AVP_CODE = convert_to_4_bytes(1008)
ONLINE_AVP_CODE = convert_to_4_bytes(1009)
PRECEDENCE_AVP_CODE = convert_to_4_bytes(1010)
REPORTING_LEVEL_AVP_CODE = convert_to_4_bytes(1011)
QOS_INFORMATION_AVP_CODE = convert_to_4_bytes(1016)
CHARGING_RULE_REPORT_AVP_CODE = convert_to_4_bytes(1018)
PCC_RULE_STATUS_AVP_CODE = convert_to_4_bytes(1019)
ACCESS_NETWORK_CHARGING_IDENTIFIER_GX_AVP_CODE = convert_to_4_bytes(1022)
NETWORK_REQUEST_SUPPORT_AVP_CODE = convert_to_4_bytes(1024)
GUARANTEED_BITRATE_DL_AVP_CODE = convert_to_4_bytes(1025)
GUARANTEED_BITRATE_UL_AVP_CODE = convert_to_4_bytes(1026)
IP_CAN_TYPE_AVP_CODE = convert_to_4_bytes(1027)
QOS_CLASS_IDENTIFIER_AVP_CODE = convert_to_4_bytes(1028)
RULE_FAILURE_CODE_AVP_CODE = convert_to_4_bytes(1031)
RAT_TYPE_AVP_CODE = convert_to_4_bytes(1032)
APN_AGGREGATE_MAX_BITRATE_DL_AVP_CODE = convert_to_4_bytes(1040)
APN_AGGREGATE_MAX_BITRATE_UL_AVP_CODE = convert_to_4_bytes(1041)
PRIORITY_LEVEL_AVP_CODE = convert_to_4_bytes(1046)
PRE_EMPTION_CAPABILITY_AVP_CODE = convert_to_4_bytes(1047)
PRE_EMPTION_VULNERABILITY_AVP_CODE = convert_to_4_bytes(1048)
DEFAULT_EPS_BEARER_QOS_AVP_CODE = convert_to_4_bytes(1049)
AN_GW_ADDRESS_AVP_CODE = convert_to_4_bytes(1050)
FLOW_INFORMATION_AVP_CODE = convert_to_4_bytes(1058)
CHARGING_CORRELATION_INDICATOR_AVP_CODE = convert_to_4_bytes(1073)
UE_LOCAL_IP_ADDRESS_AVP_CODE = convert_to_4_bytes(2805)

#: List of Bearer-Usage AVP values.
#: For more information, please refer to Section 5.3.1 of 
# ETSI TS 129 212 V15.3.0 (2018-07).
BEARER_USAGE_GENERAL = convert_to_4_bytes(0)
BEARER_USAGE_SIGNALLING = convert_to_4_bytes(1)

#: List of Event-Trigger AVP values.
#: For more information, please refer to Section 5.3.7 of 
#: ETSI TS 129 212 V15.3.0 (2018-07).
EVENT_TRIGGER_SGSN_CHANGE = convert_to_4_bytes(0)
EVENT_TRIGGER_QOS_CHANGE = convert_to_4_bytes(1)
EVENT_TRIGGER_RAT_CHANGE = convert_to_4_bytes(2)
EVENT_TRIGGER_TFT_CHANGE = convert_to_4_bytes(3)
EVENT_TRIGGER_PLMN_CHANGE = convert_to_4_bytes(4)
EVENT_TRIGGER_LOSS_OF_BEARER = convert_to_4_bytes(5)
EVENT_TRIGGER_RECOVERY_OF_BEARER = convert_to_4_bytes(6)
EVENT_TRIGGER_IP_CAN_CHANGE = convert_to_4_bytes(7)
EVENT_TRIGGER_QOS_CHANGE_EXCEEDING_AUTHORIZATION = convert_to_4_bytes(11)
EVENT_TRIGGER_RAI_CHANGE = convert_to_4_bytes(12)
EVENT_TRIGGER_USER_LOCATION_CHANGE = convert_to_4_bytes(13)
EVENT_TRIGGER_NO_EVENT_TRIGGERS = convert_to_4_bytes(14)
EVENT_TRIGGER_OUT_OF_CREDIT = convert_to_4_bytes(15)
EVENT_TRIGGER_REALLOCATION_OF_CREDIT = convert_to_4_bytes(16)
EVENT_TRIGGER_REVALIDATION_TIMEOUT = convert_to_4_bytes(17)
EVENT_TRIGGER_UE_IP_ADDRESS_ALLOCATE = convert_to_4_bytes(18)
EVENT_TRIGGER_UE_IP_ADDRESS_RELEASE = convert_to_4_bytes(19)
EVENT_TRIGGER_DEFAULT_EPS_BEARER_QOS_CHANGE = convert_to_4_bytes(20)
EVENT_TRIGGER_AN_GW_CHANGE = convert_to_4_bytes(21)
EVENT_TRIGGER_SUCCESSFUL_RESOURCE_ALLOCATION = convert_to_4_bytes(22)
EVENT_TRIGGER_RESOURCE_MODIFICATION_REQUEST = convert_to_4_bytes(23)
EVENT_TRIGGER_PGW_TRACE_CONTROL = convert_to_4_bytes(24)
EVENT_TRIGGER_UE_TIME_ZONE_CHANGE = convert_to_4_bytes(25)
EVENT_TRIGGER_TAI_CHANGE = convert_to_4_bytes(26)
EVENT_TRIGGER_ECGI_CHANGE = convert_to_4_bytes(27)
EVENT_TRIGGER_CHARGING_CORRELATION_EXCHANGE = convert_to_4_bytes(28)
EVENT_TRIGGER_APN_AMBR_MODIFICATION_FAILURE = convert_to_4_bytes(29)
EVENT_TRIGGER_USER_CSG_INFORMATION_CHANGE = convert_to_4_bytes(30)
EVENT_TRIGGER_USAGE_REPORT = convert_to_4_bytes(33)
EVENT_TRIGGER_DEFAULT_EPS_BEARER_QOS_MODIFICATION_FAILURE = convert_to_4_bytes(34)
EVENT_TRIGGER_USER_CSG_HYBRID_SUBSCRIBED_INFORMATION_CHANGE = convert_to_4_bytes(35)
EVENT_TRIGGER_USER_CSG_HYBRID_UNSUBSCRIBED_INFORMATION_CHANGE = convert_to_4_bytes(36)
EVENT_TRIGGER_ROUTING_RULE_CHANGE = convert_to_4_bytes(37)
EVENT_TRIGGER_APPLICATION_START = convert_to_4_bytes(39)
EVENT_TRIGGER_APPLICATION_STOP = convert_to_4_bytes(40)
EVENT_TRIGGER_CS_TO_PS_HANDOVER = convert_to_4_bytes(42)
EVENT_TRIGGER_UE_LOCAL_IP_ADDRESS_CHANGE = convert_to_4_bytes(43)
EVENT_TRIGGER_HENB_LOCAL_IP_ADDRESS_CHANGE = convert_to_4_bytes(44)
EVENT_TRIGGER_ACCESS_NETWORK_INFO_REPORT = convert_to_4_bytes(45)
EVENT_TRIGGER_CREDIT_MANAGEMENT_SESSION_FAILURE = convert_to_4_bytes(46)
EVENT_TRIGGER_DEFAULT_QOS_CHANGE = convert_to_4_bytes(47)
EVENT_TRIGGER_CHANGE_OF_UE_PRESENCE_IN_PRESENCE_REPORTING_AREA_REPORT = convert_to_4_bytes(48)
EVENT_TRIGGER_ADDITION_OF_ACCESS = convert_to_4_bytes(49)
EVENT_TRIGGER_REMOVAL_OF_ACCESS = convert_to_4_bytes(50)
EVENT_TRIGGER_UNAVAILABILITY_OF_ACCESS = convert_to_4_bytes(51)
EVENT_TRIGGER_AVAILABILITY_OF_ACCESS = convert_to_4_bytes(52)
EVENT_TRIGGER_RESOURCE_RELEASE = convert_to_4_bytes(53)
EVENT_TRIGGER_ENODEB_CHANGE = convert_to_4_bytes(54)
EVENT_TRIGGER_3GPP_PS_DATA_OFF_CHANGE = convert_to_4_bytes(55)

#: List of Metering-Method AVP values.
#: For more information, please refer to Section 5.3.8 of
#: ETSI TS 129 212 V15.3.0 (2018-07).
METERING_METHOD_DURATION = convert_to_4_bytes(0)
METERING_METHOD_VOLUME = convert_to_4_bytes(1)
METERING_METHOD_DURATION_VOLUME = convert_to_4_bytes(2)
METERING_METHOD_EVENT = convert_to_4_bytes(3)

#: List of Offline AVP values.
#: For more information, please refer to Section 5.3.9 of
#: ETSI TS 129 212 V15.3.0 (2018-07).
OFFLINE_DISABLE_OFFLINE = convert_to_4_bytes(0)
OFFLINE_ENABLE_OFFLINE = convert_to_4_bytes(1)

#: List of Online AVP values.
#: For more information, please refer to Section 5.3.10 of
#: ETSI TS 129 212 V15.3.0 (2018-07).
ONLINE_DISABLE_ONLINE = convert_to_4_bytes(0)
ONLINE_ENABLE_ONLINE = convert_to_4_bytes(1)

#: List of Reporting-Level AVP values.
#: For more information, please refer to Section 5.3.12 of 
#: ETSI TS 129 212 V15.3.0 (2018-07).
REPORTING_LEVEL_SERVICE_IDENTIFIER_LEVEL = convert_to_4_bytes(0)
REPORTING_LEVEL_RATING_GROUP_LEVEL = convert_to_4_bytes(1)
REPORTING_LEVEL_SPONSORED_CONNECTIVITY_LEVEL = convert_to_4_bytes(2)

#: List of QOS-CLASS-IDENTIFIER.
#: For more information, please refer to Section 5.3.17 of 
#: of ETSI TS 129 212 V15.3.0 (2018-07).
QCI_1 = convert_to_4_bytes(1)
QCI_2 = convert_to_4_bytes(2)
QCI_3 = convert_to_4_bytes(3)
QCI_4 = convert_to_4_bytes(4)
QCI_5 = convert_to_4_bytes(5)
QCI_6 = convert_to_4_bytes(6)
QCI_7 = convert_to_4_bytes(7)
QCI_8 = convert_to_4_bytes(8)
QCI_9 = convert_to_4_bytes(9)
QCI_65 = convert_to_4_bytes(65)
QCI_66 = convert_to_4_bytes(66)
QCI_69 = convert_to_4_bytes(69)
QCI_70 = convert_to_4_bytes(70)
QCI_75 = convert_to_4_bytes(75)
QCI_79 = convert_to_4_bytes(79)
QCI_80 = convert_to_4_bytes(80)
QCI_82 = convert_to_4_bytes(82)
QCI_83 = convert_to_4_bytes(83)
QCI_84 = convert_to_4_bytes(84)
QCI_85 = convert_to_4_bytes(85)

#: List of PCC-Rule-Status AVP values.
#: For more information, please refer to Section 5.3.19 of
#: ETSI TS 129 212 V15.3.0 (2018-07).
PCC_RULE_STATUS_ACTIVE = convert_to_4_bytes(0)
PCC_RULE_STATUS_INACTIVE = convert_to_4_bytes(1)
PCC_RULE_STATUS_TEMPORARILY_INACTIVE = convert_to_4_bytes(2)

#: List of Network-Request-Support AVP values.
#: For more information, please refer to Section 5.3.24 of
#: ETSI TS 129 212 V15.3.0 (2018-07).
NETWORK_REQUEST_NOT_SUPPORTED = convert_to_4_bytes(0)
NETWORK_REQUEST_SUPPORTED = convert_to_4_bytes(1)

#: List of IP-CAN-Type AVP values.
#: For more information, please refer to Section 5.3.27 of 
#: ETSI TS 129 212 V15.3.0 (2018-07).
IP_CAN_TYPE_3GPP_GPRS = convert_to_4_bytes(0)
IP_CAN_TYPE_DOCSIS = convert_to_4_bytes(1)
IP_CAN_TYPE_XDSL = convert_to_4_bytes(2)
IP_CAN_TYPE_WIMAX = convert_to_4_bytes(3)
IP_CAN_TYPE_3GPP2 = convert_to_4_bytes(4)
IP_CAN_TYPE_3GPP_EPS = convert_to_4_bytes(5)
IP_CAN_TYPE_NON_3GPP_EPS = convert_to_4_bytes(6)
IP_CAN_TYPE_FBA = convert_to_4_bytes(7)
IP_CAN_TYPE_3GPP_5GS = convert_to_4_bytes(8)
IP_CAN_TYPE_NON_3GPP_5GS = convert_to_4_bytes(9)

#: List of RAT-TYPES.
#: For more information, please refer to Section 5.3.31 of 3GPP TS 129 212.
RAT_TYPE_WLAN = convert_to_4_bytes(0)
RAT_TYPE_VIRTUAL = convert_to_4_bytes(1)
RAT_TYPE_UTRAN = convert_to_4_bytes(1000)
RAT_TYPE_GERAN = convert_to_4_bytes(1001)
RAT_TYPE_GAN = convert_to_4_bytes(1002)
RAT_TYPE_HSPA_EVOLUTION = convert_to_4_bytes(1003)
RAT_TYPE_EUTRAN = convert_to_4_bytes(1004)
RAT_TYPE_CDMA2000_1X = convert_to_4_bytes(2000)
RAT_TYPE_HRPD = convert_to_4_bytes(2001)
RAT_TYPE_UMB = convert_to_4_bytes(2002)
RAT_TYPE_EHRPD = convert_to_4_bytes(2003)

#: List of Rule-Failure-Code AVP values.
#: For more information, please refer to Section 5.3.38 of
#: ETSI TS 129 212 V15.3.0 (2018-07).
RULE_FAILURE_CODE_UNKNOWN_RULE_NAME = convert_to_4_bytes(1)
RULE_FAILURE_CODE_RATING_GROUP_ERROR = convert_to_4_bytes(2)
RULE_FAILURE_CODE_SERVICE_IDENTIFIER_ERROR = convert_to_4_bytes(3)
RULE_FAILURE_CODE_GW_PCEF_MALFUNCTION = convert_to_4_bytes(4)
RULE_FAILURE_CODE_RESOURCES_LIMITATION = convert_to_4_bytes(5)
RULE_FAILURE_CODE_MAX_NR_BEARERS_REACHED = convert_to_4_bytes(6)
RULE_FAILURE_CODE_UNKNOWN_BEARER_ID = convert_to_4_bytes(7)
RULE_FAILURE_CODE_MISSING_BEARER_ID = convert_to_4_bytes(8)
RULE_FAILURE_CODE_MISSING_FLOW_INFORMATION = convert_to_4_bytes(9)
RULE_FAILURE_CODE_RESOURCE_ALLOCATION_FAILURE = convert_to_4_bytes(10)
RULE_FAILURE_CODE_UNSUCCESSFUL_QOS_VALIDATION = convert_to_4_bytes(11)
RULE_FAILURE_CODE_INCORRECT_FLOW_INFORMATION = convert_to_4_bytes(12)
RULE_FAILURE_CODE_PS_TO_CS_HANDOVER = convert_to_4_bytes(13)
RULE_FAILURE_CODE_TDF_APPLICATION_IDENTIFIER_ERROR = convert_to_4_bytes(14)
RULE_FAILURE_CODE_NO_BEARER_BOUND = convert_to_4_bytes(15)
RULE_FAILURE_CODE_FILTER_RESTRICTIONS = convert_to_4_bytes(16)
RULE_FAILURE_CODE_AN_GW_FAILED = convert_to_4_bytes(17)
RULE_FAILURE_CODE_MISSING_REDIRECT_SERVER_ADDRESS = convert_to_4_bytes(18)
RULE_FAILURE_CODE_CM_END_USER_SERVICE_DENIED = convert_to_4_bytes(19)
RULE_FAILURE_CODE_CM_CREDIT_CONTROL_NOT_APPLICABLE = convert_to_4_bytes(20)
RULE_FAILURE_CODE_CM_AUTHORIZATION_REJECTED = convert_to_4_bytes(21)
RULE_FAILURE_CODE_CM_USER_UNKNOWN = convert_to_4_bytes(22)
RULE_FAILURE_CODE_CM_RATING_FAILED = convert_to_4_bytes(23)
RULE_FAILURE_CODE_ROUTING_RULE_REJECTION = convert_to_4_bytes(24)
RULE_FAILURE_CODE_UNKNOWN_ROUTING_ACCESS_INFORMATION = convert_to_4_bytes(25)
RULE_FAILURE_CODE_NO_NBIFOM_SUPPORT = convert_to_4_bytes(26)

#: List of Pre-emption-Capability AVP values.
#: For more information, please refer to Section Section 5.3.46 of 
#: ETSI TS 129 212 V15.3.0 (2018-07).
PRE_EMPTION_CAPABILITY_ENABLED = convert_to_4_bytes(0)
PRE_EMPTION_CAPABILITY_DISABLED = convert_to_4_bytes(1)

#: List of Pre-emption-Vulnerability AVP values.
#: For more information, please refer to Section Section 5.3.47 of 
#: ETSI TS 129 212 V15.3.0 (2018-07).
PRE_EMPTION_VULNERABILITY_ENABLED = convert_to_4_bytes(0)
PRE_EMPTION_VULNERABILITY_DISABLED = convert_to_4_bytes(1)

#: List of Charging-Correlation-Indicator AVP values.
#: For more information, please refer to Section 5.3.67 of 
#: ETSI TS 129 212 V15.3.0 (2018-07).
CHARGING_CORRELATION_INDICATOR_CHARGING_IDENTIFIER_REQUIRED = convert_to_4_bytes(0)
