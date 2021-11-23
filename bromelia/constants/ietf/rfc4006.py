# -*- coding: utf-8 -*-
"""
    bromelia.constants.ietf.rfc4006
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    
    This module contains constants defined in IETF RFC 4006.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_4_bytes


#: Diameter AVPs
SUBSCRIPTION_ID_AVP_CODE = convert_to_4_bytes(443)
SUBSCRIPTION_ID_DATA_AVP_CODE = convert_to_4_bytes(444)
SUBSCRIPTION_ID_TYPE_AVP_CODE = convert_to_4_bytes(450)

#: List of Subscription-Id-Type values.
#: For more information, please refer to Section 8.47 of IETF RFC 4006.
END_USER_E164 = convert_to_4_bytes(0)
END_USER_IMSI = convert_to_4_bytes(1)
END_USER_SIP_URI = convert_to_4_bytes(2)
END_USER_NAI = convert_to_4_bytes(3)
END_USER_PRIVATE = convert_to_4_bytes(4)
