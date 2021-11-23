# -*- coding: utf-8 -*-
"""
    bromelia.avps.ietf.rfc8506
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in IETF RFC 8506.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ...base import DiameterAVP
from ...constants.ietf.rfc8506 import *
from ...types import *


class CcRequestNumberAVP(DiameterAVP, Unsigned32Type):
    """Implementation of CC-Request-Number AVP in Section 8.2 of 
    IETF RFC 8506.

    The CC-Request-Number AVP (AVP Code 415) is of type Unsigned32.
    """
    code = CC_REQUEST_NUMBER_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             CcRequestNumberAVP.code,
                             CcRequestNumberAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class CcRequestTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of CC-Request-Type AVP in Section 8.3 of 
    IETF RFC 8506.

    The CC-Request-Type AVP (AVP Code 416) is of type Enumerated.
    """
    code = CC_REQUEST_TYPE_AVP_CODE
    vendor_id = None

    values = [
                CC_REQUEST_TYPE_INITIAL_REQUEST,
                CC_REQUEST_TYPE_UPDATE_REQUEST,
                CC_REQUEST_TYPE_TERMINATION_REQUEST,
                CC_REQUEST_TYPE_EVENT_REQUEST
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             CcRequestTypeAVP.code,
                             CcRequestTypeAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class RatingGroupAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Rating-Group AVP in Section 8.29 of 
    IETF RFC 8506.

    The Rating-Group AVP (AVP Code 432) is of type Unsigned32.
    """
    code = RATING_GROUP_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             RatingGroupAVP.code,
                             RatingGroupAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class ServiceIdentifierAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Service-Identifier AVP in Section 8.28 of 
    IETF RFC 8506.

    The Service-Identifier AVP (AVP Code 439) is of type Unsigned32.
    """
    code = SERVICE_IDENTIFIER_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ServiceIdentifierAVP.code,
                             ServiceIdentifierAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class UserEquipmentInfoAVP(DiameterAVP, GroupedType):
    """Implementation of User-Equipment-Info AVP in Section 8.49 of 
    IETF RFC 8506.

    The User-Equipment-Info AVP (AVP Code 458) is of type Grouped.
    """
    code = USER_EQUIPMENT_INFO_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             UserEquipmentInfoAVP.code,
                             UserEquipmentInfoAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)


class UserEquipmentInfoTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of User-Equipment-Info-Type AVP in Section 8.50 of 
    IETF RFC 8506.

    The User-Equipment-Info-Type AVP (AVP Code 459) is of type Enumerated.
    """
    code = USER_EQUIPMENT_INFO_TYPE_AVP_CODE
    vendor_id = None

    values = [
                USER_EQUIPMENT_INFO_TYPE_IMEISV,
                USER_EQUIPMENT_INFO_TYPE_MAC,
                USER_EQUIPMENT_INFO_TYPE_EUI64,
                USER_EQUIPMENT_INFO_TYPE_MODIFIED_EUI64,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             UserEquipmentInfoTypeAVP.code,
                             UserEquipmentInfoTypeAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class UserEquipmentInfoValueAVP(DiameterAVP, OctetStringType):
    """Implementation of User-Equipment-Info-Value AVP in Section 8.51 of 
    IETF RFC 8506.

    The User-Equipment-Info-Value AVP (AVP Code 460) is of type OctetString.
    """
    code = USER_EQUIPMENT_INFO_VALUE_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             UserEquipmentInfoValueAVP.code,
                             UserEquipmentInfoValueAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        OctetStringType.__init__(self, data=data)