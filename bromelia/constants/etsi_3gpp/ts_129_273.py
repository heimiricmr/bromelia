# -*- coding: utf-8 -*-
"""
    bromelia.constants.etsi_3gpp.ts_129_273
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains constants defined in ETSI TS 129 273.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_3_bytes
from ..._internal_utils import convert_to_4_bytes


#: Diameter Messages
RE_AUTH_MESSAGE = convert_to_3_bytes(258)
AA_MESSAGE = convert_to_3_bytes(265)
DIAMETER_EAP_MESSAGE = convert_to_3_bytes(268)
SESSION_TERMINATION_MESSAGE = convert_to_3_bytes(275)
SERVER_ASSIGNMENT_MESSAGE = convert_to_3_bytes(301)
MULTIMEDIA_AUTH_MESSAGE = convert_to_3_bytes(303)
REGISTRATION_TERMINATION_MESSAGE = convert_to_3_bytes(304)
PUSH_PROFILE_MESSAGE = convert_to_3_bytes(305)

#: Diameter AVPs
MIP6_FEATURE_VECTOR_AVP_CODE = convert_to_4_bytes(124)
MOBILE_NODE_IDENTIFIER_AVP_CODE = convert_to_4_bytes(506)
NON_3GPP_USER_DATA_AVP_CODE = convert_to_4_bytes(1500)
NON_3GPP_IP_ACCESS_AVP_CODE = convert_to_4_bytes(1501)
NON_3GPP_IP_ACCESS_APN_AVP_CODE = convert_to_4_bytes(1502)
AN_TRUSTED_AVP_CODE = convert_to_4_bytes(1503)

#: List of AN-Trusted AVP values.
#: For more information, please refer to Section 5.2.3.9 of 
#: ETSI TS 129 273 V12.5.0 (2014-10).
AN_TRUSTED_TRUSTED = convert_to_4_bytes(0)
AN_TRUSTED_UNTRUSTED = convert_to_4_bytes(1)

#: List of Non-3GPP-IP-Access values.
#: For more information, please refer to Section 8.2.3.3 of
#  ETSI TS 129 273 V14.5.0 (2019-10).
NON_3GPP_SUBSCRIPTION_ALLOWED = convert_to_4_bytes(0)
NON_3GPP_SUBSCRIPTION_BARRED = convert_to_4_bytes(1)

#: List of Non-3GPP-IP-Access-APN AVP values.
#: For more information, please refer to Section 8.2.3.4 of 
#: ETSI TS 129 273 V14.3.0 (2017-07).
NON_3GPP_APNS_ENABLE = convert_to_4_bytes(0)
NON_3GPP_APNS_DISABLE = convert_to_4_bytes(1)

#: List of Server-Assignment-Type AVP values.
#: For more information, please refer to Section 8.2.3.12 of 
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
