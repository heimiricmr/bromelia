# -*- coding: utf-8 -*-
"""
    bromelia.utils
    ~~~~~~~~~~~~~~

    Defines utility functions that are consumed by the library.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from collections import namedtuple

from ._internal_utils import convert_to_integer_from_bytes
from .constants import *

FLAG_VENDOR_BIT = FLAG_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED


def is_result_code_family_1xxx(result_code):
    if result_code >= 1001 and result_code < 2000:
        return True
    else:
        return False


def is_result_code_family_2xxx(result_code):
    if result_code >= 2001 and result_code < 3000:
        return True
    else:
        return False


def is_result_code_family_3xxx(result_code):
    if result_code >= 3001 and result_code < 4000:
        return True
    else:
        return False


def is_result_code_family_4xxx(result_code):
    if result_code >= 4001 and result_code < 5000:
        return True
    else:
        return False


def is_result_code_family_5xxx(result_code):
    if result_code >= 5001 and result_code < 6000:
        return True
    else:
        return False


def is_vendor_id(flag):
    return (convert_to_integer_from_bytes(flag) & 
            convert_to_integer_from_bytes(FLAG_VENDOR_BIT) != 0)


def is_base_request(msg):
    if is_cer_message(msg):
        return True

    if is_dwr_message(msg):
        return True

    if is_dpr_message(msg):
        return True


def is_base_answer(msg):
    if is_cea_message(msg):
        return True

    if is_dwa_message(msg):
        return True

    if is_dpa_message(msg):
        return True


def is_dwr_message(msg):
    if (msg.header.is_request() 
            and msg.header.command_code == DEVICE_WATCHDOG_MESSAGE):
        return True
    return False


def is_dwa_message(msg):
    if (not msg.header.is_request() 
            and msg.header.command_code == DEVICE_WATCHDOG_MESSAGE):
        return True
    return False    


def is_dpr_message(msg):
    if (msg.header.is_request() 
            and msg.header.command_code == DISCONNECT_PEER_MESSAGE):
        return True
    return False


def is_dpa_message(msg):
    if (not msg.header.is_request() 
            and msg.header.command_code == DISCONNECT_PEER_MESSAGE):
        return True
    return False


def is_cer_message(msg):
    if (msg.header.is_request() 
            and msg.header.command_code == CAPABILITIES_EXCHANGE_MESSAGE):
        return True
    return False


def is_cea_message(msg):
    if (not msg.header.is_request() 
            and msg.header.command_code == CAPABILITIES_EXCHANGE_MESSAGE):
        return True
    return False


def is_answer_message(msg):
    if (not msg.header.is_request() or 
            (not msg.header.is_request() and msg.header.is_proxiable())):
        return True
    return False


def is_request_message(msg):
    if (msg.header.is_request() or 
            (msg.header.is_request() and msg.header.is_proxiable())):
        return True
    return False


def is_client_mode(association):
    if association.connection.mode == DIAMETER_AGENT_CLIENT_MODE:
        return True
    return False


def is_server_mode(association):
    if association.connection.mode == DIAMETER_AGENT_SERVER_MODE:
        return True
    return False


def is_1xxx_informational(answer):
    if answer.has_avp("result_code_avp"):
        code = answer.result_code_avp.data
        return bytes([m & n for m, n in zip(DIAMETER_ERROR_1XXX, code)]) == DIAMETER_ERROR_1XXX


def is_2xxx_success(answer):
    if answer.has_avp("result_code_avp"):
        code = answer.result_code_avp.data
        return bytes([m & n for m, n in zip(DIAMETER_ERROR_2XXX, code)]) == DIAMETER_ERROR_2XXX


def is_3xxx_failure(answer):
    if answer.has_avp("result_code_avp"):
        code = answer.result_code_avp.data
        return bytes([m & n for m, n in zip(DIAMETER_ERROR_3XXX, code)]) == DIAMETER_ERROR_3XXX


def is_4xxx_failure(answer):
    if answer.has_avp("result_code_avp"):
        code = answer.result_code_avp.data
        return bytes([m & n for m, n in zip(DIAMETER_ERROR_4XXX, code)]) == DIAMETER_ERROR_4XXX


def is_5xxx_failure(answer):
    if answer.has_avp("result_code_avp"):
        code = answer.result_code_avp.data
        return bytes([m & n for m, n in zip(DIAMETER_ERROR_5XXX, code)]) == DIAMETER_ERROR_5XXX


def is_result_code_error(answer):
    if answer.has_avp("result_code_avp"):
        if answer.header.is_error():
            return True
        return False
