# -*- coding: utf-8 -*-
"""
    bromelia.constants.ietf.rfc4006
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    
    This module contains constants defined in IETF RFC 4006.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_4_bytes


#: Diameter AVPs
CC_INPUT_OCTETS_AVP_CODE = convert_to_4_bytes(412)
CC_OUTPUT_OCTETS_AVP_CODE = convert_to_4_bytes(414)
CC_SESSION_FAILOVER_AVP_CODE = convert_to_4_bytes(418)
CC_TIME_AVP_CODE = convert_to_4_bytes(420)
CC_TOTAL_OCTETS_AVP_CODE = convert_to_4_bytes(421)
COST_INFORMATION_AVP_CODE = convert_to_4_bytes(423)
COST_UNIT_AVP_CODE = convert_to_4_bytes(424)
CURRENCY_CODE_AVP_CODE = convert_to_4_bytes(425)
CREDIT_CONTROL_FAILURE_HANDLING_AVP_CODE = convert_to_4_bytes(427)
DIRECT_DEBITING_FAILURE_HANDLING_AVP_CODE = convert_to_4_bytes(428)
EXPONENT_AVP_CODE = convert_to_4_bytes(429)
GRANTED_SERVICE_UNIT_AVP_CODE = convert_to_4_bytes(431)
REQUESTED_SERVICE_UNIT_AVP_CODE = convert_to_4_bytes(437)
SUBSCRIPTION_ID_AVP_CODE = convert_to_4_bytes(443)
SUBSCRIPTION_ID_DATA_AVP_CODE = convert_to_4_bytes(444)
UNIT_VALUE_AVP_CODE = convert_to_4_bytes(445)
VALUE_DIGITS_AVP_CODE = convert_to_4_bytes(447)
VALIDITY_TIME_AVP_CODE = convert_to_4_bytes(448)
SUBSCRIPTION_ID_TYPE_AVP_CODE = convert_to_4_bytes(450)
TARIFF_CHANGE_USAGE_AVP_CODE = convert_to_4_bytes(451)
MULTIPLE_SERVICES_CREDIT_CONTROL_AVP_CODE = convert_to_4_bytes(456)


#: List of Subscription-Id-Type values.
#: For more information, please refer to Section 8.47 of IETF RFC 4006.
END_USER_E164 = convert_to_4_bytes(0)
END_USER_IMSI = convert_to_4_bytes(1)
END_USER_SIP_URI = convert_to_4_bytes(2)
END_USER_NAI = convert_to_4_bytes(3)
END_USER_PRIVATE = convert_to_4_bytes(4)

#: List of CC-Session-Failover AVP values.
#: For more information, please refer to Section 8.4 of IETF RFC 4006.
CC_SESSION_FAILOVER_NOT_SUPPORTED = convert_to_4_bytes(0)
CC_SESSION_FAILOVER_SUPPORTED = convert_to_4_bytes(1)

#: List of Credit-Control-Failure-Handling AVP values.
#: For more information, please refer to Section 8.14 of IETF RFC 4006.
CREDIT_CONTROL_FAILURE_HANDLING_TERMINATE = convert_to_4_bytes(0)
CREDIT_CONTROL_FAILURE_HANDLING_CONTINUE = convert_to_4_bytes(1)
CREDIT_CONTROL_FAILURE_HANDLING_RETRY_AND_TERMINATE = convert_to_4_bytes(2)

#: List of Direct-Debiting-Failure-Handling AVP values.
#: For more information, please refer to Section 8.15 of IETF RFC 4006.
DIRECT_DEBITING_FAILURE_HANDLING_TERMINATE_OR_BUFFER = convert_to_4_bytes(0)
DIRECT_DEBITING_FAILURE_HANDLING_CONTINUE = convert_to_4_bytes(1)