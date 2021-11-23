# -*- coding: utf-8 -*-
"""
    bromelia.avps.ietf.rfc4072
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in IETF RFC 4072.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import base64

from ..._internal_utils import convert_to_1_byte
from ...base import DiameterAVP
from ...constants.ietf.rfc4072 import *
from ...types import *


class EapPayloadAVP(DiameterAVP, OctetStringType):
    """Implementation of EAP-Payload AVP in Section 4.1.1 of IETF RFC 4072.

    The EAP-Payload AVP (AVP Code 462) is of type OctetString.
    """
    code = EAP_PAYLOAD_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, EapPayloadAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)    

        EapPayloadAVP.parser_data(self, data)

        OctetStringType.__init__(self, data=self.data)


    def parser_data(self, data):
        if not isinstance(data, bytes):
            if data.eap_type == EAP_TYPE_IDENTITY:
                eap_nai_data = data.content["nai"].encode("utf-8")
                eap_length = convert_to_2_bytes(len(data.eap_code + convert_to_1_byte(data.eap_id) + data.eap_type + eap_nai_data) + 2)
                
                data = data.eap_code + convert_to_1_byte(data.eap_id) + eap_length + data.eap_type + eap_nai_data
                        
            elif data.eap_type == EAP_TYPE_UMTS_AUTHENTICATION_AND_KEY_AGREEMENT_EAP:
                data = base64.b64decode(data.content["payload"])

        self.data = data


class EapMasterSessionKeyAVP(DiameterAVP, OctetStringType):
    """Implementation of EAP-Master-Session-Key AVP in Section 4.1.3
    of IETF RFC 4072.

    The EAP-Master-Session-Key AVP (AVP Code 464) is of type OctetString.
    """
    code = EAP_MASTER_SESSION_KEY_AVP_CODE
    vendor_id = None

    def __init__(self, data): 
        DiameterAVP.__init__(self, EapMasterSessionKeyAVP.code)
        OctetStringType.__init__(self, data=data)