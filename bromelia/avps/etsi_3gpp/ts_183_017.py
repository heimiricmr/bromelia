# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp.ts_183_017
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in ETSI TS 183 017.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ...base import DiameterAVP
from ...constants import *
from ...types import *


class ReservationPriorityAVP(DiameterAVP, EnumeratedType):
    """Implementation of Reservation-Priority AVP in Section 7.3.9 of 
    ETSI TS 183 017 V2.3.1 (2008-09).

    The Reservation-Priority AVP (AVP Code 458) is of type Enumerated.
    """
    code = RESERVATION_PRIORITY_AVP_CODE
    vendor_id = VENDOR_ID_ETSI

    values = [
                PRIORITY_DEFAULT,
                PRIORITY_ONE,
                PRIORITY_TWO,
                PRIORITY_THREE,
                PRIORITY_FOUR,
                PRIORITY_FIVE,
                PRIORITY_SIX,
                PRIORITY_SEVEN
    ]

    def __init__(self, data=PRIORITY_DEFAULT):
        DiameterAVP.__init__(self, 
                             ReservationPriorityAVP.code,
                             ReservationPriorityAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_ETSI)
