# -*- coding: utf-8 -*-
"""
    bromelia.constants.ietf.rfc4072
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    
    This module contains constants defined in IETF RFC 4070.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_1_byte
from ..._internal_utils import convert_to_4_bytes


#: Diameter AVPs
EAP_PAYLOAD_AVP_CODE = convert_to_4_bytes(462)
EAP_MASTER_SESSION_KEY_AVP_CODE = convert_to_4_bytes(464)

#: EAP Codes
EAP_CODE_REQUEST = convert_to_1_byte(1)
EAP_CODE_RESPONSE = convert_to_1_byte(2)
EAP_CODE_SUCCESS = convert_to_1_byte(3)
EAP_CODE_FAILURE = convert_to_1_byte(4)

#: EAP Types
EAP_TYPE_IDENTITY = convert_to_1_byte(1)
EAP_TYPE_UMTS_AUTHENTICATION_AND_KEY_AGREEMENT_EAP = convert_to_1_byte(23)

#: EAP-AKA Subtypes
AKA_CHALLENGE = convert_to_1_byte(1)
NOTIFICATION = convert_to_1_byte(12)