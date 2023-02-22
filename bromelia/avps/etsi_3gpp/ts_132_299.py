# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp.ts_132_299
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in ETSI TS 132 299.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..ietf.rfc4006 import CurrencyCodeAVP
from ..ietf.rfc4006 import UnitValueAVP

from ...base import DiameterAVP
from ...constants.etsi_3gpp.ts_132_299 import *
from ...types import *


class LowBalanceIndicationAVP(DiameterAVP, EnumeratedType):
    """Implementation of Low-Balance-Indication AVP in Section 7.2.97 of 
    ETSI TS 132 299 V14.3.0 (2017-04).

    The Low-Balance-Indication AVP (AVP Code 2020) is of type Enumerated.
    """
    code = LOW_BALANCE_INDICATION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                LOW_BALANCE_INDICATION_NOT_APPLICABLE,
                LOW_BALANCE_INDICATION_YES,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             LowBalanceIndicationAVP.code,
                             LowBalanceIndicationAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class RemainingBalanceAVP(DiameterAVP, GroupedType):
    """Implementation of Remaining-Balance AVP in Section 7.2.172 of 
    ETSI TS 132 299 V14.3.0 (2017-04).

    The Remaining-Balance AVP (AVP Code 2021) is of type Grouped.
    """
    code = REMAINING_BALANCE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "unit_value": UnitValueAVP,
                    "currency_code": CurrencyCodeAVP
    }
    optionals = {}

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             RemainingBalanceAVP.code,
                             RemainingBalanceAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)

