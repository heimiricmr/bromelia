# -*- coding: utf-8 -*-
"""
    bromelia.avps.ietf.rfc4006
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in IETF RFC 4006.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ...base import DiameterAVP
from ...constants.ietf.rfc4006 import *
from ...types import *


class SubscriptionIdDataAVP(DiameterAVP, UTF8StringType):
    """Implementation of Subscription-Id-Data AVP in Section 8.48 of 
    IETF RFC 4006.

    The Subscription-Id-Data AVP (AVP Code 444) is of type UTF8String.
    """
    code = SUBSCRIPTION_ID_DATA_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, SubscriptionIdDataAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


class SubscriptionIdTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Subscription-Id-Type AVP in Section 8.47 of 
    IETF RFC 4006.

    The Subscription-Id-Type AVP (AVP Code 450) is of type Enumerated.
    """
    code = SUBSCRIPTION_ID_TYPE_AVP_CODE
    vendor_id = None

    values = [
                END_USER_E164,
                END_USER_IMSI,
                END_USER_SIP_URI,
                END_USER_NAI,
                END_USER_PRIVATE
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, SubscriptionIdTypeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class SubscriptionIdAVP(DiameterAVP, GroupedType):
    """Implementation of Subscription-Id AVP in Section 8.46 of IETF RFC 4006.

    The Subscription-Id AVP (AVP Code 443) is of type Grouped.
    """
    code = SUBSCRIPTION_ID_AVP_CODE
    vendor_id = None

    mandatory = {
                    "subscription_id_data": SubscriptionIdDataAVP,
                    "subscription_id_type": SubscriptionIdTypeAVP,
    }
    optionals = {}

    def __init__(self, data):
        DiameterAVP.__init__(self, SubscriptionIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)