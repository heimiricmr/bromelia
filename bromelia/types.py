# -*- coding: utf-8 -*-
"""
    bromelia.types
    ~~~~~~~~~~~~~~

    This module contains the base structures that power the
    bromelia.avps module.

    Defines the AVP library that are used to create Diameter messages.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import abc
import datetime
import ipaddress
import re

from ._internal_utils import avp_look_up
from ._internal_utils import convert_to_3_bytes
from ._internal_utils import convert_to_4_bytes
from ._internal_utils import convert_to_8_bytes
from .base import DiameterAVP
from .base import loader
from .constants import *
from .exceptions import AVPAttributeValueError
from .exceptions import DataTypeError
from .exceptions import DiameterAvpError
from .exceptions import DiameterTypeError


class BaseDataType(abc.ABC):
    @classmethod
    def load(cls, avp):
        return cls(avp.data)


class OctetStringType(BaseDataType):
    @abc.abstractmethod
    def __init__(self, data, vendor_id=None):
        self.parser_data(data)

        if isinstance(vendor_id, bytes):
            if len(vendor_id) != 4:
                raise DataTypeError("Invalid vendor_id format for "\
                                    "OctetStringType. It MUST be 4 bytes long")

            self._length = convert_to_3_bytes(len(self.data) + 
                                                    AVP_HEADER_LENGTH_LONGER)
            self._vendor_id = vendor_id

        elif vendor_id is None:
            self._length = convert_to_3_bytes(len(self.data) + 
                                                    AVP_HEADER_LENGTH)
            self._vendor_id = None

        self._padding = self.set_padding()


    def parser_data(self, data):
        if isinstance(data, str):
            self._data = data.encode("utf-8")

        elif isinstance(data, bytes):
            self._data = data

        else:
            raise DataTypeError("OctetStringType MUST have data argument "\
                                "of 'bytes' or 'str'")


    def set_padding(self):
        mod = len(self.data) % 4
        if mod != 0:
            return bytes(4 - mod)
        else:
            return bytes(0)


class Integer32Type(BaseDataType):
    @abc.abstractmethod
    def __init__(self, data, vendor_id=None):
        self.parser_data(data)

        if isinstance(vendor_id, bytes):
            if len(vendor_id) != 4:
                raise DataTypeError("Integer32Type MUST have vendor_id "\
                                    "argument of 'bytes'")

            self._length = convert_to_3_bytes(16)
            self._vendor_id = vendor_id

        elif vendor_id is None:
            self._length = convert_to_3_bytes(12)
            self._vendor_id = None                        
    

    def parser_data(self, data):
        if len(data) != 4:
            raise DataTypeError("Integer32Type MUST have data argument "\
                                "of 'bytes' with 32-bit signed value")

        self._data = data


class Unsigned32Type(BaseDataType):
    @abc.abstractmethod
    def __init__(self, data, vendor_id=None):
        self.parser_data(data)

        if isinstance(vendor_id, bytes):
            if len(vendor_id) != 4:
                raise DataTypeError("Unsigned32Type MUST have vendor_id "\
                                    "argument of 'bytes'")

            self._length = convert_to_3_bytes(16)
            self._vendor_id = vendor_id

        elif vendor_id is None:
            self._length = convert_to_3_bytes(12)
            self._vendor_id = None                        


    def parser_data(self, data):
        if isinstance(data, int):
            self._data = convert_to_4_bytes(data)


        elif isinstance(data, bytes):
            if len(data) != 4:
                raise DataTypeError("Unsigned32Type MUST have data argument "\
                                    "of 'bytes' with 32-bit signed value")

            self._data = data


    def is_bit_set(self, bit):
        if 0 <= bit < 8:
            return self.data[3] & (2 ** bit) !=0
        elif 8 <= bit < 16:
            return self.data[2] & (2 ** (bit % 8)) !=0
        elif 16 <= bit < 24:
            return self.data[1] & (2 ** (bit % 8)) !=0
        elif 24 <= bit < 32:
            return self.data[0] & (2 ** (bit % 8)) !=0
        else:
            raise DiameterTypeError("Bit index out of range")


    def set_bit(self, bit):
        if self.is_bit_set(bit):
            raise DiameterTypeError("Unable to set an already set bit")

        if 0 <= bit < 8:
            data = self.data[3] | 2 ** bit
            self.data = bytes(bytearray([self.data[0], self.data[1], self.data[2], data]))
        elif 8 <= bit < 16:
            data = self.data[2] | 2 ** (bit % 8) 
            self.data = bytes(bytearray([self.data[0], self.data[1], data, self.data[3]]))
        elif 16 <= bit < 24:
            data = self.data[1] | 2 ** (bit % 8)
            self.data = bytes(bytearray([self.data[0], data, self.data[2], self.data[3]]))
        elif 24 <= bit < 32:
            data = self.data[0] | 2 ** (bit % 8)
            self.data = bytes(bytearray([data, self.data[1], self.data[2], self.data[3]]))

        return self.data


    def unset_bit(self, bit):
        if not self.is_bit_set(bit):
            raise DiameterTypeError("Unable to unset an already unset bit")

        if 0 <= bit < 8:
            data = self.data[3] ^ 2 ** bit
            self.data = bytes(bytearray([self.data[0], self.data[1], self.data[2], data]))
        elif 8 <= bit < 16:
            data = self.data[2] ^ 2 ** (bit % 8) 
            self.data = bytes(bytearray([self.data[0], self.data[1], data, self.data[3]]))
        elif 16 <= bit < 24:
            data = self.data[1] ^ 2 ** (bit % 8)
            self.data = bytes(bytearray([self.data[0], data, self.data[2], self.data[3]]))
        elif 24 <= bit < 32:
            data = self.data[0] ^ 2 ** (bit % 8)
            self.data = bytes(bytearray([data, self.data[1], self.data[2], self.data[3]]))

        return self.data


class Unsigned64Type(BaseDataType):
    @abc.abstractmethod
    def __init__(self, data, vendor_id=None):
        self.parser_data(data)

        if isinstance(vendor_id, bytes):
            if len(vendor_id) != 4:
                raise DataTypeError("Unsigned64Type MUST have vendor_id "\
                                    "argument of 'bytes'")

            self._length = convert_to_3_bytes(20)
            self._vendor_id = vendor_id

        elif vendor_id is None:
            self._length = convert_to_3_bytes(16)
            self._vendor_id = None                        


    def parser_data(self, data):
        if isinstance(data, int):
            self._data = convert_to_8_bytes(data)

        elif isinstance(data, bytes):
            if len(data) != 8:
                raise DataTypeError("Unsigned64Type MUST have data argument "\
                                    "of 'bytes' with 64-bit unsigned value")

            self._data = data


class GroupedType(BaseDataType):
    mandatory = {}
    optionals = {}

    @abc.abstractmethod
    def __init__(self, data, vendor_id=None):
        if isinstance(data, bytes):
            self._data = data
            self.avps = DiameterAVP.load(data)

        elif isinstance(data, list):
            self._data = b""
            self.avps = data
            for avp in data:
                if not isinstance(avp, DiameterAVP):
                    raise DataTypeError("GroupedType MUST have data "\
                                        "argument of 'list' with "\
                                        "DiameterAVP objects")
                
        else:
            raise DataTypeError("GroupedType MUST have data argument "\
                                "of 'list' with DiameterAVP objects")

        if self.mandatory:
            mandatory_avps_codes = [avp.code for avp in self.mandatory.values()]
            data_avp_codes = [avp.code for avp in self.avps]
            
            if not set(mandatory_avps_codes).issubset(data_avp_codes):
                raise AVPAttributeValueError("missing mandatory avp", 
                                              DIAMETER_MISSING_AVP)
        
        #: TO-DO: maybe create a custom condtional method to check specific
        #: rules for a given AVP. 

        if isinstance(vendor_id, bytes):
            if len(vendor_id) != 4:
                raise DataTypeError("GroupedType MUST have vendor_id "\
                                    "argument of 'bytes'")

            self._vendor_id = vendor_id
    
            if isinstance(data, bytes):
                _length = AVP_HEADER_LENGTH_LONGER
                self._length = convert_to_3_bytes(len(data) + _length)

        elif vendor_id is None:
            self._vendor_id = None

            if isinstance(data, bytes):
                _length = AVP_HEADER_LENGTH
                self._length = convert_to_3_bytes(len(data) + _length)


    @classmethod
    def load(cls, avp):
        self.append(avp)
        return cls(avp)


    @property
    def avps(self):
        return tuple(self._avps)


    @avps.setter
    def avps(self, value):
        if not isinstance(value, list):
            raise DiameterAvpError(f"only list allowed. Cannot append a "\
                                   f"data type of '{type(value)}'")
    
        self.cleanup()

        if len(value) == 1:
            self.append(value[0])
        elif len(value) > 1:
            self.extend(value)


    def __getitem__(self, idx):
        return self._avps[idx]


    def __setitem__(self, idx, value):
        self._avps[idx] = value


    def append(self, avp):
        if not isinstance(avp, DiameterAVP):
            raise DiameterAvpError(f"cannot append a data type of "\
                                   f"'{type(avp)}'")

        avp_name = avp_look_up(avp)
        if avp_name == "Unknown":
            avp_name = loader.get_avp_class_name(avp)

        _name = avp_name.replace("-", "_").lower()
        avp_key = f"{_name}_avp"


        if avp_key in self.__dict__:
            index = 0
            for key in self.__dict__.keys():
                if avp_key in key:
                    index += 1
            avp_key = f"{avp_key}__{index}"

        self._avps.append(avp)
        self.__dict__.update({avp_key: avp})

        self._data += avp.dump()


    def extend(self, avps):
        for avp in avps:
            self.append(avp)


    def has_avp(self, avp_key):
        if not isinstance(avp_key, str):
            raise DiameterAvpError("`avp_key` must be str")

        if not self.avps:
            return False
        elif avp_key in self.__dict__:
            return True
        return False


    def pop(self, avp_key):
        if not self.avps:
            raise DiameterAvpError("`avps` attribute is empty. There is "\
                                   "no DiameterAVP object to be removed")

        try:
            item = self.__dict__[avp_key]
        except KeyError:
            raise DiameterAvpError(f"`{avp_key}` key not defined")

        self._avps.remove(item)
        self.__dict__.pop(avp_key, None)

        self._data = b""
        for avp in self.avps:
            self._data += avp.dump()


    def update_key(self, old_avp_key, new_avp_key):
        if not self.has_avp(old_avp_key):
            raise DiameterAvpError(f"`{old_avp_key}` key not defined")
            
        if self.has_avp(new_avp_key):
            raise DiameterAvpError(f"`{new_avp_key}` key already defined")

        self.__dict__[new_avp_key] = self.__dict__.pop(old_avp_key)


    def cleanup(self):
        self._data = b""
        self._avps = list()

        avps_keys = list()
        for avp_key in self.__dict__.keys():
            if "_avp" in avp_key and avp_key != "_avps":
                avps_keys.append(avp_key)
                    
        for avp_key in avps_keys:
            self.__dict__.pop(avp_key, None)


    #: TO-DO: refresh does not work properly, it needs to refresh all data, 
    #: specialy if avp is of grouped type.
    def refresh(self):
        if self.is_vendor_id():
            avp_length = AVP_HEADER_LENGTH_LONGER
        else:
            avp_length = AVP_HEADER_LENGTH

        real_length = 0

        for avp in self.avps:
            avp_length += len(avp)
            padding = avp.get_padding_length()
            if padding:
                real_length += avp.get_padding_length()

        if real_length != self.get_length():
            self.header.length = convert_to_3_bytes(real_length)


class AddressType(OctetStringType):
    @abc.abstractmethod
    def __init__(self, data, vendor_id=None):
        AddressType.parser_data(self, data)
        OctetStringType.__init__(self, data, vendor_id)


    def parser_data(self, data):
        if isinstance(data, bytes):
            if data[:2] == HOST_IP_ADDRESS_FAMILY_CODE_IPV4:
                try:
                    ipaddress.IPv4Address(data[2:])
                except ipaddress.AddressValueError:
                    raise DataTypeError("Stream of bytes does not "\
                                        "correspond to a valid IPv4 address "\
                                        "format")

            elif data[:2] == HOST_IP_ADDRESS_FAMILY_CODE_IPV6:
                try:
                    ipaddress.IPv6Address(data[2:])
                except ipaddress.AddressValueError:
                    raise DataTypeError("Stream of bytes does not "\
                                        "correspond to a valid IPv6 address "\
                                        "format")

        else:
            ip_address = ipaddress.ip_address(data)
    
            if isinstance(ip_address, ipaddress.IPv4Address):
                ip_address_family_code = HOST_IP_ADDRESS_FAMILY_CODE_IPV4

            elif isinstance(ip_address, ipaddress.IPv6Address):
                ip_address_family_code = HOST_IP_ADDRESS_FAMILY_CODE_IPV6

            else:
                raise DataTypeError("AddressType MUST have data argument "\
                                    "of 'str' with IP address format value")

            data = ip_address_family_code + ip_address.packed
        
        self._data = data                


    def is_ipv4(self):
        ip_address = ipaddress.ip_address(self.data[2:])

        if isinstance(ip_address, ipaddress.IPv4Address):
            return True
        return False


    def is_ipv6(self):
        ip_address = ipaddress.ip_address(self.data[2:])

        if isinstance(ip_address, ipaddress.IPv6Address):
            return True
        return False

    
    def get_ip_address(self):
        if self.is_ipv4():
            return str(ipaddress.IPv4Address(self.data[2:]))

        if self.is_ipv6():
            return str(ipaddress.IPv6Address(self.data[2:]))


class TimeType(OctetStringType):
    @abc.abstractmethod
    def __init__(self, data, vendor_id=None):
        if isinstance(data, bytes):
            if len(data) != 4:
                raise DataTypeError("Invalid data format for TimeType. It "\
                                    "MUST be 4 bytes long")

        elif isinstance(data, datetime.datetime):
            ref = datetime.datetime(1900, 1, 1, 0, 0, 0)
            diff = data - ref

            timestamp = diff.days*24*60*60 + diff.seconds
            data = convert_to_4_bytes(timestamp)
        
        elif not isinstance(data, datetime.datetime) or not isinstance(data, bytes):
            raise DataTypeError("Invalid data format for TimeType. It MUST "\
                                "be a datetime object")

        OctetStringType.__init__(self, data, vendor_id)    


class UTF8StringType(OctetStringType):
    @abc.abstractmethod
    def __init__(self, data, vendor_id=None):
        OctetStringType.__init__(self, data, vendor_id)


class DiameterIdentityType(OctetStringType):
    @abc.abstractmethod
    def __init__(self, data, vendor_id=None):
        OctetStringType.__init__(self, data, vendor_id)


class DiameterURIType(OctetStringType):
    @abc.abstractmethod
    def __init__(self, data, vendor_id=None):
        self.parser_data(data)
        OctetStringType.__init__(self, data, vendor_id)


    def parser_data(self, data):
        if isinstance(data, bytes):
            data = data.decode("utf-8")

        elif isinstance(data, str):
            data = data

        else:
            raise DataTypeError("invalid data format. Data MUST be of "\
                                "'str' or 'bytes' and follow the URI syntax")

        pattern = r"aaa[s]{0,1}://(?!\d\.)[a-zA-Z1-9_\-].{1,62}"\
                  r"[a-zA-Z1-9_\-](\:\b([1-9]|[1-9][0-9]|[1-9]"\
                  r"[0-9][0-9]|[1-9][0-9][0-9][0-9]|[1-3][0-9]"\
                  r"[0-9][0-9][0-9]|4[0-8][0-9][0-9][0-9]|490[0-9]"\
                  r"[0-9]|491[0-4][0-9]|49150|49151)\b){0,1}(;transport"\
                  r"=(tcp|udp|sctp)){0,1}(;protocol=(diameter|radius)){0,1}"

        if not re.fullmatch(pattern, data):
            raise DataTypeError("invalid data format. It does not comply "\
                                "to the DiameterURI syntax")

        self._data = data.encode("utf-8")


class EnumeratedType(Integer32Type):
    @abc.abstractmethod
    def __init__(self, data, vendor_id=None):
        avp_class_name = self.__class__.__name__

        if data not in self.values:
            raise AVPAttributeValueError(f"invalid input argument for "\
                                         f"{avp_class_name}. Refer to the "\
                                         f"`values` class attribute for options")

        Integer32Type.__init__(self, data, vendor_id)
