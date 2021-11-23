# -*- coding: utf-8 -*-
"""
    bromelia.constants.result_codes
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains list of Diameter Result Codes defined in IETF RFC 6733.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""


#: List of DIAMETER Family Codes.

DIAMETER_ERROR_1XXX = bytes.fromhex("000003e8")                 #: 1xxx
DIAMETER_ERROR_2XXX = bytes.fromhex("000007d0")                 #: 2xxx
DIAMETER_ERROR_3XXX = bytes.fromhex("00000bb8")                 #: 3xxx
DIAMETER_ERROR_4XXX = bytes.fromhex("00000fa0")                 #: 4xxx
DIAMETER_ERROR_5XXX = bytes.fromhex("00001388")                 #: 5xxx

#: Informational Result-Codes.
DIAMETER_MULTI_ROUND_AUTH = bytes.fromhex("000003e9")           #: 1001 - Subsequent messages triggered by client shall also used in Authentication and to get access of required resources. Generally used in Diameter NAS.

#: Success Result-Codes.
DIAMETER_SUCCESS = bytes.fromhex("000007d1")                    #: 2001 - Request processed successfully.
DIAMETER_LIMITED_SUCCESS = bytes.fromhex("000007d2")            #: 2002 - Request is processed but some more processing is required by Server to provide access to user.

#: Protocol Errors [E-bit set].
DIAMETER_COMMAND_UNSUPPORTED = bytes.fromhex("00000bb9")        #: 3001 - Server returns it if Diameter Command-Code is un-recognized by server.
DIAMETER_UNABLE_TO_DELIVER = bytes.fromhex("00000bba")          #: 3002 - Message can’t be delivered because there is no Host with Diameter URI present in Destination-Host AVP in associated Realm.
DIAMETER_REALM_NOT_SERVED = bytes.fromhex("00000bbb")           #: 3003 - Intended Realm is not recognized.
DIAMETER_TOO_BUSY = bytes.fromhex("00000bbc")                   #: 3004 - Shall return by server only when server unable to provide requested service, where all the pre-requisites are also met. Client should also send the request to alternate peer.
DIAMETER_LOOP_DETECTED = bytes.fromhex("00000bbd")              #: 3005
DIAMETER_REDIRECT_INDICATION = bytes.fromhex("00000bbe")        #: 3006 - In Response from Redirect Agent.
DIAMETER_APPLICATION_UNSUPPORTED = bytes.fromhex("00000bbf")    #: 3007
DIAMETER_INVALID_HDR_BITS = bytes.fromhex("00000bc0")           #: 3008 - It is sent when a request is received with invalid bits combination for considered command-code in DIAMETER Header structure. E.g. Marking Proxy-Bit in CER message.
DIAMETER_INVALID_AVP_BITS = bytes.fromhex("00000bc1")           #: 3009 - It is sent when a request is received with invalid flag bits in an AVP.
DIAMETER_UNKNOWN_PEER = bytes.fromhex("00000bc2")               #: 3010 - A DIAMETER server can be configured whether it shall accept DIAMETER connection from all nodes or only from specific nodes. If it is configured to accept connection from specific nodes and receives CER from message from any node other than specified. Here Server shall send considered error.

#: Transient Failures [Could not satisfy request at this moment].
DIAMETER_AUTHENTICATION_REJECTED = bytes.fromhex("00000fa1")    #: 4001 - Returned by Server, most likely because of invalid password.
DIAMETER_OUT_OF_SPACE = bytes.fromhex("00000fa2")               #: 4002 - Returned by node, when it receives accounting information but unable to store it because of lack of memory.
DIAMETER_ELECTION_LOST = bytes.fromhex("00000fa3")              #: 4003 - Peer determines that it has lost election by comparing Origin-Host value received in CER with its own DIAMETER IDENTITY and found that received DIAMETER IDENTITY is higher.

#: Permanent Failures [To inform peer, request is failed, shouldn’t be attempted again].
DIAMETER_AVP_UNSUPPORTED = bytes.fromhex("00001389")            #: 5001 - AVP marked with Mandatory Bit, but peer does not support it.
DIAMETER_UNKNOWN_SESSION_ID = bytes.fromhex("0000138a")         #: 5002
DIAMETER_AUTHORIZATION_REJECTED = bytes.fromhex("0000138b")     #: 5003 - User can not be authorized. E.g. Comes in AIA on s6a interface.
DIAMETER_INVALID_AVP_VALUE = bytes.fromhex("0000138c")          #: 5004
DIAMETER_MISSING_AVP = bytes.fromhex("0000138d")                #: 5005 - Mandatory AVP in request message is missing.
DIAMETER_RESOURCES_EXCEEDED = bytes.fromhex("0000138e")         #: 5006 - A request was received that cannot be authorized because the user has already expended allowed resources. An example of this error condition is a user that is restricted to one dial-up PPP port, attempts to establish a second PPP connection.
DIAMETER_CONTRADICTING_AVPS = bytes.fromhex("0000138f")         #: 5007 - Server has identified that AVPs are present that are contradictory to each other.
DIAMETER_AVP_NOT_ALLOWED = bytes.fromhex("00001390")            #: 5008 - Message is received by node (Server) that contain AVP must not be present.
DIAMETER_AVP_OCCURS_TOO_MANY_TIMES = bytes.fromhex("00001391")  #: 5009 - If message contains the a AVP number of times that exceeds permitted occurrence of AVP in message definition.
DIAMETER_NO_COMMON_APPLICATION = bytes.fromhex("00001392")      #: 5010 - In response of CER if no common application supported between the peers.
DIAMETER_UNSUPPORTED_VERSION = bytes.fromhex("00001393")        #: 5011 - Self explanatory.
DIAMETER_UNABLE_TO_COMPLY = bytes.fromhex("00001394")           #: 5012 - Message rejected because of unspecified reasons.
DIAMETER_INVALID_BIT_IN_HEADER = bytes.fromhex("00001395")      #: 5013 - When an unrecognized bit in the Diameter header is set to one.
DIAMETER_INVALID_AVP_LENGTH = bytes.fromhex("00001396")         #: 5014 - Self explanatory. 
DIAMETER_INVALID_MESSAGE_LENGTH = bytes.fromhex("00001397")     #: 5015 - Self explanatory.
DIAMETER_INVALID_AVP_BIT_COMBO = bytes.fromhex("00001398")      #: 5016 - E.g. Marking AVP to Mandatory while message definition doesn’t say so.
DIAMETER_NO_COMMON_SECURITY = bytes.fromhex("00001399")         #: 5017 - In response of CER if no common security mechanism supported between the peers.
