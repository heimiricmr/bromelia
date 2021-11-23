# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp.ts_129_329
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in ETSI TS 129 329.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ...base import DiameterAVP
from ...constants.etsi_3gpp.ts_129_329 import *
from ...types import *
from ...utils import decode_from_tbcd, encode_to_tbcd


class MsisdnAVP(DiameterAVP, OctetStringType):
    """Implementation of MSISDN AVP in Section 6.3.2 of 
    ETSI TS 129 329 V15.1.0 (2018-07).

    The MSISDN AVP (AVP Code 701) is of type OctetString.
    """
    code = MSISDN_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             MsisdnAVP.code,
                             MsisdnAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=self.encode(data), vendor_id=VENDOR_ID_3GPP)


    def encode(self, data):
        if isinstance(data, int):
            return bytes.fromhex(encode_to_tbcd(data))
        
        elif isinstance(data, str):
            return bytes.fromhex(encode_to_tbcd(int(data)))

        elif isinstance(data, bytes):
            return data


    def decode(self):
        return decode_from_tbcd(self.data)