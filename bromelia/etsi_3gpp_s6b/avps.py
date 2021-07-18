# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_s6b.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP S6b Application Id.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..base import *
from ..constants import *
from ..types import *


class Mip6FeatureVectorAVP(DiameterAVP, Unsigned64Type):
    """Implementation of MIP6-Feature-Vector AVP in Section 9.2.3.2.3 of 
    ETSI TS 129 273 V14.3.0 (2017-07).

    The MIP6-Feature-Vector AVP (AVP Code 124) is of type Unsigned64.
    """
    code = MIP6_FEATURE_VECTOR_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, Mip6FeatureVectorAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned64Type.__init__(self, data=data)