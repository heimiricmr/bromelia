# -*- coding: utf-8 -*-
"""
    bromelia.avps.ietf.rfc7155
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in IETF RFC 7155.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ...base import DiameterAVP
from ...constants.ietf.rfc7155 import *
from ...types import *


class FramedIpAddressAVP(DiameterAVP, AddressType):
    """Implementation of Framed-IP-Address AVP in Section 4.4.10.5.1 of 
    IETF RFC 7155.

    The Framed-IP-Address AVP (AVP Code 8) is of type Address.
    """
    code = FRAMED_IP_ADDRESS_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, FramedIpAddressAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        AddressType.__init__(self, data=data)


    def parser_data(self, data):
        if isinstance(data, str):
            ip_address = ipaddress.ip_address(data)

            if isinstance(ip_address, ipaddress.IPv4Address):
                self._data = ip_address.packed

            else:
                raise DataTypeError("AddressType MUST have data argument "\
                                    "of 'str' with IPv4 address format value")

        elif isinstance(data, bytes):
            self._data = data


class CalledStationIdAVP(DiameterAVP, UTF8StringType):
    """Implementation of Called-Station-Id AVP in Section 4.2.5 of
    IETF RFC 7155.

    The Called-Station-Id AVP (AVP Code 30) is of type UTF8String.
    """
    code = CALLED_STATION_ID_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, CalledStationIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


class FramedIpv6PrefixAVP(DiameterAVP, OctetStringType):
    """Implementation of Framed-IPv6-Prefix AVP in Section 4.4.10.5.6 of 
    IETF RFC 7155.

    The Framed-IPv6-Prefix AVP (AVP Code 97) is of type OctetString.
    """
    code = FRAMED_IPV6_PREFIX_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, FramedIpv6PrefixAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        OctetStringType.__init__(self, data=data)


class CallingStationIdAVP(DiameterAVP, UTF8StringType):
    """Implementation of Calling-Station-Id AVP in Section 4.2.6 of 
    IETF RFC 7155.

    The Calling-Station-Id AVP (AVP Code 31) is of type UTF8String.
    """
    code = CALLING_STATION_ID_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, CallingStationIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)