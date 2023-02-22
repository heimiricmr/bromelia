# -*- coding: utf-8 -*-
"""
    bromelia.tools
    ~~~~~~~~~~~~~~

    Defines toolkit functions that facilitate Diameter messages handling.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from .avps import *
from .base import (
    DiameterAVP,
    DiameterAnswer,
    DiameterRequest
)


class ResponseGenerator:
    def __init__(self, request: DiameterRequest, proxy_response: type[DiameterAnswer]):
        self.request = request
        self.proxy_response = proxy_response
        self.kwargs = {}


    def load_avps(self, **kwargs):
        self.kwargs = kwargs


    def missing_avp(self, msg: str = None, avp: DiameterAVP = None):
        return create_missing_avp_response(self.proxy_response, msg, avp, **self.kwargs)


    def invalid_avp_value(self, msg: str = None, avp: DiameterAVP = None):
        return create_invalid_avp_value_response(self.proxy_response, msg, avp, **self.kwargs)


    def user_unknown(self):
        return create_user_unknown_response(self.proxy_response, **self.kwargs)


    def unknown_serving_node(self):
        return create_unknown_serving_node_response(self.proxy_response, **self.kwargs)


    def rat_not_allowed(self):
        return create_rat_not_allowed_response(self.proxy_response, **self.kwargs)


    def roaming_not_allowed(self, msg: str):
        return create_roaming_not_allowed_response(self.proxy_response, msg, **self.kwargs)


    def realm_not_served(self, msg: str):
        return create_realm_not_served_response(self.proxy_response, msg, **self.kwargs)


    def unknown_eps_subscription(self):
        return create_unknown_eps_subscription_response(self.proxy_response)


    def authentication_data_unavailable(self, msg: str = None, avp: DiameterAVP = None):
        return create_authentication_data_unavailable_response(self.proxy_response, msg, avp)


    def success(self, **kwargs):
        return create_success_response(self.proxy_response, **self.kwargs, **kwargs)


def create_experimental_result_data(code: bytes) -> list:
    return [
            ExperimentalResultCodeAVP(code), 
            VendorIdAVP(VENDOR_ID_3GPP)
    ]


def include_error_bit(func):
    def inner(*args, **kwargs):
        r = func(*args, **kwargs)
        r.header.set_error_bit(True)
        return r

    return inner


@include_error_bit
def create_missing_avp_response(proxy_response: type[DiameterAnswer], msg: str = None, avp: DiameterAVP = None, **kwargs):
    if avp is not None:
        return proxy_response(result_code=DIAMETER_MISSING_AVP,
                              failed_avp=[avp],
                              error_message=ErrorMessageAVP(msg),
                              **kwargs)

    return proxy_response(result_code=DIAMETER_MISSING_AVP,
                          error_message=ErrorMessageAVP(msg),
                          **kwargs)


@include_error_bit
def create_invalid_avp_value_response(proxy_response: type[DiameterAnswer], msg: str = None, avp: DiameterAVP = None, **kwargs):
    if avp is not None:
        return proxy_response(result_code=DIAMETER_INVALID_AVP_VALUE,
                              failed_avp=[avp],
                              error_message=ErrorMessageAVP(msg),
                              **kwargs)

    return proxy_response(result_code=DIAMETER_INVALID_AVP_VALUE,
                          error_message=ErrorMessageAVP(msg),
                          **kwargs)


@include_error_bit
def create_user_unknown_response(proxy_response: type[DiameterAnswer], **kwargs):
    return proxy_response(experimental_result=create_experimental_result_data(DIAMETER_ERROR_USER_UNKNOWN),
                          **kwargs)


@include_error_bit
def create_authentication_data_unavailable_response(proxy_response: type[DiameterAnswer], msg: str = None, avp: DiameterAVP = None, **kwargs):
    if avp is not None:
        return proxy_response(result_code=DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE,
                              failed_avp=[avp],
                              error_message=ErrorMessageAVP(msg),
                              **kwargs)

    return proxy_response(result_code=DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE,
                          error_message=ErrorMessageAVP(msg),
                          **kwargs)


@include_error_bit
def create_unknown_serving_node_response(proxy_response: type[DiameterAnswer], **kwargs):
    return proxy_response(experimental_result=create_experimental_result_data(DIAMETER_ERROR_UNKOWN_SERVING_NODE),
                          **kwargs)


@include_error_bit
def create_rat_not_allowed_response(proxy_response: type[DiameterAnswer], **kwargs):
    return proxy_response(experimental_result=create_experimental_result_data(DIAMETER_ERROR_RAT_NOT_ALLOWED),
           **kwargs)


@include_error_bit
def create_roaming_not_allowed_response(proxy_response: type[DiameterAnswer], msg: str, **kwargs):
    return proxy_response(experimental_result=create_experimental_result_data(DIAMETER_ERROR_ROAMING_NOT_ALLOWED),
                          error_diagnostic=msg,
                          **kwargs)


@include_error_bit
def create_realm_not_served_response(proxy_response: type[DiameterAnswer], msg: str, **kwargs):
    return proxy_response(result_code=DIAMETER_REALM_NOT_SERVED,
                          error_message=ErrorMessageAVP(msg),
                          **kwargs)


@include_error_bit
def create_unknown_eps_subscription_response(proxy_response: type[DiameterAnswer], **kwargs):
    return proxy_response(experimental_result=create_experimental_result_data(DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION),
                          **kwargs)


@include_error_bit
def create_success_response(proxy_response: type[DiameterAnswer], **kwargs):
    return proxy_response(result_code=DIAMETER_SUCCESS, **kwargs)
