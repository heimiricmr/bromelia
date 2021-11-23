# -*- coding: utf-8 -*-
"""
    bromelia.constants.ietf.rfc7155
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    
    This module contains constants defined in IETF RFC 7155.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_4_bytes


#: Diameter AVPs
FRAMED_IP_ADDRESS_AVP_CODE = convert_to_4_bytes(8)
CALLED_STATION_ID_AVP_CODE = convert_to_4_bytes(30)
CALLING_STATION_ID_AVP_CODE = convert_to_4_bytes(31)
FRAMED_IPV6_PREFIX_AVP_CODE = convert_to_4_bytes(97)
