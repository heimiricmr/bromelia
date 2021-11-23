#: -*- coding: utf-8 -*-
"""
    bromelia.constants.general
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains general constants defined in IETF RFC 6733.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from .._internal_utils import convert_to_1_byte
from .._internal_utils import convert_to_4_bytes

#: General constants.
PRODUCT_NAME = f"Python bromelia"

DIAMETER_VERSION = convert_to_1_byte(1)
FIRMWARE_VERSION = convert_to_4_bytes(1)

#: Diameter Agent Types.
DIAMETER_AGENT_CLIENT_MODE = "CLIENT"
DIAMETER_AGENT_SERVER_MODE = "SERVER"

#: Basic AVP Data Formats.
AVP_LENGTH_UNSIGNED32 = 12
AVP_LENGTH_UNSIGNED32_AND_V_BIT = 16

AVP_LENGTH_INTEGER32 = 12
AVP_LENGTH_INTEGER32_AND_V_BIT = 16

AVP_LENGTH_INTEGER64 = 16
AVP_LENGTH_INTEGER64_AND_V_BIT = 20

#: Constants for Fields Lenght of Diameter Header.
DIAMETER_VERSION_FIELD = 1
DIAMETER_LENGTH_FIELD = 3
DIAMETER_FLAG_FIELD = 1
DIAMETER_COMMAND_CODE_FIELD = 3
DIAMETER_APPLICATION_ID_FIELD = 4
DIAMETER_HOP_BY_HOP_FIELD = 4
DIAMETER_END_TO_END_FIELD = 4

DIAMETER_HEADER_LENGTH = DIAMETER_VERSION_FIELD + \
                         DIAMETER_LENGTH_FIELD + \
                         DIAMETER_FLAG_FIELD + \
                         DIAMETER_COMMAND_CODE_FIELD + \
                         DIAMETER_APPLICATION_ID_FIELD + \
                         DIAMETER_HOP_BY_HOP_FIELD + \
                         DIAMETER_END_TO_END_FIELD

#: Constants for Fields Lenght of Diameter AVP Header.
AVP_CODE_FIELD = 4
AVP_FLAG_FIELD = 1
AVP_LENGTH_FIELD = 3
AVP_VENDOR_ID_FIELD = 4

AVP_HEADER_LENGTH = AVP_CODE_FIELD + AVP_FLAG_FIELD + AVP_LENGTH_FIELD
AVP_HEADER_LENGTH_LONGER = AVP_HEADER_LENGTH + AVP_VENDOR_ID_FIELD
