# -*- coding: utf-8 -*-
"""
    bromelia.constants.ietf.rfc8506
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    This module contains constants defined in IETF RFC 8506.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_4_bytes


#: Diameter AVPs
CC_REQUEST_NUMBER_AVP_CODE = convert_to_4_bytes(415)
CC_REQUEST_TYPE_AVP_CODE = convert_to_4_bytes(416)
RATING_GROUP_AVP_CODE = convert_to_4_bytes(432)
SERVICE_IDENTIFIER_AVP_CODE = convert_to_4_bytes(439)
USER_EQUIPMENT_INFO_AVP_CODE = convert_to_4_bytes(458)
USER_EQUIPMENT_INFO_TYPE_AVP_CODE = convert_to_4_bytes(459)
USER_EQUIPMENT_INFO_VALUE_AVP_CODE = convert_to_4_bytes(460)

#: List of CC-Request-Type AVP values.
#: For more information, please refer to Section 8.3 of IETF RFC 8506.
CC_REQUEST_TYPE_INITIAL_REQUEST = convert_to_4_bytes(1)
CC_REQUEST_TYPE_UPDATE_REQUEST = convert_to_4_bytes(2)
CC_REQUEST_TYPE_TERMINATION_REQUEST = convert_to_4_bytes(3)
CC_REQUEST_TYPE_EVENT_REQUEST = convert_to_4_bytes(4)

#: List of User-Equipment-Info-Type AVP values.
#: For more information, please refer to Section 8.50 of IETF RFC 8506.
USER_EQUIPMENT_INFO_TYPE_IMEISV = convert_to_4_bytes(0)
USER_EQUIPMENT_INFO_TYPE_MAC = convert_to_4_bytes(1)
USER_EQUIPMENT_INFO_TYPE_EUI64 = convert_to_4_bytes(2)
USER_EQUIPMENT_INFO_TYPE_MODIFIED_EUI64 = convert_to_4_bytes(3)
