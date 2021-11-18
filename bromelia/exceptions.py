# -*- coding: utf-8 -*-
"""
    bromelia.exceptions
    ~~~~~~~~~~~~~~~~~~~
    
    This module implements the central Diameter application object. It works
    as per Peer State Machine defined in RFC 6733 in order to establish a 
    Diameter association with another Peer Node.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""


class DiameterApplicationError(BaseException):
    """A Diameter Application error occurred."""
    pass


class DiameterAssociationError(BaseException):
    """A Diameter Association error occurred."""
    pass


class DiameterMessageError(BaseException):
    """A Diameter Message error occurred."""
    pass


class DiameterHeaderError(BaseException):
    """A Diameter Header error occurred."""
    pass


class DiameterAvpError(BaseException):
    """ A Diameter AVP error occurred."""
    pass


class DiameterTypeError(BaseException):
    """ A Diameter Type error occurred """
    pass


class DiameterHeaderAttributeValueError(BaseException):
    """A valid attribute value is required."""
    pass


class AVPAttributeValueError(BaseException):
    """A valid attribute value is required."""
    pass


class AVPOperationError(BaseException):
    """Invalid operation between two DiameterAVP objects"""


class AVPParsingError(BaseException):
    """An invalid AVP byte stream has been found."""
    pass


class ProcessRequestException(BaseException):
    pass


class DataTypeError(BaseException):
    pass


class ParsingDataTypeError(BaseException):
    pass


class InvalidConfigKey(BaseException):
    """Invalid config key found"""


class InvalidConfigValue(BaseException):
    """Invalid config value found"""


class MissingAttributes(KeyError):
    """ Not found attributes for a given class """


class BromeliaException(BaseException):
    """ Something went wrong in Bromelia class """


class DiameterInvalidAvpValue(BaseException):
    """ Refer to DIAMETER_INVALID_AVP_VALUE constant """

    
class DiameterMissingAvp(BaseException):
    """ Refer to DIAMETER_MISSING_AVP constant"""
