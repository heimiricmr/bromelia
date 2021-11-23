# -*- coding: utf-8 -*-
"""
    bromelia.constants.etsi_3gpp.ts_183_017
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains constants defined in ETSI TS 183 017.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_4_bytes


#: Diameter AVPs
RESERVATION_PRIORITY_AVP_CODE = convert_to_4_bytes(458)

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
