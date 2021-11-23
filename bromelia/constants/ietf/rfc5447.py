# -*- coding: utf-8 -*-
"""
    bromelia.constants.ietf.rfc5447
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    
    This module contains constants defined in IETF RFC 5447.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_4_bytes


#: Diameter AVPs
MIP_HOME_AGENT_HOST_AVP_CODE = convert_to_4_bytes(348)
MIP6_AGENT_INFO_AVP_CODE = convert_to_4_bytes(486)
