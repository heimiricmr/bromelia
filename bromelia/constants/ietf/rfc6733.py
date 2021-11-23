# -*- coding: utf-8 -*-
"""
    bromelia.constants.ietf.rfc6733
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains constants defined in IETF RFC 6733.
 
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_2_bytes
from ..._internal_utils import convert_to_3_bytes
from ..._internal_utils import convert_to_4_bytes


#: Diameter Messages
CAPABILITIES_EXCHANGE_MESSAGE = convert_to_3_bytes(257)
ABORT_SESSION_MESSAGE = convert_to_3_bytes(274)
DEVICE_WATCHDOG_MESSAGE = convert_to_3_bytes(280)
DISCONNECT_PEER_MESSAGE = convert_to_3_bytes(282)

#: Diameter AVPs
USER_NAME_AVP_CODE = convert_to_4_bytes(1)
CLASS_AVP_CODE = convert_to_4_bytes(25)
SESSION_TIMEOUT_AVP_CODE = convert_to_4_bytes(27)
PROXY_STATE_AVP_CODE = convert_to_4_bytes(33)
ACCT_SESSION_ID_AVP_CODE = convert_to_4_bytes(44)
ACCT_MULTI_SESSION_ID_AVP_CODE = convert_to_4_bytes(50)
EVENT_TIMESTAMP_AVP_CODE = convert_to_4_bytes(55)
ACCT_INTERIM_INTERVAL_AVP_CODE = convert_to_4_bytes(85)
HOST_IP_ADDRESS_AVP_CODE = convert_to_4_bytes(257)
AUTH_APPLICATION_ID_AVP_CODE = convert_to_4_bytes(258)
ACCT_APPLICATION_ID_AVP_CODE = convert_to_4_bytes(259)
VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE = convert_to_4_bytes(260)
REDIRECT_HOST_USAGE_AVP_CODE = convert_to_4_bytes(261)
REDIRECT_MAX_CACHE_TIME_AVP_CODE = convert_to_4_bytes(262)
SESSION_ID_AVP_CODE = convert_to_4_bytes(263)
ORIGIN_HOST_AVP_CODE = convert_to_4_bytes(264)
SUPPORTED_VENDOR_ID_AVP_CODE = convert_to_4_bytes(265)
VENDOR_ID_AVP_CODE = convert_to_4_bytes(266)
FIRMWARE_REVISION_AVP_CODE = convert_to_4_bytes(267)
RESULT_CODE_AVP_CODE = convert_to_4_bytes(268)
PRODUCT_NAME_AVP_CODE = convert_to_4_bytes(269)
SESSION_BINDING_AVP_CODE = convert_to_4_bytes(270)
SESSION_SERVER_FAILOVER_AVP_CODE = convert_to_4_bytes(271)
MULTI_ROUND_TIME_OUT_AVP_CODE = convert_to_4_bytes(272)
DISCONNECT_CAUSE_AVP_CODE = convert_to_4_bytes(273)
AUTH_REQUEST_TYPE_AVP_CODE = convert_to_4_bytes(274)
AUTH_GRACE_PERIOD_AVP_CODE = convert_to_4_bytes(276)
AUTH_SESSION_STATE_AVP_CODE = convert_to_4_bytes(277)
ORIGIN_STATE_ID_AVP_CODE = convert_to_4_bytes(278)
FAILED_AVP_AVP_CODE = convert_to_4_bytes(279)
PROXY_HOST_AVP_CODE = convert_to_4_bytes(280)
ERROR_MESSAGE_AVP_CODE = convert_to_4_bytes(281)
ROUTE_RECORD_AVP_CODE = convert_to_4_bytes(282)
DESTINATION_REALM_AVP_CODE = convert_to_4_bytes(283)
PROXY_INFO_AVP_CODE = convert_to_4_bytes(284)
RE_AUTH_REQUEST_TYPE_AVP_CODE = convert_to_4_bytes(285)
ACCOUNTING_SUB_SESSION_ID_AVP_CODE = convert_to_4_bytes(287)
AUTHORIZATION_LIFETIME_AVP_CODE = convert_to_4_bytes(291)
REDIRECT_HOST_AVP_CODE = convert_to_4_bytes(292)
DESTINATION_HOST_AVP_CODE = convert_to_4_bytes(293)
ERROR_REPORTING_HOST_AVP_CODE = convert_to_4_bytes(294)
TERMINATION_CAUSE_AVP_CODE = convert_to_4_bytes(295)
ORIGIN_REALM_AVP_CODE = convert_to_4_bytes(296)
EXPERIMENTAL_RESULT_AVP_CODE = convert_to_4_bytes(297)
EXPERIMENTAL_RESULT_CODE_AVP_CODE = convert_to_4_bytes(298)
INBAND_SECURITY_ID_AVP_CODE = convert_to_4_bytes(299)
ACCOUNTING_RECORD_TYPE_AVP_CODE = convert_to_4_bytes(480)
ACCOUNTING_REALTIME_REQUIRED_AVP_CODE = convert_to_4_bytes(483)
ACCOUNTING_RECORD_NUMBER_AVP_CODE = convert_to_4_bytes(485)

#: List of Host-IP-Address types.
#: For more information, please refer to Section 5.3.5 of IETF RFC 6733.
HOST_IP_ADDRESS_FAMILY_CODE_IPV4 = convert_to_2_bytes(1)
HOST_IP_ADDRESS_FAMILY_CODE_IPV6 = convert_to_2_bytes(2)

#: List of Vendor-Id values.
#: For more information, please refer to Section 5.3.3 of IETF RFC 6733.
VENDOR_ID_DEFAULT = convert_to_4_bytes(0)
VENDOR_ID_TEKELEC = convert_to_4_bytes(323)
VENDOR_ID_3GPP = convert_to_4_bytes(10415)
VENDOR_ID_ETSI = convert_to_4_bytes(13019)

#: List of Disconnect-Cause AVP values.
#: For more information, please refer to Section 5.4.3 of IETF RFC 6733.
DISCONNECT_CAUSE_REBOOTING = convert_to_4_bytes(0)
DISCONNECT_CAUSE_BUSY = convert_to_4_bytes(1)
DISCONNECT_CAUSE_DO_NOT_WANT_TO_TALK_TO_YOU = convert_to_4_bytes(2)

#: List of Inband-Security-Id AVP values.
#: For more information, please refer to Section 6.10 of IETF RFC 6733.
INBAND_SECURITY_ID_NO_SECURITY = convert_to_4_bytes(0)
INBAND_SECURITY_ID_TLS = convert_to_4_bytes(1)

#: List of Redirect-Host-Usage AVP values.
#: For more information, please refer to Section 6.13 of IETF RFC 6733.
REDIRECT_HOST_USAGE_DONT_CACHE = convert_to_4_bytes(0)
REDIRECT_HOST_USAGE_ALL_SESSION = convert_to_4_bytes(1)
REDIRECT_HOST_USAGE_ALL_REALM = convert_to_4_bytes(2)
REDIRECT_HOST_USAGE_REALM_AND_APPLICATION = convert_to_4_bytes(3)
REDIRECT_HOST_USAGE_ALL_APPLICATION = convert_to_4_bytes(4)
REDIRECT_HOST_USAGE_ALL_HOST = convert_to_4_bytes(5)
REDIRECT_HOST_USAGE_ALL_USER = convert_to_4_bytes(6)

#: List of Auth-Request-Type AVP values.
#: For more information, please refer to Section 8.7 of IETF RFC 6733.
AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY = convert_to_4_bytes(1)
AUTH_REQUEST_TYPE_AUTHORIZE_ONLY = convert_to_4_bytes(2)
AUTH_REQUEST_TYPE_AUTHORIZE_AUTHENTICATE = convert_to_4_bytes(3)

#: List of Auth-Session-State AVP values.
#: For more information, please refer to Section 8.11 of IETF RFC 6733.
STATE_MAINTAINED = convert_to_4_bytes(0)
NO_STATE_MAINTAINED = convert_to_4_bytes(1)

#: List of Re-Auth-Request-Type AVP values.
#: For more information, please refer to Section 8.12 of IETF RFC 6733.
RE_AUTH_REQUEST_TYPE_AUTHORIZE_ONLY = convert_to_4_bytes(0)
RE_AUTH_REQUEST_TYPE_AUTHORIZE_AUTHENTICATE = convert_to_4_bytes(1)

#: List of Session-Server-Failover AVP values.
#: For more information, please refer to Section 8.18 of IETF RFC 6733.
SESSION_SERVER_FAILOVER_REFUSE_SERVICE = convert_to_4_bytes(0)
SESSION_SERVER_FAILOVER_TRY_AGAIN = convert_to_4_bytes(1)
SESSION_SERVER_FAILOVER_ALLOW_SERVICE = convert_to_4_bytes(2)
SESSION_SERVER_FAILOVER_TRY_AGAIN_ALLOW_SERVICE = convert_to_4_bytes(3)

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

#: List of Accounting-Record-Type AVP values.
#: For more information, please refer to Section 9.8.1 of IETF RFC 6733.
ACCOUNTING_RECORD_TYPE_EVENT_RECORD = convert_to_4_bytes(1)
ACCOUNTING_RECORD_TYPE_START_RECORD = convert_to_4_bytes(2)
ACCOUNTING_RECORD_TYPE_INTERIM_RECORD = convert_to_4_bytes(3)
ACCOUNTING_RECORD_TYPE_STOP_RECORD = convert_to_4_bytes(4)

#: List of Accounting-Realtime-Required AVP values.
#: For more information, please refer to Section 9.8.7 of IETF RFC 6733.
ACCOUNTING_REALTIME_REQUIRED_DELIVER_AND_GRANT = convert_to_4_bytes(1)
ACCOUNTING_REALTIME_REQUIRED_GRANT_AND_STORE = convert_to_4_bytes(2)
ACCOUNTING_REALTIME_REQUIRED_GRAND_AND_LOSE = convert_to_4_bytes(3)
