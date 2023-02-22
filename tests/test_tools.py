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
from bromelia.tools import *

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
