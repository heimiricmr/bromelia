# -*- coding: utf-8 -*-
"""
    test.test_tools
    ~~~~~~~~~~~~~~~

    This module contains the Bromelia tools unittests.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.constants import *
from bromelia.lib.etsi_3gpp_s6a import AIA, CLA, NOA, PUA, ULA
from bromelia.tools import (
    create_authentication_data_unavailable_response,
    create_rat_not_allowed_response,
    create_realm_not_served_response,
    create_roaming_not_allowed_response,
    create_invalid_avp_value_response,
    create_missing_avp_response,
    create_success_response,
    create_unknown_eps_subscription_response,
    create_unknown_serving_node_response,
    create_user_unknown_response
)


class TestCreateMissingAvpResponse(unittest.TestCase):
    def test__create_missing_avp_response__1__s6a_aia(self):
        #: Create a AIA message object with Error-Message AVP due missing AVP error
        r = create_missing_avp_response(
            proxy_response=AIA,
            msg="User-Name AVP not found",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, AUTHENTICATION_INFORMATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_MISSING_AVP
        self.assertEqual(r.result_code_avp.data, DIAMETER_MISSING_AVP)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"User-Name AVP not found")

    def test__create_missing_avp_response__2__s6a_cla(self):
        #: Create a CLA message object with Error-Message AVP due missing AVP error
        r = create_missing_avp_response(
            proxy_response=CLA,
            msg="User-Name AVP not found",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, CANCEL_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_MISSING_AVP
        self.assertEqual(r.result_code_avp.data, DIAMETER_MISSING_AVP)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"User-Name AVP not found")

    def test__create_missing_avp_response__3__s6a_noa(self):
        #: Create a NOA message object with Error-Message AVP due missing AVP error
        r = create_missing_avp_response(
            proxy_response=NOA,
            msg="User-Name AVP not found",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, NOTIFY_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_MISSING_AVP
        self.assertEqual(r.result_code_avp.data, DIAMETER_MISSING_AVP)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"User-Name AVP not found")

    def test__create_missing_avp_response__4__s6a_pua(self):
        #: Create a PUA message object with Error-Message AVP due missing AVP error
        r = create_missing_avp_response(
            proxy_response=PUA,
            msg="User-Name AVP not found",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, PURGE_UE_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_MISSING_AVP
        self.assertEqual(r.result_code_avp.data, DIAMETER_MISSING_AVP)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"User-Name AVP not found")

    def test__create_missing_avp_response__5__s6a_ula(self):
        #: Create a ULA message object with Error-Message AVP due missing AVP error
        r = create_missing_avp_response(
            proxy_response=ULA,
            msg="User-Name AVP not found",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, UPDATE_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_MISSING_AVP
        self.assertEqual(r.result_code_avp.data, DIAMETER_MISSING_AVP)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"User-Name AVP not found")


class TestCreateInvalidAvpValueResponse(unittest.TestCase):
    def test__create_invalid_avp_value_response__1__s6a_aia(self):
        #: Create a AIA message object with Error-Message AVP due invalid AVP error
        r = create_invalid_avp_value_response(
            proxy_response=AIA,
            msg="User-Name AVP has invalid value",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, AUTHENTICATION_INFORMATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_INVALID_AVP_VALUE
        self.assertEqual(r.result_code_avp.data, DIAMETER_INVALID_AVP_VALUE)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"User-Name AVP has invalid value")

    def test__create_invalid_avp_value_response__2__s6a_cla(self):
        #: Create a CLA message object with Error-Message AVP due invalid AVP error
        r = create_invalid_avp_value_response(
            proxy_response=CLA,
            msg="User-Name AVP has invalid value",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, CANCEL_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_INVALID_AVP_VALUE
        self.assertEqual(r.result_code_avp.data, DIAMETER_INVALID_AVP_VALUE)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"User-Name AVP has invalid value")

    def test__create_invalid_avp_value_response__3__s6a_noa(self):
        #: Create a NOA message object with Error-Message AVP due invalid AVP error
        r = create_invalid_avp_value_response(
            proxy_response=NOA,
            msg="User-Name AVP has invalid value",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, NOTIFY_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_INVALID_AVP_VALUE
        self.assertEqual(r.result_code_avp.data, DIAMETER_INVALID_AVP_VALUE)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"User-Name AVP has invalid value")

    def test__create_invalid_avp_value_response__4__s6a_pua(self):
        #: Create a PUA message object with Error-Message AVP due invalid AVP error
        r = create_invalid_avp_value_response(
            proxy_response=PUA,
            msg="User-Name AVP has invalid value",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, PURGE_UE_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_INVALID_AVP_VALUE
        self.assertEqual(r.result_code_avp.data, DIAMETER_INVALID_AVP_VALUE)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"User-Name AVP has invalid value")

    def test__create_invalid_avp_value_response__5__s6a_ula(self):
        #: Create a ULA message object with Error-Message AVP due invalid AVP error
        r = create_invalid_avp_value_response(
            proxy_response=ULA,
            msg="User-Name AVP has invalid value",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, UPDATE_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_INVALID_AVP_VALUE
        self.assertEqual(r.result_code_avp.data, DIAMETER_INVALID_AVP_VALUE)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"User-Name AVP has invalid value")


class TestCreateAuthenticationDataUnavailableResponse(unittest.TestCase):
    def test__create_authentication_data_unavailable_response__1__s6a_aia(self):
        #: Create a AIA message object with Error-Message AVP
        r = create_authentication_data_unavailable_response(
            proxy_response=AIA,
            msg="Too much vectors requested in Number-Of-Requested-Vectors AVP",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, AUTHENTICATION_INFORMATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE
        self.assertEqual(r.result_code_avp.data, DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"Too much vectors requested in Number-Of-Requested-Vectors AVP")

    def test__create_authentication_data_unavailable_response__2__s6a_cla(self):
        #: Create a CLA message object with Error-Message AVP
        r = create_authentication_data_unavailable_response(
            proxy_response=CLA,
            msg="Too much vectors requested in Number-Of-Requested-Vectors AVP",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, CANCEL_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE
        self.assertEqual(r.result_code_avp.data, DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"Too much vectors requested in Number-Of-Requested-Vectors AVP")

    def test__create_authentication_data_unavailable_response__3__s6a_noa(self):
        #: Create a NOA message object with Error-Message AVP
        r = create_authentication_data_unavailable_response(
            proxy_response=NOA,
            msg="Too much vectors requested in Number-Of-Requested-Vectors AVP",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, NOTIFY_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE
        self.assertEqual(r.result_code_avp.data, DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"Too much vectors requested in Number-Of-Requested-Vectors AVP")

    def test__create_authentication_data_unavailable_response__4__s6a_pua(self):
        #: Create a PUA message object with Error-Message AVP
        r = create_authentication_data_unavailable_response(
            proxy_response=PUA,
            msg="Too much vectors requested in Number-Of-Requested-Vectors AVP",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, PURGE_UE_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE
        self.assertEqual(r.result_code_avp.data, DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"Too much vectors requested in Number-Of-Requested-Vectors AVP")

    def test__create_authentication_data_unavailable_response__5__s6a_ula(self):
        #: Create a ULA message object with Error-Message AVP
        r = create_authentication_data_unavailable_response(
            proxy_response=ULA,
            msg="Too much vectors requested in Number-Of-Requested-Vectors AVP",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, UPDATE_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE
        self.assertEqual(r.result_code_avp.data, DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"Too much vectors requested in Number-Of-Requested-Vectors AVP")


class TestCreateUserUnknownResponse(unittest.TestCase):
    def test__create_user_unknown_response__1__s6a_aia(self):
        #: Create a AIA message object with Error-Message AVP
        r = create_user_unknown_response(
            proxy_response=AIA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, AUTHENTICATION_INFORMATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_USER_UNKNOWN
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_USER_UNKNOWN)

    def test__create_user_unknown_response__2__s6a_cla(self):
        #: Create a CLA message object with Error-Message AVP
        r = create_user_unknown_response(
            proxy_response=CLA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, CANCEL_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_USER_UNKNOWN
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_USER_UNKNOWN)

    def test__create_user_unknown_response__3__s6a_noa(self):
        #: Create a NOA message object with Error-Message AVP
        r = create_user_unknown_response(
            proxy_response=NOA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, NOTIFY_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_USER_UNKNOWN
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_USER_UNKNOWN)

    def test__create_user_unknown_response__4__s6a_pua(self):
        #: Create a PUA message object with Error-Message AVP
        r = create_user_unknown_response(
            proxy_response=PUA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, PURGE_UE_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_USER_UNKNOWN
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_USER_UNKNOWN)

    def test__create_user_unknown_response__5__s6a_ula(self):
        #: Create a ULA message object with Error-Message AVP
        r = create_user_unknown_response(
            proxy_response=ULA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, UPDATE_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_USER_UNKNOWN
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_USER_UNKNOWN)


class TestCreateUnknownServingNodeResponse(unittest.TestCase):
    def test__create_unknown_serving_node_response__1__s6a_aia(self):
        #: Create a AIA message object with Error-Message AVP
        r = create_unknown_serving_node_response(
            proxy_response=AIA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, AUTHENTICATION_INFORMATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_UNKOWN_SERVING_NODE
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_UNKOWN_SERVING_NODE)

    def test__create_unknown_serving_node_response__2__s6a_cla(self):
        #: Create a CLA message object with Error-Message AVP
        r = create_unknown_serving_node_response(
            proxy_response=CLA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, CANCEL_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_UNKOWN_SERVING_NODE
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_UNKOWN_SERVING_NODE)

    def test__create_unknown_serving_node_response__3__s6a_noa(self):
        #: Create a NOA message object with Error-Message AVP
        r = create_unknown_serving_node_response(
            proxy_response=NOA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, NOTIFY_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_UNKOWN_SERVING_NODE
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_UNKOWN_SERVING_NODE)

    def test__create_unknown_serving_node_response__4__s6a_pua(self):
        #: Create a PUA message object with Error-Message AVP
        r = create_unknown_serving_node_response(
            proxy_response=PUA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, PURGE_UE_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_UNKOWN_SERVING_NODE
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_UNKOWN_SERVING_NODE)

    def test__create_unknown_serving_node_response__5__s6a_ula(self):
        #: Create a ULA message object with Error-Message AVP
        r = create_unknown_serving_node_response(
            proxy_response=ULA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, UPDATE_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_UNKOWN_SERVING_NODE
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_UNKOWN_SERVING_NODE)


class TestCreateRatNotAllowedResponse(unittest.TestCase):
    def test__create_rat_not_allowed_response__1__s6a_aia(self):
        #: Create a AIA message object with Error-Message AVP
        r = create_rat_not_allowed_response(
            proxy_response=AIA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, AUTHENTICATION_INFORMATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_RAT_NOT_ALLOWED
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_RAT_NOT_ALLOWED)

    def test__create_rat_not_allowed_response__2__s6a_cla(self):
        #: Create a CLA message object with Error-Message AVP
        r = create_rat_not_allowed_response(
            proxy_response=CLA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, CANCEL_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_RAT_NOT_ALLOWED
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_RAT_NOT_ALLOWED)

    def test__create_rat_not_allowed_response__3__s6a_noa(self):
        #: Create a NOA message object with Error-Message AVP
        r = create_rat_not_allowed_response(
            proxy_response=NOA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, NOTIFY_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_RAT_NOT_ALLOWED
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_RAT_NOT_ALLOWED)

    def test__create_rat_not_allowed_response__4__s6a_pua(self):
        #: Create a PUA message object with Error-Message AVP
        r = create_rat_not_allowed_response(
            proxy_response=PUA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, PURGE_UE_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_RAT_NOT_ALLOWED
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_RAT_NOT_ALLOWED)

    def test__create_rat_not_allowed_response__5__s6a_ula(self):
        #: Create a ULA message object with Error-Message AVP
        r = create_rat_not_allowed_response(
            proxy_response=ULA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, UPDATE_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_RAT_NOT_ALLOWED
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_RAT_NOT_ALLOWED)


class TestCreateRoamingNotAllowedResponse(unittest.TestCase):
    def test__create_roaming_not_allowed_response__1__s6a_aia(self):
        #: Create a AIA message object with Error-Message AVP
        r = create_roaming_not_allowed_response(
            proxy_response=AIA,
            msg=ERROR_DIAGNOSTIC_ODB_ALL_APN
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, AUTHENTICATION_INFORMATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_ROAMING_NOT_ALLOWED
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_ROAMING_NOT_ALLOWED)

        #: Check if Error-Diagnostic AVP has been included
        self.assertEqual(r.error_diagnostic_avp.data, ERROR_DIAGNOSTIC_ODB_ALL_APN)

    def test__create_roaming_not_allowed_response__5__s6a_ula(self):
        #: Create a ULA message object with Error-Message AVP
        r = create_roaming_not_allowed_response(
            proxy_response=ULA,
            msg=ERROR_DIAGNOSTIC_ODB_ALL_APN
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, UPDATE_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_ROAMING_NOT_ALLOWED
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_ROAMING_NOT_ALLOWED)

        #: Check if Error-Diagnostic AVP has been included
        self.assertEqual(r.error_diagnostic_avp.data, ERROR_DIAGNOSTIC_ODB_ALL_APN)


class TestCreateRealmNotServedResponse(unittest.TestCase):
    def test__create_realm_not_served_response__1__s6a_aia(self):
        #: Create a AIA message object with Error-Message AVP due missing AVP error
        r = create_realm_not_served_response(
            proxy_response=AIA,
            msg="Origin-Realm AVP does not comply with 3GPP format: mncMNC.mccMCC.3gppnetwork.org",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, AUTHENTICATION_INFORMATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_REALM_NOT_SERVED
        self.assertEqual(r.result_code_avp.data, DIAMETER_REALM_NOT_SERVED)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"Origin-Realm AVP does not comply with 3GPP format: mncMNC.mccMCC.3gppnetwork.org")

    def test__create_realm_not_served_response__2__s6a_cla(self):
        #: Create a CLA message object with Error-Message AVP due missing AVP error
        r = create_realm_not_served_response(
            proxy_response=CLA,
            msg="Origin-Realm AVP does not comply with 3GPP format: mncMNC.mccMCC.3gppnetwork.org",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, CANCEL_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_REALM_NOT_SERVED
        self.assertEqual(r.result_code_avp.data, DIAMETER_REALM_NOT_SERVED)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"Origin-Realm AVP does not comply with 3GPP format: mncMNC.mccMCC.3gppnetwork.org")

    def test__create_realm_not_served_response__3__s6a_noa(self):
        #: Create a NOA message object with Error-Message AVP due missing AVP error
        r = create_realm_not_served_response(
            proxy_response=NOA,
            msg="Origin-Realm AVP does not comply with 3GPP format: mncMNC.mccMCC.3gppnetwork.org",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, NOTIFY_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_REALM_NOT_SERVED
        self.assertEqual(r.result_code_avp.data, DIAMETER_REALM_NOT_SERVED)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"Origin-Realm AVP does not comply with 3GPP format: mncMNC.mccMCC.3gppnetwork.org")

    def test__create_realm_not_served_response__4__s6a_pua(self):
        #: Create a PUA message object with Error-Message AVP due missing AVP error
        r = create_realm_not_served_response(
            proxy_response=PUA,
            msg="Origin-Realm AVP does not comply with 3GPP format: mncMNC.mccMCC.3gppnetwork.org",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, PURGE_UE_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_REALM_NOT_SERVED
        self.assertEqual(r.result_code_avp.data, DIAMETER_REALM_NOT_SERVED)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"Origin-Realm AVP does not comply with 3GPP format: mncMNC.mccMCC.3gppnetwork.org")

    def test__create_realm_not_served_response__5__s6a_ula(self):
        #: Create a ULA message object with Error-Message AVP due missing AVP error
        r = create_realm_not_served_response(
            proxy_response=ULA,
            msg="Origin-Realm AVP does not comply with 3GPP format: mncMNC.mccMCC.3gppnetwork.org",
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, UPDATE_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_REALM_NOT_SERVED
        self.assertEqual(r.result_code_avp.data, DIAMETER_REALM_NOT_SERVED)

        #: Check if Error-Message AVP has been included with a message
        self.assertEqual(r.error_message_avp.data, b"Origin-Realm AVP does not comply with 3GPP format: mncMNC.mccMCC.3gppnetwork.org")


class TestCreateUnknownEpsSubscriptionResponse(unittest.TestCase):
    def test__create_unknown_eps_subscription_response_1__s6a_aia(self):
        #: Create a AIA message object with Error-Message AVP
        r = create_unknown_eps_subscription_response(
            proxy_response=AIA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, AUTHENTICATION_INFORMATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION)

    def test__create_unknown_eps_subscription_response_2__s6a_cla(self):
        #: Create a CLA message object with Error-Message AVP
        r = create_unknown_eps_subscription_response(
            proxy_response=CLA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, CANCEL_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION)

    def test__create_unknown_eps_subscription_response_3__s6a_noa(self):
        #: Create a NOA message object with Error-Message AVP
        r = create_unknown_eps_subscription_response(
            proxy_response=NOA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, NOTIFY_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION)

    def test__create_unknown_eps_subscription_response_4__s6a_pua(self):
        #: Create a PUA message object with Error-Message AVP
        r = create_unknown_eps_subscription_response(
            proxy_response=PUA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, PURGE_UE_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION)

    def test__create_unknown_eps_subscription_response_5__s6a_ula(self):
        #: Create a ULA message object with Error-Message AVP
        r = create_unknown_eps_subscription_response(
            proxy_response=ULA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, UPDATE_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION
        self.assertEqual(r.experimental_result_avp.experimental_result_code_avp.data, DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION)


class TestCreateSuccessResponse(unittest.TestCase):
    def test__create_success_response__1__s6a_aia(self):
        #: Create a AIA message object with Error-Message AVP due missing AVP error
        r = create_success_response(
            proxy_response=AIA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, AUTHENTICATION_INFORMATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_SUCCESS
        self.assertEqual(r.result_code_avp.data, DIAMETER_SUCCESS)

    def test__create_success_response__2__s6a_cla(self):
        #: Create a CLA message object with Error-Message AVP due missing AVP error
        r = create_success_response(
            proxy_response=CLA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, CANCEL_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_SUCCESS
        self.assertEqual(r.result_code_avp.data, DIAMETER_SUCCESS)

    def test__create_success_response__3__s6a_noa(self):
        #: Create a NOA message object with Error-Message AVP due missing AVP error
        r = create_success_response(
            proxy_response=NOA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, NOTIFY_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_SUCCESS
        self.assertEqual(r.result_code_avp.data, DIAMETER_SUCCESS)

    def test__create_success_response__4__s6a_pua(self):
        #: Create a PUA message object with Error-Message AVP due missing AVP error
        r = create_success_response(
            proxy_response=PUA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, PURGE_UE_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_SUCCESS
        self.assertEqual(r.result_code_avp.data, DIAMETER_SUCCESS)

    def test__create_success_response__5__s6a_ula(self):
        #: Create a ULA message object with Error-Message AVP due missing AVP error
        r = create_success_response(
            proxy_response=ULA,
        )

        #: Check if header fields keep values
        self.assertEqual(r.header.command_code, UPDATE_LOCATION_MESSAGE)
        self.assertEqual(r.header.application_id, DIAMETER_APPLICATION_S6a)

        #: Check if flag header field has turned on error bit
        self.assertEqual(r.header.flags, FLAG_RESPONSE_AND_PROXYABLE_AND_ERROR)

        #: Check if Result-Code AVP is set to DIAMETER_SUCCESS
        self.assertEqual(r.result_code_avp.data, DIAMETER_SUCCESS)
