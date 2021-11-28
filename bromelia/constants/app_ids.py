# -*- coding: utf-8 -*-
"""
    bromelia.constants.app_ids
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains list of Application Ids that are defined in several
    Diameter standard documents (both ETSI and IETF specs).
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""


from .._internal_utils import convert_to_4_bytes

DIAMETER_APPLICATION_DEFAULT = convert_to_4_bytes(0)
DIAMETER_APPLICATION_Cx = convert_to_4_bytes(16777216)
DIAMETER_APPLICATION_Sh = convert_to_4_bytes(16777217)
DIAMETER_APPLICATION_Zh = convert_to_4_bytes(16777221)
DIAMETER_APPLICATION_Rx = convert_to_4_bytes(16777236)
DIAMETER_APPLICATION_Gx = convert_to_4_bytes(16777238)
DIAMETER_APPLICATION_S6a = convert_to_4_bytes(16777251)
DIAMETER_APPLICATION_S6a_S6d = convert_to_4_bytes(16777251)
DIAMETER_APPLICATION_S13 = convert_to_4_bytes(16777252)
DIAMETER_APPLICATION_S13_S13 = convert_to_4_bytes(16777252)
DIAMETER_APPLICATION_SWm = convert_to_4_bytes(16777264)
DIAMETER_APPLICATION_SWx = convert_to_4_bytes(16777265)
DIAMETER_APPLICATION_S6b = convert_to_4_bytes(16777272)
DIAMETER_APPLICATION_SLh = convert_to_4_bytes(16777291)
DIAMETER_APPLICATION_UNKNOWN = convert_to_4_bytes(4123456789)
DIAMETER_APPLICATION_RELAY = convert_to_4_bytes(4294967295)
