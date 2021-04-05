# -*- coding: utf-8 -*-
"""
    bromelia.base
    ~~~~~~~~~~~~~

    This module contains the base structures that power 
    bromelia.messages module.

    :copyright: (c) 2020 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import os
import re
from copy import deepcopy

from ._internal_utils import avp_look_up
from ._internal_utils import header_representation
from .constants import *
from .exceptions import AVPAttributeValueError
from .exceptions import AVPParsingError
from .exceptions import DiameterAvpError
from .exceptions import DiameterHeaderAttributeValueError
from .exceptions import DiameterHeaderError
from .exceptions import DiameterMessageError
from .utils import is_vendor_id


class DiameterAvpLoader:
    def __init__(self):
        self.avps = None


    def has_updated(self):
        avps = DiameterAVP.__subclasses__()
        if len(self.avps) == len(avps):
            return False
        return True


    def _get_load_avps_dictionary(self):
        avps = DiameterAVP.__subclasses__()
        loaded_avps = dict()
        for avp in avps:
            loaded_avps.update({avp.code: avp})
        return loaded_avps


    def get_avp_class_by_avp_code(self, avp_code):
        if self.avps is not None:
            if self.has_updated():
                self.avps = self._get_load_avps_dictionary()
        else:
            self.avps = self._get_load_avps_dictionary()

        return self.avps[avp_code]


    def get_avp_class_name_by_avp_code(self, avp_code):
        try: 
            avp_name = self.get_avp_class_by_avp_code(avp_code).__name__[:-3]
            if len(avp_name.split("-")) == 1:
                return "-".join(re.findall("[A-Z][^A-Z]*", avp_name))

        except KeyError:
            return "Unknown"    
            

class DiameterAVP(object):
    """Implementation of a Diameter AVP. 
    
    Refer to Section 4 of IETF RFC 6733 for details. The constructor has
    input arguments as per Header AVP fields.

    Provides a general-case interface for create custom and standard 
    Diameter AVPs.

    :param code: the AVP Code which identifies the attribute uniquely.
    :param flags: the AVP Flags field informs the receiver how each attribute
        must be handled.
    :param length: the AVP Length field is three octets, and indicates the 
        number of octets in this AVP including the AVP Code field, AVP Length
        field, AVP Flags field, Vendor-ID field (if present), and the AVP Data
        field.
    :param vendor_id: the Vendor-ID field is present if the 'V' bit is set
        in the AVP Flags field. It is the only optional field in a AVP header.
    :param data: the Data field is zero or more octets and contains 
        information specific to the Attribute.

    Usage::

        >>> from bromelia.avps import DiameterAVP
        >>> avp = DiameterAVP()
        <Diameter AVP: 0 [Diameter]>
    """

    __slots__ = ("_code", "_flags", "_length", 
                "_vendor_id", "_data", "_padding")

    flag_vendor_id_bit = convert_to_1_byte(0x80)
    flag_mandatory_bit = convert_to_1_byte(0x40)
    flag_protected_bit = convert_to_1_byte(0x20)
    flag_reserved5_bit = convert_to_1_byte(0x10)
    flag_reserved4_bit = convert_to_1_byte(0x08)
    flag_reserved3_bit = convert_to_1_byte(0x04)
    flag_reserved2_bit = convert_to_1_byte(0x02)
    flag_reserved1_bit = convert_to_1_byte(0x01)

    def __init__(self, 
                 code=0, 
                 flags=0, 
                 vendor_id=None, 
                 data=None, 
                 padding=None):
        self.code = code
        self.flags = flags
        self.vendor_id = vendor_id
        self.data = data
        self._padding = padding


    def __repr__(self):
        avp_name = avp_look_up(self)
        if avp_name == "Unknown":
            avp_name = loader.get_avp_class_name_by_avp_code(self.code)


        flag_representation = ""

        if self.is_vendor_id():
            flag_representation += " VENDOR,"

        if self.is_mandatory():
            flag_representation += " MANDATORY,"

        if self.is_protected():
            flag_representation += " PROTECTED "

        return f"<Diameter AVP: {self.get_code()} [{avp_name}]"\
                f"{flag_representation[:-1]}>"


    def __add__(self, other):
        return self.dump() + other.dump()


    def __len__(self):
        return self.get_length()


    def __eq__(self, other):
        return self.dump() == other.dump()


    def __bytes__(self):
        return self.dump()


    def copy(self):
        return deepcopy(self)


    @classmethod
    def convert(cls, avp):
        if not isinstance(avp, DiameterAVP):
            raise DiameterAVPError("invalid AVP. It MUST be a DiameterAVP "\
                                "subclass object to be converted into "\
                                "DiameterAVP object")
        
        return cls(code=avp.code,
                   flags=avp.flags,
                   vendor_id=avp.vendor_id,
                   data=avp.data,
                   padding=avp._padding)


    @property
    def code(self):
        return self._code


    @code.setter
    def code(self, value):
        if isinstance(value, int) and (value >= 0 and value <= 4294967295):
            self._code = convert_to_4_bytes(value)

        if isinstance(value, bytes) and len(value) == 4:
            self._code = value

        elif isinstance(value, int) and (value < 0 or value > 4294967295):
            raise AVPAttributeValueError("code attribute has 4-bytes "\
                                        "length long")

        elif isinstance(value, bytes) and len(value) != 4:
            raise AVPAttributeValueError("code attribute has 4-bytes "\
                                        "length long")

        elif not isinstance(value, bytes) and not isinstance(value, int):
            raise AVPAttributeValueError("invalid code attribute value")


    @property
    def flags(self):
        return self._flags


    @flags.setter
    def flags(self, value):
        if isinstance(value, int) and (value >= 0 and value <= 255):
            self._flags = convert_to_1_byte(value)

        elif isinstance(value, bytes) and len(value) == 1:
            self._flags = value

        elif isinstance(value, int) and (value < 0 or value > 255):
            raise AVPAttributeValueError("flags attribute has 1-byte "\
                                        "length long")

        elif isinstance(value, bytes) and len(value) != 1:
            raise AVPAttributeValueError("flags attribute has 1-byte "\
                                        "length long")

        elif not isinstance(value, bytes) and not isinstance(value, int):
            raise AVPAttributeValueError("invalid flags attribute value")


    @property
    def length(self):
        try:
            length = len(self.data)
        except TypeError as e:
            if "object of type 'NoneType' has no len()" in e.args[0]:
                length = 0

        if self.vendor_id:        
            length += AVP_HEADER_LENGTH_LONGER

        else:
            length += AVP_HEADER_LENGTH

        return convert_to_3_bytes(length)


    @length.setter
    def length(self, value):
        if value is None:
            self._length = value

        elif isinstance(value, int) and (value >= 0 and value <= 16777215):
            self._length = convert_to_3_bytes(value)

        elif isinstance(value, int) and (value < 0 or value > 16777215):
            raise DiameterHeaderAttributeValueError("length attribute "\
                                                "has 3-bytes length long")

        elif isinstance(value, bytes) and len(value) == 3:
            self._length = value

        elif isinstance(value, bytes) and len(value) != 3:
            raise DiameterHeaderAttributeValueError("length attribute "\
                                                "has 3-bytes length long")

        elif not isinstance(value, bytes) and not isinstance(value, int):
            raise DiameterHeaderAttributeValueError("invalid length "\
                                                "attribute value")

    @property
    def vendor_id(self):
        return self._vendor_id


    @vendor_id.setter
    def vendor_id(self, value):
        if value is None:
            self._vendor_id = value

        elif isinstance(value, int) and (value >= 0 and value <= 4294967295):
            self._vendor_id = convert_to_4_bytes(value)

        elif isinstance(value, int) and (value < 0 or value > 4294967295):
            raise AVPAttributeValueError("vendor_id attribute has 4-bytes "\
                                        "length long")

        elif isinstance(value, bytes) and len(value) == 4:
            self._vendor_id = value

        elif isinstance(value, bytes) and len(value) != 4:
            raise AVPAttributeValueError("vendor_id attribute has 4-bytes "\
                                        "length long")

        elif not isinstance(value, bytes) and not isinstance(value, int):
            raise AVPAttributeValueError("invalid vendor_id attribute value")


    @property
    def data(self):
        return self._data


    @data.setter
    def data(self, value):
        data = value
        if value:
            if isinstance(value, str):
                data = value.encode("utf-8")
            elif isinstance(value, int):
                data = convert_to_4_bytes(value)
            elif isinstance(value, bytes):
                data = value
            else:
                raise AVPAttributeValueError("invalid data value. Consider "\
                                            "create a data type object "\
                                            "before assigning")

        self._data = data                                


    @property
    def padding(self):
        if self.data:
            mod = len(self.data) % 4
            if mod != 0:
                return bytes(4 - mod)

        return None


    @staticmethod
    def load(stream):
        avps = list()
        index = 0
        
        while index < len(stream):
            avp = DiameterAVP()

            try:
                avp._code = stream[index:index+4]
                avp._flags = convert_to_1_byte(stream[index+4])
                avp._length = stream[index+5:index+8]
                if len(avp._length) != 3:
                    raise AVPParsingError("invalid bytes stream. It "\
                                    "contains only the code and flags fields")

                boundary = int.from_bytes(avp._length, byteorder="big")
                
                if is_vendor_id(avp._flags):
                    avp._vendor_id = stream[index+8:index+12]
                    if len(avp._vendor_id) != 4:
                        raise AVPParsingError("invalid bytes stream. It "\
                                        "contains only the code, flags "\
                                        "and length fields")

                    avp._data = stream[index+12:index+boundary]
                    avp_header_length = AVP_HEADER_LENGTH_LONGER

                else:
                    avp._vendor_id = None
                    avp._data = stream[index+8:index+boundary]
                    avp_header_length = AVP_HEADER_LENGTH

                if len(avp._data) != boundary - avp_header_length:
                        raise AVPParsingError("invalid bytes stream. The "\
                                    "length field value does not correspond "\
                                    "to the AVP length")


            except IndexError as e:
                if e.args[0] == "index out of range":
                    raise AVPParsingError("invalid bytes stream")


            if (boundary % 4) != 0:
                padding = 4 - (boundary % 4)
            else:
                padding = 0

            avp._padding = stream[index+boundary:index+boundary+padding]

            index += boundary + padding

            try:
                _avp_class = loader.get_avp_class_by_avp_code(avp.code)
                avp_object = _avp_class(avp.data)
                avps.append(avp_object)

            except KeyError as e:
                avps.append(avp)

        return avps


    def set_vendor_id_bit(self, state):
        if not isinstance(state, bool):
            raise AVPAttributeValueError("V-bit is of type Boolean")

        if state:
            if self.is_vendor_id():
                raise AVPAttributeValueError("V-bit was already set")

            flags = (self.get_flags() | 
                        self.get_flags_bit(DiameterAVP.flag_vendor_id_bit))

        else:
            if not self.is_vendor_id():
                raise AVPAttributeValueError("V-bit was already unset")

            flags = (self.get_flags() ^ 
                        self.get_flags_bit(DiameterAVP.flag_vendor_id_bit))

        self.flags = convert_to_1_byte(flags)


    def is_vendor_id(self):
        return (self.get_flags() & 
                    self.get_flags_bit(DiameterAVP.flag_vendor_id_bit) != 0)


    def set_mandatory_bit(self, state):
        if not isinstance(state, bool):
            raise AVPAttributeValueError("M-bit is of type Boolean")

        if state:
            if self.is_mandatory():
                raise AVPAttributeValueError("M-bit was already set")

            flags = (self.get_flags() | 
                        self.get_flags_bit(DiameterAVP.flag_mandatory_bit))
        else:
            if not self.is_mandatory():
                raise AVPAttributeValueError("M-bit was already unset")

            flags = (self.get_flags() ^ 
                        self.get_flags_bit(DiameterAVP.flag_mandatory_bit))

        self.flags = convert_to_1_byte(flags)


    def is_mandatory(self):
        return (self.get_flags() & 
                    self.get_flags_bit(DiameterAVP.flag_mandatory_bit) != 0)


    def set_protected_bit(self, state):
        if not isinstance(state, bool):
            raise AVPAttributeValueError("P-bit is of type Boolean")

        if state:
            if self.is_protected():
                raise AVPAttributeValueError("P-bit was already set")

            flags = (self.get_flags() | 
                        self.get_flags_bit(DiameterAVP.flag_protected_bit))
        else:
            if not self.is_protected():
                raise AVPAttributeValueError("P-bit was already unset")

            flags = (self.get_flags() ^ 
                        self.get_flags_bit(DiameterAVP.flag_protected_bit))

        self.flags = convert_to_1_byte(flags)


    def is_protected(self):
        return (self.get_flags() & 
                    self.get_flags_bit(DiameterAVP.flag_protected_bit) != 0)


    def get_code(self):
        return int.from_bytes(self.code, byteorder="big")


    def get_flags(self):
        return int.from_bytes(self.flags, byteorder="big")


    def get_length(self):
        return int.from_bytes(self.length, byteorder="big")


    def get_vendor_id(self):
        if self.vendor_id:
            return int.from_bytes(self.vendor_id, byteorder="big")
        return None


    def get_padding_length(self):
        if self.padding:
            return len(self.padding)
        return None


    def get_flags_bit(self, flag_bit):
        return int.from_bytes(flag_bit, byteorder="big")


    def dump(self):
        stream = self.code + self.flags + self.length
        if self.vendor_id:
            stream += self.vendor_id

        if self.data:
            stream += self.data

        if self.padding:
            stream += self.padding

        return stream


class DiameterHeader(object):
    """Implementation of a Diameter Header. 
    
    Refer to Section 3 of IETF RFC 6733 for details. The constructor has
    input arguments as per Diameter Header fields.

    Provides a general-case interface for create custom and standard Diameter 
    Header.

    WARNING: strongly not recommended passing the `length` input argument. 
    It is used for internal implementation purpose, in order to support the
    `.load()` classmethod. 

    :param version: represents the Version field to indicate Diameter Version.
    :param flags: represents the Command Flags field.
    :param command_code: represents the Command Code field.
    :param application_id: represents the Application-ID field.
    :param hop_by_hop: represents the Hop-by-Hop Identifier field.
    :param end_to_end: represents the End-to-End Identifier field.
    :param length: represents the Message Length field.

    Usage::

        >>> from bromelia.base import DiameterHeader
        >>> header = DiameterHeader()
        >>> header
        <Diameter Header: Unknown [], 0 [Diameter common message]>
    """

    __slots__ = ("_version", "_length", "_flags", "_command_code", 
                    "_application_id", "_hop_by_hop", "_end_to_end")

    flag_request_bit = convert_to_1_byte(0x80)
    flag_proxiable_bit = convert_to_1_byte(0x40)
    flag_error_bit = convert_to_1_byte(0x20)
    flag_retransmitted = convert_to_1_byte(0x10)
    flag_reserved4_bit = convert_to_1_byte(0x08)
    flag_reserved3_bit = convert_to_1_byte(0x04)
    flag_reserved2_bit = convert_to_1_byte(0x02)
    flag_reserved1_bit = convert_to_1_byte(0x01)


    def __init__(self, 
                 version=DIAMETER_VERSION,
                 flags=0,
                 command_code=0,
                 application_id=0,
                 hop_by_hop=0,
                 end_to_end=0,
                 length=20):
                
        self.version = version
        self.length = length
        self.flags = flags
        self.command_code = command_code
        self.application_id = application_id
        self.hop_by_hop = hop_by_hop
        self.end_to_end = end_to_end


    def __repr__(self):
        representations = header_representation(self)
    
        return "<Diameter Header: "\
                "{cmd_code_int} [{cmd_code_str}]"\
                "{flag_representation}, "\
                "{app_id_int} [{app_id_str}]>".format(**representations)


    def __len__(self):
        return self.get_length()


    def __eq__(self, other):
        return self.dump() == other.dump()


    def __bytes__(self):
        return self.dump()


    def copy(self):
        return deepcopy(self)


    @property
    def version(self):
        return self._version


    @version.setter
    def version(self, value):
        if isinstance(value, int) and (value >= 0 and value <= 255):
            self._version = convert_to_1_byte(value)

        elif isinstance(value, bytes) and len(value) == 1:
            self._version = value

        elif isinstance(value, int) and (value < 0 or value > 255):
            raise DiameterHeaderAttributeValueError("version attribute has "\
                                                "1-byte length long")

        elif isinstance(value, bytes) and len(value) != 1:
            raise DiameterHeaderAttributeValueError("version attribute has "\
                                                "1-byte length long")

        elif not isinstance(value, bytes) and not isinstance(value, int):
            raise DiameterHeaderAttributeValueError("invalid version "\
                                                    "attribute value")


    @property
    def length(self):
        return self._length


    @length.setter
    def length(self, value):
        if value is None:
            self._length = value

        elif isinstance(value, int) and (value >= 0 and value <= 16777215):
            self._length = convert_to_3_bytes(value)

        elif isinstance(value, int) and (value < 0 or value > 16777215):
            raise DiameterHeaderAttributeValueError("length attribute "\
                                                "has 3-bytes length long")

        elif isinstance(value, bytes) and len(value) == 3:
            self._length = value

        elif isinstance(value, bytes) and len(value) != 3:
            raise DiameterHeaderAttributeValueError("length attribute "\
                                                "has 3-bytes length long")

        elif not isinstance(value, bytes) and not isinstance(value, int):
            raise DiameterHeaderAttributeValueError("invalid length "\
                                                "attribute value")


    @property
    def flags(self):
        return self._flags


    @flags.setter
    def flags(self, value):
        if isinstance(value, int) and (value >= 0 and value <= 255):
            self._flags = convert_to_1_byte(value)

        elif isinstance(value, bytes) and len(value) == 1:
            self._flags = value

        elif isinstance(value, int) and (value < 0 or value > 255):
            raise DiameterHeaderAttributeValueError("flags attribute has "\
                                                "1-byte length long")

        elif isinstance(value, bytes) and len(value) != 1:
            raise DiameterHeaderAttributeValueError("flags attribute has "\
                                                "1-byte length long")

        elif not isinstance(value, bytes) and not isinstance(value, int):
            raise DiameterHeaderAttributeValueError("invalid flags "\
                                                "attribute value")


    @property
    def command_code(self):
        return self._command_code


    @command_code.setter
    def command_code(self, value):
        if value is None:
            self._command_code = value

        elif isinstance(value, int) and (value >= 0 and value <= 16777215):
            self._command_code = convert_to_3_bytes(value)

        elif isinstance(value, int) and (value < 0 or value > 16777215):
            raise DiameterHeaderAttributeValueError("command_code attribute "\
                                                "has 3-bytes length long")

        elif isinstance(value, bytes) and len(value) == 3:
            self._command_code = value

        elif isinstance(value, bytes) and len(value) != 3:
            raise DiameterHeaderAttributeValueError("command_code attribute "\
                                                "has 3-bytes length long")

        elif not isinstance(value, bytes) and not isinstance(value, int):
            raise DiameterHeaderAttributeValueError("invalid command_code "\
                                                "attribute value")


    @property
    def application_id(self):
        return self._application_id


    @application_id.setter
    def application_id(self, value):
        if value is None:
            self._application_id = value

        elif isinstance(value, int) and (value >= 0 and value <= 4294967295):
            self._application_id = convert_to_4_bytes(value)

        elif isinstance(value, int) and (value < 0 or value > 4294967295):
            raise DiameterHeaderAttributeValueError("application_id "\
                                        "attribute has 4-bytes length long")

        elif isinstance(value, bytes) and len(value) == 4:
            self._application_id = value

        elif isinstance(value, bytes) and len(value) != 4:
            raise DiameterHeaderAttributeValueError("application_id "\
                                        "attribute has 4-bytes length long")

        elif not isinstance(value, bytes) and not isinstance(value, int):
            raise DiameterHeaderAttributeValueError("invalid application_id "\
                                        "attribute value")


    @property
    def hop_by_hop(self):
        return self._hop_by_hop


    @hop_by_hop.setter
    def hop_by_hop(self, value):
        if value is None:
            self._hop_by_hop = value

        elif isinstance(value, int) and (value >= 0 and value <= 4294967295):
            self._hop_by_hop = convert_to_4_bytes(value)

        elif isinstance(value, int) and (value < 0 or value > 4294967295):
            raise DiameterHeaderAttributeValueError("hop_by_hop attribute "\
                                                "has 4-bytes length long")

        elif isinstance(value, bytes) and len(value) == 4:
            self._hop_by_hop = value

        elif isinstance(value, bytes) and len(value) != 4:
            raise DiameterHeaderAttributeValueError("hop_by_hop attribute "\
                                                "has 4-bytes length long")

        elif not isinstance(value, bytes) and not isinstance(value, int):
            raise DiameterHeaderAttributeValueError("invalid hop_by_hop "\
                                                "attribute value")


    @property
    def end_to_end(self):
        return self._end_to_end


    @end_to_end.setter
    def end_to_end(self, value):
        if value is None:
            self._end_to_end = value

        elif isinstance(value, int) and (value >= 0 and value <= 4294967295):
            self._end_to_end = convert_to_4_bytes(value)

        elif isinstance(value, int) and (value < 0 or value > 4294967295):
            raise DiameterHeaderAttributeValueError("end_to_end attribute "\
                                                "has 4-bytes length long")

        elif isinstance(value, bytes) and len(value) == 4:
            self._end_to_end = value

        elif isinstance(value, bytes) and len(value) != 4:
            raise DiameterHeaderAttributeValueError("end_to_end attribute "\
                                                "has 4-bytes length long")

        elif not isinstance(value, bytes) and not isinstance(value, int):
            raise DiameterHeaderAttributeValueError("invalid end_to_end "\
                                                "attribute value")


    def set_request_bit(self, state):
        if not isinstance(state, bool):
            raise DiameterHeaderError("R-bit is of type Boolean")

        if self.is_error():
            raise DiameterHeaderError("R-bit MUST NOT be set when E-bit "\
                                    "is set")

        if state:
            if self.is_request():
                raise DiameterHeaderError("R-bit was already set")

            flags = self.get_flags() | self.get_flags_bit(DiameterHeader.flag_request_bit)
        else:
            if not self.is_request():
                raise DiameterHeaderError("R-bit was already unset")

            flags = self.get_flags() ^ self.get_flags_bit(DiameterHeader.flag_request_bit)
        
        self.flags = convert_to_1_byte(flags)


    def is_request(self):
        return self.get_flags() & self.get_flags_bit(DiameterHeader.flag_request_bit) != 0


    def set_proxiable_bit(self, state):
        if not isinstance(state, bool):
            raise DiameterHeaderError("P-bit is of type Boolean")

        if state:
            if self.is_proxiable():
                raise DiameterHeaderError("P-bit was already set")

            flags = self.get_flags() | self.get_flags_bit(DiameterHeader.flag_proxiable_bit)
        else:
            if not self.is_proxiable():
                raise DiameterHeaderError("P-bit was already unset")

            flags = self.get_flags() ^ self.get_flags_bit(DiameterHeader.flag_proxiable_bit)

        self.flags = convert_to_1_byte(flags)


    def is_proxiable(self):
        return self.get_flags() & self.get_flags_bit(DiameterHeader.flag_proxiable_bit) != 0


    def set_error_bit(self, state):
        if not isinstance(state, bool):
            raise DiameterHeaderError("E-bit is of type Boolean")

        if self.is_request():
            raise DiameterHeaderError("E-bit MUST NOT be set when R-bit "\
                                    "is set")

        if state:
            if self.is_error():
                raise DiameterHeaderError("E-bit was already set")

            flags = self.get_flags() | self.get_flags_bit(DiameterHeader.flag_error_bit)
        else:
            if not self.is_error():
                raise DiameterHeaderError("E-bit was already unset")

            flags = self.get_flags() ^ self.get_flags_bit(DiameterHeader.flag_error_bit)

        self.flags = convert_to_1_byte(flags)


    def is_error(self):
        return self.get_flags() & self.get_flags_bit(DiameterHeader.flag_error_bit) != 0


    def set_retransmitted_bit(self, state):
        if not isinstance(state, bool):
            raise DiameterHeaderError("T-bit is of type Boolean")

        if state:
            if self.is_retransmitted():
                raise DiameterHeaderError("T-bit was already set")

            flags = self.get_flags() | self.get_flags_bit(DiameterHeader.flag_retransmitted)
        else:
            if not self.is_retransmitted():
                raise DiameterHeaderError("T-bit was already unset")

            flags = self.get_flags() ^ self.get_flags_bit(DiameterHeader.flag_retransmitted)

        self.flags = convert_to_1_byte(flags)


    def is_retransmitted(self):
        return self.get_flags() & self.get_flags_bit(DiameterHeader.flag_retransmitted) != 0


    def get_version(self):
        return int.from_bytes(self.version, byteorder="big")


    def get_length(self):
        return int.from_bytes(self.length, byteorder="big")


    def get_flags(self):
        return int.from_bytes(self.flags, byteorder="big")


    def get_command_code(self):
        return int.from_bytes(self.command_code, byteorder="big")


    def get_application_id(self):
        return int.from_bytes(self.application_id, byteorder="big")


    def get_hop_by_hop(self):
        return int.from_bytes(self.hop_by_hop, byteorder="big")


    def get_end_to_end(self):
        return int.from_bytes(self.end_to_end, byteorder="big")


    def get_flags_bit(self, flag_bit):
        return int.from_bytes(flag_bit, byteorder="big")


    def dump(self):
        dump = self.version + self.length + self.flags
        if self.command_code:
            dump += self.command_code
        if self.application_id:
            dump += self.application_id
        if self.hop_by_hop:
            dump += self.hop_by_hop
        if self.end_to_end:
            dump += self.end_to_end
        
        return dump


    @classmethod
    def load(cls, stream):
        version  = convert_to_1_byte(stream[0])
        length = stream[1:4]        
        flags = convert_to_1_byte(stream[4])
        command_code = stream[5:8]
        application_id = stream[8:12]
        hop_by_hop = stream[12:16]
        end_to_end = stream[16:20]

        return cls(version=version, 
                   length=length, 
                   flags=flags, 
                   command_code=command_code, 
                   application_id=application_id,
                   hop_by_hop=hop_by_hop,
                   end_to_end=end_to_end)

    
class DiameterMessage:
    """Implementation of a Diameter Message. 
    
    Refer to Section 3 of IETF RFC 6733 for details. The constructor has
    input arguments represented by DiameterHeader object and a list of 
    DiameterAVP object. Together they define the set of Diameter Message 
    attributes.

    Provides a general-case interface for create custom and standard Diameter 
    Message.

    :param header: the DiameterHeader object which represents the Diameter 
        Header format within a Diameter Message.
    :param avps: the list of DiameterAVP objects, which represents the set of
        available AVPs within a Diameter Message.

    Usage::

        >>> from bromelia.base import DiameterMessage
        >>> message = DiameterMessage()
        >>> message
        <Diameter Message: Unknown [], 0 [Diameter common message], 0 AVP(s)>
    """

    def __init__(self, header=None, avps=None, loaded=False):
        self.header = header
        self.avps = list()
        self._loaded = loaded
        
        if avps is not None:
            if not isinstance(avps, list):
                raise DiameterMessageError("invalid input argument: 'avps'. "\
                                        "It MUST be a list of DiameterAVP "\
                                        "objects")

            for idx, avp in enumerate(avps):
                if not isinstance(avp, DiameterAVP):
                    raise DiameterMessageError("invalid element found in "\
                                            "list argument: 'avps'. The "\
                                            f"element {avp} in position "\
                                            f"{idx} does not represent a "\
                                            "DiameterAVP object")

                self.append(avp)
            self._loaded = False


    def __repr__(self):
        representations = header_representation(self.header)
        representations.update({"num_of_avps": len(self.avps)})
    
        return "<Diameter Message: {cmd_code_int} [{cmd_code_str}]"\
                "{flag_representation}, {app_id_int} [{app_id_str}], "\
                "{num_of_avps} AVP(s)>".format(**representations)


    def __add__(self, other):
        return self.dump() + other.dump()


    def __len__(self):
        return self.get_length()


    def __eq__(self, other):
        return self.dump() == other.dump()


    def __bytes__(self):
        return self.dump()


    def copy(self):
        return deepcopy(self)


    @classmethod
    def convert(cls, msg):
        if not isinstance(msg, DiameterMessage):
            raise DiameterMessageError("invalid message. It MUST be a "\
                                "DiameterMessage subclass object to be "\
                                "converted into DiameterMessage object")
        
        return cls(header=msg.header,
                   avps=msg.avps)


    def append(self, avp):
        if not isinstance(avp, DiameterAVP):
            raise DiameterMessageError("cannot append a data type of "\
                                    f"'{type(avp)}'")

        avp_name = avp_look_up(avp)
        if avp_name == "Unknown":
            avp_name = loader.get_avp_class_name_by_avp_code(avp.code)

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

        if not self._loaded:
            header_length = self.header.get_length() + avp.get_length()

            if avp.get_padding_length():
                header_length += avp.get_padding_length()
            self.header.length = convert_to_3_bytes(header_length)


    def extend(self, avps):
        for avp in avps:
            self.append(avp)


    def has_avp(self, avp_key):
        if not isinstance(avp_key, str):
            raise DiameterMessageError("`avp_key` must be str")

        if not self.avps:
            return False
        elif avp_key in self.__dict__:
            return True
        return False


    def pop(self, avp_key):
        if not self.avps:
            raise DiameterMessageError("`avps` attribute is empty. There is "\
                                    "no DiameterAVP object to be removed")

        item = self.__dict__[avp_key]

        self._avps.remove(item)
        self.__dict__.pop(avp_key, None)

        header_length = self.header.get_length() - item.get_length()
        if item.get_padding_length():
            header_length -= item.get_padding_length()
        self.header.length = convert_to_3_bytes(header_length)


    def update_key(self, old_avp_key, new_avp_key):
        if not self.has_avp(old_avp_key):
            raise DiameterMessageError(f"`{old_avp_key}` key not defined")
            
        if self.has_avp(new_avp_key):
            raise DiameterMessageError(f"`{new_avp_key}` key already defined")

        self.__dict__[new_avp_key] = self.__dict__.pop(old_avp_key)


    def cleanup(self):
        self._avps = list()

        avps_keys = list()
        for avp_key in self.__dict__.keys():
            if "_avp" in avp_key and avp_key != "_avps":
                avps_keys.append(avp_key)
                    
        for avp_key in avps_keys:
            item = self.__dict__[avp_key]

            self.__dict__.pop(avp_key, None)

            header_length = self.header.get_length() - item.get_length()
            if item.get_padding_length():
                header_length -= item.get_padding_length()
            self.header.length = convert_to_3_bytes(header_length)


    @staticmethod
    def load(stream):
        messages = []
        index = 0

        while index < len(stream):
            header_stream = stream[index:index+DIAMETER_HEADER_LENGTH]
            header = DiameterHeader.load(header_stream)

            lower_limit = index + DIAMETER_HEADER_LENGTH
            upper_limit = index + header.get_length()

            avp_stream = stream[lower_limit:upper_limit]
            avps = DiameterAVP.load(avp_stream)

            message = DiameterMessage(header, avps, loaded=True)
            messages.append(message)

            index += header.get_length()

        return messages


    def _load(self, values):
        _kwargs = values.get("kwargs", None)
        if _kwargs:
            values.update(_kwargs)

        values.pop("kwargs", None)
        values.pop("self", None)

        avps_info = values.items()

        kwargs = dict()
        for avp_name, avp_value in avps_info:
            _name = f"{avp_name}_avp"

            if avp_name in self.mandatory and avp_value is None:
                raise DiameterMessageError("missing mandatory AVP "\
                                        f"argument avp_value: '{avp_name}'")

            elif avp_name in self.mandatory and avp_value is not None:
                _value = self.mandatory[avp_name](avp_value)
                self.append(_value)
            
            elif avp_name in self.optionals and avp_value is not None:
                _value = self.optionals[avp_name](avp_value)
                self.append(_value)

            elif avp_name not in self.optionals and avp_value is not None:
                if not isinstance(avp_value, DiameterAVP):
                    raise DiameterMessageError("non-mandatory and "\
                                        "non-optionals AVPs should "\
                                        "include DiameterAVP object "\
                                        "only")
                self.append(avp_value)

            self.__dict__.update(kwargs)

        self.header.length = self.length


    @property
    def header(self):
        return self._header


    @header.setter
    def header(self, value):
        if value is None:
            self._header = DiameterHeader()
        else:
            self._header = value


    @property
    def avps(self):
        return tuple(self._avps)


    @avps.setter
    def avps(self, value):
        if not isinstance(value, list):
            raise DiameterMessageError("only list allowed. Cannot append a "\
                                    f"data type of '{type(avp)}'")
    
        self.cleanup()

        if len(value) == 1:
            self.append(value[0])
        elif len(value) > 1:
            self.extend(value)


    def __getitem__(self, idx):
        return self._avps[idx]


    def __setitem__(self, idx, value):
        self._avps[idx] = value


    @property
    def loaded(self):
        return self._loaded


    @loaded.setter
    def loaded(self, value):
        if not isinstance(value, bool):
            raise DiameterMessageError("only bool allowed")
                
        self._loaded = value            


    #: TO-DO: review it
    def refresh(self):
        real_length = 20
        for avp in self.avps:
            real_length += len(avp)
            padding = avp.get_padding_length()
            if padding:
                real_length += avp.get_padding_length()

        if real_length != self.header.get_length():
            self.header.length = convert_to_3_bytes(real_length)

        
    @property
    def length(self):
        self.refresh()
        return self.header.length


    def get_version(self):
        return int.from_bytes(self.header.version, byteorder="big")


    def get_length(self):
        return int.from_bytes(self.length, byteorder="big")


    def get_flags(self):
        return int.from_bytes(self.header.flags, byteorder="big")


    def get_command_code(self):
        return int.from_bytes(self.header.command_code, byteorder="big")


    def get_application_id(self):
        return int.from_bytes(self.header.application_id, byteorder="big")


    def get_hop_by_hop(self):
        return int.from_bytes(self.header.hop_by_hop, byteorder="big")


    def get_end_to_end(self):
        return int.from_bytes(self.header.end_to_end, byteorder="big")
            

    def get_result(self):
        return int.from_bytes(self.result, byteorder="big")
    

    def set_flag_by_app_id(self, app_id):
        if app_id == DIAMETER_APPLICATION_DEFAULT:
            if self.header.is_proxiable():
                self.header.set_proxiable_bit(False)
        else:
            self.header.set_proxiable_bit(True)

        if isinstance(self, DiameterRequest):
            self.header.set_request_bit(True)

        elif isinstance(self, DiameterAnswer):
            if self.header.is_request():
                self.header.set_request_bit(False)


    def dump(self):
        dump = self.header.dump()
        for avp in self.avps:
            dump += avp.dump()
        return dump


class DiameterRequest(DiameterMessage):
    """Implementation of a Diameter Request.
    
    Refer to Section 3 of IETF RFC 6733 for details. It relies on the 
    DiameterMessage. The difference is that DiameterRequest set 'R-bit' and 
    implements two private methods to calculate the Hop-by-Hop and End-to-End
    fields.

    :param application_id: represents the Application-ID field.
    :param command_code: represents the Command Code field.

    Usage::

        >>> from bromelia.base import DiameterRequest
        >>> request = DiameterRequest()
        >>> request
        <Diameter Message: Unknown [] REQ, 0 [Diameter common message], 0 AVP(s)>
    """

    hop_by_hop_identifiers = list()
    end_to_end_identifiers = list()

    def __init__(self, 
                 version=DIAMETER_VERSION, 
                 command_code=0, 
                 application_id=0,
                 header=None,
                 avps=None):

        if header:
            _header = DiameterHeader(version=header.version,
                                    command_code=header.command_code,
                                    application_id=header.application_id,
                                    hop_by_hop=header.hop_by_hop,
                                    end_to_end=header.end_to_end)
        else:
            hop_by_hop = self.__set_hop_by_hop_identifier()
            end_to_end = self.__set_end_to_end_identifier()

            _header = DiameterHeader(version=version,
                                    command_code=command_code,
                                    application_id=application_id,
                                    hop_by_hop=hop_by_hop,
                                    end_to_end=end_to_end)

        DiameterMessage.__init__(self, _header, avps)
        DiameterMessage.set_flag_by_app_id(self, application_id)        


    def __set_hop_by_hop_identifier(self):
        while True:
            random_identifier = os.urandom(4)
            if random_identifier not in DiameterRequest.hop_by_hop_identifiers:
                DiameterRequest.hop_by_hop_identifiers.append(random_identifier)
                return random_identifier


    def __set_end_to_end_identifier(self):
        while True:
            random_identifier = os.urandom(4)
            if random_identifier not in DiameterRequest.end_to_end_identifiers:
                DiameterRequest.end_to_end_identifiers.append(random_identifier)
                return random_identifier


    @staticmethod
    def convert(msg):
        raise DiameterMessageError("DiameterRequest class does not have "\
                                "this method available for use")


class DiameterAnswer(DiameterMessage):
    """Implementation of a Diameter Answer.
    
    Refer to Section 3 of IETF RFC 6733 for details. It relies on the 
    DiameterMessage. The difference is that DiameterAnswer does not set 
    'R-bit'.

    :param application_id: represents the Application-ID field.
    :param command_code: represents the Command Code field.

    Usage::

        >>> from bromelia.base import DiameterAnswer
        >>> answer = DiameterAnswer()
        >>> answer
        <Diameter Message: Unknown [], 0 [Diameter common message], 0 AVP(s)>
    """

    def __init__(self, 
                 version=DIAMETER_VERSION, 
                 command_code=0, 
                 application_id=0,
                 header=None,
                 avps=None):

        if header:
            _header = DiameterHeader(version=header.version,
                                     command_code=header.command_code,
                                     application_id=header.application_id,
                                     hop_by_hop=header.hop_by_hop,
                                     end_to_end=header.end_to_end)
        else:
            _header = DiameterHeader(version=version,
                                     command_code=command_code, 
                                     application_id=application_id)

        DiameterMessage.__init__(self, _header, avps)
        DiameterMessage.set_flag_by_app_id(self, application_id)


    @staticmethod
    def convert(msg):
        raise DiameterMessageError("DiameterAnswer class does not have "\
                                "this method available for use")


loader = DiameterAvpLoader()
