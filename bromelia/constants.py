#: -*- coding: utf-8 -*-
"""
    bromelia.constants
    ~~~~~~~~~~~~~~~~~~

    This module contains constants that are defined in several
    Diameter standard documents (both ETSI and IETF specs), not 
    only the main Diameter protocol document (RFC 6733).
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ._internal_utils import convert_to_1_byte
from ._internal_utils import convert_to_2_bytes
from ._internal_utils import convert_to_3_bytes
from ._internal_utils import convert_to_4_bytes

PRODUCT_NAME = f"Python bromelia"

#: *************************************************************************************************

DIAMETER_VERSION = convert_to_1_byte(1)
FIRMWARE_VERSION = convert_to_4_bytes(1)

#: *************************************************************************************************

#: DIAMETER AGENT TYPES.
DIAMETER_AGENT_CLIENT_MODE = "CLIENT"
DIAMETER_AGENT_SERVER_MODE = "SERVER"

#: *************************************************************************************************

#: DIAMETER AVPS.
USER_NAME_AVP_CODE = convert_to_4_bytes(1)                              # OK
FRAMED_IP_ADDRESS_AVP_CODE = convert_to_4_bytes(8)                      # TBT Rx
X_3GPP_CHARGING_CHARACTERISTICS_AVP_CODE = convert_to_4_bytes(13)
CLASS_AVP_CODE = convert_to_4_bytes(25)
SESSION_TIMEOUT_AVP_CODE = convert_to_4_bytes(27)                       # OK
CALLED_STATION_ID_AVP_CODE = convert_to_4_bytes(30)                     # TBT Rx
CALLING_STATION_ID_AVP_CODE = convert_to_4_bytes(31)                    # OK
PROXY_STATE_AVP_CODE = convert_to_4_bytes(33)                           # OK
ACCT_SESSION_ID_AVP_CODE = convert_to_4_bytes(44)                       # OK
ACCT_MULTI_SESSION_ID_AVP_CODE = convert_to_4_bytes(50)                 # OK
EVENT_TIMESTAMP_AVP_CODE = convert_to_4_bytes(55)                       # OK
ACCT_INTERIM_INTERVAL_AVP_CODE = convert_to_4_bytes(85)                 # OK
FRAMED_IPV6_PREFIX_AVP_CODE = convert_to_4_bytes(97)                    # TBT Rx
MIP6_FEATURE_VECTOR_AVP_CODE = convert_to_4_bytes(124)
HOST_IP_ADDRESS_AVP_CODE = convert_to_4_bytes(257)                      # OK
AUTH_APPLICATION_ID_AVP_CODE = convert_to_4_bytes(258)                  # OK
ACCT_APPLICATION_ID_AVP_CODE = convert_to_4_bytes(259)                  # OK
VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE = convert_to_4_bytes(260)
REDIRECT_HOST_USAGE_AVP_CODE = convert_to_4_bytes(261)
REDIRECT_MAX_CACHE_TIME_AVP_CODE = convert_to_4_bytes(262)
SESSION_ID_AVP_CODE = convert_to_4_bytes(263)                           # OK
ORIGIN_HOST_AVP_CODE = convert_to_4_bytes(264)                          # OK
SUPPORTED_VENDOR_ID_AVP_CODE = convert_to_4_bytes(265)                  # OK
VENDOR_ID_AVP_CODE = convert_to_4_bytes(266)                            # OK
FIRMWARE_REVISION_AVP_CODE = convert_to_4_bytes(267)                    # OK
RESULT_CODE_AVP_CODE = convert_to_4_bytes(268)                          # OK
PRODUCT_NAME_AVP_CODE = convert_to_4_bytes(269)                         # OK
SESSION_BINDING_AVP_CODE = convert_to_4_bytes(270)                      # OK
SESSION_SERVER_FAILOVER_AVP_CODE = convert_to_4_bytes(271)              # OK
MULTI_ROUND_TIME_OUT_AVP_CODE = convert_to_4_bytes(272)                 # OK
DISCONNECT_CAUSE_AVP_CODE = convert_to_4_bytes(273)                     # OK
AUTH_REQUEST_TYPE_AVP_CODE = convert_to_4_bytes(274)                    # OK
AUTH_GRACE_PERIOD_AVP_CODE = convert_to_4_bytes(276)                    # OK
AUTH_SESSION_STATE_AVP_CODE = convert_to_4_bytes(277)                   # OK
ORIGIN_STATE_ID_AVP_CODE = convert_to_4_bytes(278)
FAILED_AVP_AVP_CODE = convert_to_4_bytes(279)
PROXY_HOST_AVP_CODE = convert_to_4_bytes(280)
ERROR_MESSAGE_AVP_CODE = convert_to_4_bytes(281)
ROUTE_RECORD_AVP_CODE = convert_to_4_bytes(282)                         # OK
DESTINATION_REALM_AVP_CODE = convert_to_4_bytes(283)                    # OK
PROXY_INFO_AVP_CODE = convert_to_4_bytes(284)
RE_AUTH_REQUEST_TYPE_AVP_CODE = convert_to_4_bytes(285)
ACCOUNTING_SUB_SESSION_ID_AVP_CODE = convert_to_4_bytes(287)            # OK
AUTHORIZATION_LIFETIME_AVP_CODE = convert_to_4_bytes(291)               # OK
REDIRECT_HOST_AVP_CODE = convert_to_4_bytes(292)
DESTINATION_HOST_AVP_CODE = convert_to_4_bytes(293)                     # OK
ERROR_REPORTING_HOST_AVP_CODE = convert_to_4_bytes(294)
TERMINATION_CAUSE_AVP_CODE = convert_to_4_bytes(295)                    # OK
ORIGIN_REALM_AVP_CODE = convert_to_4_bytes(296)                         # OK
EXPERIMENTAL_RESULT_AVP_CODE = convert_to_4_bytes(297)                  # OK
EXPERIMENTAL_RESULT_CODE_AVP_CODE = convert_to_4_bytes(298)
INBAND_SECURITY_ID_AVP_CODE = convert_to_4_bytes(299)
MIP_HOME_AGENT_HOST_AVP_CODE = convert_to_4_bytes(348)
SUBSCRIPTION_ID_AVP_CODE = convert_to_4_bytes(443)
SUBSCRIPTION_ID_DATA_AVP_CODE = convert_to_4_bytes(444)
SUBSCRIPTION_ID_TYPE_AVP_CODE = convert_to_4_bytes(450)
RESERVATION_PRIORITY_AVP_CODE = convert_to_4_bytes(458)                 # TBT Rx
EAP_PAYLOAD_AVP_CODE = convert_to_4_bytes(462)
EAP_MASTER_SESSION_KEY_AVP_CODE = convert_to_4_bytes(464)
ACCOUNTING_RECORD_TYPE_AVP_CODE = convert_to_4_bytes(480)               # OK
ACCOUNTING_REALTIME_REQUIRED_AVP_CODE = convert_to_4_bytes(483)   		# OK
ACCOUNTING_RECORD_NUMBER_AVP_CODE = convert_to_4_bytes(485)             # OK
MIP6_AGENT_INFO_AVP_CODE = convert_to_4_bytes(486)
SERVICE_SELECTION_AVP_CODE = convert_to_4_bytes(493)
ABORT_CAUSE_AVP_CODE = convert_to_4_bytes(500)                          # TBT Rx
ACCESS_NETWORK_CHARGING_ADDRESS_AVP_CODE = convert_to_4_bytes(501)
AF_APPLICATION_IDENTIFIER_AVP_CODE = convert_to_4_bytes(504)            # TBT Rx
AF_CHARGING_IDENTIFIER_AVP_CODE = convert_to_4_bytes(505)               # TBT Rx
MOBILE_NODE_IDENTIFIER_AVP_CODE = convert_to_4_bytes(506)
FLOW_DESCRIPTION_AVP_CODE = convert_to_4_bytes(507)                     # TBT Rx
FLOW_NUMBER_AVP_CODE = convert_to_4_bytes(509)                          # TBT Rx
FLOW_STATUS_AVP_CODE = convert_to_4_bytes(511)                          # TBT Rx
FLOW_USAGE_AVP_CODE = convert_to_4_bytes(512)                           # TBT Rx
SPECIFIC_ACTION_AVP_CODE = convert_to_4_bytes(513)                      # TBT Rx
MAX_REQUESTED_BANDWIDTH_DL_AVP_CODE = convert_to_4_bytes(515)
MAX_REQUESTED_BANDWIDTH_UL_AVP_CODE = convert_to_4_bytes(516)
MEDIA_COMPONENT_DESCRIPTION_AVP_CODE = convert_to_4_bytes(517)          # TBT Rx
MEDIA_COMPONENT_NUMBER_AVP_CODE = convert_to_4_bytes(518)               # TBT Rx
MEDIA_SUB_COMPONENT_AVP_CODE = convert_to_4_bytes(519)                  # TBT Rx
MEDIA_TYPE_AVP_CODE = convert_to_4_bytes(520)                           # TBT Rx
SERVICE_INFO_STATUS_AVP_CODE = convert_to_4_bytes(527)                  # TBT Rx
VISITED_NETWORK_IDENTIFIER_AVP_CODE = convert_to_4_bytes(600)

SIP_NUMBER_AUTH_ITEMS_AVP_CODE = convert_to_4_bytes(607)				# OK
SIP_AUTHENTICATION_SCHEME_AVP_CODE = convert_to_4_bytes(608)		    # OK
SIP_AUTHENTICATE_AVP_CODE = convert_to_4_bytes(609)						# OK
SIP_AUTHORIZATION_AVP_CODE = convert_to_4_bytes(610)					# OK
SIP_AUTH_DATA_ITEM_AVP_CODE = convert_to_4_bytes(612)					# OK
SERVER_ASSIGNMENT_TYPE_AVP_CODE = convert_to_4_bytes(614)
DE_REGISTRATION_REASON_AVP_CODE = convert_to_4_bytes(615)
REASON_CODE_AVP_CODE = convert_to_4_bytes(616)
REASON_INFO_AVP_CODE = convert_to_4_bytes(617)
CONFIDENTIALITY_KEY_AVP_CODE = convert_to_4_bytes(625)					# OK
INTEGRITY_KEY_AVP_CODE = convert_to_4_bytes(626)						# OK

SUPPORTED_FEATURES_AVP_CODE = convert_to_4_bytes(628)
FEATURE_LIST_ID_AVP_CODE = convert_to_4_bytes(629)
FEATURE_LIST_AVP_CODE = convert_to_4_bytes(630)
PRECEDENCE_AVP_CODE = convert_to_4_bytes(1010)                          # TBT Rx
REPORTING_LEVEL_AVP_CODE = convert_to_4_bytes(1011)                     # TBT Rx
IP_CAN_TYPE_AVP_CODE = convert_to_4_bytes(1027)                         # TBT Rx
QOS_CLASS_IDENTIFIER_AVP_CODE = convert_to_4_bytes(1028)
RAT_TYPE_AVP_CODE = convert_to_4_bytes(1032)
ALLOCATION_RETENTION_PRIORITY_AVP_CODE = convert_to_4_bytes(1034)
PRIORITY_LEVEL_AVP_CODE = convert_to_4_bytes(1046)
PRE_EMPTION_CAPABILITY_AVP_CODE = convert_to_4_bytes(1047)              # TBT
PRE_EMPTION_VULNERABILITY_AVP_CODE = convert_to_4_bytes(1048)           # TBT
AN_GW_ADDRESS_AVP_CODE = convert_to_4_bytes(1050)                       # TBT Rx
CHARGING_CORRELATION_INDICATOR_AVP_CODE = convert_to_4_bytes(1073)      # TBT Rx
TERMINAL_INFORMATION_AVP_CODE = convert_to_4_bytes(1401)
IMEI_AVP_CODE = convert_to_4_bytes(1402)
SOFTWARE_VERSION_AVP_CODE = convert_to_4_bytes(1403)
ULR_FLAGS_AVP_CODE = convert_to_4_bytes(1405)
VISITED_PLMN_ID_AVP_CODE = convert_to_4_bytes(1407)
CANCELLATION_TYPE_AVP_CODE = convert_to_4_bytes(1420)
CONTEXT_IDENTIFIER_AVP_CODE = convert_to_4_bytes(1423)
APN_CONFIGURATION_AVP_CODE = convert_to_4_bytes(1430)
EPS_SUBSCRIBED_QOS_PROFILE_AVP_CODE = convert_to_4_bytes(1431)
VPLMN_DYNAMIC_ADDRESS_ALLOWED_AVP_CODE = convert_to_4_bytes(1432)
AMBR_AVP_CODE = convert_to_4_bytes(1435)
PDN_GW_ALLOCATION_TYPE_AVP_CODE = convert_to_4_bytes(1438)
EQUIPMENT_STATUS_AVP_CODE = convert_to_4_bytes(1445)
PDN_TYPE_AVP_CODE = convert_to_4_bytes(1456)
NON_3GPP_USER_DATA_AVP_CODE = convert_to_4_bytes(1500)
NON_3GPP_IP_ACCESS_AVP_CODE = convert_to_4_bytes(1501)
NON_3GPP_IP_ACCESS_APN_AVP_CODE = convert_to_4_bytes(1502)
AN_TRUSTED_AVP_CODE = convert_to_4_bytes(1503)                          # TBT Rx
UE_SRVCC_CAPABILITY_AVP_CODE = convert_to_4_bytes(1615)
CLR_FLAGS_AVP_CODE = convert_to_4_bytes(1638)
UE_LOCAL_IP_ADDRESS_AVP_CODE = convert_to_4_bytes(2805)
SUPPORTED_SERVICES_AVP_CODE = convert_to_4_bytes(3143)
SUPPORTED_MONITORING_EVENTS_AVP_CODE = convert_to_4_bytes(3144)

#: *************************************************************************************************

#: COMMAND CODES.
CAPABILITIES_EXCHANGE_MESSAGE = convert_to_3_bytes(257)
RE_AUTH_MESSAGE = convert_to_3_bytes(258)
AA_MESSAGE = convert_to_3_bytes(265)
DIAMETER_EAP_MESSAGE = convert_to_3_bytes(268)
ABORT_SESSION_MESSAGE = convert_to_3_bytes(274)
SESSION_TERMINATION_MESSAGE = convert_to_3_bytes(275)
DEVICE_WATCHDOG_MESSAGE = convert_to_3_bytes(280)
DISCONNECT_PEER_MESSAGE = convert_to_3_bytes(282)
SERVER_ASSIGNMENT_MESSAGE = convert_to_3_bytes(301)
MULTIMEDIA_AUTH_MESSAGE = convert_to_3_bytes(303)
REGISTRATION_TERMINATION_MESSAGE = convert_to_3_bytes(304)
PUSH_PROFILE_MESSAGE = convert_to_3_bytes(305)
CANCEL_LOCATION_MESSAGE = convert_to_3_bytes(317)
EC_MESSAGE = convert_to_3_bytes(324)

#: *************************************************************************************************

#: BASIC AVP DATA FORMATS.
AVP_LENGTH_UNSIGNED32 = 12
AVP_LENGTH_UNSIGNED32_AND_V_BIT = 16

AVP_LENGTH_INTEGER32 = 12
AVP_LENGTH_INTEGER32_AND_V_BIT = 16

AVP_LENGTH_INTEGER64 = 16
AVP_LENGTH_INTEGER64_AND_V_BIT = 20

#: *************************************************************************************************

#: CONSTANTS FOR FIELDS LENGHT OF DIAMETER HEADER.
DIAMETER_VERSION_FIELD = 1
DIAMETER_LENGTH_FIELD = 3
DIAMETER_FLAG_FIELD = 1
DIAMETER_COMMAND_CODE_FIELD = 3
DIAMETER_APPLICATION_ID_FIELD = 4
DIAMETER_HOP_BY_HOP_FIELD = 4
DIAMETER_END_TO_END_FIELD = 4

DIAMETER_HEADER_LENGTH = DIAMETER_VERSION_FIELD + DIAMETER_LENGTH_FIELD + DIAMETER_FLAG_FIELD + \
                        DIAMETER_COMMAND_CODE_FIELD + DIAMETER_APPLICATION_ID_FIELD + \
                        DIAMETER_HOP_BY_HOP_FIELD + DIAMETER_END_TO_END_FIELD

#: *************************************************************************************************

#: CONSTANTS FOR FIELDS LENGHT OF DIAMETER AVP HEADER.
AVP_CODE_FIELD = 4
AVP_FLAG_FIELD = 1
AVP_LENGTH_FIELD = 3
AVP_VENDOR_ID_FIELD = 4

AVP_HEADER_LENGTH = AVP_CODE_FIELD + AVP_FLAG_FIELD + AVP_LENGTH_FIELD
AVP_HEADER_LENGTH_LONGER = AVP_HEADER_LENGTH + AVP_VENDOR_ID_FIELD

#: *************************************************************************************************

#: List of COMMAND FLAGS IN DIAMETER HEADER.
FLAG_RESPONSE = convert_to_1_byte(0x00)
FLAG_RESPONSE_AND_RETRANSMITTED = convert_to_1_byte(0x10)
FLAG_RESPONSE_AND_ERROR = convert_to_1_byte(0x20)
FLAG_RESPONSE_AND_ERROR_AND_RETRANSMITTED = convert_to_1_byte(0x30)
FLAG_RESPONSE_AND_PROXYABLE = convert_to_1_byte(0x40)
FLAG_RESPONSE_AND_PROXYABLE_AND_RETRANSMITTED = convert_to_1_byte(0x50)
FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR = convert_to_1_byte(0x60)
FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR_AND_RETRANSMITTED = convert_to_1_byte(0x70)

FLAG_REQUEST = convert_to_1_byte(0x80)
FLAG_REQUEST_AND_RETRANSMITTED = convert_to_1_byte(0x90)
FLAG_REQUEST_AND_ERROR = convert_to_1_byte(0xa0)
FLAG_REQUEST_AND_ERROR_AND_RETRANSMITTED = convert_to_1_byte(0xb0)
FLAG_REQUEST_AND_PROXYABLE = convert_to_1_byte(0xc0)
FLAG_REQUEST_AND_PROXYABLE_AND_RETRANSMITTED = convert_to_1_byte(0xd0)
FLAG_REQUEST_AND_PROXYABLE_AND_ERROR = convert_to_1_byte(0xe0)
FLAG_REQUEST_AND_PROXYABLE_AND_ERROR_AND_RETRANSMITTED = convert_to_1_byte(0xf0)

#: *************************************************************************************************

#: List of COMMAND FLAGS IN DIAMETER AVP HEADER.
FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED = bytes.fromhex("00")
FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_PROTECTED = bytes.fromhex("20")
FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED = bytes.fromhex("40")
FLAG_NOT_VENDOR_SPECIFIC_MANDATORY_AND_PROTECTED = bytes.fromhex("60")

FLAG_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED = bytes.fromhex("80")
FLAG_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_PROTECTED = bytes.fromhex("a0")
FLAG_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED = bytes.fromhex("c0")
FLAG_VENDOR_SPECIFIC_MANDATORY_AND_PROTECTED = bytes.fromhex("e0")

#: *************************************************************************************************

#: List of DIAMETER APPLICATION ID.
DIAMETER_APPLICATION_DEFAULT = convert_to_4_bytes(0)
DIAMETER_APPLICATION_Cx = convert_to_4_bytes(16777216)
DIAMETER_APPLICATION_Sh = convert_to_4_bytes(16777217)
DIAMETER_APPLICATION_Zh = convert_to_4_bytes(16777221)
DIAMETER_APPLICATION_Rx = convert_to_4_bytes(16777236)
DIAMETER_APPLICATION_Gx = convert_to_4_bytes(16777238)
DIAMETER_APPLICATION_S6a_S6d = convert_to_4_bytes(16777251)
DIAMETER_APPLICATION_S13_S13 = convert_to_4_bytes(16777252)
DIAMETER_APPLICATION_SWm = convert_to_4_bytes(16777264)
DIAMETER_APPLICATION_SWx = convert_to_4_bytes(16777265)
DIAMETER_APPLICATION_S6b = convert_to_4_bytes(16777272)
DIAMETER_APPLICATION_SLh = convert_to_4_bytes(16777291)
DIAMETER_APPLICATION_UNKNOWN = convert_to_4_bytes(4123456789)
DIAMETER_APPLICATION_RELAY = convert_to_4_bytes(4294967295)

#: List of Termination-Cause AVP values.
#: For more information, please refer to IANA's website or Section 8.47 
#: of IETF RFC 6733.
#: https://www.iana.org/assignments/aaa-parameters/aaa-parameters.xml#aaa-parameters-16
DIAMETER_LOGOUT = convert_to_4_bytes(1)
DIAMETER_SERVICE_NOT_PROVIDED = convert_to_4_bytes(2)
DIAMETER_BAD_ANSWER = convert_to_4_bytes(3)
DIAMETER_ADMINISTRATIVE = convert_to_4_bytes(4)
DIAMETER_LINK_BROKEN = convert_to_4_bytes(5)
DIAMETER_AUTH_EXPIRED = convert_to_4_bytes(6)
DIAMETER_USER_MOVED = convert_to_4_bytes(7)
DIAMETER_SESSION_TIMEOUT = convert_to_4_bytes(8)

#: List of DISCONNECT-CAUSE. 
#: For more information, please refer to Section 5.4.3 of IETF RFC 3588.
DISCONNECT_CAUSE_REBOOTING = convert_to_4_bytes(0)
DISCONNECT_CAUSE_BUSY = convert_to_4_bytes(1)
DISCONNECT_CAUSE_DO_NOT_WANT_TO_TALK_TO_YOU = convert_to_4_bytes(2)

#: List of QOS-CLASS-IDENTIFIER.
#: For more information, please refer to Section 5.3.17 of 
#: ETSI TS 129 212 V12.6.0 (2014-10).
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

#: List of Auth-Request-Type AVP values.
#: For more information, please refer to Section 8.7 of IETF RFC 3588.
AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY = convert_to_4_bytes(1)
AUTH_REQUEST_TYPE_AUTHORIZE_ONLY = convert_to_4_bytes(2)
AUTH_REQUEST_TYPE_AUTHORIZE_AUTHENTICATE = convert_to_4_bytes(3)

#: List of Re-Auth-Request-Type AVP values.
#: For more information, please refer to Section 8.12 of IETF RFC 6733.
RE_AUTH_REQUEST_TYPE_AUTHORIZE_ONLY = convert_to_4_bytes(0)
RE_AUTH_REQUEST_TYPE_AUTHORIZE_AUTHENTICATE = convert_to_4_bytes(1)

#: List of AUTH-SESSION-STATE.
#: For more information, please refer to Section 8.11 of IETF RFC 3588.
STATE_MAINTAINED = convert_to_4_bytes(0)
NO_STATE_MAINTAINED = convert_to_4_bytes(1)

#: List of RAT-TYPES.
#: For more information, please refer to Section 5.3.31 of 3GPP TS 29.212.
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

#: List of VPLMN-Dynamic-Address-Allowed.
#: For more information, please refer to Section 7.3.38 of 
#: ETSI TS 129.272 V12.6.0 (2014-10).
VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED = convert_to_4_bytes(0)
VPLMN_DYNAMIC_ADDRESS_ALLOWED_ALLOWED = convert_to_4_bytes(1)

#: List of Host-IP-Address types.
#: 
HOST_IP_ADDRESS_FAMILY_CODE_IPV4 = convert_to_2_bytes(1)
HOST_IP_ADDRESS_FAMILY_CODE_IPV6 = convert_to_2_bytes(2)

#: List of Vendor-Id values.
#: 
VENDOR_ID_DEFAULT = convert_to_4_bytes(0)
VENDOR_ID_TEKELEC = convert_to_4_bytes(323)
VENDOR_ID_3GPP = convert_to_4_bytes(10415)
VENDOR_ID_ETSI = convert_to_4_bytes(13019)

#: List of Subscription-Id-Type values.
#: For more information, please refer to Section 8.47 of IETF RFC 4006.
END_USER_E164 = convert_to_4_bytes(0)
END_USER_IMSI = convert_to_4_bytes(1)
END_USER_SIP_URI = convert_to_4_bytes(2)
END_USER_NAI = convert_to_4_bytes(3)
END_USER_PRIVATE = convert_to_4_bytes(4)

#: List of PDN-Type values.
#: For more information, please refer to Section 7.3.62 of
#  ETSI TS 129.272 V15.10.0 (2020-01).
PDN_TYPE_IPV4 = convert_to_4_bytes(0)
PDN_TYPE_IPV6 = convert_to_4_bytes(1)
PDN_TYPE_IPV4V6 = convert_to_4_bytes(2)
PDN_TYPE_IPV4_OR_IPV6 = convert_to_4_bytes(3)

#: List of PDN-GW-Allocation-Type values.
#: For more information, please refer to Section 7.3.44 of
#  ETSI TS 129.272 V15.10.0 (2020-01).
PDN_GW_ALLOCATION_TYPE_STATIC = convert_to_4_bytes(0)
PDN_GW_ALLOCATION_TYPE_DYNAMIC = convert_to_4_bytes(1)

#: List of Non-3GPP-IP-Access values.
#: For more information, please refer to Section 8.2.3.3 of
#  ETSI TS 129 273 V14.5.0 (2019-10).
NON_3GPP_SUBSCRIPTION_ALLOWED = convert_to_4_bytes(0)
NON_3GPP_SUBSCRIPTION_BARRED = convert_to_4_bytes(1)

#: List of Inband-Security-Id AVP values.
INBAND_SECURITY_ID_NO_SECURITY = convert_to_4_bytes(0)
INBAND_SECURITY_ID_TLS = convert_to_4_bytes(1)

#: List of Redirect-Host-Usage AVP values.
REDIRECT_HOST_USAGE_DONT_CACHE = convert_to_4_bytes(0)
REDIRECT_HOST_USAGE_ALL_SESSION = convert_to_4_bytes(1)
REDIRECT_HOST_USAGE_ALL_REALM = convert_to_4_bytes(2)
REDIRECT_HOST_USAGE_REALM_AND_APPLICATION = convert_to_4_bytes(3)
REDIRECT_HOST_USAGE_ALL_APPLICATION = convert_to_4_bytes(4)
REDIRECT_HOST_USAGE_ALL_HOST = convert_to_4_bytes(5)
REDIRECT_HOST_USAGE_ALL_USER = convert_to_4_bytes(6)

#: List of Session-Server-Failover AVP values.
SESSION_SERVER_FAILOVER_REFUSE_SERVICE = convert_to_4_bytes(0)
SESSION_SERVER_FAILOVER_TRY_AGAIN = convert_to_4_bytes(1)
SESSION_SERVER_FAILOVER_ALLOW_SERVICE = convert_to_4_bytes(2)
SESSION_SERVER_FAILOVER_TRY_AGAIN_ALLOW_SERVICE = convert_to_4_bytes(3)

#: List of Accounting-Record-Type AVP values.
ACCOUNTING_RECORD_TYPE_EVENT_RECORD = convert_to_4_bytes(1)
ACCOUNTING_RECORD_TYPE_START_RECORD = convert_to_4_bytes(2)
ACCOUNTING_RECORD_TYPE_INTERIM_RECORD = convert_to_4_bytes(3)
ACCOUNTING_RECORD_TYPE_STOP_RECORD = convert_to_4_bytes(4)

#: List of Accounting-Realtime-Required AVP values.
ACCOUNTING_REALTIME_REQUIRED_DELIVER_AND_GRANT = convert_to_4_bytes(1)
ACCOUNTING_REALTIME_REQUIRED_GRANT_AND_STORE = convert_to_4_bytes(2)
ACCOUNTING_REALTIME_REQUIRED_GRAND_AND_LOSE = convert_to_4_bytes(3)

#: List of UE-SRVCC-Capability AVP values.
#: For more information, please refer to Section 7.3.130 of 
#: ETSI TS 129 272 V15.10.0 (2020-01).
UE_SRVCC_NOT_SUPPORTED = convert_to_4_bytes(0)
UE_SRVCC_SUPPORTED = convert_to_4_bytes(1)

#: List of Feature-List-ID AVP values.
#: For more information, please refer to Section 6.3.30 of 
#: ETSI TS 129 229 V14.3.0 (2019-10).
FEATURE_LIST_ID_1 = convert_to_4_bytes(1)
FEATURE_LIST_ID_2 = convert_to_4_bytes(2)

#: List of Non-3GPP-IP-Access AVP values.
#: For more information, please refer to Section 8.2.3.3 of 
#: ETSI TS 129 273 V14.3.0 (2017-07).
NON_3GPP_SUBSCRIPTION_ALLOWED = convert_to_4_bytes(0)
NON_3GPP_SUBSCRIPTION_BARRED = convert_to_4_bytes(1)

#: List of Non-3GPP-IP-Access-APN AVP values.
#: For more information, please refer to Section 8.2.3.4 of 
#: ETSI TS 129 273 V14.3.0 (2017-07).
NON_3GPP_APNS_ENABLE = convert_to_4_bytes(0)
NON_3GPP_APNS_DISABLE = convert_to_4_bytes(1)

#: List of Server-Assignment-Type AVP values.
#: For more information, please refer to Section 8.2.3.4 of 
#: ETSI TS 129 273 V14.3.0 (2017-07).
SERVER_ASSIGNMENT_TYPE_NO_ASSIGNMENT = convert_to_4_bytes(0)
SERVER_ASSIGNMENT_TYPE_REGISTRATION = convert_to_4_bytes(1)
SERVER_ASSIGNMENT_TYPE_RE_REGISTRATION = convert_to_4_bytes(2)
SERVER_ASSIGNMENT_TYPE_UNREGISTERED_USER = convert_to_4_bytes(3)
SERVER_ASSIGNMENT_TYPE_TIMEOUT_DEREGISTRATION = convert_to_4_bytes(4)
SERVER_ASSIGNMENT_TYPE_USER_DEREGISTRATION = convert_to_4_bytes(5)
SERVER_ASSIGNMENT_TYPE_DEREGISTRATION_STORE_SERVER_NAME = convert_to_4_bytes(6)
SERVER_ASSIGNMENT_TYPE_USER_DEREGISTRATION_STORE_SERVER_NAME = convert_to_4_bytes(7)
SERVER_ASSIGNMENT_TYPE_ADMINISTRATIVE_DEREGISTRATION = convert_to_4_bytes(8)
SERVER_ASSIGNMENT_TYPE_AUTHENTICATION_FAILURE = convert_to_4_bytes(9)
SERVER_ASSIGNMENT_TYPE_AUTHENTICATION_TIMEOUT = convert_to_4_bytes(10)
SERVER_ASSIGNMENT_TYPE_DEREGISTRATION_TOO_MUCH_DATA = convert_to_4_bytes(11)
SERVER_ASSIGNMENT_TYPE_AAA_USER_DATA_REQUEST = convert_to_4_bytes(12)
SERVER_ASSIGNMENT_TYPE_PGW_UPDATE = convert_to_4_bytes(13)
SERVER_ASSIGNMENT_TYPE_RESTORATION = convert_to_4_bytes(14)

#: List of Cancellation-Type AVP values.
#: For more information, please refer to Section 7.3.24 of 
#: ETSI TS 129 272 V15.4.0 (2018-07).
CANCELLATION_TYPE_MME_UPDATE_PROCEDURE = convert_to_4_bytes(0)
CANCELLATION_TYPE_SGSN_UPDATE_PROCEDURE = convert_to_4_bytes(1)
CANCELLATION_TYPE_SUBSCRIPTION_WITHDRAWAL = convert_to_4_bytes(2)
CANCELLATION_TYPE_UPDATE_PROCEDURE_IWF = convert_to_4_bytes(3)
CANCELLATION_TYPE_INITIAL_ATTACH_PROCEDURE = convert_to_4_bytes(4)

#: List of Reason-Code AVP values.
#: For more information, please refer to Section 6.3.17 of 
#: ETSI TS 129 229 V11.3.0 (2013-04).
REASON_CODE_PERMANENT_TERMINATION = convert_to_4_bytes(0)
REASON_CODE_NEW_SERVER_ASSIGNED = convert_to_4_bytes(1)
REASON_CODE_SERVER_CHANGE = convert_to_4_bytes(2)
REASON_CODE_REMOVE_CHANGE = convert_to_4_bytes(3)

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

#: List of Equipment-Status AVP values.
#: For more information, please refer to Section 7.3.51 of 
#: ETSI TS 129 272 V15.4.0 (2018-07).
EQUIPMENT_STATUS_WHITELISTED = convert_to_4_bytes(0)
EQUIPMENT_STATUS_BLACKLISTED = convert_to_4_bytes(1)
EQUIPMENT_STATUS_GREYLISTED = convert_to_4_bytes(2)

#: List of Reservation-Priority AVP values.
#: For more information, please refer to Section 7.3.9 of 
#: ETSI TS 183 017 V2.3.1 (2008-09).
PRIORITY_DEFAULT = convert_to_4_bytes(0)
PRIORITY_ONE = convert_to_4_bytes(1)
PRIORITY_TWO = convert_to_4_bytes(2)
PRIORITY_THREE = convert_to_4_bytes(3)
PRIORITY_FOUR = convert_to_4_bytes(4)
PRIORITY_FIVE = convert_to_4_bytes(5)
PRIORITY_SIX = convert_to_4_bytes(6)
PRIORITY_SEVEN = convert_to_4_bytes(7)

#: List of AN-Trusted AVP values.
#: For more information, please refer to Section 5.2.3.9 of 
#: ETSI TS 129 273 V12.5.0 (2014-10).
AN_TRUSTED_TRUSTED = convert_to_4_bytes(0)
AN_TRUSTED_UNTRUSTED = convert_to_4_bytes(1)

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

#: List of Service-Info-Status AVP values.
#: For more information, please refer to Section 5.3.25 of 
#: ETSI TS 129 214 V15.4.0 (2018-07).
SERVICE_INFO_STATUS_FINAL_SERVICE_INFORMATION = convert_to_4_bytes(0)
SERVICE_INFO_STATUS_PRELIMINARY_SERVICE_INFORMATION = convert_to_4_bytes(1)

#: List of Reporting-Level AVP values.
#: For more information, please refer to Section 5.3.12 of 
#: ETSI TS 129 212 V15.3.0 (2018-07).
REPORTING_LEVEL_SERVICE_IDENTIFIER_LEVEL = convert_to_4_bytes(0)
REPORTING_LEVEL_RATING_GROUP_LEVEL = convert_to_4_bytes(1)
REPORTING_LEVEL_SPONSORED_CONNECTIVITY_LEVEL = convert_to_4_bytes(2)

#: List of Charging-Correlation-Indicator AVP values.
#: For more information, please refer to Section 5.3.67 of 
#: ETSI TS 129 212 V15.3.0 (2018-07).
CHARGING_CORRELATION_INDICATOR_CHARGING_IDENTIFIER_REQUIRED = convert_to_4_bytes(0)

#: List of Abort-Cause AVP values.
#: For more information, please refer to Section 5.3.1 of 
#: ETSI TS 129 214 V15.4.0 (2018-07).
ABORT_CAUSE_BEARER_RELEASED = convert_to_4_bytes(0)
ABORT_CAUSE_INSUFFICIENT_SERVER_RESOURCES = convert_to_4_bytes(1)
ABORT_CAUSE_INSUFFICIENT_BEARER_RESOURCES = convert_to_4_bytes(2)
ABORT_CAUSE_PS_TO_CS_HANDOVER = convert_to_4_bytes(3)
ABORT_CAUSE_SPONSORED_DATA_CONNECTIVITY_DISALLOWED = convert_to_4_bytes(4)

#: *************************************************************************************************

#: List of DIAMETER Family Codes.

DIAMETER_ERROR_1XXX = bytes.fromhex("000003e8")                 #: 1xxx
DIAMETER_ERROR_2XXX = bytes.fromhex("000007d0")                 #: 2xxx
DIAMETER_ERROR_3XXX = bytes.fromhex("00000bb8")                 #: 3xxx
DIAMETER_ERROR_4XXX = bytes.fromhex("00000fa0")                 #: 4xxx
DIAMETER_ERROR_5XXX = bytes.fromhex("00001388")                 #: 5xxx

#: *************************************************************************************************

#: List of DIAMETER RESULT-CODES.

#: Informational Result-Codes.
DIAMETER_MULTI_ROUND_AUTH = bytes.fromhex("000003e9")           #: 1001 - Subsequent messages triggered by client shall also used in Authentication and to get access of required resources. Generally used in Diameter NAS.

#: Success Result-Codes.
DIAMETER_SUCCESS = bytes.fromhex("000007d1")                    #: 2001 - Request processed successfully.
DIAMETER_LIMITED_SUCCESS = bytes.fromhex("000007d2")            #: 2002 - Request is processed but some more processing is required by Server to provide access to user.

#: Protocol Errors [E-bit set].
DIAMETER_COMMAND_UNSUPPORTED = bytes.fromhex("00000bb9")        #: 3001 - Server returns it if Diameter Command-Code is un-recognized by server.
DIAMETER_UNABLE_TO_DELIVER = bytes.fromhex("00000bba")          #: 3002 - Message can’t be delivered because there is no Host with Diameter URI present in Destination-Host AVP in associated Realm.
DIAMETER_REALM_NOT_SERVED = bytes.fromhex("00000bbb")           #: 3003 - Intended Realm is not recognized.
DIAMETER_TOO_BUSY = bytes.fromhex("00000bbc")                   #: 3004 - Shall return by server only when server unable to provide requested service, where all the pre-requisites are also met. Client should also send the request to alternate peer.
DIAMETER_LOOP_DETECTED = bytes.fromhex("00000bbd")              #: 3005
DIAMETER_REDIRECT_INDICATION = bytes.fromhex("00000bbe")        #: 3006 - In Response from Redirect Agent.
DIAMETER_APPLICATION_UNSUPPORTED = bytes.fromhex("00000bbf")    #: 3007
DIAMETER_INVALID_HDR_BITS = bytes.fromhex("00000bc0")           #: 3008 - It is sent when a request is received with invalid bits combination for considered command-code in DIAMETER Header structure. E.g. Marking Proxy-Bit in CER message.
DIAMETER_INVALID_AVP_BITS = bytes.fromhex("00000bc1")           #: 3009 - It is sent when a request is received with invalid flag bits in an AVP.
DIAMETER_UNKNOWN_PEER = bytes.fromhex("00000bc2")               #: 3010 - A DIAMETER server can be configured whether it shall accept DIAMETER connection from all nodes or only from specific nodes. If it is configured to accept connection from specific nodes and receives CER from message from any node other than specified. Here Server shall send considered error.

#: Transient Failures [Could not satisfy request at this moment].
DIAMETER_AUTHENTICATION_REJECTED = bytes.fromhex("00000fa1")    #: 4001 - Returned by Server, most likely because of invalid password.
DIAMETER_OUT_OF_SPACE = bytes.fromhex("00000fa2")               #: 4002 - Returned by node, when it receives accounting information but unable to store it because of lack of memory.
DIAMETER_ELECTION_LOST = bytes.fromhex("00000fa3")              #: 4003 - Peer determines that it has lost election by comparing Origin-Host value received in CER with its own DIAMETER IDENTITY and found that received DIAMETER IDENTITY is higher.

#: Permanent Failures [To inform peer, request is failed, shouldn’t be attempted again].
DIAMETER_AVP_UNSUPPORTED = bytes.fromhex("00001389")            #: 5001 - AVP marked with Mandatory Bit, but peer does not support it.
DIAMETER_UNKNOWN_SESSION_ID = bytes.fromhex("0000138a")         #: 5002
DIAMETER_AUTHORIZATION_REJECTED = bytes.fromhex("0000138b")     #: 5003 - User can not be authorized. E.g. Comes in AIA on s6a interface.
DIAMETER_INVALID_AVP_VALUE = bytes.fromhex("0000138c")          #: 5004
DIAMETER_MISSING_AVP = bytes.fromhex("0000138d")                #: 5005 - Mandatory AVP in request message is missing.
DIAMETER_RESOURCES_EXCEEDED = bytes.fromhex("0000138e")         #: 5006 - A request was received that cannot be authorized because the user has already expended allowed resources. An example of this error condition is a user that is restricted to one dial-up PPP port, attempts to establish a second PPP connection.
DIAMETER_CONTRADICTING_AVPS = bytes.fromhex("0000138f")         #: 5007 - Server has identified that AVPs are present that are contradictory to each other.
DIAMETER_AVP_NOT_ALLOWED = bytes.fromhex("00001390")            #: 5008 - Message is received by node (Server) that contain AVP must not be present.
DIAMETER_AVP_OCCURS_TOO_MANY_TIMES = bytes.fromhex("00001391")  #: 5009 - If message contains the a AVP number of times that exceeds permitted occurrence of AVP in message definition.
DIAMETER_NO_COMMON_APPLICATION = bytes.fromhex("00001392")      #: 5010 - In response of CER if no common application supported between the peers.
DIAMETER_UNSUPPORTED_VERSION = bytes.fromhex("00001393")        #: 5011 - Self explanatory.
DIAMETER_UNABLE_TO_COMPLY = bytes.fromhex("00001394")           #: 5012 - Message rejected because of unspecified reasons.
DIAMETER_INVALID_BIT_IN_HEADER = bytes.fromhex("00001395")      #: 5013 - When an unrecognized bit in the Diameter header is set to one.
DIAMETER_INVALID_AVP_LENGTH = bytes.fromhex("00001396")         #: 5014 - Self explanatory. 
DIAMETER_INVALID_MESSAGE_LENGTH = bytes.fromhex("00001397")     #: 5015 - Self explanatory.
DIAMETER_INVALID_AVP_BIT_COMBO = bytes.fromhex("00001398")      #: 5016 - E.g. Marking AVP to Mandatory while message definition doesn’t say so.
DIAMETER_NO_COMMON_SECURITY = bytes.fromhex("00001399")         #: 5017 - In response of CER if no common security mechanism supported between the peers.

#: *************************************************************************************************

#: List of DIAMETER EXPERIMENTAL-RESULT-CODES.

DIAMETER_FIRST_REGISTRATION = bytes.fromhex("000007d1")                     #: 2001
DIAMETER_SUBSEQUENT_REGISTRATION = bytes.fromhex("000007d2")                #: 2002
DIAMETER_UNREGISTERED_SERVICE = bytes.fromhex("000007d3")                   #: 2003
DIAMETER_SUCCESS_SERVER_NAME_NOT_STORED = bytes.fromhex("000007d1")         #: 2004

DIAMETER_USER_DATA_NOT_AVAILABLE = bytes.fromhex("00001004")                #: 4100
DIAMETER_PRIOR_UPDATE_IN_PROGRESS = bytes.fromhex("00001005")               #: 4101
DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE = bytes.fromhex("00001055")        #: 4181

DIAMETER_ERROR_USER_UNKNOWN = bytes.fromhex("00001389")                     #: 5001
DIAMETER_ERROR_IDENTITIES_DONT_MATCH = bytes.fromhex("0000138a")            #: 5002
DIAMETER_ERROR_IDENTITY_NOT_REGISTERED = bytes.fromhex("0000138b")          #: 5003
DIAMETER_ERROR_ROAMING_NOT_ALLOWED = bytes.fromhex("0000138c")              #: 5004
DIAMETER_ERROR_IDENTITY_ALREADY_REGISTERED = bytes.fromhex("0000138d")      #: 5005
DIAMETER_ERROR_AUTH_SCHEME_NOT_SUPPORTED = bytes.fromhex("0000138e")        #: 5006
DIAMETER_ERROR_IN_ASSIGNMENT_TYPE = bytes.fromhex("0000138f")               #: 5007
DIAMETER_ERROR_TOO_MUCH_DATA = bytes.fromhex("00001390")                    #: 5008
DIAMETER_ERROR_NOT_SUPPORTED_USER_DATA = bytes.fromhex("00001391")          #: 5009
DIAMETER_ERROR_FEATURE_UNSUPPORTED = bytes.fromhex("00001393")              #: 5011
DIAMETER_ERROR_SERVING_NODE_FEATURE_UNSUPPORTED = bytes.fromhex("00001394") #: 5012
DIAMETER_ERROR_USER_DATA_NOT_RECOGNIZED = bytes.fromhex("000013ec")         #: 5100
DIAMETER_ERROR_OPERATION_NOT_ALLOWED = bytes.fromhex("000013ed")            #: 5101
DIAMETER_ERROR_USER_DATA_CANNOT_BE_READ = bytes.fromhex("000013ee")         #: 5102
DIAMETER_ERROR_USER_DATA_CANNOT_BE_MODIFIED = bytes.fromhex("000013ef")     #: 5103
DIAMETER_ERROR_USER_DATA_CANNOT_BE_NOTIFIED = bytes.fromhex("000013f0")     #: 5104
DIAMETER_ERROR_TRANSPARENT_DATA_OUT_OF_SYNC = bytes.fromhex("000013f1")     #: 5105
DIAMETER_ERROR_SUBS_DATA_ABSENT = bytes.fromhex("000013f2")                 #: 5106
DIAMETER_ERROR_NO_SUBSCRIPTION_TO_DATA = bytes.fromhex("000013f3")          #: 5107
DIAMETER_ERROR_DSAI_NOT_AVAILABLE = bytes.fromhex("000013f4")               #: 5108
DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION = bytes.fromhex("0000152c")         #: 5420
DIAMETER_ERROR_RAT_NOT_ALLOWED = bytes.fromhex("0000152d")                  #: 5421
DIAMETER_ERROR_EQUIPMENT_UNKNOWN = bytes.fromhex("0000152e")                #: 5422
DIAMETER_ERROR_UNKOWN_SERVING_NODE = bytes.fromhex("0000152f")              #: 5423
DIAMETER_ERROR_USER_NO_NON_3GPP_SUBSCRIPTION = bytes.fromhex("0000154a")    #: 5450
DIAMETER_ERROR_USER_NO_APN_SUBSCRIPTION = bytes.fromhex("0000154b")         #: 5451
DIAMETER_ERROR_RAT_TYPE_NOT_ALLOWED = bytes.fromhex("0000154c")             #: 5452

#: *************************************************************************************************

#: EAP Codes.
EAP_CODE_REQUEST = convert_to_1_byte(1)
EAP_CODE_RESPONSE = convert_to_1_byte(2)
EAP_CODE_SUCCESS = convert_to_1_byte(3)
EAP_CODE_FAILURE = convert_to_1_byte(4)

#: EAP Types.
EAP_TYPE_IDENTITY = convert_to_1_byte(1)
EAP_TYPE_UMTS_AUTHENTICATION_AND_KEY_AGREEMENT_EAP = convert_to_1_byte(23)

#: EAP-AKA Subtypes.
AKA_CHALLENGE = convert_to_1_byte(1)
NOTIFICATION = convert_to_1_byte(12)
