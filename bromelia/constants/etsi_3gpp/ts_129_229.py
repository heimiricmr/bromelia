# -*- coding: utf-8 -*-
"""
    bromelia.constants.etsi_3gpp.ts_129_229
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains constants defined in ETSI TS 129 229.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_4_bytes


#: Diameter AVPs
VISITED_NETWORK_IDENTIFIER_AVP_CODE = convert_to_4_bytes(600)
SIP_NUMBER_AUTH_ITEMS_AVP_CODE = convert_to_4_bytes(607)
SIP_AUTHENTICATION_SCHEME_AVP_CODE = convert_to_4_bytes(608)
SIP_AUTHENTICATE_AVP_CODE = convert_to_4_bytes(609)
SIP_AUTHORIZATION_AVP_CODE = convert_to_4_bytes(610)
SIP_AUTH_DATA_ITEM_AVP_CODE = convert_to_4_bytes(612)
SERVER_ASSIGNMENT_TYPE_AVP_CODE = convert_to_4_bytes(614)
REASON_CODE_AVP_CODE = convert_to_4_bytes(616)
DE_REGISTRATION_REASON_AVP_CODE = convert_to_4_bytes(615)
REASON_INFO_AVP_CODE = convert_to_4_bytes(617)
CONFIDENTIALITY_KEY_AVP_CODE = convert_to_4_bytes(625)
INTEGRITY_KEY_AVP_CODE = convert_to_4_bytes(626)
SUPPORTED_FEATURES_AVP_CODE = convert_to_4_bytes(628)
FEATURE_LIST_ID_AVP_CODE = convert_to_4_bytes(629)
FEATURE_LIST_AVP_CODE = convert_to_4_bytes(630)

#: List of Reason-Code AVP values.
#: For more information, please refer to Section 6.3.17 of 
#: ETSI TS 129 229 V11.3.0 (2013-04).
REASON_CODE_PERMANENT_TERMINATION = convert_to_4_bytes(0)
REASON_CODE_NEW_SERVER_ASSIGNED = convert_to_4_bytes(1)
REASON_CODE_SERVER_CHANGE = convert_to_4_bytes(2)
REASON_CODE_REMOVE_CHANGE = convert_to_4_bytes(3)

#: List of Feature-List-ID AVP values.
#: For more information, please refer to Section 6.3.30 of 
#: ETSI TS 129 229 V14.3.0 (2019-10).
FEATURE_LIST_ID_1 = convert_to_4_bytes(1)
FEATURE_LIST_ID_2 = convert_to_4_bytes(2)
