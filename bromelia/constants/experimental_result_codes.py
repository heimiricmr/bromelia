# -*- coding: utf-8 -*-
"""
    bromelia.constants.experimental_result_codes
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains list of Diameter Experimental Result Codes defined
    in IETF RFC xxxx.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

DIAMETER_FIRST_REGISTRATION = bytes.fromhex("000007d1")                     #: 2001
DIAMETER_SUBSEQUENT_REGISTRATION = bytes.fromhex("000007d2")                #: 2002
DIAMETER_UNREGISTERED_SERVICE = bytes.fromhex("000007d3")                   #: 2003
DIAMETER_SUCCESS_SERVER_NAME_NOT_STORED = bytes.fromhex("000007d1")         #: 2004

DIAMETER_USER_DATA_NOT_AVAILABLE = bytes.fromhex("00001004")                #: 4100
DIAMETER_PRIOR_UPDATE_IN_PROGRESS = bytes.fromhex("00001005")               #: 4101
DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE = bytes.fromhex("00001055")        #: 4181

DIAMETER_ERROR_USER_UNKNOWN = bytes.fromhex("00001389")                     #: 5001
DIAMETER_ERROR_IDENTITIES_DONT_MATCH = bytes.fromhex("0000138a")            #: 5002
DIAMETER_ERROR_IDENTITY_NOT_REGISTERED = bytes.fromhex("0000138b")          #: 5003
DIAMETER_ERROR_ROAMING_NOT_ALLOWED = bytes.fromhex("0000138c")              #: 5004
DIAMETER_ERROR_IDENTITY_ALREADY_REGISTERED = bytes.fromhex("0000138d")      #: 5005
DIAMETER_ERROR_AUTH_SCHEME_NOT_SUPPORTED = bytes.fromhex("0000138e")        #: 5006
DIAMETER_ERROR_IN_ASSIGNMENT_TYPE = bytes.fromhex("0000138f")               #: 5007
DIAMETER_ERROR_TOO_MUCH_DATA = bytes.fromhex("00001390")                    #: 5008
DIAMETER_ERROR_NOT_SUPPORTED_USER_DATA = bytes.fromhex("00001391")          #: 5009
DIAMETER_ERROR_FEATURE_UNSUPPORTED = bytes.fromhex("00001393")              #: 5011
DIAMETER_ERROR_SERVING_NODE_FEATURE_UNSUPPORTED = bytes.fromhex("00001394") #: 5012
DIAMETER_ERROR_USER_DATA_NOT_RECOGNIZED = bytes.fromhex("000013ec")         #: 5100
DIAMETER_ERROR_OPERATION_NOT_ALLOWED = bytes.fromhex("000013ed")            #: 5101
DIAMETER_ERROR_USER_DATA_CANNOT_BE_READ = bytes.fromhex("000013ee")         #: 5102
DIAMETER_ERROR_USER_DATA_CANNOT_BE_MODIFIED = bytes.fromhex("000013ef")     #: 5103
DIAMETER_ERROR_USER_DATA_CANNOT_BE_NOTIFIED = bytes.fromhex("000013f0")     #: 5104
DIAMETER_ERROR_TRANSPARENT_DATA_OUT_OF_SYNC = bytes.fromhex("000013f1")     #: 5105
DIAMETER_ERROR_SUBS_DATA_ABSENT = bytes.fromhex("000013f2")                 #: 5106
DIAMETER_ERROR_NO_SUBSCRIPTION_TO_DATA = bytes.fromhex("000013f3")          #: 5107
DIAMETER_ERROR_DSAI_NOT_AVAILABLE = bytes.fromhex("000013f4")               #: 5108
DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION = bytes.fromhex("0000152c")         #: 5420
DIAMETER_ERROR_RAT_NOT_ALLOWED = bytes.fromhex("0000152d")                  #: 5421
DIAMETER_ERROR_EQUIPMENT_UNKNOWN = bytes.fromhex("0000152e")                #: 5422
DIAMETER_ERROR_UNKOWN_SERVING_NODE = bytes.fromhex("0000152f")              #: 5423
DIAMETER_ERROR_USER_NO_NON_3GPP_SUBSCRIPTION = bytes.fromhex("0000154a")    #: 5450
DIAMETER_ERROR_USER_NO_APN_SUBSCRIPTION = bytes.fromhex("0000154b")         #: 5451
DIAMETER_ERROR_RAT_TYPE_NOT_ALLOWED = bytes.fromhex("0000154c")             #: 5452
