# -*- coding: utf-8 -*-
"""
    tests.avps.ietf.test_rfc6733
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP unittests defined for IETF RFC 6733.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys
import datetime

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.avps.ietf.rfc6733 import *
from bromelia.exceptions import *


class TestDiameterAVP(unittest.TestCase):
    def test_diameter_avp__load_staticmethod__parsing_user_name_avp_stream(self):
        stream = bytes.fromhex("00000001400000356d792d75736572406e61692e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], UserNameAVP))
        self.assertEqual(avps[0].code, USER_NAME_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 53)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"my-user@nai.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avps[0].get_padding_length(), 3)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 1 [User-Name] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_class_avp_stream(self):
        stream = bytes.fromhex("000000194000000e4f50454e45440000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], ClassAVP))
        self.assertEqual(avps[0].code, CLASS_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 14)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"OPENED")
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 25 [Class] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_session_timeout_avp_stream(self):
        stream = bytes.fromhex("0000001b4000000c00002a2f")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], SessionTimeoutAVP))
        self.assertEqual(avps[0].code, SESSION_TIMEOUT_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, bytes.fromhex("00002a2f"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 27 [Session-Timeout] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_proxy_state_avp_stream(self):
        stream = bytes.fromhex("000000214000000e434c4f5345440000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], ProxyStateAVP))
        self.assertEqual(avps[0].code, PROXY_STATE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 14)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"CLOSED")
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 33 [Proxy-State] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_acct_session_id_avp_stream(self):
        stream = bytes.fromhex("0000002c4000000c00001a4d")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], AcctSessionIdAVP))
        self.assertEqual(avps[0].code, ACCT_SESSION_ID_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, convert_to_4_bytes(6733))
        self.assertEqual(avps[0].get_padding_length(), None)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 44 [Acct-Session-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_acct_multi_session_id_avp_stream(self):
        stream = bytes.fromhex("000000324000003a6d792d6469616d657465722d7365727665722e6d792d6e6574776f726b3b3430333239323b3430333239323b3430333239320000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], AcctMultiSessionIdAVP))
        self.assertEqual(avps[0].code, ACCT_MULTI_SESSION_ID_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 58)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"my-diameter-server.my-network;403292;403292;403292")
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 50 [Acct-Multi-Session-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_event_timestamp_avp_stream(self):
        stream = bytes.fromhex("000000374000000ce357fa5b")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], EventTimestampAVP))
        self.assertEqual(avps[0].code, EVENT_TIMESTAMP_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data.hex(), "e357fa5b")
        self.assertEqual(avps[0].get_padding_length(), None)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 55 [Event-Timestamp] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_acct_interim_interval_avp_stream(self):
        stream = bytes.fromhex("000000554000000c0000012c")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], AcctInterimIntervalAVP))
        self.assertEqual(avps[0].code, ACCT_INTERIM_INTERVAL_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data.hex(), "0000012c")
        self.assertEqual(avps[0].get_padding_length(), None)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 85 [Acct-Interim-Interval] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_host_ip_address_avp_stream(self):
        stream = bytes.fromhex("000001014000000e00010a9f78240000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], HostIpAddressAVP))
        self.assertEqual(avps[0].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 14)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, bytes.fromhex("00010a9f7824"))
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 257 [Host-Ip-Address] MANDATORY>")

        self.assertTrue(avps[0].is_ipv4())
        self.assertFalse(avps[0].is_ipv6())
        self.assertEqual(avps[0].get_ip_address(), "10.159.120.36")

    def test_diameter_avp__load_staticmethod__parsing_auth_application_id_avp_stream(self):
        stream = bytes.fromhex("000001024000000c01000030")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], AuthApplicationIdAVP))
        self.assertEqual(avps[0].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, DIAMETER_APPLICATION_SWm)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 258 [Auth-Application-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_acct_application_id_avp_stream(self):
        stream = bytes.fromhex("000001034000000c01000030")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], AcctApplicationIdAVP))
        self.assertEqual(avps[0].code, ACCT_APPLICATION_ID_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, DIAMETER_APPLICATION_SWm)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 259 [Acct-Application-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_vendor_specific_application_id_avp_stream(self):
        stream = bytes.fromhex("00000104400000200000010a4000000c000028af000001024000000c01000030")

        avps = DiameterAVP.load(stream)

        vendor_specific_application_id_avp = avps[0]
        self.assertTrue(isinstance(vendor_specific_application_id_avp, VendorSpecificApplicationIdAVP))
        self.assertEqual(vendor_specific_application_id_avp.code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertFalse(vendor_specific_application_id_avp.is_vendor_id())
        self.assertTrue(vendor_specific_application_id_avp.is_mandatory())
        self.assertFalse(vendor_specific_application_id_avp.is_protected())
        self.assertEqual(vendor_specific_application_id_avp.get_length(), 32)
        self.assertIsNone(vendor_specific_application_id_avp.vendor_id)
        self.assertEqual(vendor_specific_application_id_avp.data.hex(), "0000010a4000000c000028af000001024000000c01000030")
        self.assertEqual(vendor_specific_application_id_avp.__repr__(), "<Diameter AVP: 260 [Vendor-Specific-Application-Id] MANDATORY>")

        vendor_id_avp = vendor_specific_application_id_avp.avps[0]
        auth_app_id_avp = vendor_specific_application_id_avp.avps[1]

        self.assertTrue(isinstance(vendor_id_avp, VendorIdAVP))
        self.assertEqual(vendor_id_avp.code, VENDOR_ID_AVP_CODE)
        self.assertFalse(vendor_id_avp.is_vendor_id())
        self.assertTrue(vendor_id_avp.is_mandatory())
        self.assertFalse(vendor_id_avp.is_protected())
        self.assertEqual(vendor_id_avp.get_length(), 12)
        self.assertIsNone(vendor_id_avp.vendor_id)
        self.assertEqual(vendor_id_avp.data.hex(), "000028af")
        self.assertEqual(vendor_id_avp.__repr__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")

        self.assertTrue(isinstance(auth_app_id_avp, AuthApplicationIdAVP))
        self.assertEqual(auth_app_id_avp.code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertFalse(auth_app_id_avp.is_vendor_id())
        self.assertTrue(auth_app_id_avp.is_mandatory())
        self.assertFalse(auth_app_id_avp.is_protected())
        self.assertEqual(auth_app_id_avp.get_length(), 12)
        self.assertIsNone(auth_app_id_avp.vendor_id)
        self.assertEqual(auth_app_id_avp.data.hex(), "01000030")
        self.assertEqual(auth_app_id_avp.__repr__(), "<Diameter AVP: 258 [Auth-Application-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_redirect_host_usage_avp_stream(self):
        stream = bytes.fromhex("000001054000000c00000000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], RedirectHostUsageAVP))
        self.assertEqual(avps[0].code, REDIRECT_HOST_USAGE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, REDIRECT_HOST_USAGE_DONT_CACHE)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 261 [Redirect-Host-Usage] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_redirect_max_cache_time_avp_stream(self):
        stream = bytes.fromhex("000001064000000c00002a2f")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], RedirectMaxCacheTimeAVP))
        self.assertEqual(avps[0].code, REDIRECT_MAX_CACHE_TIME_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, convert_to_4_bytes(10799))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 262 [Redirect-Max-Cache-Time] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_session_id_avp_stream(self):
        stream = bytes.fromhex("00000107400000206573323b3430333239323b3430333239323b343033323932")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], SessionIdAVP))
        self.assertEqual(avps[0].code, SESSION_ID_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 32)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"es2;403292;403292;403292")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 263 [Session-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_origin_host_avp_stream(self):
        stream = bytes.fromhex("000001084000000b65733200")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], OriginHostAVP))
        self.assertEqual(avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 11)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"es2")
        self.assertEqual(avps[0].get_padding_length(), 1)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 264 [Origin-Host] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_supported_vendor_id_avp_stream(self):
        stream = bytes.fromhex("000001094000000c000028af")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], SupportedVendorIdAVP))
        self.assertEqual(avps[0].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, VENDOR_ID_3GPP)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 265 [Supported-Vendor-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_vendor_id_avp_stream(self):
        stream = bytes.fromhex("0000010a4000000c00000000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], VendorIdAVP))
        self.assertEqual(avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, bytes.fromhex("00000000"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_firmware_revision_avp_stream(self):
        stream = bytes.fromhex("0000010b0000000c00000001")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], FirmwareRevisionAVP))
        self.assertEqual(avps[0].code, FIRMWARE_REVISION_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, bytes.fromhex("00000001"))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 267 [Firmware-Revision]>")

    def test_diameter_avp__load_staticmethod__parsing_result_code_avp_stream(self):
        stream = bytes.fromhex("0000010c4000000c000007d1")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], ResultCodeAVP))
        self.assertEqual(avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 268 [Result-Code] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_product_name_avp_stream(self):
        stream = bytes.fromhex("0000010d0000001e507974686f6e2062726f6d656c69612076312e302e300000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], ProductNameAVP))
        self.assertEqual(avps[0].code, PRODUCT_NAME_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 30)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"Python bromelia v1.0.0")
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 269 [Product-Name]>")

    def test_diameter_avp__load_staticmethod__parsing_session_binding_avp_stream(self):
        stream = bytes.fromhex("0000010e4000000c00000002")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], SessionBindingAVP))
        self.assertEqual(avps[0].code, SESSION_BINDING_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data.hex(), "00000002")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 270 [Session-Binding] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_session_server_failover_avp_stream(self):
        stream = bytes.fromhex("0000010f4000000c00000000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], SessionServerFailoverAVP))
        self.assertEqual(avps[0].code, SESSION_SERVER_FAILOVER_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, SESSION_SERVER_FAILOVER_REFUSE_SERVICE)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 271 [Session-Server-Failover] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_multi_round_time_out_avp_stream(self):
        stream = bytes.fromhex("000001104000000c00015180")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], MultiRoundTimeOutAVP))
        self.assertEqual(avps[0].code, MULTI_ROUND_TIME_OUT_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data.hex(), "00015180")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 272 [Multi-Round-Time-Out] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_disconnect_cause_avp_stream(self):
        stream = bytes.fromhex("000001114000000c00000002")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], DisconnectCauseAVP))
        self.assertEqual(avps[0].code, DISCONNECT_CAUSE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, DISCONNECT_CAUSE_DO_NOT_WANT_TO_TALK_TO_YOU)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 273 [Disconnect-Cause] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_auth_request_type_avp_stream(self):
        stream = bytes.fromhex("000001124000000c00000001")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], AuthRequestTypeAVP))
        self.assertEqual(avps[0].code, AUTH_REQUEST_TYPE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 274 [Auth-Request-Type] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_auth_grace_period_avp_stream(self):
        stream = bytes.fromhex("000001144000000c00000e10")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], AuthGracePeriodAVP))
        self.assertEqual(avps[0].code, AUTH_GRACE_PERIOD_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data.hex(), "00000e10")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 276 [Auth-Grace-Period] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_auth_session_state_avp_stream(self):
        stream = bytes.fromhex("000001154000000c00000001")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], AuthSessionStateAVP))
        self.assertEqual(avps[0].code, AUTH_SESSION_STATE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, NO_STATE_MAINTAINED)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 277 [Auth-Session-State] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_origin_state_id_avp_stream(self):
        stream = bytes.fromhex("000001164000000c5ae19512")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], OriginStateIdAVP))
        self.assertEqual(avps[0].code, ORIGIN_STATE_ID_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, convert_to_4_bytes(1524733202))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 278 [Origin-State-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_failed_avp_avp_stream(self):
        stream = bytes.fromhex("00000117400000680000011a4000002f68656272612e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000011a4000002f656c64696e2e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f726700")

        avps = DiameterAVP.load(stream)
        failed_avp_avp = avps[0]

        self.assertTrue(isinstance(failed_avp_avp, FailedAvpAVP))
        self.assertEqual(failed_avp_avp.code, FAILED_AVP_AVP_CODE)
        self.assertFalse(failed_avp_avp.is_vendor_id())
        self.assertTrue(failed_avp_avp.is_mandatory())
        self.assertFalse(failed_avp_avp.is_protected())
        self.assertEqual(failed_avp_avp.get_length(), 104)
        self.assertIsNone(failed_avp_avp.vendor_id)
        self.assertEqual(failed_avp_avp.data.hex(), "0000011a4000002f68656272612e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000011a4000002f656c64696e2e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f726700")
        self.assertIsNone(failed_avp_avp.get_padding_length())
        self.assertEqual(failed_avp_avp.__repr__(), "<Diameter AVP: 279 [Failed-Avp] MANDATORY>")

        route_record_avp__1 = failed_avp_avp.avps[0]
        route_record_avp__2 = failed_avp_avp.avps[1]

        self.assertTrue(isinstance(route_record_avp__1, RouteRecordAVP))
        self.assertEqual(route_record_avp__1.code, ROUTE_RECORD_AVP_CODE)
        self.assertFalse(route_record_avp__1.is_vendor_id())
        self.assertTrue(route_record_avp__1.is_mandatory())
        self.assertFalse(route_record_avp__1.is_protected())
        self.assertEqual(route_record_avp__1.get_length(), 47)
        self.assertIsNone(route_record_avp__1.vendor_id)
        self.assertEqual(route_record_avp__1.data, b"hebra.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertTrue(route_record_avp__1.get_padding_length(), 1)
        self.assertEqual(route_record_avp__1.__repr__(), "<Diameter AVP: 282 [Route-Record] MANDATORY>")

        self.assertTrue(isinstance(route_record_avp__2, RouteRecordAVP))
        self.assertEqual(route_record_avp__2.code, ROUTE_RECORD_AVP_CODE)
        self.assertFalse(route_record_avp__2.is_vendor_id())
        self.assertTrue(route_record_avp__2.is_mandatory())
        self.assertFalse(route_record_avp__2.is_protected())
        self.assertEqual(route_record_avp__2.get_length(), 47)
        self.assertIsNone(route_record_avp__2.vendor_id)
        self.assertEqual(route_record_avp__2.data, b"eldin.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertIsNotNone(route_record_avp__2.get_padding_length())
        self.assertEqual(route_record_avp__2.__repr__(), "<Diameter AVP: 282 [Route-Record] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_proxy_host_avp_stream(self):
        stream = bytes.fromhex("0000011840000030687373736d322e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], ProxyHostAVP))
        self.assertEqual(avps[0].code, PROXY_HOST_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 48)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 280 [Proxy-Host] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_error_message_avp_stream(self):
        stream = bytes.fromhex("000001190000001a44524c2d4552522d333030322d3330343a2e0000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], ErrorMessageAVP))
        self.assertEqual(avps[0].code, ERROR_MESSAGE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 26)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"DRL-ERR-3002-304:.")
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 281 [Error-Message]>")

    def test_diameter_avp__load_staticmethod__parsing_route_record_avp_stream(self):
        stream = bytes.fromhex("0000011a400000326a616773616530332e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], RouteRecordAVP))
        self.assertEqual(avps[0].code, ROUTE_RECORD_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 50)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"jagsae03.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avps[0].get_padding_length(), 2)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 282 [Route-Record] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_destination_realm_avp_stream(self):
        stream = bytes.fromhex("0000011b400000296570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], DestinationRealmAVP))
        self.assertEqual(avps[0].code, DESTINATION_REALM_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 41)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avps[0].get_padding_length(), 3)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 283 [Destination-Realm] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_proxy_info_avp_stream(self):
        stream = bytes.fromhex("0000011c400000480000011840000030687373736d322e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000214000000e434c4f5345440000")

        avps = DiameterAVP.load(stream)
        proxy_info_avp = avps[0]

        self.assertTrue(isinstance(proxy_info_avp, ProxyInfoAVP))
        self.assertEqual(proxy_info_avp.code, PROXY_INFO_AVP_CODE)
        self.assertFalse(proxy_info_avp.is_vendor_id())
        self.assertTrue(proxy_info_avp.is_mandatory())
        self.assertFalse(proxy_info_avp.is_protected())
        self.assertEqual(proxy_info_avp.get_length(), 72)
        self.assertIsNone(proxy_info_avp.vendor_id)
        self.assertEqual(proxy_info_avp.data.hex(), "0000011840000030687373736d322e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000214000000e434c4f5345440000")
        self.assertIsNone(proxy_info_avp.get_padding_length())
        self.assertEqual(proxy_info_avp.__repr__(), "<Diameter AVP: 284 [Proxy-Info] MANDATORY>")

        proxy_host_avp = proxy_info_avp.avps[0]
        proxy_state_avp = proxy_info_avp.avps[1]

        self.assertTrue(isinstance(proxy_host_avp, ProxyHostAVP))
        self.assertEqual(proxy_host_avp.code, PROXY_HOST_AVP_CODE)
        self.assertFalse(proxy_host_avp.is_vendor_id())
        self.assertTrue(proxy_host_avp.is_mandatory())
        self.assertFalse(proxy_host_avp.is_protected())
        self.assertEqual(proxy_host_avp.get_length(), 48)
        self.assertIsNone(proxy_host_avp.vendor_id)
        self.assertEqual(proxy_host_avp.data, b"hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertIsNone(proxy_host_avp.get_padding_length())
        self.assertEqual(proxy_host_avp.__repr__(), "<Diameter AVP: 280 [Proxy-Host] MANDATORY>")

        self.assertTrue(isinstance(proxy_state_avp, ProxyStateAVP))
        self.assertEqual(proxy_state_avp.code, PROXY_STATE_AVP_CODE)
        self.assertFalse(proxy_state_avp.is_vendor_id())
        self.assertTrue(proxy_state_avp.is_mandatory())
        self.assertFalse(proxy_state_avp.is_protected())
        self.assertEqual(proxy_state_avp.get_length(), 14)
        self.assertIsNone(proxy_state_avp.vendor_id)
        self.assertEqual(proxy_state_avp.data, b"CLOSED")
        self.assertEqual(proxy_state_avp.get_padding_length(), 2)
        self.assertEqual(proxy_state_avp.__repr__(), "<Diameter AVP: 33 [Proxy-State] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_re_auth_request_type_avp_stream(self):
        stream = bytes.fromhex("0000011d4000000c00000000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], ReAuthRequestTypeAVP))
        self.assertEqual(avps[0].code, RE_AUTH_REQUEST_TYPE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, RE_AUTH_REQUEST_TYPE_AUTHORIZE_ONLY)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 285 [Re-Auth-Request-Type] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_accounting_sub_session_id_avp_stream(self):
        stream = bytes.fromhex("0000011f4000001000000000057c8f9f")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], AccountingSubSessionIdAVP))
        self.assertEqual(avps[0].code, ACCOUNTING_SUB_SESSION_ID_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 16)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data.hex(), "00000000057c8f9f")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 287 [Accounting-Sub-Session-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_authorization_lifetime_avp_stream(self):
        stream = bytes.fromhex("000001234000000c00015180")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], AuthorizationLifetimeAVP))
        self.assertEqual(avps[0].code, AUTHORIZATION_LIFETIME_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data.hex(), "00015180")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 291 [Authorization-Lifetime] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_redirect_host_avp_stream(self):
        stream = bytes.fromhex("000001244000002c6161613a2f2f686f73742e6578616d706c652e636f6d3b7472616e73706f72743d746370")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], RedirectHostAVP))
        self.assertEqual(avps[0].code, REDIRECT_HOST_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 44)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"aaa://host.example.com;transport=tcp")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 292 [Redirect-Host] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_destination_host_avp_stream(self):
        stream = bytes.fromhex("0000012540000030687373736d322e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], DestinationHostAVP))
        self.assertEqual(avps[0].code, DESTINATION_HOST_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 48)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 293 [Destination-Host] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_error_reporting_host_avp_stream(self):
        stream = bytes.fromhex("000001260000002d726a342e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], ErrorReportingHostAVP))
        self.assertEqual(avps[0].code, ERROR_REPORTING_HOST_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 45)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"rj4.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avps[0].get_padding_length(), 3)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 294 [Error-Reporting-Host]>")

    def test_diameter_avp__load_staticmethod__parsing_termination_cause_avp_stream(self):
        stream = bytes.fromhex("000001274000000c00000001")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], TerminationCauseAVP))
        self.assertEqual(avps[0].code, TERMINATION_CAUSE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, DIAMETER_LOGOUT)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 295 [Termination-Cause] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_origin_realm_avp_stream(self):
        stream = bytes.fromhex("000001284000000b65736d00")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], OriginRealmAVP))
        self.assertEqual(avps[0].code, ORIGIN_REALM_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 11)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, b"esm")
        self.assertEqual(avps[0].get_padding_length(), 1)
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 296 [Origin-Realm] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_experimental_result_avp_stream(self):
        stream = bytes.fromhex("00000129000000200000012a4000000c000013940000010a4000000c000028af")

        avps = DiameterAVP.load(stream)

        experimental_result_avp = avps[0]
        self.assertTrue(isinstance(experimental_result_avp, ExperimentalResultAVP))
        self.assertEqual(experimental_result_avp.code, EXPERIMENTAL_RESULT_AVP_CODE)
        self.assertFalse(experimental_result_avp.is_vendor_id())
        self.assertFalse(experimental_result_avp.is_mandatory())
        self.assertFalse(experimental_result_avp.is_protected())
        self.assertEqual(experimental_result_avp.get_length(), 32)
        self.assertIsNone(experimental_result_avp.vendor_id)
        self.assertEqual(experimental_result_avp.data.hex(), "0000012a4000000c000013940000010a4000000c000028af")
        self.assertEqual(experimental_result_avp.__repr__(), "<Diameter AVP: 297 [Experimental-Result]>")

        experimental_result_code_avp = experimental_result_avp.avps[0]
        vendor_id_avp = experimental_result_avp.avps[1]
        
        self.assertTrue(isinstance(experimental_result_code_avp, ExperimentalResultCodeAVP))
        self.assertEqual(experimental_result_code_avp.code, EXPERIMENTAL_RESULT_CODE_AVP_CODE)
        self.assertFalse(experimental_result_code_avp.is_vendor_id())
        self.assertTrue(experimental_result_code_avp.is_mandatory())
        self.assertFalse(experimental_result_code_avp.is_protected())
        self.assertEqual(experimental_result_code_avp.get_length(), 12)
        self.assertIsNone(experimental_result_code_avp.vendor_id)
        self.assertEqual(experimental_result_code_avp.data, DIAMETER_ERROR_SERVING_NODE_FEATURE_UNSUPPORTED)
        self.assertIsNone(experimental_result_code_avp.get_padding_length())
        self.assertEqual(experimental_result_code_avp.__repr__(), "<Diameter AVP: 298 [Experimental-Result-Code] MANDATORY>")

        self.assertTrue(isinstance(vendor_id_avp, VendorIdAVP))
        self.assertEqual(vendor_id_avp.code, VENDOR_ID_AVP_CODE)
        self.assertFalse(vendor_id_avp.is_vendor_id())
        self.assertTrue(vendor_id_avp.is_mandatory())
        self.assertFalse(vendor_id_avp.is_protected())
        self.assertEqual(vendor_id_avp.get_length(), 12)
        self.assertIsNone(vendor_id_avp.vendor_id)
        self.assertEqual(vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertIsNone(vendor_id_avp.get_padding_length())
        self.assertEqual(vendor_id_avp.__repr__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_experimental_result_code_avp_stream(self):
        stream = bytes.fromhex("0000012a4000000c000007d1")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], ExperimentalResultCodeAVP))
        self.assertEqual(avps[0].code, EXPERIMENTAL_RESULT_CODE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, DIAMETER_SUCCESS_SERVER_NAME_NOT_STORED)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 298 [Experimental-Result-Code] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_inband_security_id_avp_stream(self):
        stream = bytes.fromhex("0000012b0000000c00000000")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], InbandSecurityIdAVP))
        self.assertEqual(avps[0].code, INBAND_SECURITY_ID_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, INBAND_SECURITY_ID_NO_SECURITY)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 299 [Inband-Security-Id]>")

    def test_diameter_avp__load_staticmethod__parsing_accounting_record_type_avp_stream(self):
        stream = bytes.fromhex("000001e04000000c00000003")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], AccountingRecordTypeAVP))
        self.assertEqual(avps[0].code, ACCOUNTING_RECORD_TYPE_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, ACCOUNTING_RECORD_TYPE_INTERIM_RECORD)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 480 [Accounting-Record-Type] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_accounting_realtime_required_avp_stream(self):
        stream = bytes.fromhex("000001e34000000c00000003")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], AccountingRealtimeRequiredAVP))
        self.assertEqual(avps[0].code, ACCOUNTING_REALTIME_REQUIRED_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, ACCOUNTING_REALTIME_REQUIRED_GRAND_AND_LOSE)
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 483 [Accounting-Realtime-Required] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_accounting_record_number_avp_stream(self):
        stream = bytes.fromhex("000001e54000000c00000002")

        avps = DiameterAVP.load(stream)

        self.assertTrue(isinstance(avps[0], AccountingRecordNumberAVP))
        self.assertEqual(avps[0].code, ACCOUNTING_RECORD_NUMBER_AVP_CODE)
        self.assertFalse(avps[0].is_vendor_id())
        self.assertTrue(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data.hex(), "00000002")
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 485 [Accounting-Record-Number] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_stream_of_2_different_avps(self):
        stream = bytes.fromhex("0000012b0000000c0000000000000129000000200000012a4000000c000013940000010a4000000c000028af")

        avps = DiameterAVP.load(stream)

        #: First AVP
        inband_security_id_avp = avps[0]
        self.assertTrue(isinstance(inband_security_id_avp, InbandSecurityIdAVP))
        self.assertEqual(inband_security_id_avp.code, INBAND_SECURITY_ID_AVP_CODE)
        self.assertFalse(inband_security_id_avp.is_vendor_id())
        self.assertFalse(inband_security_id_avp.is_mandatory())
        self.assertFalse(inband_security_id_avp.is_protected())
        self.assertEqual(inband_security_id_avp.get_length(), 12)
        self.assertIsNone(inband_security_id_avp.vendor_id)
        self.assertEqual(inband_security_id_avp.data, INBAND_SECURITY_ID_NO_SECURITY)
        self.assertIsNone(inband_security_id_avp.get_padding_length())
        self.assertEqual(inband_security_id_avp.__repr__(), "<Diameter AVP: 299 [Inband-Security-Id]>")

        #: Second AVP
        experimental_result_avp = avps[1]
        self.assertTrue(isinstance(experimental_result_avp, ExperimentalResultAVP))
        self.assertEqual(experimental_result_avp.code, EXPERIMENTAL_RESULT_AVP_CODE)
        self.assertFalse(experimental_result_avp.is_vendor_id())
        self.assertFalse(experimental_result_avp.is_mandatory())
        self.assertFalse(experimental_result_avp.is_protected())
        self.assertEqual(experimental_result_avp.get_length(), 32)
        self.assertIsNone(experimental_result_avp.vendor_id)
        self.assertEqual(experimental_result_avp.data.hex(), "0000012a4000000c000013940000010a4000000c000028af")
        self.assertEqual(experimental_result_avp.__repr__(), "<Diameter AVP: 297 [Experimental-Result]>")

        experimental_result_code_avp = experimental_result_avp.avps[0]
        vendor_id_avp = experimental_result_avp.avps[1]
        
        self.assertTrue(isinstance(experimental_result_code_avp, ExperimentalResultCodeAVP))
        self.assertEqual(experimental_result_code_avp.code, EXPERIMENTAL_RESULT_CODE_AVP_CODE)
        self.assertFalse(experimental_result_code_avp.is_vendor_id())
        self.assertTrue(experimental_result_code_avp.is_mandatory())
        self.assertFalse(experimental_result_code_avp.is_protected())
        self.assertEqual(experimental_result_code_avp.get_length(), 12)
        self.assertIsNone(experimental_result_code_avp.vendor_id)
        self.assertEqual(experimental_result_code_avp.data, DIAMETER_ERROR_SERVING_NODE_FEATURE_UNSUPPORTED)
        self.assertIsNone(experimental_result_code_avp.get_padding_length())
        self.assertEqual(experimental_result_code_avp.__repr__(), "<Diameter AVP: 298 [Experimental-Result-Code] MANDATORY>")

        self.assertTrue(isinstance(vendor_id_avp, VendorIdAVP))
        self.assertEqual(vendor_id_avp.code, VENDOR_ID_AVP_CODE)
        self.assertFalse(vendor_id_avp.is_vendor_id())
        self.assertTrue(vendor_id_avp.is_mandatory())
        self.assertFalse(vendor_id_avp.is_protected())
        self.assertEqual(vendor_id_avp.get_length(), 12)
        self.assertIsNone(vendor_id_avp.vendor_id)
        self.assertEqual(vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertIsNone(vendor_id_avp.get_padding_length())
        self.assertEqual(vendor_id_avp.__repr__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_stream_of_3_different_avps(self):
        stream = bytes.fromhex("000001260000002d726a342e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000001274000000c00000001000001284000000b65736d00")

        avps = DiameterAVP.load(stream)

        #: First AVP
        experimental_result_avp = avps[0]
        self.assertTrue(isinstance(experimental_result_avp, ErrorReportingHostAVP))
        self.assertEqual(experimental_result_avp.code, ERROR_REPORTING_HOST_AVP_CODE)
        self.assertFalse(experimental_result_avp.is_vendor_id())
        self.assertFalse(experimental_result_avp.is_mandatory())
        self.assertFalse(experimental_result_avp.is_protected())
        self.assertEqual(experimental_result_avp.get_length(), 45)
        self.assertIsNone(experimental_result_avp.vendor_id)
        self.assertEqual(experimental_result_avp.data, b"rj4.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(experimental_result_avp.get_padding_length(), 3)
        self.assertEqual(experimental_result_avp.__repr__(), "<Diameter AVP: 294 [Error-Reporting-Host]>")

        #: Second AVP
        termination_cause_avp = avps[1]
        self.assertTrue(isinstance(termination_cause_avp, TerminationCauseAVP))
        self.assertEqual(termination_cause_avp.code, TERMINATION_CAUSE_AVP_CODE)
        self.assertFalse(termination_cause_avp.is_vendor_id())
        self.assertTrue(termination_cause_avp.is_mandatory())
        self.assertFalse(termination_cause_avp.is_protected())
        self.assertEqual(termination_cause_avp.get_length(), 12)
        self.assertIsNone(termination_cause_avp.vendor_id)
        self.assertEqual(termination_cause_avp.data, DIAMETER_LOGOUT)
        self.assertIsNone(termination_cause_avp.get_padding_length())
        self.assertEqual(termination_cause_avp.__repr__(), "<Diameter AVP: 295 [Termination-Cause] MANDATORY>")

        #: Third AVP
        origin_realm_avp = avps[2]
        self.assertTrue(isinstance(origin_realm_avp, OriginRealmAVP))
        self.assertEqual(origin_realm_avp.code, ORIGIN_REALM_AVP_CODE)
        self.assertFalse(origin_realm_avp.is_vendor_id())
        self.assertTrue(origin_realm_avp.is_mandatory())
        self.assertFalse(origin_realm_avp.is_protected())
        self.assertEqual(origin_realm_avp.get_length(), 11)
        self.assertIsNone(origin_realm_avp.vendor_id)
        self.assertEqual(origin_realm_avp.data, b"esm")
        self.assertEqual(origin_realm_avp.get_padding_length(), 1)
        self.assertEqual(origin_realm_avp.__repr__(), "<Diameter AVP: 296 [Origin-Realm] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_stream_of_4_different_avps(self):
        stream = bytes.fromhex("000001260000002d726a342e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000000000012540000030687373736d322e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000011d4000000c00000000000001124000000c00000001")

        avps = DiameterAVP.load(stream)

        #: First AVP
        error_reporting_host_avp = avps[0]
        self.assertTrue(isinstance(error_reporting_host_avp, ErrorReportingHostAVP))
        self.assertEqual(error_reporting_host_avp.code, ERROR_REPORTING_HOST_AVP_CODE)
        self.assertFalse(error_reporting_host_avp.is_vendor_id())
        self.assertFalse(error_reporting_host_avp.is_mandatory())
        self.assertFalse(error_reporting_host_avp.is_protected())
        self.assertEqual(error_reporting_host_avp.get_length(), 45)
        self.assertIsNone(error_reporting_host_avp.vendor_id)
        self.assertEqual(error_reporting_host_avp.data, b"rj4.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(error_reporting_host_avp.get_padding_length(), 3)
        self.assertEqual(error_reporting_host_avp.__repr__(), "<Diameter AVP: 294 [Error-Reporting-Host]>")

        #: Second AVP
        destination_host_avp = avps[1]
        self.assertTrue(isinstance(destination_host_avp, DestinationHostAVP))
        self.assertEqual(destination_host_avp.code, DESTINATION_HOST_AVP_CODE)
        self.assertFalse(destination_host_avp.is_vendor_id())
        self.assertTrue(destination_host_avp.is_mandatory())
        self.assertFalse(destination_host_avp.is_protected())
        self.assertEqual(destination_host_avp.get_length(), 48)
        self.assertIsNone(destination_host_avp.vendor_id)
        self.assertEqual(destination_host_avp.data, b"hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertIsNone(destination_host_avp.get_padding_length())
        self.assertEqual(destination_host_avp.__repr__(), "<Diameter AVP: 293 [Destination-Host] MANDATORY>")

        #: Third AVP
        re_auth_request_type_avp = avps[2]
        self.assertTrue(isinstance(re_auth_request_type_avp, ReAuthRequestTypeAVP))
        self.assertEqual(re_auth_request_type_avp.code, RE_AUTH_REQUEST_TYPE_AVP_CODE)
        self.assertFalse(re_auth_request_type_avp.is_vendor_id())
        self.assertTrue(re_auth_request_type_avp.is_mandatory())
        self.assertFalse(re_auth_request_type_avp.is_protected())
        self.assertEqual(re_auth_request_type_avp.get_length(), 12)
        self.assertIsNone(re_auth_request_type_avp.vendor_id)
        self.assertEqual(re_auth_request_type_avp.data, RE_AUTH_REQUEST_TYPE_AUTHORIZE_ONLY)
        self.assertIsNone(re_auth_request_type_avp.get_padding_length())
        self.assertEqual(re_auth_request_type_avp.__repr__(), "<Diameter AVP: 285 [Re-Auth-Request-Type] MANDATORY>")

        #: Fourth AVP
        auth_request_type_avp = avps[3]
        self.assertTrue(isinstance(auth_request_type_avp, AuthRequestTypeAVP))
        self.assertEqual(auth_request_type_avp.code, AUTH_REQUEST_TYPE_AVP_CODE)
        self.assertFalse(auth_request_type_avp.is_vendor_id())
        self.assertTrue(auth_request_type_avp.is_mandatory())
        self.assertFalse(auth_request_type_avp.is_protected())
        self.assertEqual(auth_request_type_avp.get_length(), 12)
        self.assertIsNone(auth_request_type_avp.vendor_id)
        self.assertEqual(auth_request_type_avp.data, AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY)
        self.assertIsNone(auth_request_type_avp.get_padding_length())
        self.assertEqual(auth_request_type_avp.__repr__(), "<Diameter AVP: 274 [Auth-Request-Type] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_stream_of_2_similar_avps(self):
        stream = bytes.fromhex("0000010c4000000c000007d10000010c4000000c000007d1")

        avps = DiameterAVP.load(stream)

        for avp in avps:
            self.assertTrue(isinstance(avp, ResultCodeAVP))
            self.assertEqual(avp.code, RESULT_CODE_AVP_CODE)
            self.assertFalse(avp.is_vendor_id())
            self.assertTrue(avp.is_mandatory())
            self.assertFalse(avp.is_protected())
            self.assertEqual(avp.get_length(), 12)
            self.assertIsNone(avp.vendor_id)
            self.assertEqual(avp.data, DIAMETER_SUCCESS)
            self.assertIsNone(avp.get_padding_length())
            self.assertEqual(avp.__repr__(), "<Diameter AVP: 268 [Result-Code] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_stream_of_3_similar_avps(self):
        stream = bytes.fromhex("000001094000000c000028af000001094000000c000028af000001094000000c000028af")

        avps = DiameterAVP.load(stream)

        for avp in avps:
            self.assertTrue(isinstance(avp, SupportedVendorIdAVP))
            self.assertEqual(avp.code, SUPPORTED_VENDOR_ID_AVP_CODE)
            self.assertFalse(avp.is_vendor_id())
            self.assertTrue(avp.is_mandatory())
            self.assertFalse(avp.is_protected())
            self.assertEqual(avp.get_length(), 12)
            self.assertIsNone(avp.vendor_id)
            self.assertEqual(avp.data, VENDOR_ID_3GPP)
            self.assertIsNone(avp.get_padding_length())
            self.assertEqual(avp.__repr__(), "<Diameter AVP: 265 [Supported-Vendor-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_stream_of_4_similar_avps(self):
        stream = bytes.fromhex("00000104400000200000010a4000000c000028af000001024000000c0100003000000104400000200000010a4000000c000028af000001024000000c0100003000000104400000200000010a4000000c000028af000001024000000c0100003000000104400000200000010a4000000c000028af000001024000000c01000030")

        avps = DiameterAVP.load(stream)

        for avp in avps:
            vendor_specific_application_id_avp = avp
            self.assertTrue(isinstance(vendor_specific_application_id_avp, VendorSpecificApplicationIdAVP))
            self.assertEqual(vendor_specific_application_id_avp.code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
            self.assertFalse(vendor_specific_application_id_avp.is_vendor_id())
            self.assertTrue(vendor_specific_application_id_avp.is_mandatory())
            self.assertFalse(vendor_specific_application_id_avp.is_protected())
            self.assertEqual(vendor_specific_application_id_avp.get_length(), 32)
            self.assertIsNone(vendor_specific_application_id_avp.vendor_id)
            self.assertEqual(vendor_specific_application_id_avp.data.hex(), "0000010a4000000c000028af000001024000000c01000030")
            self.assertEqual(vendor_specific_application_id_avp.__repr__(), "<Diameter AVP: 260 [Vendor-Specific-Application-Id] MANDATORY>")

            vendor_id_avp = vendor_specific_application_id_avp.avps[0]
            auth_app_id_avp = vendor_specific_application_id_avp.avps[1]

            self.assertTrue(isinstance(vendor_id_avp, VendorIdAVP))
            self.assertEqual(vendor_id_avp.code, VENDOR_ID_AVP_CODE)
            self.assertFalse(vendor_id_avp.is_vendor_id())
            self.assertTrue(vendor_id_avp.is_mandatory())
            self.assertFalse(vendor_id_avp.is_protected())
            self.assertEqual(vendor_id_avp.get_length(), 12)
            self.assertIsNone(vendor_id_avp.vendor_id)
            self.assertEqual(vendor_id_avp.data.hex(), "000028af")
            self.assertEqual(vendor_id_avp.__repr__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")

            self.assertTrue(isinstance(auth_app_id_avp, AuthApplicationIdAVP))
            self.assertEqual(auth_app_id_avp.code, AUTH_APPLICATION_ID_AVP_CODE)
            self.assertFalse(auth_app_id_avp.is_vendor_id())
            self.assertTrue(auth_app_id_avp.is_mandatory())
            self.assertFalse(auth_app_id_avp.is_protected())
            self.assertEqual(auth_app_id_avp.get_length(), 12)
            self.assertIsNone(auth_app_id_avp.vendor_id)
            self.assertEqual(auth_app_id_avp.data.hex(), "01000030")
            self.assertEqual(auth_app_id_avp.__repr__(), "<Diameter AVP: 258 [Auth-Application-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_stream_of_unknown_avp(self):
        stream = bytes.fromhex("000000000000000c00000000")

        avps = DiameterAVP.load(stream)

        self.assertEqual(str(type(avps[0])), "<class 'bromelia.base.DiameterAVP'>")
        self.assertTrue(isinstance(avps[0], DiameterAVP))
        self.assertFalse(avps[0].is_vendor_id())
        self.assertFalse(avps[0].is_mandatory())
        self.assertFalse(avps[0].is_protected())
        self.assertEqual(avps[0].get_length(), 12)
        self.assertIsNone(avps[0].vendor_id)
        self.assertEqual(avps[0].data, convert_to_4_bytes(0))
        self.assertIsNone(avps[0].get_padding_length())
        self.assertEqual(avps[0].__repr__(), "<Diameter AVP: 0 [Unknown]>")

    def test_diameter_avp__load_staticmethod__parsing_stream_of_2_similar_unknown_avps(self):
        stream = bytes.fromhex("000000000000000c00000000000000000000000c00000000")

        avps = DiameterAVP.load(stream)

        for avp in avps:
            self.assertEqual(str(type(avp)), "<class 'bromelia.base.DiameterAVP'>")
            self.assertTrue(isinstance(avp, DiameterAVP))
            self.assertFalse(avp.is_vendor_id())
            self.assertFalse(avp.is_mandatory())
            self.assertFalse(avp.is_protected())
            self.assertEqual(avp.get_length(), 12)
            self.assertIsNone(avp.vendor_id)
            self.assertEqual(avp.data, convert_to_4_bytes(0))
            self.assertIsNone(avp.get_padding_length())
            self.assertEqual(avp.__repr__(), "<Diameter AVP: 0 [Unknown]>")

    def test_diameter_avp__load_staticmethod__parsing_stream_of_3_similar_unknown_avps(self):
        stream = bytes.fromhex("000000000000000c00000000000000000000000c00000000000000000000000c00000000")

        avps = DiameterAVP.load(stream)

        for avp in avps:
            self.assertEqual(str(type(avp)), "<class 'bromelia.base.DiameterAVP'>")
            self.assertTrue(isinstance(avp, DiameterAVP))
            self.assertFalse(avp.is_vendor_id())
            self.assertFalse(avp.is_mandatory())
            self.assertFalse(avp.is_protected())
            self.assertEqual(avp.get_length(), 12)
            self.assertIsNone(avp.vendor_id)
            self.assertEqual(avp.data, convert_to_4_bytes(0))
            self.assertIsNone(avp.get_padding_length())
            self.assertEqual(avp.__repr__(), "<Diameter AVP: 0 [Unknown]>")

    def test_diameter_avp__load_staticmethod__parsing_stream_of_4_similar_unknown_avps(self):
        stream = bytes.fromhex("000000000000000c00000000000000000000000c00000000000000000000000c00000000000000000000000c00000000")

        avps = DiameterAVP.load(stream)

        for avp in avps:
            self.assertEqual(str(type(avp)), "<class 'bromelia.base.DiameterAVP'>")
            self.assertTrue(isinstance(avp, DiameterAVP))
            self.assertFalse(avp.is_vendor_id())
            self.assertFalse(avp.is_mandatory())
            self.assertFalse(avp.is_protected())
            self.assertEqual(avp.get_length(), 12)
            self.assertIsNone(avp.vendor_id)
            self.assertEqual(avp.data, convert_to_4_bytes(0))
            self.assertIsNone(avp.get_padding_length())
            self.assertEqual(avp.__repr__(), "<Diameter AVP: 0 [Unknown]>")

    def test_diameter_avp__load_staticmethod__parsing_stream_of_2_unknown_avps_and_2_known_avps(self):
        stream = bytes.fromhex("000000000000000c00000000000000000000000c00000000000001034000000c01000030000001034000000c01000030")

        avps = DiameterAVP.load(stream)

        #: First AVP
        first_avp = avps[0]
        self.assertEqual(str(type(first_avp)), "<class 'bromelia.base.DiameterAVP'>")
        self.assertTrue(isinstance(first_avp, DiameterAVP))
        self.assertFalse(first_avp.is_vendor_id())
        self.assertFalse(first_avp.is_mandatory())
        self.assertFalse(first_avp.is_protected())
        self.assertEqual(first_avp.get_length(), 12)
        self.assertIsNone(first_avp.vendor_id)
        self.assertEqual(first_avp.data, convert_to_4_bytes(0))
        self.assertIsNone(first_avp.get_padding_length())
        self.assertEqual(first_avp.__repr__(), "<Diameter AVP: 0 [Unknown]>")

        #: Second AVP
        second_avp = avps[1]
        self.assertEqual(str(type(second_avp)), "<class 'bromelia.base.DiameterAVP'>")
        self.assertTrue(isinstance(second_avp, DiameterAVP))
        self.assertFalse(second_avp.is_vendor_id())
        self.assertFalse(second_avp.is_mandatory())
        self.assertFalse(second_avp.is_protected())
        self.assertEqual(second_avp.get_length(), 12)
        self.assertIsNone(second_avp.vendor_id)
        self.assertEqual(second_avp.data, convert_to_4_bytes(0))
        self.assertIsNone(second_avp.get_padding_length())
        self.assertEqual(second_avp.__repr__(), "<Diameter AVP: 0 [Unknown]>")

        #: Third AVP
        acc_application_id_avp__1 = avps[2]
        self.assertTrue(isinstance(acc_application_id_avp__1, AcctApplicationIdAVP))
        self.assertEqual(acc_application_id_avp__1.code, ACCT_APPLICATION_ID_AVP_CODE)
        self.assertFalse(acc_application_id_avp__1.is_vendor_id())
        self.assertTrue(acc_application_id_avp__1.is_mandatory())
        self.assertFalse(acc_application_id_avp__1.is_protected())
        self.assertEqual(acc_application_id_avp__1.get_length(), 12)
        self.assertIsNone(acc_application_id_avp__1.vendor_id)
        self.assertEqual(acc_application_id_avp__1.data, DIAMETER_APPLICATION_SWm)
        self.assertIsNone(acc_application_id_avp__1.get_padding_length())
        self.assertEqual(acc_application_id_avp__1.__repr__(), "<Diameter AVP: 259 [Acct-Application-Id] MANDATORY>")

        #: Fourth AVP
        acc_application_id_avp__2 = avps[3]
        self.assertTrue(isinstance(acc_application_id_avp__2, AcctApplicationIdAVP))
        self.assertEqual(acc_application_id_avp__2.code, ACCT_APPLICATION_ID_AVP_CODE)
        self.assertFalse(acc_application_id_avp__2.is_vendor_id())
        self.assertTrue(acc_application_id_avp__2.is_mandatory())
        self.assertFalse(acc_application_id_avp__2.is_protected())
        self.assertEqual(acc_application_id_avp__2.get_length(), 12)
        self.assertIsNone(acc_application_id_avp__2.vendor_id)
        self.assertEqual(acc_application_id_avp__2.data, DIAMETER_APPLICATION_SWm)
        self.assertIsNone(acc_application_id_avp__2.get_padding_length())
        self.assertEqual(acc_application_id_avp__2.__repr__(), "<Diameter AVP: 259 [Acct-Application-Id] MANDATORY>")

    def test_diameter_avp__load_staticmethod__parsing_invalid_stream_only_1_byte__incomplete_code(self):
        stream = bytes.fromhex("00")

        with self.assertRaises(AVPParsingError) as cm:
            avps = DiameterAVP.load(stream)

        self.assertEqual(cm.exception.args[0], "invalid bytes stream")

    def test_diameter_avp__load_staticmethod__parsing_invalid_stream_only_2_bytes__incomplete_code(self):
        stream = bytes.fromhex("0000")

        with self.assertRaises(AVPParsingError) as cm:
            avps = DiameterAVP.load(stream)

        self.assertEqual(cm.exception.args[0], "invalid bytes stream")

    def test_diameter_avp__load_staticmethod__parsing_invalid_stream_only_3_bytes__incomplete_code(self):
        stream = bytes.fromhex("000000")

        with self.assertRaises(AVPParsingError) as cm:
            avps = DiameterAVP.load(stream)

        self.assertEqual(cm.exception.args[0], "invalid bytes stream")

    def test_diameter_avp__load_staticmethod__parsing_invalid_stream_only_4_bytes__only_code(self):
        stream = bytes.fromhex("00000000")

        with self.assertRaises(AVPParsingError) as cm:
            avps = DiameterAVP.load(stream)

        self.assertEqual(cm.exception.args[0], "invalid bytes stream")

    def test_diameter_avp__load_staticmethod__parsing_invalid_stream_only_5_bytes__only_code_and_flags(self):
        stream = bytes.fromhex("0000000011")
        
        with self.assertRaises(AVPParsingError) as cm:
            avps = DiameterAVP.load(stream)

        self.assertEqual(cm.exception.args[0], "invalid bytes stream. It contains only the code and flags fields")

    def test_diameter_avp__load_staticmethod__parsing_invalid_stream_only_6_bytes__only_code_and_flags_and_incomplete_length(self):
        stream = bytes.fromhex("0000000011")
        
        with self.assertRaises(AVPParsingError) as cm:
            avps = DiameterAVP.load(stream)

        self.assertEqual(cm.exception.args[0], "invalid bytes stream. It contains only the code and flags fields")

    def test_diameter_avp__load_staticmethod__parsing_invalid_stream_only_7_bytes__only_code_and_flags_and_incomplete_length(self):
        stream = bytes.fromhex("000000001100")
        
        with self.assertRaises(AVPParsingError) as cm:
            avps = DiameterAVP.load(stream)

        self.assertEqual(cm.exception.args[0], "invalid bytes stream. It contains only the code and flags fields")

    def test_diameter_avp__load_staticmethod__parsing_invalid_stream_only_8_bytes__only_code_and_flags_and_length(self):
        stream = bytes.fromhex("00000000000011")
        
        with self.assertRaises(AVPParsingError) as cm:
            avps = DiameterAVP.load(stream)

        self.assertEqual(cm.exception.args[0], "invalid bytes stream. It contains only the code and flags fields")

    def test_diameter_avp__load_staticmethod__parsing_stream_of_9_bytes(self):
        stream = bytes.fromhex("000000000000004f12")

        with self.assertRaises(AVPParsingError) as cm:
            avps = DiameterAVP.load(stream)

        self.assertEqual(cm.exception.args[0], "invalid bytes stream. The length field value does not correspond to the AVP length")


class TestUserNameAVP(unittest.TestCase):
    def test_user_name_avp__no_value(self):
        self.assertRaises(TypeError, UserNameAVP)

    def test_user_name_avp__repr_dunder(self):
        nai = "my-user@nai.epc.mncXXX.mccYYY.3gppnetwork.org"
        avp = UserNameAVP(nai)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 1 [User-Name] MANDATORY>")

    def test_user_name_avp__diameter_avp_convert_classmethod(self):
        nai = "my-user@nai.epc.mncXXX.mccYYY.3gppnetwork.org"
        avp = UserNameAVP(nai)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_user_name_avp__nai_format(self):
        nai = "my-user@nai.epc.mncXXX.mccYYY.3gppnetwork.org"
        avp = UserNameAVP(nai)
        ref = "00000001400000356d792d75736572406e61692e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_user_name_avp__imsi_format(self):
        nai = "012345678901234"
        avp = UserNameAVP(nai)
        ref = "000000014000001730313233343536373839303132333400"
        self.assertEqual(avp.dump().hex(), ref)


class TestClassAVP(unittest.TestCase):
    def test_class_avp__no_value(self):
        self.assertRaises(TypeError, ClassAVP)

    def test_class_avp__repr_dunder(self):
        avp = ClassAVP("CLOSED")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 25 [Class] MANDATORY>")

    def test_class_avp__diameter_avp_convert_classmethod(self):
        avp = ClassAVP("CLOSED")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_class_avp__1(self):
        avp = ClassAVP("CLOSED")
        ref = "000000194000000e434c4f5345440000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_class_avp__2(self):
        avp = ClassAVP("OPENED")
        ref = "000000194000000e4f50454e45440000"
        self.assertEqual(avp.dump().hex(), ref)


class TestSessionTimeoutAVP(unittest.TestCase):
    def test_session_timeout_avp__no_value(self):
        self.assertRaises(TypeError, SessionTimeoutAVP)

    def test_session_timeout_avp__repr_dunder(self):
        avp = SessionTimeoutAVP(10799)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 27 [Session-Timeout] MANDATORY>")

    def test_session_timeout_avp__diameter_avp_convert_classmethod(self):
        avp = SessionTimeoutAVP(10799)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_session_timeout_avp__1(self):
        avp = SessionTimeoutAVP(10799)
        ref = "0000001b4000000c00002a2f"
        self.assertEqual(avp.dump().hex(), ref)


class TestProxyStateAVP(unittest.TestCase):
    def test_proxy_state_avp__no_value(self):
        self.assertRaises(TypeError, ProxyStateAVP)

    def test_proxy_state_avp__repr_dunder(self):
        avp = ProxyStateAVP("CLOSED")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 33 [Proxy-State] MANDATORY>")

    def test_proxy_state_avp__diameter_avp_convert_classmethod(self):
        avp = ProxyStateAVP("CLOSED")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_proxy_state_avp__(self):
        avp = ProxyStateAVP("CLOSED")
        ref = "000000214000000e434c4f5345440000"
        self.assertEqual(avp.dump().hex(), ref)


class TestAcctSessionIdAVP(unittest.TestCase):
    def test_acct_session_id_avp__no_value(self):
        self.assertRaises(TypeError, AcctSessionIdAVP)

    def test_acct_session_id_avp__repr_dunder(self):
        data = convert_to_4_bytes(42)
        avp = AcctSessionIdAVP(data)

        self.assertEqual(avp.__repr__(), "<Diameter AVP: 44 [Acct-Session-Id] MANDATORY>")

    def test_acct_session_id_avp__diameter_avp_convert_classmethod(self):
        data = convert_to_4_bytes(42)
        avp = AcctSessionIdAVP(data)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_acct_session_id_avp__1(self):
        data = convert_to_4_bytes(6733)
        avp = AcctSessionIdAVP(data)
        ref = "0000002c4000000c00001a4d"
        self.assertEqual(avp.dump().hex(), ref)

    def test_acct_session_id_avp__2(self):
        data = convert_to_4_bytes(3588)
        avp = AcctSessionIdAVP(data)
        ref = "0000002c4000000c00000e04"
        self.assertEqual(avp.dump().hex(), ref)


class TestAcctMultiSessionIdAVP(unittest.TestCase):
    def test_acct_multi_session_id_avp__no_value(self):
        self.assertRaises(TypeError, AcctMultiSessionIdAVP)

    def test_acct_multi_session_id_avp__repr_dunder(self):
        avp = AcctMultiSessionIdAVP("es2")

        self.assertEqual(avp.__repr__(), "<Diameter AVP: 50 [Acct-Multi-Session-Id] MANDATORY>")

    def test_acct_multi_session_id_avp__diameter_avp_convert_classmethod(self):
        avp = AcctMultiSessionIdAVP("es2")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_acct_multi_session_id_avp__1(self):
        avp = AcctMultiSessionIdAVP("es2")
        ref = "00000032400000206573323b3430333239323b3430333239323b343033323932"
        self.assertEqual(avp.dump().hex(), ref)

    def test_acct_multi_session_id_avp__2(self):
        avp = AcctMultiSessionIdAVP("my-diameter-server.my-network")
        ref = "000000324000003a6d792d6469616d657465722d7365727665722e6d792d6e6574776f726b3b3430333239323b3430333239323b3430333239320000"
        self.assertEqual(avp.dump().hex(), ref)


class TestEventTimestampAVP(unittest.TestCase):
    def test_event_timestamp_avp__repr_dunder(self):
        avp = EventTimestampAVP()
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 55 [Event-Timestamp] MANDATORY>")

    def test_event_timestamp_avp__diameter_avp_convert_classmethod(self):
        avp = EventTimestampAVP()

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_event_timestamp_avp__1(self):
        timestamp = datetime.datetime.strptime("Nov 12, 2020 18:15:55", '%b %d, %Y %H:%M:%S')

        avp = EventTimestampAVP(timestamp)
        ref = "000000374000000ce357fa5b"
        self.assertEqual(avp.dump().hex(), ref)

    def test_event_timestamp_avp__2(self):
        timestamp = datetime.datetime.strptime("Nov 12, 2020 18:12:08", '%b %d, %Y %H:%M:%S')

        avp = EventTimestampAVP(timestamp)
        ref = "000000374000000ce357f978"
        self.assertEqual(avp.dump().hex(), ref)


class TestAcctInterimIntervalAVP(unittest.TestCase):
    def test_acct_interim_interval_avp__no_value(self):
        self.assertRaises(TypeError, AcctInterimIntervalAVP)

    def test_acct_interim_interval_avp__repr_dunder(self):
        avp = AcctInterimIntervalAVP(DIAMETER_APPLICATION_SWm)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 85 [Acct-Interim-Interval] MANDATORY>")

    def test_acct_interim_interval_avp__diameter_avp_convert_classmethod(self):
        avp = AcctInterimIntervalAVP(300)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_acct_interim_interval_avp__swm(self):
        avp = AcctInterimIntervalAVP(300)
        ref = "000000554000000c0000012c"
        self.assertEqual(avp.dump().hex(), ref)


class TestHostIpAddressAVP(unittest.TestCase):
    def test_host_ip_address_avp__no_value(self):
        self.assertRaises(TypeError, HostIpAddressAVP)

    def test_host_ip_address_avp__repr_dunder(self):
        avp = HostIpAddressAVP("10.129.241.235")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 257 [Host-Ip-Address] MANDATORY>")

    def test_host_ip_address_avp__diameter_avp_convert_classmethod(self):
        avp = HostIpAddressAVP("10.129.241.235")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_host_ip_address_avp__1(self):
        avp = HostIpAddressAVP("10.129.241.235")
        ref = "000001014000000e00010a81f1eb0000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_host_ip_address_avp__2(self):
        avp = HostIpAddressAVP("10.159.120.36")
        ref = "000001014000000e00010a9f78240000"
        self.assertEqual(avp.dump().hex(), ref)


class TestAuthApplicationIdAVP(unittest.TestCase):
    def test_auth_application_id_avp__no_value(self):
        self.assertRaises(TypeError, AuthApplicationIdAVP)

    def test_auth_application_id_avp__repr_dunder(self):
        avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_SWm)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 258 [Auth-Application-Id] MANDATORY>")

    def test_auth_application_id_avp__diameter_avp_convert_classmethod(self):
        avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_SWm)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_auth_application_id_avp__swm(self):
        avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_SWm)
        ref = "000001024000000c01000030"
        self.assertEqual(avp.dump().hex(), ref)

    def test_auth_application_id_avp__swx(self):
        avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_SWx)
        ref = "000001024000000c01000031"
        self.assertEqual(avp.dump().hex(), ref)

    def test_auth_application_id_avp__rx(self):
        avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_Rx)
        ref = "000001024000000c01000014"
        self.assertEqual(avp.dump().hex(), ref)

    def test_auth_application_id_avp__gx(self):
        avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_Gx)
        ref = "000001024000000c01000016"
        self.assertEqual(avp.dump().hex(), ref)

    def test_auth_application_id_avp__s6a_s6d(self):
        avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)
        ref = "000001024000000c01000023"
        self.assertEqual(avp.dump().hex(), ref)


class TestAcctApplicationIdAVP(unittest.TestCase):
    def test_acct_application_id_avp__no_value(self):
        self.assertRaises(TypeError, AcctApplicationIdAVP)

    def test_acct_application_id_avp__repr_dunder(self):
        avp = AcctApplicationIdAVP(DIAMETER_APPLICATION_SWm)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 259 [Acct-Application-Id] MANDATORY>")

    def test_acct_application_id_avp__diameter_avp_convert_classmethod(self):
        avp = AcctApplicationIdAVP(DIAMETER_APPLICATION_SWm)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_acct_application_id_avp__swm(self):
        avp = AcctApplicationIdAVP(DIAMETER_APPLICATION_SWm)
        ref = "000001034000000c01000030"
        self.assertEqual(avp.dump().hex(), ref)

    def test_acct_application_id_avp__swx(self):
        avp = AcctApplicationIdAVP(DIAMETER_APPLICATION_SWx)
        ref = "000001034000000c01000031"
        self.assertEqual(avp.dump().hex(), ref)

    def test_acct_application_id_avp__rx(self):
        avp = AcctApplicationIdAVP(DIAMETER_APPLICATION_Rx)
        ref = "000001034000000c01000014"
        self.assertEqual(avp.dump().hex(), ref)

    def test_acct_application_id_avp__gx(self):
        avp = AcctApplicationIdAVP(DIAMETER_APPLICATION_Gx)
        ref = "000001034000000c01000016"
        self.assertEqual(avp.dump().hex(), ref)

    def test_acct_application_id_avp__s6a_s6d(self):
        avp = AcctApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)
        ref = "000001034000000c01000023"
        self.assertEqual(avp.dump().hex(), ref)


class TestVendorSpecificApplicationIdAVP(unittest.TestCase):
    def test_vendor_specific_application_id_avp__no_value(self):
        self.assertRaises(TypeError, VendorSpecificApplicationIdAVP)

    def test_vendor_specific_application_id_avp__repr_dunder(self):
        vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)
        auth_app_id_avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_SWm)

        avps = [vendor_id_avp, auth_app_id_avp]
        avp = VendorSpecificApplicationIdAVP(avps)

        self.assertEqual(avp.__repr__(), "<Diameter AVP: 260 [Vendor-Specific-Application-Id] MANDATORY>")

    def test_vendor_specific_application_id_avp__diameter_avp_convert_classmethod(self):
        vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)
        auth_app_id_avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_SWm)

        avps = [vendor_id_avp, auth_app_id_avp]
        avp = VendorSpecificApplicationIdAVP(avps)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_vendor_specific_application_id_avp__default(self):
        ref = "00000104400000200000010a4000000c000028af000001024000000c01000030"

        vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)
        auth_app_id_avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_SWm)

        avps = [vendor_id_avp, auth_app_id_avp]
        avp = VendorSpecificApplicationIdAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)

    def test_vendor_specific_application_id_avp__only_auth_and_acct_app_avps(self):
        auth_app_id_avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_SWm)
        acct_app_id_avp = AcctApplicationIdAVP(DIAMETER_APPLICATION_SWm)

        avps = [auth_app_id_avp, acct_app_id_avp]

        with self.assertRaises(AVPAttributeValueError) as cm: 
            avp = VendorSpecificApplicationIdAVP(avps)
        
        self.assertEqual(cm.exception.args[1], DIAMETER_MISSING_AVP)


class TestRedirectHostUsageAVP(unittest.TestCase):
    def test_redirect_host_usage_avp__no_value(self):
        self.assertRaises(TypeError, RedirectHostUsageAVP)

    def test_redirect_host_usage_avp__repr_dunder(self):
        avp = RedirectHostUsageAVP(REDIRECT_HOST_USAGE_DONT_CACHE)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 261 [Redirect-Host-Usage] MANDATORY>")

    def test_redirect_host_usage_avp__diameter_avp_convert_classmethod(self):
        avp = RedirectHostUsageAVP(REDIRECT_HOST_USAGE_DONT_CACHE)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_redirect_host_usage_avp__dont_cache(self):
        avp = RedirectHostUsageAVP(REDIRECT_HOST_USAGE_DONT_CACHE)
        ref = "000001054000000c00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_redirect_host_usage_avp__all_session(self):
        avp = RedirectHostUsageAVP(REDIRECT_HOST_USAGE_ALL_SESSION)
        ref = "000001054000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_redirect_host_usage_avp__all_realm(self):
        avp = RedirectHostUsageAVP(REDIRECT_HOST_USAGE_ALL_REALM)
        ref = "000001054000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_redirect_host_usage_avp__realm_and_application(self):
        avp = RedirectHostUsageAVP(REDIRECT_HOST_USAGE_REALM_AND_APPLICATION)
        ref = "000001054000000c00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test_redirect_host_usage_avp__all_application(self):
        avp = RedirectHostUsageAVP(REDIRECT_HOST_USAGE_ALL_APPLICATION)
        ref = "000001054000000c00000004"
        self.assertEqual(avp.dump().hex(), ref)

    def test_redirect_host_usage_avp__all_host(self):
        avp = RedirectHostUsageAVP(REDIRECT_HOST_USAGE_ALL_HOST)
        ref = "000001054000000c00000005"
        self.assertEqual(avp.dump().hex(), ref)

    def test_redirect_host_usage_avp__all_user(self):
        avp = RedirectHostUsageAVP(REDIRECT_HOST_USAGE_ALL_USER)
        ref = "000001054000000c00000006"
        self.assertEqual(avp.dump().hex(), ref)


class TestRedirectMaxCacheTimeAVP(unittest.TestCase):
    def test_redirect_max_cache_time_avp__no_value(self):
        self.assertRaises(TypeError, RedirectMaxCacheTimeAVP)

    def test_redirect_max_cache_time_avp__repr_dunder(self):
        avp = RedirectMaxCacheTimeAVP(10799)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 262 [Redirect-Max-Cache-Time] MANDATORY>")

    def test_redirect_max_cache_time_avp__diameter_avp_convert_classmethod(self):
        avp = RedirectMaxCacheTimeAVP(10799)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_redirect_max_cache_time_avp__1(self):
        avp = RedirectMaxCacheTimeAVP(10799)
        ref = "000001064000000c00002a2f"
        self.assertEqual(avp.dump().hex(), ref)


class TestSessionIdAVP(unittest.TestCase):
    def test_session_id_avp__no_value(self):
        self.assertRaises(TypeError, SessionIdAVP)

    def test_session_id_avp__repr_dunder(self):
        avp = SessionIdAVP("es2")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 263 [Session-Id] MANDATORY>")

    def test_session_id_avp__diameter_avp_convert_classmethod(self):
        avp = SessionIdAVP("es2")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)


class TestOriginHostAVP(unittest.TestCase):
    def test_origin_host_avp__no_value(self):
        self.assertRaises(TypeError, OriginHostAVP)

    def test_origin_host_avp__repr_dunder(self):
        avp = OriginHostAVP("es2")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 264 [Origin-Host] MANDATORY>")

    def test_origin_host_avp__diameter_avp_convert_classmethod(self):
        avp = OriginHostAVP("es2")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_origin_host_avp__1(self):
        avp = OriginHostAVP("rx.pcscf-ni0.ims.mncXXX.mccYYY.3gppnetwork.org")
        ref = "000001084000003672782e70637363662d6e69302e696d732e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_origin_host_avp__2(self):
        avp = OriginHostAVP("es2")
        ref = "000001084000000b65733200"
        self.assertEqual(avp.dump().hex(), ref)

    def test_origin_host_avp__3(self):
        avp = OriginHostAVP("rjni0.epc.mncXXX.mccYYY.3gppnetwork.org")
        ref = "000001084000002f726a6e69302e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f726700"
        self.assertEqual(avp.dump().hex(), ref)

    def test_origin_host_avp__4(self):
        avp = OriginHostAVP("rjnt0")
        ref = "000001084000000d726a6e7430000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_origin_host_avp__5(self):
        avp = OriginHostAVP("esp-sev19.epc.mncXXX.mccYYY.3gppnetwork.org")
        ref = "00000108400000336573702d73657631392e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f726700"
        self.assertEqual(avp.dump().hex(), ref)


class TestSupportedVendorIdAVP(unittest.TestCase):
    def test_supported_vendor_id_avp__no_value(self):
        self.assertRaises(TypeError, SupportedVendorIdAVP)
    
    def test_supported_vendor_id_avp__repr_dunder(self):
        avp = SupportedVendorIdAVP(VENDOR_ID_3GPP)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 265 [Supported-Vendor-Id] MANDATORY>")

    def test_supported_vendor_id_avp__diameter_avp_convert_classmethod(self):
        avp = SupportedVendorIdAVP(VENDOR_ID_3GPP)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_supported_vendor_id_avp__vendor_id_3gpp(self):
        avp = SupportedVendorIdAVP(VENDOR_ID_3GPP)
        ref = "000001094000000c000028af"
        self.assertEqual(avp.dump().hex(), ref)


class TestVendorIdAVP(unittest.TestCase):       
    def test_vendor_id_avp__no_value(self):
        avp = VendorIdAVP()
        ref = "0000010a4000000c00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_vendor_id_avp__repr_dunder(self):
        avp = VendorIdAVP()
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 266 [Vendor-Id] MANDATORY>")

    def test_vendor_id_avp__diameter_avp_convert_classmethod(self):
        avp = VendorIdAVP()

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_vendor_id_avp__3gpp(self):
        avp = VendorIdAVP(VENDOR_ID_3GPP)
        ref = "0000010a4000000c000028af"
        self.assertEqual(avp.dump().hex(), ref)


class TestFirmwareRevisionAVP(unittest.TestCase):
    def test_firmware_revision_avp__no_value(self):
        self.assertRaises(TypeError, FirmwareRevisionAVP)

    def test_firmware_revision_avp__repr_dunder(self):
        FIRMWARE_REVISION = convert_to_4_bytes(1)
        avp = FirmwareRevisionAVP(FIRMWARE_REVISION)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 267 [Firmware-Revision]>")

    def test_firmware_revision_avp__diameter_avp_convert_classmethod(self):
        FIRMWARE_REVISION = convert_to_4_bytes(1)
        avp = FirmwareRevisionAVP(FIRMWARE_REVISION)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_firmware_revision_avp__1(self):
        FIRMWARE_REVISION = convert_to_4_bytes(1)
        avp = FirmwareRevisionAVP(FIRMWARE_REVISION)
        ref = "0000010b0000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_firmware_revision_avp__2(self):
        FIRMWARE_REVISION = convert_to_4_bytes(529153)
        avp = FirmwareRevisionAVP(FIRMWARE_REVISION)
        ref = "0000010b0000000c00081301"
        self.assertEqual(avp.dump().hex(), ref)


class TestResultCodeAVP(unittest.TestCase):
    def test_result_code_avp__no_value(self):
        self.assertRaises(TypeError, ResultCodeAVP)
        
    def test_result_code_avp__repr_dunder(self):
        avp = ResultCodeAVP(DIAMETER_SUCCESS)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 268 [Result-Code] MANDATORY>")

    def test_result_code_avp__diameter_avp_convert_classmethod(self):
        avp = ResultCodeAVP(DIAMETER_SUCCESS)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_result_code_avp__diameter_success(self):
        avp = ResultCodeAVP(DIAMETER_SUCCESS)
        ref = "0000010c4000000c000007d1"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_command_unsupported(self):
        avp = ResultCodeAVP(DIAMETER_COMMAND_UNSUPPORTED)
        ref = "0000010c4000000c00000bb9"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_unable_to_deliver(self):
        avp = ResultCodeAVP(DIAMETER_UNABLE_TO_DELIVER)
        ref = "0000010c4000000c00000bba"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_realm_not_served(self):
        avp = ResultCodeAVP(DIAMETER_REALM_NOT_SERVED)
        ref = "0000010c4000000c00000bbb"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_too_busy(self):
        avp = ResultCodeAVP(DIAMETER_TOO_BUSY)
        ref = "0000010c4000000c00000bbc"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_loop_detected(self):
        avp = ResultCodeAVP(DIAMETER_LOOP_DETECTED)
        ref = "0000010c4000000c00000bbd"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_redirect_indication(self):
        avp = ResultCodeAVP(DIAMETER_REDIRECT_INDICATION)
        ref = "0000010c4000000c00000bbe"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_application_unsupported(self):
        avp = ResultCodeAVP(DIAMETER_APPLICATION_UNSUPPORTED)
        ref = "0000010c4000000c00000bbf"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_invalid_hdr_bits(self):
        avp = ResultCodeAVP(DIAMETER_INVALID_HDR_BITS)
        ref = "0000010c4000000c00000bc0"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_invalid_avp_bits(self):
        avp = ResultCodeAVP(DIAMETER_INVALID_AVP_BITS)
        ref = "0000010c4000000c00000bc1"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_unknown_peer(self):
        avp = ResultCodeAVP(DIAMETER_UNKNOWN_PEER)
        ref = "0000010c4000000c00000bc2"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_authentication_rejected(self):
        avp = ResultCodeAVP(DIAMETER_AUTHENTICATION_REJECTED)
        ref = "0000010c4000000c00000fa1"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_out_of_space(self):
        avp = ResultCodeAVP(DIAMETER_OUT_OF_SPACE)
        ref = "0000010c4000000c00000fa2"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_election_lost(self):
        avp = ResultCodeAVP(DIAMETER_ELECTION_LOST)
        ref = "0000010c4000000c00000fa3"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_avp_unsupported(self):
        avp = ResultCodeAVP(DIAMETER_AVP_UNSUPPORTED)
        ref = "0000010c4000000c00001389"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_unknown_session_id(self):
        avp = ResultCodeAVP(DIAMETER_UNKNOWN_SESSION_ID)
        ref = "0000010c4000000c0000138a"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_authorization_rejected(self):
        avp = ResultCodeAVP(DIAMETER_AUTHORIZATION_REJECTED)
        ref = "0000010c4000000c0000138b"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_invalid_avp_value(self):
        avp = ResultCodeAVP(DIAMETER_INVALID_AVP_VALUE)
        ref = "0000010c4000000c0000138c"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_missing_avp(self):
        avp = ResultCodeAVP(DIAMETER_MISSING_AVP)
        ref = "0000010c4000000c0000138d"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_resources_exceeded(self):
        avp = ResultCodeAVP(DIAMETER_RESOURCES_EXCEEDED)
        ref = "0000010c4000000c0000138e"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_contradicting_avps(self):
        avp = ResultCodeAVP(DIAMETER_CONTRADICTING_AVPS)
        ref = "0000010c4000000c0000138f"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_avp_not_allowed(self):
        avp = ResultCodeAVP(DIAMETER_AVP_NOT_ALLOWED)
        ref = "0000010c4000000c00001390"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_avp_occurs_too_many_times(self):
        avp = ResultCodeAVP(DIAMETER_AVP_OCCURS_TOO_MANY_TIMES)
        ref = "0000010c4000000c00001391"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_no_common_application(self):
        avp = ResultCodeAVP(DIAMETER_NO_COMMON_APPLICATION)
        ref = "0000010c4000000c00001392"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_unsupported_version(self):
        avp = ResultCodeAVP(DIAMETER_UNSUPPORTED_VERSION)
        ref = "0000010c4000000c00001393"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_unable_to_comply(self):
        avp = ResultCodeAVP(DIAMETER_UNABLE_TO_COMPLY)
        ref = "0000010c4000000c00001394"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_invalid_bit_in_header(self):
        avp = ResultCodeAVP(DIAMETER_INVALID_BIT_IN_HEADER)
        ref = "0000010c4000000c00001395"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_invalid_avp_length(self):
        avp = ResultCodeAVP(DIAMETER_INVALID_AVP_LENGTH)
        ref = "0000010c4000000c00001396"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_invalid_message_length(self):
        avp = ResultCodeAVP(DIAMETER_INVALID_MESSAGE_LENGTH)
        ref = "0000010c4000000c00001397"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_invalid_avp_bit_combo(self):
        avp = ResultCodeAVP(DIAMETER_INVALID_AVP_BIT_COMBO)
        ref = "0000010c4000000c00001398"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_non_common_security(self):
        avp = ResultCodeAVP(DIAMETER_NO_COMMON_SECURITY)
        ref = "0000010c4000000c00001399"
        self.assertEqual(avp.dump().hex(), ref)
        

class TestProductNameAVP(unittest.TestCase):
    def test_product_name_avp__default(self):
        avp = ProductNameAVP()
        ref = "0000010d0000001e507974686f6e2062726f6d656c69612076302e322e300000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_product_name_avp__repr_dunder(self):
        avp = ProductNameAVP()
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 269 [Product-Name]>")

    def test_product_name_avp__diameter_avp_convert_classmethod(self):
        avp = ProductNameAVP()

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_product_name_avp__1(self):
        avp = ProductNameAVP("Entitlement Server")
        ref = "0000010d0000001a456e7469746c656d656e74205365727665720000"
        self.assertEqual(avp.dump().hex(), ref)


class TestSessionBindingAVP(unittest.TestCase):
    def test_session_binding_avp__no_value(self):
        self.assertRaises(TypeError, SessionBindingAVP)

    def test_session_binding_avp__repr_dunder(self):
        avp = SessionBindingAVP(1)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 270 [Session-Binding] MANDATORY>")

    def test_session_binding_avp__diameter_avp_convert_classmethod(self):
        avp = SessionBindingAVP(2)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_session_binding_avp__re_auth_bit(self):
        avp = SessionBindingAVP(1)
        ref = "0000010e4000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_session_binding_avp__str_bit(self):
        avp = SessionBindingAVP(2)
        ref = "0000010e4000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_session_binding_avp__accounting_bit(self):
        avp = SessionBindingAVP(4)
        ref = "0000010e4000000c00000004"
        self.assertEqual(avp.dump().hex(), ref)


class TestSessionServerFailoverAVP(unittest.TestCase):
    def test_session_server_failover_avp__no_value(self):
        avp = SessionServerFailoverAVP()
        ref = "0000010f4000000c00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_session_server_failover_avp__repr_dunder(self):
        avp = SessionServerFailoverAVP()
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 271 [Session-Server-Failover] MANDATORY>")

    def test_session_server_failover_avp__diameter_avp_convert_classmethod(self):
        avp = SessionServerFailoverAVP()

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_session_server_failover_avp__refuse_service(self):
        avp = SessionServerFailoverAVP(SESSION_SERVER_FAILOVER_REFUSE_SERVICE)
        ref = "0000010f4000000c00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_session_server_failover_avp__try_again(self):
        avp = SessionServerFailoverAVP(SESSION_SERVER_FAILOVER_TRY_AGAIN)
        ref = "0000010f4000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_session_server_failover_avp__allow_service(self):
        avp = SessionServerFailoverAVP(SESSION_SERVER_FAILOVER_ALLOW_SERVICE)
        ref = "0000010f4000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_session_server_failover_avp__try_again_allow_service(self):
        avp = SessionServerFailoverAVP(SESSION_SERVER_FAILOVER_TRY_AGAIN_ALLOW_SERVICE)
        ref = "0000010f4000000c00000003"
        self.assertEqual(avp.dump().hex(), ref)


class TestMultiRoundTimeOutAVP(unittest.TestCase):
    def test_multi_round_time_out_avp__no_value(self):
        self.assertRaises(TypeError, MultiRoundTimeOutAVP)

    def test_multi_round_time_out_avp__repr_dunder(self):
        avp = MultiRoundTimeOutAVP(60)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 272 [Multi-Round-Time-Out] MANDATORY>")

    def test_multi_round_time_out_avp__diameter_avp_convert_classmethod(self):
        avp = MultiRoundTimeOutAVP(3600)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_multi_round_time_out_avp__1(self):
        avp = MultiRoundTimeOutAVP(60)
        ref = "000001104000000c0000003c"
        self.assertEqual(avp.dump().hex(), ref)

    def test_multi_round_time_out_avp__2(self):
        avp = MultiRoundTimeOutAVP(3600)
        ref = "000001104000000c00000e10"
        self.assertEqual(avp.dump().hex(), ref)

    def test_multi_round_time_out_avp__3(self):
        avp = MultiRoundTimeOutAVP(86400)
        ref = "000001104000000c00015180"
        self.assertEqual(avp.dump().hex(), ref)


class TestDisconnectCauseAVP(unittest.TestCase):
    def test_disconnect_cause_avp__no_value(self):
        avp = DisconnectCauseAVP()
        ref = "000001114000000c00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_disconnect_cause_avp__repr_dunder(self):
        avp = DisconnectCauseAVP()
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 273 [Disconnect-Cause] MANDATORY>")

    def test_disconnect_cause_avp__diameter_avp_convert_classmethod(self):
        avp = DisconnectCauseAVP()

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_disconnect_cause_avp__rebooting(self):
        avp = DisconnectCauseAVP(DISCONNECT_CAUSE_REBOOTING)
        ref = "000001114000000c00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_disconnect_cause_avp__busy(self):
        avp = DisconnectCauseAVP(DISCONNECT_CAUSE_BUSY)
        ref = "000001114000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_disconnect_cause_avp__do_not_want_to_talk_to_you(self):
        avp = DisconnectCauseAVP(DISCONNECT_CAUSE_DO_NOT_WANT_TO_TALK_TO_YOU)
        ref = "000001114000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)


class TestAuthRequestTypeAVP(unittest.TestCase):
    def test_auth_request_type_avp__no_value(self):
        self.assertRaises(TypeError, AuthRequestTypeAVP)
    
    def test_auth_request_type_avp__repr_dunder(self):
        avp = AuthRequestTypeAVP(AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 274 [Auth-Request-Type] MANDATORY>")

    def test_auth_request_type_avp__diameter_avp_convert_classmethod(self):
        avp = AuthRequestTypeAVP(AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_auth_request_type_avp__authenticate_only(self):
        avp = AuthRequestTypeAVP(AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY)
        ref = "000001124000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_auth_request_type_avp__authorize_only(self):
        avp = AuthRequestTypeAVP(AUTH_REQUEST_TYPE_AUTHORIZE_ONLY)
        ref = "000001124000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_auth_request_type_avp__authorize_authenticate(self):
        avp = AuthRequestTypeAVP(AUTH_REQUEST_TYPE_AUTHORIZE_AUTHENTICATE)
        ref = "000001124000000c00000003"
        self.assertEqual(avp.dump().hex(), ref)


class TestAuthGracePeriodAVP(unittest.TestCase):
    def test_auth_grace_period_avp__no_value(self):
        self.assertRaises(TypeError, AuthGracePeriodAVP)

    def test_auth_grace_period_avp__repr_dunder(self):
        avp = AuthGracePeriodAVP(60)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 276 [Auth-Grace-Period] MANDATORY>")

    def test_auth_grace_period_avp__diameter_avp_convert_classmethod(self):
        avp = AuthGracePeriodAVP(3600)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_auth_grace_period_avp__1(self):
        avp = AuthGracePeriodAVP(60)
        ref = "000001144000000c0000003c"
        self.assertEqual(avp.dump().hex(), ref)

    def test_auth_grace_period_avp__2(self):
        avp = AuthGracePeriodAVP(3600)
        ref = "000001144000000c00000e10"
        self.assertEqual(avp.dump().hex(), ref)

    def test_auth_grace_period_avp__3(self):
        avp = AuthGracePeriodAVP(86400)
        ref = "000001144000000c00015180"
        self.assertEqual(avp.dump().hex(), ref)


class TestAuthSessionStateAVP(unittest.TestCase):
    def test_auth_session_state_avp__no_value(self):
        self.assertRaises(TypeError, AuthSessionStateAVP)

    def test_auth_session_state_avp__repr_dunder(self):
        avp = AuthSessionStateAVP(STATE_MAINTAINED)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 277 [Auth-Session-State] MANDATORY>")

    def test_auth_session_state_avp__diameter_avp_convert_classmethod(self):
        avp = AuthSessionStateAVP(STATE_MAINTAINED)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_auth_session_state_avp__state_maintained(self):
        avp = AuthSessionStateAVP(STATE_MAINTAINED)
        ref = "000001154000000c00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_auth_session_state_avp__no_state_maintained(self):
        avp = AuthSessionStateAVP(NO_STATE_MAINTAINED)
        ref = "000001154000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestOriginStateIdAVP(unittest.TestCase):
    def test_origin_state_id_avp__no_value(self):
        self.assertRaises(TypeError, OriginStateIdAVP)

    def test_origin_state_id_avp__repr_dunder(self):
        avp = OriginStateIdAVP(1524733202)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 278 [Origin-State-Id] MANDATORY>")

    def test_origin_state_id_avp__diameter_avp_convert_classmethod(self):
        avp = OriginStateIdAVP(1524733202)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_origin_state_id_avp__1(self):
        avp = OriginStateIdAVP(1524733202)
        ref = "000001164000000c5ae19512"
        self.assertEqual(avp.dump().hex(), ref)


class TestFailedAvpAVP(unittest.TestCase):
    def test_failed_avp_avp__no_value(self):
        self.assertRaises(TypeError, FailedAvpAVP)

    def test_failed_avp_avp__repr_dunder(self):
        route_record1 = RouteRecordAVP("hssrj1.epc.mncXXX.mccYYY.3gppnetwork.org")
        route_record2 = RouteRecordAVP("drasm01b.epc.mncXXX.mccYYY.3gppnetwork.org")

        avps = [route_record1, route_record2]
        avp = FailedAvpAVP(avps)

        self.assertEqual(avp.__repr__(), "<Diameter AVP: 279 [Failed-Avp] MANDATORY>")

    def test_failed_avp_avp__diameter_avp_convert_classmethod(self):
        route_record1 = RouteRecordAVP("hssrj1.epc.mncXXX.mccYYY.3gppnetwork.org")
        route_record2 = RouteRecordAVP("drasm01b.epc.mncXXX.mccYYY.3gppnetwork.org")

        avps = [route_record1, route_record2]
        avp = FailedAvpAVP(avps)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_failed_avp_avp__1(self):
        ref = "00000117400000680000011a4000002f68656272612e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000011a4000002f656c64696e2e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f726700"

        route_record1 = RouteRecordAVP("hebra.epc.mncXXX.mccYYY.3gppnetwork.org")
        route_record2 = RouteRecordAVP("eldin.epc.mncXXX.mccYYY.3gppnetwork.org")

        avps = [route_record1, route_record2]
        avp = FailedAvpAVP(avps)

        self.maxDiff = None
        self.assertEqual(avp.dump().hex(), ref)

    def test_failed_avp_avp__2(self):
        ref = "00000117400000380000011a40000030687373736d322e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267"

        route_record1 = RouteRecordAVP("hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")

        avps = [route_record1]
        avp = FailedAvpAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)

    def test_failed_avp_avp__3(self):
        ref = "000001174000006c0000011a400000306573702d6d642e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000011a40000032746162616e7468612e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000"

        route_record1 = RouteRecordAVP("esp-md.epc.mncXXX.mccYYY.3gppnetwork.org")
        route_record2 = RouteRecordAVP("tabantha.epc.mncXXX.mccYYY.3gppnetwork.org")

        avps = [route_record1, route_record2]
        avp = FailedAvpAVP(avps)

        self.maxDiff = None
        self.assertEqual(avp.dump().hex(), ref)


class TestProxyHostAVP(unittest.TestCase):
    def test_proxy_host_avp__no_value(self):
        self.assertRaises(TypeError, ProxyHostAVP)

    def test_proxy_host_avp__repr_dunder(self):
        avp = ProxyHostAVP("hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 280 [Proxy-Host] MANDATORY>")

    def test_proxy_host_avp__diameter_avp_convert_classmethod(self):
        avp = ProxyHostAVP("hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_proxy_host_avp__1(self):
        avp = ProxyHostAVP("hsssm92.epc.mncXXX.mccYYY.3gppnetwork.org")
        ref = "0000011840000031687373736d39322e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_proxy_host_avp__2(self):
        avp = ProxyHostAVP("pgwrj03.epc.mncXXX.mccYYY.3gppnetwork.org")
        ref = "0000011840000031706777726a30332e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"
        self.assertEqual(avp.dump().hex(), ref)


class TestErrorMessageAVP(unittest.TestCase):
    def test_error_message_avp__no_value(self):
        self.assertRaises(TypeError, ErrorMessageAVP)

    def test_error_message_avp__repr_dunder(self):
        avp = ErrorMessageAVP("hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 281 [Error-Message]>")

    def test_error_message_avp__diameter_avp_convert_classmethod(self):
        avp = ErrorMessageAVP("hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_error_message_avp__1(self):
        avp = ErrorMessageAVP("DRL-ERR-3002-304:.")
        ref = "000001190000001a44524c2d4552522d333030322d3330343a2e0000"
        self.assertEqual(avp.dump().hex(), ref)


class TestRouteRecordAVP(unittest.TestCase):
    def test_route_record_avp__no_value(self):
        self.assertRaises(TypeError, RouteRecordAVP)

    def test_route_record_avp__repr_dunder(self):
        avp = RouteRecordAVP("pcrfrj1.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 282 [Route-Record] MANDATORY>")

    def test_route_record_avp__diameter_avp_convert_classmethod(self):
        avp = RouteRecordAVP("scscfsm2.epc.mncXXX.mccYYY.3gppnetwork.org")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_route_record_avp__1(self):
        avp = RouteRecordAVP("pcrfrj1.epc.mncXXX.mccYYY.3gppnetwork.org")
        ref = "0000011a4000003170637266726a312e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_route_record_avp__2(self):
        avp = RouteRecordAVP("scscfsm2.epc.mncXXX.mccYYY.3gppnetwork.org")
        ref = "0000011a400000327363736366736d322e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000"
        self.assertEqual(avp.dump().hex(), ref)


class TestDestinationRealmAVP(unittest.TestCase):
    def test_destination_realm_avp__no_value(self):
        self.assertRaises(TypeError, DestinationRealmAVP)

    def test_destination_realm_avp__repr_dunder(self):
        avp = DestinationRealmAVP("sevilla.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 283 [Destination-Realm] MANDATORY>")

    def test_destination_realm_avp__diameter_avp_convert_classmethod(self):
        avp = DestinationRealmAVP("epc.mncXXX.mccYYY.3gppnetwork.org")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_destination_realm_avp__1(self):
        avp = DestinationRealmAVP("epc.mncXXX.mccYYY.3gppnetwork.org")
        ref = "0000011b400000296570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_destination_realm_avp__2(self):
        avp = DestinationRealmAVP("gxserver.operator.com")
        ref = "0000011b4000001d67787365727665722e6f70657261746f722e636f6d000000"
        self.assertEqual(avp.dump().hex(), ref)
      

class TestProxyInfoAVP(unittest.TestCase):
    def test_proxy_info_avp__no_value(self):
        self.assertRaises(TypeError, ProxyInfoAVP)

    def test_proxy_info_avp__repr_dunder(self):
        proxy_host_avp = ProxyHostAVP("hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")
        proxy_state_avp = ProxyStateAVP("CLOSED")

        avps = [proxy_host_avp, proxy_state_avp]
        avp = ProxyInfoAVP(avps)

        self.assertEqual(avp.__repr__(), "<Diameter AVP: 284 [Proxy-Info] MANDATORY>")

    def test_proxy_info_avp__diameter_avp_convert_classmethod(self):
        proxy_host_avp = ProxyHostAVP("hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")
        proxy_state_avp = ProxyStateAVP("CLOSED")

        avps = [proxy_host_avp, proxy_state_avp]
        avp = ProxyInfoAVP(avps)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_proxy_info_avp__1(self):
        ref = "0000011c400000480000011840000030687373736d322e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000214000000e434c4f5345440000"
      
        proxy_host_avp = ProxyHostAVP("hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")
        proxy_state_avp = ProxyStateAVP("CLOSED")

        avps = [proxy_host_avp, proxy_state_avp]
        avp = ProxyInfoAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)

    def test_proxy_info_avp__2(self):
        ref = "0000011c40000048000001184000002d726a342e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000000214000000e4f50454e45440000"
      
        proxy_host_avp = ProxyHostAVP("rj4.epc.mncXXX.mccYYY.3gppnetwork.org")
        proxy_state_avp = ProxyStateAVP("OPENED")

        avps = [proxy_host_avp, proxy_state_avp]
        avp = ProxyInfoAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)


class TestReAuthRequestTypeAVP(unittest.TestCase):
    def test_re_auth_request_type_avp__no_value(self):
        self.assertRaises(TypeError, ReAuthRequestTypeAVP)

    def test_re_auth_request_type_avp__repr_dunder(self):
        avp = ReAuthRequestTypeAVP(RE_AUTH_REQUEST_TYPE_AUTHORIZE_ONLY)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 285 [Re-Auth-Request-Type] MANDATORY>")

    def test_re_auth_request_type_avp__diameter_avp_convert_classmethod(self):
        avp = ReAuthRequestTypeAVP(RE_AUTH_REQUEST_TYPE_AUTHORIZE_ONLY)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_re_auth_request_type_avp__authorize_only(self):
        avp = ReAuthRequestTypeAVP(RE_AUTH_REQUEST_TYPE_AUTHORIZE_ONLY)
        ref = "0000011d4000000c00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_re_auth_request_type_avp__authorize_authenticate(self):
        avp = ReAuthRequestTypeAVP(RE_AUTH_REQUEST_TYPE_AUTHORIZE_AUTHENTICATE)
        ref = "0000011d4000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestAccountingSubSessionIdAVP(unittest.TestCase):
    def test_accounting_sub_session_id_avp__no_value(self):
        self.assertRaises(TypeError, AccountingSubSessionIdAVP)

    def test_accounting_sub_session_id_avp__repr_dunder(self):
        avp = AccountingSubSessionIdAVP(6733)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 287 [Accounting-Sub-Session-Id] MANDATORY>")

    def test_accounting_sub_session_id_avp__diameter_avp_convert_classmethod(self):
        avp = AccountingSubSessionIdAVP(3588)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_accounting_sub_session_id_avp__1(self):
        avp = AccountingSubSessionIdAVP(42)
        ref = "0000011f40000010000000000000002a"
        self.assertEqual(avp.dump().hex(), ref)

    def test_accounting_sub_session_id_avp__2(self):
        avp = AccountingSubSessionIdAVP(92049311)
        ref = "0000011f4000001000000000057c8f9f"
        self.assertEqual(avp.dump().hex(), ref)


class TestAuthorizationLifetimeAVP(unittest.TestCase):
    def test_authorization_lifetime_avp__no_value(self):
        self.assertRaises(TypeError, AuthorizationLifetimeAVP)

    def test_authorization_lifetime_avp__repr_dunder(self):
        avp = AuthorizationLifetimeAVP(60)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 291 [Authorization-Lifetime] MANDATORY>")

    def test_authorization_lifetime_avp__diameter_avp_convert_classmethod(self):
        avp = AuthorizationLifetimeAVP(3600)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_authorization_lifetime_avp__1(self):
        avp = AuthorizationLifetimeAVP(60)
        ref = "000001234000000c0000003c"
        self.assertEqual(avp.dump().hex(), ref)

    def test_authorization_lifetime_avp__2(self):
        avp = AuthorizationLifetimeAVP(3600)
        ref = "000001234000000c00000e10"
        self.assertEqual(avp.dump().hex(), ref)

    def test_authorization_lifetime_avp__3(self):
        avp = AuthorizationLifetimeAVP(86400)
        ref = "000001234000000c00015180"
        self.assertEqual(avp.dump().hex(), ref)


class TestRedirectHostAVP(unittest.TestCase):
    def test_redirect_host_avp__no_value(self):
        self.assertRaises(TypeError, RedirectHostAVP)

    def test_redirect_host_avp__repr_dunder(self):
        avp = RedirectHostAVP("aaa://host.example.com;transport=tcp")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 292 [Redirect-Host] MANDATORY>")

    def test_redirect_host_avp__diameter_avp_convert_classmethod(self):
        avp = RedirectHostAVP("aaa://host.example.com;transport=tcp")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_redirect_host_avp__1(self):
        avp = RedirectHostAVP("aaa://host.example.com;transport=tcp")
        ref = "000001244000002c6161613a2f2f686f73742e6578616d706c652e636f6d3b7472616e73706f72743d746370"
        self.assertEqual(avp.dump().hex(), ref)

    def test_redirect_host_avp__2(self):
        avp = RedirectHostAVP("aaas://host.example.com:6666;transport=tcp")
        ref = "0000012440000032616161733a2f2f686f73742e6578616d706c652e636f6d3a363636363b7472616e73706f72743d7463700000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_redirect_host_avp__3(self):
        avp = RedirectHostAVP("aaa://host.example.com;protocol=diameter")
        ref = "00000124400000306161613a2f2f686f73742e6578616d706c652e636f6d3b70726f746f636f6c3d6469616d65746572"
        self.assertEqual(avp.dump().hex(), ref)

    def test_redirect_host_avp__4(self):
        avp = RedirectHostAVP("aaa://host.example.com:6666;protocol=diameter")
        ref = "00000124400000356161613a2f2f686f73742e6578616d706c652e636f6d3a363636363b70726f746f636f6c3d6469616d65746572000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_redirect_host_avp__5(self):
        avp = RedirectHostAVP("aaa://host.example.com:6666;transport=tcp;protocol=diameter")
        ref = "00000124400000436161613a2f2f686f73742e6578616d706c652e636f6d3a363636363b7472616e73706f72743d7463703b70726f746f636f6c3d6469616d6574657200"
        self.assertEqual(avp.dump().hex(), ref)

    def test_redirect_host_avp__6(self):
        avp = RedirectHostAVP("aaa://host.example.com:1813;transport=udp;protocol=radius")
        ref = "00000124400000416161613a2f2f686f73742e6578616d706c652e636f6d3a313831333b7472616e73706f72743d7564703b70726f746f636f6c3d726164697573000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_redirect_host_avp__7(self):
        avp = RedirectHostAVP("aaas://host.example.com:1024;transport=tcp;protocol=diameter")
        ref = "0000012440000044616161733a2f2f686f73742e6578616d706c652e636f6d3a313032343b7472616e73706f72743d7463703b70726f746f636f6c3d6469616d65746572"
        self.assertEqual(avp.dump().hex(), ref)


class TestDestinationHostAVP(unittest.TestCase):
    def test_destination_host_avp__no_value(self):
        self.assertRaises(TypeError, DestinationHostAVP)

    def test_destination_host_avp__repr_dunder(self):
        avp = DestinationHostAVP("encvltapp1-ne-rx")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 293 [Destination-Host] MANDATORY>")

    def test_destination_host_avp__diameter_avp_convert_classmethod(self):
        avp = DestinationHostAVP("encvltapp1-ne-rx")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_destination_host_avp__1(self):
        avp = DestinationHostAVP("encvltapp1-ne-rx")
        ref = "0000012540000018656e63766c74617070312d6e652d7278"
        self.assertEqual(avp.dump().hex(), ref)

    def test_destination_host_avp__2(self):
        avp = DestinationHostAVP("hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")
        ref = "0000012540000030687373736d322e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267"
        self.assertEqual(avp.dump().hex(), ref)


class TestErrorReportingHostAVP(unittest.TestCase):
    def test_error_reporting_host_avp__no_value(self):
        self.assertRaises(TypeError, ErrorReportingHostAVP)

    def test_error_reporting_host_avp__repr_dunder(self):
        avp = ErrorReportingHostAVP("hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 294 [Error-Reporting-Host]>")

    def test_error_reporting_host_avp__diameter_avp_convert_classmethod(self):
        avp = ErrorReportingHostAVP("hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_error_reporting_host_avp__1(self):
        avp = ErrorReportingHostAVP("hsssm2.epc.mncXXX.mccYYY.3gppnetwork.org")
        ref = "0000012600000030687373736d322e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267"
        self.assertEqual(avp.dump().hex(), ref)

    def test_error_reporting_host_avp__2(self):
        avp = ErrorReportingHostAVP("rj4.epc.mncXXX.mccYYY.3gppnetwork.org")
        ref = "000001260000002d726a342e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"
        self.assertEqual(avp.dump().hex(), ref)


class TestTerminationCauseAVP(unittest.TestCase):
    def test_termination_cause_avp__no_value(self):
        self.assertRaises(TypeError, TerminationCauseAVP)

    def test_error_reporting_host_avp__repr_dunder(self):
        avp = TerminationCauseAVP(DIAMETER_LOGOUT)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 295 [Termination-Cause] MANDATORY>")

    def test_error_reporting_host_avp__diameter_avp_convert_classmethod(self):
        avp = TerminationCauseAVP(DIAMETER_LOGOUT)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_termination_cause_avp__diameter_logout(self):
        avp = TerminationCauseAVP(DIAMETER_LOGOUT)
        ref = "000001274000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_termination_cause_avp__diameter_service_not_provided(self):
        avp = TerminationCauseAVP(DIAMETER_SERVICE_NOT_PROVIDED)
        ref = "000001274000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_termination_cause_avp__diameter_bad_answer(self):
        avp = TerminationCauseAVP(DIAMETER_BAD_ANSWER)
        ref = "000001274000000c00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test_termination_cause_avp__diameter_administrative(self):
        avp = TerminationCauseAVP(DIAMETER_ADMINISTRATIVE)
        ref = "000001274000000c00000004"
        self.assertEqual(avp.dump().hex(), ref)

    def test_termination_cause_avp__diameter_link_broken(self):
        avp = TerminationCauseAVP(DIAMETER_LINK_BROKEN)
        ref = "000001274000000c00000005"
        self.assertEqual(avp.dump().hex(), ref)

    def test_termination_cause_avp__diameter_auth_expired(self):
        avp = TerminationCauseAVP(DIAMETER_AUTH_EXPIRED)
        ref = "000001274000000c00000006"
        self.assertEqual(avp.dump().hex(), ref)

    def test_termination_cause_avp__diameter_user_moved(self):
        avp = TerminationCauseAVP(DIAMETER_USER_MOVED)
        ref = "000001274000000c00000007"
        self.assertEqual(avp.dump().hex(), ref)

    def test_termination_cause_avp__diameter_session_timeout(self):
        avp = TerminationCauseAVP(DIAMETER_SESSION_TIMEOUT)
        ref = "000001274000000c00000008"
        self.assertEqual(avp.dump().hex(), ref)


class TestOriginRealmAVP(unittest.TestCase):
    def test_origin_realm_avp__no_value(self):
        self.assertRaises(TypeError, OriginRealmAVP)

    def test_origin_realm_avp__repr_dunder(self):
        avp = OriginRealmAVP("ims.mncXXX.mccYYY.3gppnetwork.org")
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 296 [Origin-Realm] MANDATORY>")

    def test_origin_realm_avp__diameter_avp_convert_classmethod(self):
        avp = OriginRealmAVP("ims.mncXXX.mccYYY.3gppnetwork.org")

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_origin_realm_avp__1(self):
        avp = OriginRealmAVP("ims.mncXXX.mccYYY.3gppnetwork.org")
        ref = "0000012840000029696d732e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_origin_realm_avp__2(self):
        avp = OriginRealmAVP("esm")
        ref = "000001284000000b65736d00"
        self.assertEqual(avp.dump().hex(), ref)


class TestExperimentalResultAVP(unittest.TestCase):
    def test_experimental_result_avp__no_value(self):
        self.assertRaises(TypeError, ExperimentalResultAVP)

    def test_experimental_result_avp__repr_dunder(self):
        experimental_result_code_avp = ExperimentalResultCodeAVP(
                            DIAMETER_ERROR_SERVING_NODE_FEATURE_UNSUPPORTED
        )
        vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)

        avps = [experimental_result_code_avp, vendor_id_avp]
        avp = ExperimentalResultAVP(avps)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 297 [Experimental-Result]>")

    def test_experimental_result_avp__diameter_avp_convert_classmethod(self):
        experimental_result_code_avp = ExperimentalResultCodeAVP(
                            DIAMETER_ERROR_SERVING_NODE_FEATURE_UNSUPPORTED
        )
        vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)

        avps = [experimental_result_code_avp, vendor_id_avp]
        avp = ExperimentalResultAVP(avps)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_experimental_result_avp__serving_node_feature_unsupported(self):
        ref = "00000129000000200000012a4000000c000013940000010a4000000c000028af"
      
        experimental_result_code_avp = ExperimentalResultCodeAVP(
                            DIAMETER_ERROR_SERVING_NODE_FEATURE_UNSUPPORTED
        )
        vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)

        avps = [experimental_result_code_avp, vendor_id_avp]
        avp = ExperimentalResultAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)

    def test_experimental_result_avp__user_unknown(self):
        ref = "00000129000000200000012a4000000c000013890000010a4000000c000028af"
               
        experimental_result_code_avp = ExperimentalResultCodeAVP(
                                                    DIAMETER_ERROR_USER_UNKNOWN
        )
        vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)

        avps = [experimental_result_code_avp, vendor_id_avp]
        avp = ExperimentalResultAVP(avps)

        self.assertEqual(avp.dump().hex(), ref)


class TestExperimentalResultCodeAVP(unittest.TestCase):
    def test_experimental_result_code_avp__no_value(self):
        self.assertRaises(TypeError, ExperimentalResultCodeAVP)

    def test_result_code_avp__repr_dunder(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_FIRST_REGISTRATION)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 298 [Experimental-Result-Code] MANDATORY>")

    def test_result_code_avp__diameter_avp_convert_classmethod(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_FIRST_REGISTRATION)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_result_code_avp__diameter_first_registration(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_FIRST_REGISTRATION)
        ref = "0000012a4000000c000007d1"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_subsequent_registration(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_SUBSEQUENT_REGISTRATION)
        ref = "0000012a4000000c000007d2"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_unregistered_service(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_UNREGISTERED_SERVICE)
        ref = "0000012a4000000c000007d3"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_success_server_name_not_stored(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_SUCCESS_SERVER_NAME_NOT_STORED)
        ref = "0000012a4000000c000007d1"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_user_data_not_available(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_USER_DATA_NOT_AVAILABLE)
        ref = "0000012a4000000c00001004"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_prior_update_in_progress(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_PRIOR_UPDATE_IN_PROGRESS)
        ref = "0000012a4000000c00001005"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_authentication_data_unavailable(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE)
        ref = "0000012a4000000c00001055"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_error_user_unknown(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_USER_UNKNOWN)
        ref = "0000012a4000000c00001389"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_error_identities_dont_match(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_IDENTITIES_DONT_MATCH)
        ref = "0000012a4000000c0000138a"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_error_identity_not_registered(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_IDENTITY_NOT_REGISTERED)
        ref = "0000012a4000000c0000138b"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_error_roaming_not_allowed(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_ROAMING_NOT_ALLOWED)
        ref = "0000012a4000000c0000138c"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_error_identity_already_registered(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_IDENTITY_ALREADY_REGISTERED)
        ref = "0000012a4000000c0000138d"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_error_auth_scheme_not_supported(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_AUTH_SCHEME_NOT_SUPPORTED)
        ref = "0000012a4000000c0000138e"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_error_in_assignment_type(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_IN_ASSIGNMENT_TYPE)
        ref = "0000012a4000000c0000138f"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_error_too_much_data(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_TOO_MUCH_DATA)
        ref = "0000012a4000000c00001390"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_error_not_supported_user_data(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_NOT_SUPPORTED_USER_DATA)
        ref = "0000012a4000000c00001391"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_error_feature_unsupported(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_FEATURE_UNSUPPORTED)
        ref = "0000012a4000000c00001393"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_error_user_data_not_recognized(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_USER_DATA_NOT_RECOGNIZED)
        ref = "0000012a4000000c000013ec"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_error_operation_not_allowed(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_OPERATION_NOT_ALLOWED)
        ref = "0000012a4000000c000013ed"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_error_user_data_cannot_be_read(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_USER_DATA_CANNOT_BE_READ)
        ref = "0000012a4000000c000013ee"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_error_user_data_cannot_be_modified(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_USER_DATA_CANNOT_BE_MODIFIED)
        ref = "0000012a4000000c000013ef"
        self.assertEqual(avp.dump().hex(), ref)      

    def test_result_code_avp__diameter_error_user_data_cannot_be_notified(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_USER_DATA_CANNOT_BE_NOTIFIED)
        ref = "0000012a4000000c000013f0"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_error_transparent_data_out_of_sync(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_TRANSPARENT_DATA_OUT_OF_SYNC)
        ref = "0000012a4000000c000013f1"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_error_subs_data_absent(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_SUBS_DATA_ABSENT)
        ref = "0000012a4000000c000013f2"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_error_no_subscription_to_data(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_NO_SUBSCRIPTION_TO_DATA)
        ref = "0000012a4000000c000013f3"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_error_dsai_not_available(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_DSAI_NOT_AVAILABLE)
        ref = "0000012a4000000c000013f4"
        self.assertEqual(avp.dump().hex(), ref) 

    def test_result_code_avp__diameter_error_unknown_eps_subscription(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION)
        ref = "0000012a4000000c0000152c"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_error_rat_not_allowed(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_RAT_NOT_ALLOWED)
        ref = "0000012a4000000c0000152d"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_error_equipement_unknown(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_EQUIPMENT_UNKNOWN)
        ref = "0000012a4000000c0000152e"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_error_unknown_serving_node(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_UNKOWN_SERVING_NODE)
        ref = "0000012a4000000c0000152f"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_error_user_no_non_3gpp_subscription(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_USER_NO_NON_3GPP_SUBSCRIPTION)
        ref = "0000012a4000000c0000154a"
        self.assertEqual(avp.dump().hex(), ref)

    def test_result_code_avp__diameter_error_user_no_apn_subscription(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_USER_NO_APN_SUBSCRIPTION)
        ref = "0000012a4000000c0000154b"
        self.assertEqual(avp.dump().hex(), ref)
        
    def test_result_code_avp__diameter_error_rat_type_not_allowed(self):
        avp = ExperimentalResultCodeAVP(DIAMETER_ERROR_RAT_TYPE_NOT_ALLOWED)
        ref = "0000012a4000000c0000154c"
        self.assertEqual(avp.dump().hex(), ref)


class TestInbandSecurityIdAVP(unittest.TestCase):
    def test_inband_security_id_avp__no_value(self):
        self.assertRaises(TypeError, InbandSecurityIdAVP)

    def test_inband_security_id_avp__repr_dunder(self):
        avp = InbandSecurityIdAVP(INBAND_SECURITY_ID_NO_SECURITY)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 299 [Inband-Security-Id]>")

    def test_inband_security_id_avp__diameter_avp_convert_classmethod(self):
        avp = InbandSecurityIdAVP(INBAND_SECURITY_ID_NO_SECURITY)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_inband_security_id_avp__no_inband_security(self):
        avp = InbandSecurityIdAVP(INBAND_SECURITY_ID_NO_SECURITY)
        ref = "0000012b0000000c00000000"
        self.assertEqual(avp.dump().hex(), ref)

    def test_inband_security_id_avp__tls(self):
        avp = InbandSecurityIdAVP(INBAND_SECURITY_ID_TLS)
        ref = "0000012b0000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)


class TestAccountingRecordTypeAVP(unittest.TestCase):
    def test_accounting_record_type_avp__repr_dunder(self):
        avp = AccountingRecordTypeAVP()
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 480 [Accounting-Record-Type] MANDATORY>")

    def test_accounting_record_type_avp__diameter_avp_convert_classmethod(self):
        avp = AccountingRecordTypeAVP(ACCOUNTING_RECORD_TYPE_EVENT_RECORD)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_accounting_record_type_avp__event_record(self):
        avp = AccountingRecordTypeAVP(ACCOUNTING_RECORD_TYPE_EVENT_RECORD)
        ref = "000001e04000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_accounting_record_type_avp__start_record(self):
        avp = AccountingRecordTypeAVP(ACCOUNTING_RECORD_TYPE_START_RECORD)
        ref = "000001e04000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_accounting_record_type_avp__interim_record(self):
        avp = AccountingRecordTypeAVP(ACCOUNTING_RECORD_TYPE_INTERIM_RECORD)
        ref = "000001e04000000c00000003"
        self.assertEqual(avp.dump().hex(), ref)

    def test_accounting_record_type_avp__stop_record(self):
        avp = AccountingRecordTypeAVP(ACCOUNTING_RECORD_TYPE_STOP_RECORD)
        ref = "000001e04000000c00000004"
        self.assertEqual(avp.dump().hex(), ref)


class TestAccountingRealtimeRequiredAVP(unittest.TestCase):
    def test_accounting_realtime_required_avp__no_value(self):
        self.assertRaises(TypeError, AccountingRealtimeRequiredAVP)

    def test_accounting_realtime_required_avp__repr_dunder(self):
        avp = AccountingRealtimeRequiredAVP(ACCOUNTING_RECORD_TYPE_EVENT_RECORD)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 483 [Accounting-Realtime-Required] MANDATORY>")

    def test_accounting_realtime_required_avp__diameter_avp_convert_classmethod(self):
        avp = AccountingRealtimeRequiredAVP(ACCOUNTING_RECORD_TYPE_EVENT_RECORD)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_accounting_realtime_required_avp__deliver_and_grant(self):
        avp = AccountingRealtimeRequiredAVP(ACCOUNTING_REALTIME_REQUIRED_DELIVER_AND_GRANT)
        ref = "000001e34000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_accounting_realtime_required_avp__grant_and_store(self):
        avp = AccountingRealtimeRequiredAVP(ACCOUNTING_REALTIME_REQUIRED_GRANT_AND_STORE)
        ref = "000001e34000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)

    def test_accounting_realtime_required_avp__grant_and_lose(self):
        avp = AccountingRealtimeRequiredAVP(ACCOUNTING_REALTIME_REQUIRED_GRAND_AND_LOSE)
        ref = "000001e34000000c00000003"
        self.assertEqual(avp.dump().hex(), ref)


class TestAccountingRecordNumberAVP(unittest.TestCase):
    def test_accounting_record_number_avp__no_value(self):
        self.assertRaises(TypeError, AccountingRecordNumberAVP)

    def test_accounting_record_number_avp__repr_dunder(self):
        avp = AccountingRecordNumberAVP(1)
        self.assertEqual(avp.__repr__(), "<Diameter AVP: 485 [Accounting-Record-Number] MANDATORY>")

    def test_accounting_record_number_avp__diameter_avp_convert_classmethod(self):
        avp = AccountingRecordNumberAVP(1)

        custom = DiameterAVP.convert(avp)
        self.assertEqual(custom.code, avp.code)
        self.assertEqual(custom.flags, avp.flags)
        self.assertEqual(custom.length, avp.length)
        self.assertEqual(custom.vendor_id, avp.vendor_id)
        self.assertEqual(custom.data, avp.data)
        self.assertEqual(custom._padding, avp._padding)

    def test_accounting_record_number_avp__event_record(self):
        avp = AccountingRecordNumberAVP(1)
        ref = "000001e54000000c00000001"
        self.assertEqual(avp.dump().hex(), ref)

    def test_accounting_record_number_avp__start_record(self):
        avp = AccountingRecordNumberAVP(2)
        ref = "000001e54000000c00000002"
        self.assertEqual(avp.dump().hex(), ref)


if __name__ == "__main__":
    unittest.main()