# -*- coding: utf-8 -*-
"""
    test.test_proxy
    ~~~~~~~~~~~~~~~

    This module contains the Bromelia proxy unittests.

    :copyright: (c) 2021 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia._internal_utils import _convert_config_to_connection_obj
from bromelia.avps import *
from bromelia.constants import *
from bromelia.messages import CapabilitiesExchangeAnswer
from bromelia.messages import CapabilitiesExchangeRequest
from bromelia.messages import DeviceWatchdogAnswer
from bromelia.messages import DeviceWatchdogRequest
from bromelia.messages import DisconnectPeerAnswer
from bromelia.messages import DisconnectPeerRequest
from bromelia.proxy import DiameterBaseProxy


# @unittest.SkipTest
class TestDiameterBaseProxy(unittest.TestCase):
    def setUp(self):
        config = {
                "MODE": "CLIENT",
                "TRANSPORT_TYPE": "TCP",
                "APPLICATIONS": [],
                "LOCAL_NODE_HOSTNAME": "client.network",
                "LOCAL_NODE_REALM": "network",
                "LOCAL_NODE_IP_ADDRESS": "127.0.0.1",
                "LOCAL_NODE_PORT": None,
                "PEER_NODE_HOSTNAME": "server.network",
                "PEER_NODE_REALM": "network",
                "PEER_NODE_IP_ADDRESS": "127.0.0.1",
                "PEER_NODE_PORT": None,
                "WATCHDOG_TIMEOUT": 30
            }
        self.connection = _convert_config_to_connection_obj(config)

    def test__load_cea(self):
        cea = DiameterBaseProxy.load_cea(self.connection)

        #: Check Diameter Header
        self.assertEqual(cea.header.version, DIAMETER_VERSION)
        self.assertEqual(cea.header.flags, FLAG_RESPONSE)
        self.assertEqual(cea.header.length.hex(), "000088")
        self.assertEqual(cea.header.get_length(), 136)
        self.assertEqual(cea.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(cea.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(cea.__repr__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 7 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(cea.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[0].vendor_id)
        self.assertEqual(cea.avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[0].get_length(), 12)
        self.assertEqual(cea.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(cea.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(cea.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[1].vendor_id)
        self.assertEqual(cea.avps[1].length.hex(), "000016")
        self.assertEqual(cea.avps[1].get_length(), 22)
        self.assertEqual(cea.avps[1].data, b"client.network")
        self.assertEqual(cea.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(cea.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cea.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[2].vendor_id)
        self.assertEqual(cea.avps[2].length.hex(), "00000f")
        self.assertEqual(cea.avps[2].get_length(), 15)
        self.assertEqual(cea.avps[2].data, b"network")
        self.assertEqual(cea.avps[2].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(cea.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cea.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[3].vendor_id)
        self.assertEqual(cea.avps[3].length.hex(), "00000e")
        self.assertEqual(cea.avps[3].get_length(), 14)
        self.assertEqual(cea.avps[3].data.hex(), "00017f000001")
        self.assertEqual(cea.avps[3].get_ip_address(), "127.0.0.1")
        self.assertEqual(cea.avps[3].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(cea.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cea.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[4].vendor_id)
        self.assertEqual(cea.avps[4].length.hex(), "00000c")
        self.assertEqual(cea.avps[4].get_length(), 12)
        self.assertEqual(cea.avps[4].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(cea.avps[4].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(cea.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cea.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[5].vendor_id)
        self.assertEqual(cea.avps[5].length.hex(), "000017")
        self.assertEqual(cea.avps[5].get_length(), 23)
        self.assertEqual(cea.avps[5].data, b"Python bromelia")
        self.assertEqual(cea.avps[5].get_padding_length(), 1)

        #: Auth-Application-Id AVP
        self.assertEqual(cea.auth_application_id_avp.dump().hex(), "000001024000000c00000000")
        self.assertEqual(cea.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[6].vendor_id)
        self.assertEqual(cea.avps[6].length.hex(), "00000c")
        self.assertEqual(cea.avps[6].get_length(), 12)
        self.assertEqual(cea.avps[6].data, DIAMETER_APPLICATION_DEFAULT)
        self.assertIsNone(cea.avps[6].get_padding_length())

    def test__load_cer(self):
        cer = DiameterBaseProxy.load_cer(self.connection)

        #: Check Diameter Header
        self.assertEqual(cer.header.version, DIAMETER_VERSION)
        self.assertEqual(cer.header.flags, FLAG_REQUEST)
        self.assertEqual(cer.header.length.hex(), "00007c")
        self.assertEqual(cer.header.get_length(), 124)
        self.assertEqual(cer.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(cer.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(cer.__repr__(), "<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 6 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(cer.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(cer.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(cer.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(cer.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[0].vendor_id)
        self.assertEqual(cer.avps[0].length.hex(), "000016")
        self.assertEqual(cer.avps[0].get_length(), 22)
        self.assertEqual(cer.avps[0].data, b"client.network")
        self.assertEqual(cer.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(cer.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cer.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cer.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(cer.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[1].vendor_id)
        self.assertEqual(cer.avps[1].length.hex(), "00000f")
        self.assertEqual(cer.avps[1].get_length(), 15)
        self.assertEqual(cer.avps[1].data, b"network")
        self.assertEqual(cer.avps[1].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(cer.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cer.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cer.avps[2].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(cer.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[2].vendor_id)
        self.assertEqual(cer.avps[2].length.hex(), "00000e")
        self.assertEqual(cer.avps[2].get_length(), 14)
        self.assertEqual(cer.avps[2].data.hex(), "00017f000001")
        self.assertEqual(cer.avps[2].get_ip_address(), "127.0.0.1")
        self.assertEqual(cer.avps[2].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(cer.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cer.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cer.avps[3].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cer.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[3].vendor_id)
        self.assertEqual(cer.avps[3].length.hex(), "00000c")
        self.assertEqual(cer.avps[3].get_length(), 12)
        self.assertEqual(cer.avps[3].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(cer.avps[3].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(cer.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cer.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cer.avps[4].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(cer.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[4].vendor_id)
        self.assertEqual(cer.avps[4].length.hex(), "000017")
        self.assertEqual(cer.avps[4].get_length(), 23)
        self.assertEqual(cer.avps[4].data, b"Python bromelia")
        self.assertEqual(cer.avps[4].get_padding_length(), 1)

        #: Firmware-Revision AVP
        self.assertEqual(cer.firmware_revision_avp.dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(cer.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(cer.avps[5].code, FIRMWARE_REVISION_AVP_CODE)
        self.assertEqual(cer.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[5].vendor_id)
        self.assertEqual(cer.avps[5].length.hex(), "00000c")
        self.assertEqual(cer.avps[5].get_length(), 12)
        self.assertEqual(cer.avps[5].data, FIRMWARE_VERSION)
        self.assertIsNone(cer.avps[5].get_padding_length())

    def test__load_dwa(self):
        dwa = DiameterBaseProxy.load_dwa(self.connection)

        #: Check Diameter Header
        self.assertEqual(dwa.header.version, DIAMETER_VERSION)
        self.assertEqual(dwa.header.flags, FLAG_RESPONSE)
        self.assertEqual(dwa.header.length.hex(), "000048")
        self.assertEqual(dwa.header.get_length(), 72)
        self.assertEqual(dwa.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(dwa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(dwa.__repr__(), "<Diameter Message: 280 [DWA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(dwa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(dwa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(dwa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(dwa.avps[0].vendor_id)
        self.assertEqual(dwa.avps[0].length.hex(), "00000c")
        self.assertEqual(dwa.avps[0].get_length(), 12)
        self.assertEqual(dwa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(dwa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(dwa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(dwa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(dwa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(dwa.avps[1].vendor_id)
        self.assertEqual(dwa.avps[1].length.hex(), "000016")
        self.assertEqual(dwa.avps[1].get_length(), 22)
        self.assertEqual(dwa.avps[1].data, b"client.network")
        self.assertEqual(dwa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(dwa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(dwa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(dwa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(dwa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(dwa.avps[2].vendor_id)
        self.assertEqual(dwa.avps[2].length.hex(), "00000f")
        self.assertEqual(dwa.avps[2].get_length(), 15)
        self.assertEqual(dwa.avps[2].data, b"network")
        self.assertEqual(dwa.avps[2].get_padding_length(), 1)

    def test__load_dwr(self):
        dwr = DiameterBaseProxy.load_dwr(self.connection)

        #: Check Diameter Header
        self.assertEqual(dwr.header.version, DIAMETER_VERSION)
        self.assertEqual(dwr.header.flags, FLAG_REQUEST)
        self.assertEqual(dwr.header.length.hex(), "00003c")
        self.assertEqual(dwr.header.get_length(), 60)
        self.assertEqual(dwr.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(dwr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(dwr.__repr__(), "<Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 2 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(dwr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(dwr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(dwr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(dwr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(dwr.avps[0].vendor_id)
        self.assertEqual(dwr.avps[0].length.hex(), "000016")
        self.assertEqual(dwr.avps[0].get_length(), 22)
        self.assertEqual(dwr.avps[0].data, b"client.network")
        self.assertEqual(dwr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(dwr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(dwr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(dwr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(dwr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(dwr.avps[1].vendor_id)
        self.assertEqual(dwr.avps[1].length.hex(), "00000f")
        self.assertEqual(dwr.avps[1].get_length(), 15)
        self.assertEqual(dwr.avps[1].data, b"network")
        self.assertEqual(dwr.avps[1].get_padding_length(), 1)

    def test__load_dpa(self):
        dpa = DiameterBaseProxy.load_dpa(self.connection)

        #: Check Diameter Header
        self.assertEqual(dpa.header.version, DIAMETER_VERSION)
        self.assertEqual(dpa.header.flags, FLAG_RESPONSE)
        self.assertEqual(dpa.header.length.hex(), "000048")
        self.assertEqual(dpa.header.get_length(), 72)
        self.assertEqual(dpa.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(dpa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(dpa.__repr__(), "<Diameter Message: 282 [DPA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(dpa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(dpa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(dpa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(dpa.avps[0].vendor_id)
        self.assertEqual(dpa.avps[0].length.hex(), "00000c")
        self.assertEqual(dpa.avps[0].get_length(), 12)
        self.assertEqual(dpa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(dpa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(dpa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(dpa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(dpa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(dpa.avps[1].vendor_id)
        self.assertEqual(dpa.avps[1].length.hex(), "000016")
        self.assertEqual(dpa.avps[1].get_length(), 22)
        self.assertEqual(dpa.avps[1].data, b"client.network")
        self.assertEqual(dpa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(dpa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(dpa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(dpa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(dpa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(dpa.avps[2].vendor_id)
        self.assertEqual(dpa.avps[2].length.hex(), "00000f")
        self.assertEqual(dpa.avps[2].get_length(), 15)
        self.assertEqual(dpa.avps[2].data, b"network")
        self.assertEqual(dpa.avps[2].get_padding_length(), 1)

    def test__load_dpr(self):
        dpr = DiameterBaseProxy.load_dpr(self.connection)

        #: Check Diameter Header
        self.assertEqual(dpr.header.version, DIAMETER_VERSION)
        self.assertEqual(dpr.header.flags, FLAG_REQUEST)
        self.assertEqual(dpr.header.length.hex(), "000048")
        self.assertEqual(dpr.header.get_length(), 72)
        self.assertEqual(dpr.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(dpr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(dpr.__repr__(), "<Diameter Message: 282 [DPR] REQ, 0 [Diameter common message], 3 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(dpr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(dpr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(dpr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(dpr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(dpr.avps[0].vendor_id)
        self.assertEqual(dpr.avps[0].length.hex(), "000016")
        self.assertEqual(dpr.avps[0].get_length(), 22)
        self.assertEqual(dpr.avps[0].data, b"client.network")
        self.assertEqual(dpr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(dpr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(dpr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(dpr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(dpr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(dpr.avps[1].vendor_id)
        self.assertEqual(dpr.avps[1].length.hex(), "00000f")
        self.assertEqual(dpr.avps[1].get_length(), 15)
        self.assertEqual(dpr.avps[1].data, b"network")
        self.assertEqual(dpr.avps[1].get_padding_length(), 1)

    def test__diameter_base_proxy__get_default_messages(self):
        #: Initial setup
        proxy = DiameterBaseProxy(self.connection)
        base = proxy.get_default_messages()

        #: Initial check
        self.assertTrue(isinstance(base.cea, CapabilitiesExchangeAnswer))
        self.assertTrue(isinstance(base.cer, CapabilitiesExchangeRequest))
        self.assertTrue(isinstance(base.dwa, DeviceWatchdogAnswer))
        self.assertTrue(isinstance(base.dwr, DeviceWatchdogRequest))
        self.assertTrue(isinstance(base.dpa, DisconnectPeerAnswer))
        self.assertTrue(isinstance(base.dpr, DisconnectPeerRequest))

        ##: Check Capabilities-Exchange-Answer

        #: Check Diameter Header
        self.assertEqual(base.cea.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cea.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.cea.header.length.hex(), "000088")
        self.assertEqual(base.cea.header.get_length(), 136)
        self.assertEqual(base.cea.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cea.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cea.__repr__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 7 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.cea.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[0].vendor_id)
        self.assertEqual(base.cea.avps[0].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[0].get_length(), 12)
        self.assertEqual(base.cea.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.cea.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.cea.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[1].vendor_id)
        self.assertEqual(base.cea.avps[1].length.hex(), "000016")
        self.assertEqual(base.cea.avps[1].get_length(), 22)
        self.assertEqual(base.cea.avps[1].data, b"client.network")
        self.assertEqual(base.cea.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cea.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[2].vendor_id)
        self.assertEqual(base.cea.avps[2].length.hex(), "00000f")
        self.assertEqual(base.cea.avps[2].get_length(), 15)
        self.assertEqual(base.cea.avps[2].data, b"network")
        self.assertEqual(base.cea.avps[2].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cea.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[3].vendor_id)
        self.assertEqual(base.cea.avps[3].length.hex(), "00000e")
        self.assertEqual(base.cea.avps[3].get_length(), 14)
        self.assertEqual(base.cea.avps[3].data.hex(), "00017f000001")
        self.assertEqual(base.cea.avps[3].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cea.avps[3].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cea.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[4].vendor_id)
        self.assertEqual(base.cea.avps[4].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[4].get_length(), 12)
        self.assertEqual(base.cea.avps[4].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cea.avps[4].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cea.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[5].vendor_id)
        self.assertEqual(base.cea.avps[5].length.hex(), "000017")
        self.assertEqual(base.cea.avps[5].get_length(), 23)
        self.assertEqual(base.cea.avps[5].data, b"Python bromelia")
        self.assertEqual(base.cea.avps[5].get_padding_length(), 1)

        #: Auth-Application-Id AVP
        self.assertEqual(base.cea.auth_application_id_avp.dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[6].vendor_id)
        self.assertEqual(base.cea.avps[6].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[6].get_length(), 12)
        self.assertEqual(base.cea.avps[6].data, DIAMETER_APPLICATION_DEFAULT)
        self.assertIsNone(base.cea.avps[6].get_padding_length())


        ##: Check Capabilities-Exchange-Request

        #: Check Diameter Header
        self.assertEqual(base.cer.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cer.header.flags, FLAG_REQUEST)
        self.assertEqual(base.cer.header.length.hex(), "00007c")
        self.assertEqual(base.cer.header.get_length(), 124)
        self.assertEqual(base.cer.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cer.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cer.__repr__(), "<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 6 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.cer.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cer.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[0].vendor_id)
        self.assertEqual(base.cer.avps[0].length.hex(), "000016")
        self.assertEqual(base.cer.avps[0].get_length(), 22)
        self.assertEqual(base.cer.avps[0].data, b"client.network")
        self.assertEqual(base.cer.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cer.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cer.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[1].vendor_id)
        self.assertEqual(base.cer.avps[1].length.hex(), "00000f")
        self.assertEqual(base.cer.avps[1].get_length(), 15)
        self.assertEqual(base.cer.avps[1].data, b"network")
        self.assertEqual(base.cer.avps[1].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cer.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cer.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[2].vendor_id)
        self.assertEqual(base.cer.avps[2].length.hex(), "00000e")
        self.assertEqual(base.cer.avps[2].get_length(), 14)
        self.assertEqual(base.cer.avps[2].data.hex(), "00017f000001")
        self.assertEqual(base.cer.avps[2].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cer.avps[2].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cer.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cer.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[3].vendor_id)
        self.assertEqual(base.cer.avps[3].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[3].get_length(), 12)
        self.assertEqual(base.cer.avps[3].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cer.avps[3].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cer.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cer.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[4].vendor_id)
        self.assertEqual(base.cer.avps[4].length.hex(), "000017")
        self.assertEqual(base.cer.avps[4].get_length(), 23)
        self.assertEqual(base.cer.avps[4].data, b"Python bromelia")
        self.assertEqual(base.cer.avps[4].get_padding_length(), 1)

        #: Firmware-Revision AVP
        self.assertEqual(base.cer.firmware_revision_avp.dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].code, FIRMWARE_REVISION_AVP_CODE)
        self.assertEqual(base.cer.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[5].vendor_id)
        self.assertEqual(base.cer.avps[5].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[5].get_length(), 12)
        self.assertEqual(base.cer.avps[5].data, FIRMWARE_VERSION)
        self.assertIsNone(base.cer.avps[5].get_padding_length())


        ##: Check Device-Watchdog-Answer

        #: Check Diameter Header
        self.assertEqual(base.dwa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dwa.header.length.hex(), "000048")
        self.assertEqual(base.dwa.header.get_length(), 72)
        self.assertEqual(base.dwa.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwa.__repr__(), "<Diameter Message: 280 [DWA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dwa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dwa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dwa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[0].vendor_id)
        self.assertEqual(base.dwa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dwa.avps[0].get_length(), 12)
        self.assertEqual(base.dwa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dwa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dwa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[1].vendor_id)
        self.assertEqual(base.dwa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dwa.avps[1].get_length(), 22)
        self.assertEqual(base.dwa.avps[1].data, b"client.network")
        self.assertEqual(base.dwa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[2].vendor_id)
        self.assertEqual(base.dwa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dwa.avps[2].get_length(), 15)
        self.assertEqual(base.dwa.avps[2].data, b"network")
        self.assertEqual(base.dwa.avps[2].get_padding_length(), 1)


        ##: Check Device-Watchdog-Request

        #: Check Diameter Header
        self.assertEqual(base.dwr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dwr.header.length.hex(), "00003c")
        self.assertEqual(base.dwr.header.get_length(), 60)
        self.assertEqual(base.dwr.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwr.__repr__(), "<Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 2 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dwr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[0].vendor_id)
        self.assertEqual(base.dwr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dwr.avps[0].get_length(), 22)
        self.assertEqual(base.dwr.avps[0].data, b"client.network")
        self.assertEqual(base.dwr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[1].vendor_id)
        self.assertEqual(base.dwr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dwr.avps[1].get_length(), 15)
        self.assertEqual(base.dwr.avps[1].data, b"network")
        self.assertEqual(base.dwr.avps[1].get_padding_length(), 1)


        ##: Check Disconnect-Peer-Answer

        #: Check Diameter Header
        self.assertEqual(base.dpa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dpa.header.length.hex(), "000048")
        self.assertEqual(base.dpa.header.get_length(), 72)
        self.assertEqual(base.dpa.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpa.__repr__(), "<Diameter Message: 282 [DPA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dpa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dpa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dpa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[0].vendor_id)
        self.assertEqual(base.dpa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dpa.avps[0].get_length(), 12)
        self.assertEqual(base.dpa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dpa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dpa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[1].vendor_id)
        self.assertEqual(base.dpa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dpa.avps[1].get_length(), 22)
        self.assertEqual(base.dpa.avps[1].data, b"client.network")
        self.assertEqual(base.dpa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[2].vendor_id)
        self.assertEqual(base.dpa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dpa.avps[2].get_length(), 15)
        self.assertEqual(base.dpa.avps[2].data, b"network")
        self.assertEqual(base.dpa.avps[2].get_padding_length(), 1)


        ##: Check Disconnect-Peer-Request

        #: Check Diameter Header
        self.assertEqual(base.dpr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dpr.header.length.hex(), "000048")
        self.assertEqual(base.dpr.header.get_length(), 72)
        self.assertEqual(base.dpr.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpr.__repr__(), "<Diameter Message: 282 [DPR] REQ, 0 [Diameter common message], 3 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dpr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[0].vendor_id)
        self.assertEqual(base.dpr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dpr.avps[0].get_length(), 22)
        self.assertEqual(base.dpr.avps[0].data, b"client.network")
        self.assertEqual(base.dpr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[1].vendor_id)
        self.assertEqual(base.dpr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dpr.avps[1].get_length(), 15)
        self.assertEqual(base.dpr.avps[1].data, b"network")
        self.assertEqual(base.dpr.avps[1].get_padding_length(), 1)

    def test__diameter_base_proxy__get_custom_messages__no_list(self):
        #: Initial setup
        proxy = DiameterBaseProxy(self.connection)
        base = proxy.get_custom_messages()

        #: Initial check
        self.assertTrue(isinstance(base.cea, CapabilitiesExchangeAnswer))
        self.assertTrue(isinstance(base.cer, CapabilitiesExchangeRequest))
        self.assertTrue(isinstance(base.dwa, DeviceWatchdogAnswer))
        self.assertTrue(isinstance(base.dwr, DeviceWatchdogRequest))
        self.assertTrue(isinstance(base.dpa, DisconnectPeerAnswer))
        self.assertTrue(isinstance(base.dpr, DisconnectPeerRequest))

        ##: Check Capabilities-Exchange-Answer

        #: Check Diameter Header
        self.assertEqual(base.cea.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cea.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.cea.header.length.hex(), "000088")
        self.assertEqual(base.cea.header.get_length(), 136)
        self.assertEqual(base.cea.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cea.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cea.__repr__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 7 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.cea.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[0].vendor_id)
        self.assertEqual(base.cea.avps[0].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[0].get_length(), 12)
        self.assertEqual(base.cea.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.cea.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.cea.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[1].vendor_id)
        self.assertEqual(base.cea.avps[1].length.hex(), "000016")
        self.assertEqual(base.cea.avps[1].get_length(), 22)
        self.assertEqual(base.cea.avps[1].data, b"client.network")
        self.assertEqual(base.cea.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cea.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[2].vendor_id)
        self.assertEqual(base.cea.avps[2].length.hex(), "00000f")
        self.assertEqual(base.cea.avps[2].get_length(), 15)
        self.assertEqual(base.cea.avps[2].data, b"network")
        self.assertEqual(base.cea.avps[2].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cea.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[3].vendor_id)
        self.assertEqual(base.cea.avps[3].length.hex(), "00000e")
        self.assertEqual(base.cea.avps[3].get_length(), 14)
        self.assertEqual(base.cea.avps[3].data.hex(), "00017f000001")
        self.assertEqual(base.cea.avps[3].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cea.avps[3].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cea.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[4].vendor_id)
        self.assertEqual(base.cea.avps[4].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[4].get_length(), 12)
        self.assertEqual(base.cea.avps[4].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cea.avps[4].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cea.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[5].vendor_id)
        self.assertEqual(base.cea.avps[5].length.hex(), "000017")
        self.assertEqual(base.cea.avps[5].get_length(), 23)
        self.assertEqual(base.cea.avps[5].data, b"Python bromelia")
        self.assertEqual(base.cea.avps[5].get_padding_length(), 1)

        #: Auth-Application-Id AVP
        self.assertEqual(base.cea.auth_application_id_avp.dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[6].vendor_id)
        self.assertEqual(base.cea.avps[6].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[6].get_length(), 12)
        self.assertEqual(base.cea.avps[6].data, DIAMETER_APPLICATION_DEFAULT)
        self.assertIsNone(base.cea.avps[6].get_padding_length())


        ##: Check Capabilities-Exchange-Request

        #: Check Diameter Header
        self.assertEqual(base.cer.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cer.header.flags, FLAG_REQUEST)
        self.assertEqual(base.cer.header.length.hex(), "00007c")
        self.assertEqual(base.cer.header.get_length(), 124)
        self.assertEqual(base.cer.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cer.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cer.__repr__(), "<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 6 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.cer.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cer.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[0].vendor_id)
        self.assertEqual(base.cer.avps[0].length.hex(), "000016")
        self.assertEqual(base.cer.avps[0].get_length(), 22)
        self.assertEqual(base.cer.avps[0].data, b"client.network")
        self.assertEqual(base.cer.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cer.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cer.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[1].vendor_id)
        self.assertEqual(base.cer.avps[1].length.hex(), "00000f")
        self.assertEqual(base.cer.avps[1].get_length(), 15)
        self.assertEqual(base.cer.avps[1].data, b"network")
        self.assertEqual(base.cer.avps[1].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cer.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cer.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[2].vendor_id)
        self.assertEqual(base.cer.avps[2].length.hex(), "00000e")
        self.assertEqual(base.cer.avps[2].get_length(), 14)
        self.assertEqual(base.cer.avps[2].data.hex(), "00017f000001")
        self.assertEqual(base.cer.avps[2].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cer.avps[2].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cer.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cer.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[3].vendor_id)
        self.assertEqual(base.cer.avps[3].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[3].get_length(), 12)
        self.assertEqual(base.cer.avps[3].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cer.avps[3].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cer.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cer.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[4].vendor_id)
        self.assertEqual(base.cer.avps[4].length.hex(), "000017")
        self.assertEqual(base.cer.avps[4].get_length(), 23)
        self.assertEqual(base.cer.avps[4].data, b"Python bromelia")
        self.assertEqual(base.cer.avps[4].get_padding_length(), 1)

        #: Firmware-Revision AVP
        self.assertEqual(base.cer.firmware_revision_avp.dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].code, FIRMWARE_REVISION_AVP_CODE)
        self.assertEqual(base.cer.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[5].vendor_id)
        self.assertEqual(base.cer.avps[5].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[5].get_length(), 12)
        self.assertEqual(base.cer.avps[5].data, FIRMWARE_VERSION)
        self.assertIsNone(base.cer.avps[5].get_padding_length())


        ##: Check Device-Watchdog-Answer

        #: Check Diameter Header
        self.assertEqual(base.dwa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dwa.header.length.hex(), "000048")
        self.assertEqual(base.dwa.header.get_length(), 72)
        self.assertEqual(base.dwa.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwa.__repr__(), "<Diameter Message: 280 [DWA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dwa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dwa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dwa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[0].vendor_id)
        self.assertEqual(base.dwa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dwa.avps[0].get_length(), 12)
        self.assertEqual(base.dwa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dwa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dwa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[1].vendor_id)
        self.assertEqual(base.dwa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dwa.avps[1].get_length(), 22)
        self.assertEqual(base.dwa.avps[1].data, b"client.network")
        self.assertEqual(base.dwa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[2].vendor_id)
        self.assertEqual(base.dwa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dwa.avps[2].get_length(), 15)
        self.assertEqual(base.dwa.avps[2].data, b"network")
        self.assertEqual(base.dwa.avps[2].get_padding_length(), 1)


        ##: Check Device-Watchdog-Request

        #: Check Diameter Header
        self.assertEqual(base.dwr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dwr.header.length.hex(), "00003c")
        self.assertEqual(base.dwr.header.get_length(), 60)
        self.assertEqual(base.dwr.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwr.__repr__(), "<Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 2 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dwr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[0].vendor_id)
        self.assertEqual(base.dwr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dwr.avps[0].get_length(), 22)
        self.assertEqual(base.dwr.avps[0].data, b"client.network")
        self.assertEqual(base.dwr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[1].vendor_id)
        self.assertEqual(base.dwr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dwr.avps[1].get_length(), 15)
        self.assertEqual(base.dwr.avps[1].data, b"network")
        self.assertEqual(base.dwr.avps[1].get_padding_length(), 1)


        ##: Check Disconnect-Peer-Answer

        #: Check Diameter Header
        self.assertEqual(base.dpa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dpa.header.length.hex(), "000048")
        self.assertEqual(base.dpa.header.get_length(), 72)
        self.assertEqual(base.dpa.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpa.__repr__(), "<Diameter Message: 282 [DPA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dpa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dpa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dpa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[0].vendor_id)
        self.assertEqual(base.dpa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dpa.avps[0].get_length(), 12)
        self.assertEqual(base.dpa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dpa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dpa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[1].vendor_id)
        self.assertEqual(base.dpa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dpa.avps[1].get_length(), 22)
        self.assertEqual(base.dpa.avps[1].data, b"client.network")
        self.assertEqual(base.dpa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[2].vendor_id)
        self.assertEqual(base.dpa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dpa.avps[2].get_length(), 15)
        self.assertEqual(base.dpa.avps[2].data, b"network")
        self.assertEqual(base.dpa.avps[2].get_padding_length(), 1)


        ##: Check Disconnect-Peer-Request

        #: Check Diameter Header
        self.assertEqual(base.dpr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dpr.header.length.hex(), "000048")
        self.assertEqual(base.dpr.header.get_length(), 72)
        self.assertEqual(base.dpr.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpr.__repr__(), "<Diameter Message: 282 [DPR] REQ, 0 [Diameter common message], 3 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dpr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[0].vendor_id)
        self.assertEqual(base.dpr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dpr.avps[0].get_length(), 22)
        self.assertEqual(base.dpr.avps[0].data, b"client.network")
        self.assertEqual(base.dpr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[1].vendor_id)
        self.assertEqual(base.dpr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dpr.avps[1].get_length(), 15)
        self.assertEqual(base.dpr.avps[1].data, b"network")
        self.assertEqual(base.dpr.avps[1].get_padding_length(), 1)

    def test__diameter_base_proxy__get_custom_messages__custom_cea(self):
        #: Initial setup
        proxy = DiameterBaseProxy(self.connection)

        cea = DiameterBaseProxy.load_cea(self.connection)
        cea.append(OriginStateIdAVP(64))
        cea.append(SupportedVendorIdAVP(VENDOR_ID_3GPP))
        cea.append(SupportedVendorIdAVP(VENDOR_ID_ETSI))

        base = proxy.get_custom_messages([cea])

        #: Initial check
        self.assertTrue(isinstance(base.cea, CapabilitiesExchangeAnswer))
        self.assertTrue(isinstance(base.cer, CapabilitiesExchangeRequest))
        self.assertTrue(isinstance(base.dwa, DeviceWatchdogAnswer))
        self.assertTrue(isinstance(base.dwr, DeviceWatchdogRequest))
        self.assertTrue(isinstance(base.dpa, DisconnectPeerAnswer))
        self.assertTrue(isinstance(base.dpr, DisconnectPeerRequest))

        ##: Check Capabilities-Exchange-Answer

        #: Check Diameter Header
        self.assertEqual(base.cea.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cea.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.cea.header.length.hex(), "0000ac")
        self.assertEqual(base.cea.header.get_length(), 172)
        self.assertEqual(base.cea.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cea.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cea.__repr__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 10 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.cea.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[0].vendor_id)
        self.assertEqual(base.cea.avps[0].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[0].get_length(), 12)
        self.assertEqual(base.cea.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.cea.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.cea.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[1].vendor_id)
        self.assertEqual(base.cea.avps[1].length.hex(), "000016")
        self.assertEqual(base.cea.avps[1].get_length(), 22)
        self.assertEqual(base.cea.avps[1].data, b"client.network")
        self.assertEqual(base.cea.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cea.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[2].vendor_id)
        self.assertEqual(base.cea.avps[2].length.hex(), "00000f")
        self.assertEqual(base.cea.avps[2].get_length(), 15)
        self.assertEqual(base.cea.avps[2].data, b"network")
        self.assertEqual(base.cea.avps[2].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cea.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[3].vendor_id)
        self.assertEqual(base.cea.avps[3].length.hex(), "00000e")
        self.assertEqual(base.cea.avps[3].get_length(), 14)
        self.assertEqual(base.cea.avps[3].data.hex(), "00017f000001")
        self.assertEqual(base.cea.avps[3].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cea.avps[3].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cea.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[4].vendor_id)
        self.assertEqual(base.cea.avps[4].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[4].get_length(), 12)
        self.assertEqual(base.cea.avps[4].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cea.avps[4].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cea.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[5].vendor_id)
        self.assertEqual(base.cea.avps[5].length.hex(), "000017")
        self.assertEqual(base.cea.avps[5].get_length(), 23)
        self.assertEqual(base.cea.avps[5].data, b"Python bromelia")
        self.assertEqual(base.cea.avps[5].get_padding_length(), 1)

        #: Auth-Application-Id AVP
        self.assertEqual(base.cea.auth_application_id_avp.dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[6].vendor_id)
        self.assertEqual(base.cea.avps[6].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[6].get_length(), 12)
        self.assertEqual(base.cea.avps[6].data, DIAMETER_APPLICATION_DEFAULT)
        self.assertIsNone(base.cea.avps[6].get_padding_length())

        #: Origin-State-Id AVP
        self.assertEqual(base.cea.origin_state_id_avp.dump().hex(), "000001164000000c00000040")
        self.assertEqual(base.cea.avps[7].dump().hex(), "000001164000000c00000040")
        self.assertEqual(base.cea.avps[7].code, ORIGIN_STATE_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[7].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[7].vendor_id)
        self.assertEqual(base.cea.avps[7].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[7].get_length(), 12)
        self.assertEqual(base.cea.avps[7].data.hex(), "00000040")
        self.assertIsNone(base.cea.avps[7].get_padding_length())

        #: Supported-Vendor-Id AVP
        self.assertEqual(base.cea.supported_vendor_id_avp.dump().hex(), "000001094000000c000028af")
        self.assertEqual(base.cea.avps[8].dump().hex(), "000001094000000c000028af")
        self.assertEqual(base.cea.avps[8].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[8].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[8].vendor_id)
        self.assertEqual(base.cea.avps[8].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[8].get_length(), 12)
        self.assertEqual(base.cea.avps[8].data, VENDOR_ID_3GPP)
        self.assertIsNone(base.cea.avps[8].get_padding_length())

        #: Supported-Vendor-Id AVP
        self.assertEqual(base.cea.supported_vendor_id_avp__1.dump().hex(), "000001094000000c000032db")
        self.assertEqual(base.cea.avps[9].dump().hex(), "000001094000000c000032db")
        self.assertEqual(base.cea.avps[9].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[9].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[9].vendor_id)
        self.assertEqual(base.cea.avps[9].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[9].get_length(), 12)
        self.assertEqual(base.cea.avps[9].data, VENDOR_ID_ETSI)
        self.assertIsNone(base.cea.avps[9].get_padding_length())


        ##: Check Capabilities-Exchange-Request

        #: Check Diameter Header
        self.assertEqual(base.cer.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cer.header.flags, FLAG_REQUEST)
        self.assertEqual(base.cer.header.length.hex(), "00007c")
        self.assertEqual(base.cer.header.get_length(), 124)
        self.assertEqual(base.cer.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cer.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cer.__repr__(), "<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 6 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.cer.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cer.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[0].vendor_id)
        self.assertEqual(base.cer.avps[0].length.hex(), "000016")
        self.assertEqual(base.cer.avps[0].get_length(), 22)
        self.assertEqual(base.cer.avps[0].data, b"client.network")
        self.assertEqual(base.cer.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cer.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cer.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[1].vendor_id)
        self.assertEqual(base.cer.avps[1].length.hex(), "00000f")
        self.assertEqual(base.cer.avps[1].get_length(), 15)
        self.assertEqual(base.cer.avps[1].data, b"network")
        self.assertEqual(base.cer.avps[1].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cer.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cer.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[2].vendor_id)
        self.assertEqual(base.cer.avps[2].length.hex(), "00000e")
        self.assertEqual(base.cer.avps[2].get_length(), 14)
        self.assertEqual(base.cer.avps[2].data.hex(), "00017f000001")
        self.assertEqual(base.cer.avps[2].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cer.avps[2].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cer.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cer.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[3].vendor_id)
        self.assertEqual(base.cer.avps[3].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[3].get_length(), 12)
        self.assertEqual(base.cer.avps[3].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cer.avps[3].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cer.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cer.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[4].vendor_id)
        self.assertEqual(base.cer.avps[4].length.hex(), "000017")
        self.assertEqual(base.cer.avps[4].get_length(), 23)
        self.assertEqual(base.cer.avps[4].data, b"Python bromelia")
        self.assertEqual(base.cer.avps[4].get_padding_length(), 1)

        #: Firmware-Revision AVP
        self.assertEqual(base.cer.firmware_revision_avp.dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].code, FIRMWARE_REVISION_AVP_CODE)
        self.assertEqual(base.cer.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[5].vendor_id)
        self.assertEqual(base.cer.avps[5].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[5].get_length(), 12)
        self.assertEqual(base.cer.avps[5].data, FIRMWARE_VERSION)
        self.assertIsNone(base.cer.avps[5].get_padding_length())


        ##: Check Device-Watchdog-Answer

        #: Check Diameter Header
        self.assertEqual(base.dwa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dwa.header.length.hex(), "000048")
        self.assertEqual(base.dwa.header.get_length(), 72)
        self.assertEqual(base.dwa.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwa.__repr__(), "<Diameter Message: 280 [DWA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dwa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dwa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dwa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[0].vendor_id)
        self.assertEqual(base.dwa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dwa.avps[0].get_length(), 12)
        self.assertEqual(base.dwa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dwa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dwa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[1].vendor_id)
        self.assertEqual(base.dwa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dwa.avps[1].get_length(), 22)
        self.assertEqual(base.dwa.avps[1].data, b"client.network")
        self.assertEqual(base.dwa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[2].vendor_id)
        self.assertEqual(base.dwa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dwa.avps[2].get_length(), 15)
        self.assertEqual(base.dwa.avps[2].data, b"network")
        self.assertEqual(base.dwa.avps[2].get_padding_length(), 1)


        ##: Check Device-Watchdog-Request

        #: Check Diameter Header
        self.assertEqual(base.dwr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dwr.header.length.hex(), "00003c")
        self.assertEqual(base.dwr.header.get_length(), 60)
        self.assertEqual(base.dwr.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwr.__repr__(), "<Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 2 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dwr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[0].vendor_id)
        self.assertEqual(base.dwr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dwr.avps[0].get_length(), 22)
        self.assertEqual(base.dwr.avps[0].data, b"client.network")
        self.assertEqual(base.dwr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[1].vendor_id)
        self.assertEqual(base.dwr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dwr.avps[1].get_length(), 15)
        self.assertEqual(base.dwr.avps[1].data, b"network")
        self.assertEqual(base.dwr.avps[1].get_padding_length(), 1)


        ##: Check Disconnect-Peer-Answer

        #: Check Diameter Header
        self.assertEqual(base.dpa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dpa.header.length.hex(), "000048")
        self.assertEqual(base.dpa.header.get_length(), 72)
        self.assertEqual(base.dpa.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpa.__repr__(), "<Diameter Message: 282 [DPA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dpa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dpa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dpa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[0].vendor_id)
        self.assertEqual(base.dpa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dpa.avps[0].get_length(), 12)
        self.assertEqual(base.dpa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dpa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dpa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[1].vendor_id)
        self.assertEqual(base.dpa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dpa.avps[1].get_length(), 22)
        self.assertEqual(base.dpa.avps[1].data, b"client.network")
        self.assertEqual(base.dpa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[2].vendor_id)
        self.assertEqual(base.dpa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dpa.avps[2].get_length(), 15)
        self.assertEqual(base.dpa.avps[2].data, b"network")
        self.assertEqual(base.dpa.avps[2].get_padding_length(), 1)


        ##: Check Disconnect-Peer-Request

        #: Check Diameter Header
        self.assertEqual(base.dpr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dpr.header.length.hex(), "000048")
        self.assertEqual(base.dpr.header.get_length(), 72)
        self.assertEqual(base.dpr.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpr.__repr__(), "<Diameter Message: 282 [DPR] REQ, 0 [Diameter common message], 3 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dpr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[0].vendor_id)
        self.assertEqual(base.dpr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dpr.avps[0].get_length(), 22)
        self.assertEqual(base.dpr.avps[0].data, b"client.network")
        self.assertEqual(base.dpr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[1].vendor_id)
        self.assertEqual(base.dpr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dpr.avps[1].get_length(), 15)
        self.assertEqual(base.dpr.avps[1].data, b"network")
        self.assertEqual(base.dpr.avps[1].get_padding_length(), 1)

    def test__diameter_base_proxy__get_custom_messages__custom_cer(self):
        #: Initial setup
        proxy = DiameterBaseProxy(self.connection)

        cer = DiameterBaseProxy.load_cer(self.connection)
        cer.append(OriginStateIdAVP(64))
        cer.append(SupportedVendorIdAVP(VENDOR_ID_3GPP))
        cer.append(SupportedVendorIdAVP(VENDOR_ID_ETSI))

        base = proxy.get_custom_messages([cer])

        #: Initial check
        self.assertTrue(isinstance(base.cea, CapabilitiesExchangeAnswer))
        self.assertTrue(isinstance(base.cer, CapabilitiesExchangeRequest))
        self.assertTrue(isinstance(base.dwa, DeviceWatchdogAnswer))
        self.assertTrue(isinstance(base.dwr, DeviceWatchdogRequest))
        self.assertTrue(isinstance(base.dpa, DisconnectPeerAnswer))
        self.assertTrue(isinstance(base.dpr, DisconnectPeerRequest))

        ##: Check Capabilities-Exchange-Answer

        #: Check Diameter Header
        self.assertEqual(base.cea.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cea.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.cea.header.length.hex(), "000088")
        self.assertEqual(base.cea.header.get_length(), 136)
        self.assertEqual(base.cea.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cea.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cea.__repr__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 7 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.cea.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[0].vendor_id)
        self.assertEqual(base.cea.avps[0].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[0].get_length(), 12)
        self.assertEqual(base.cea.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.cea.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.cea.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[1].vendor_id)
        self.assertEqual(base.cea.avps[1].length.hex(), "000016")
        self.assertEqual(base.cea.avps[1].get_length(), 22)
        self.assertEqual(base.cea.avps[1].data, b"client.network")
        self.assertEqual(base.cea.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cea.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[2].vendor_id)
        self.assertEqual(base.cea.avps[2].length.hex(), "00000f")
        self.assertEqual(base.cea.avps[2].get_length(), 15)
        self.assertEqual(base.cea.avps[2].data, b"network")
        self.assertEqual(base.cea.avps[2].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cea.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[3].vendor_id)
        self.assertEqual(base.cea.avps[3].length.hex(), "00000e")
        self.assertEqual(base.cea.avps[3].get_length(), 14)
        self.assertEqual(base.cea.avps[3].data.hex(), "00017f000001")
        self.assertEqual(base.cea.avps[3].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cea.avps[3].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cea.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[4].vendor_id)
        self.assertEqual(base.cea.avps[4].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[4].get_length(), 12)
        self.assertEqual(base.cea.avps[4].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cea.avps[4].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cea.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[5].vendor_id)
        self.assertEqual(base.cea.avps[5].length.hex(), "000017")
        self.assertEqual(base.cea.avps[5].get_length(), 23)
        self.assertEqual(base.cea.avps[5].data, b"Python bromelia")
        self.assertEqual(base.cea.avps[5].get_padding_length(), 1)

        #: Auth-Application-Id AVP
        self.assertEqual(base.cea.auth_application_id_avp.dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[6].vendor_id)
        self.assertEqual(base.cea.avps[6].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[6].get_length(), 12)
        self.assertEqual(base.cea.avps[6].data, DIAMETER_APPLICATION_DEFAULT)
        self.assertIsNone(base.cea.avps[6].get_padding_length())


        ##: Check Capabilities-Exchange-Request

        #: Check Diameter Header
        self.assertEqual(base.cer.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cer.header.flags, FLAG_REQUEST)
        self.assertEqual(base.cer.header.length.hex(), "0000a0")
        self.assertEqual(base.cer.header.get_length(), 160)
        self.assertEqual(base.cer.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cer.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cer.__repr__(), "<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 9 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.cer.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cer.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[0].vendor_id)
        self.assertEqual(base.cer.avps[0].length.hex(), "000016")
        self.assertEqual(base.cer.avps[0].get_length(), 22)
        self.assertEqual(base.cer.avps[0].data, b"client.network")
        self.assertEqual(base.cer.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cer.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cer.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[1].vendor_id)
        self.assertEqual(base.cer.avps[1].length.hex(), "00000f")
        self.assertEqual(base.cer.avps[1].get_length(), 15)
        self.assertEqual(base.cer.avps[1].data, b"network")
        self.assertEqual(base.cer.avps[1].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cer.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cer.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[2].vendor_id)
        self.assertEqual(base.cer.avps[2].length.hex(), "00000e")
        self.assertEqual(base.cer.avps[2].get_length(), 14)
        self.assertEqual(base.cer.avps[2].data.hex(), "00017f000001")
        self.assertEqual(base.cer.avps[2].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cer.avps[2].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cer.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cer.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[3].vendor_id)
        self.assertEqual(base.cer.avps[3].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[3].get_length(), 12)
        self.assertEqual(base.cer.avps[3].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cer.avps[3].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cer.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cer.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[4].vendor_id)
        self.assertEqual(base.cer.avps[4].length.hex(), "000017")
        self.assertEqual(base.cer.avps[4].get_length(), 23)
        self.assertEqual(base.cer.avps[4].data, b"Python bromelia")
        self.assertEqual(base.cer.avps[4].get_padding_length(), 1)

        #: Firmware-Revision AVP
        self.assertEqual(base.cer.firmware_revision_avp.dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].code, FIRMWARE_REVISION_AVP_CODE)
        self.assertEqual(base.cer.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[5].vendor_id)
        self.assertEqual(base.cer.avps[5].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[5].get_length(), 12)
        self.assertEqual(base.cer.avps[5].data, FIRMWARE_VERSION)
        self.assertIsNone(base.cer.avps[5].get_padding_length())

        #: Origin-State-Id AVP
        self.assertEqual(base.cer.origin_state_id_avp.dump().hex(), "000001164000000c00000040")
        self.assertEqual(base.cer.avps[6].dump().hex(), "000001164000000c00000040")
        self.assertEqual(base.cer.avps[6].code, ORIGIN_STATE_ID_AVP_CODE)
        self.assertEqual(base.cer.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[6].vendor_id)
        self.assertEqual(base.cer.avps[6].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[6].get_length(), 12)
        self.assertEqual(base.cer.avps[6].data.hex(), "00000040")
        self.assertIsNone(base.cer.avps[6].get_padding_length())

        #: Supported-Vendor-Id AVP
        self.assertEqual(base.cer.supported_vendor_id_avp.dump().hex(), "000001094000000c000028af")
        self.assertEqual(base.cer.avps[7].dump().hex(), "000001094000000c000028af")
        self.assertEqual(base.cer.avps[7].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cer.avps[7].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[7].vendor_id)
        self.assertEqual(base.cer.avps[7].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[7].get_length(), 12)
        self.assertEqual(base.cer.avps[7].data, VENDOR_ID_3GPP)
        self.assertIsNone(base.cer.avps[7].get_padding_length())

        #: Supported-Vendor-Id AVP
        self.assertEqual(base.cer.supported_vendor_id_avp__1.dump().hex(), "000001094000000c000032db")
        self.assertEqual(base.cer.avps[8].dump().hex(), "000001094000000c000032db")
        self.assertEqual(base.cer.avps[8].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cer.avps[8].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[8].vendor_id)
        self.assertEqual(base.cer.avps[8].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[8].get_length(), 12)
        self.assertEqual(base.cer.avps[8].data, VENDOR_ID_ETSI)
        self.assertIsNone(base.cer.avps[8].get_padding_length())


        ##: Check Device-Watchdog-Answer

        #: Check Diameter Header
        self.assertEqual(base.dwa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dwa.header.length.hex(), "000048")
        self.assertEqual(base.dwa.header.get_length(), 72)
        self.assertEqual(base.dwa.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwa.__repr__(), "<Diameter Message: 280 [DWA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dwa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dwa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dwa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[0].vendor_id)
        self.assertEqual(base.dwa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dwa.avps[0].get_length(), 12)
        self.assertEqual(base.dwa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dwa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dwa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[1].vendor_id)
        self.assertEqual(base.dwa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dwa.avps[1].get_length(), 22)
        self.assertEqual(base.dwa.avps[1].data, b"client.network")
        self.assertEqual(base.dwa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[2].vendor_id)
        self.assertEqual(base.dwa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dwa.avps[2].get_length(), 15)
        self.assertEqual(base.dwa.avps[2].data, b"network")
        self.assertEqual(base.dwa.avps[2].get_padding_length(), 1)


        ##: Check Device-Watchdog-Request

        #: Check Diameter Header
        self.assertEqual(base.dwr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dwr.header.length.hex(), "00003c")
        self.assertEqual(base.dwr.header.get_length(), 60)
        self.assertEqual(base.dwr.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwr.__repr__(), "<Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 2 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dwr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[0].vendor_id)
        self.assertEqual(base.dwr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dwr.avps[0].get_length(), 22)
        self.assertEqual(base.dwr.avps[0].data, b"client.network")
        self.assertEqual(base.dwr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[1].vendor_id)
        self.assertEqual(base.dwr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dwr.avps[1].get_length(), 15)
        self.assertEqual(base.dwr.avps[1].data, b"network")
        self.assertEqual(base.dwr.avps[1].get_padding_length(), 1)


        ##: Check Disconnect-Peer-Answer

        #: Check Diameter Header
        self.assertEqual(base.dpa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dpa.header.length.hex(), "000048")
        self.assertEqual(base.dpa.header.get_length(), 72)
        self.assertEqual(base.dpa.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpa.__repr__(), "<Diameter Message: 282 [DPA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dpa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dpa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dpa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[0].vendor_id)
        self.assertEqual(base.dpa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dpa.avps[0].get_length(), 12)
        self.assertEqual(base.dpa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dpa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dpa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[1].vendor_id)
        self.assertEqual(base.dpa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dpa.avps[1].get_length(), 22)
        self.assertEqual(base.dpa.avps[1].data, b"client.network")
        self.assertEqual(base.dpa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[2].vendor_id)
        self.assertEqual(base.dpa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dpa.avps[2].get_length(), 15)
        self.assertEqual(base.dpa.avps[2].data, b"network")
        self.assertEqual(base.dpa.avps[2].get_padding_length(), 1)


        ##: Check Disconnect-Peer-Request

        #: Check Diameter Header
        self.assertEqual(base.dpr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dpr.header.length.hex(), "000048")
        self.assertEqual(base.dpr.header.get_length(), 72)
        self.assertEqual(base.dpr.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpr.__repr__(), "<Diameter Message: 282 [DPR] REQ, 0 [Diameter common message], 3 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dpr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[0].vendor_id)
        self.assertEqual(base.dpr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dpr.avps[0].get_length(), 22)
        self.assertEqual(base.dpr.avps[0].data, b"client.network")
        self.assertEqual(base.dpr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[1].vendor_id)
        self.assertEqual(base.dpr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dpr.avps[1].get_length(), 15)
        self.assertEqual(base.dpr.avps[1].data, b"network")
        self.assertEqual(base.dpr.avps[1].get_padding_length(), 1)

    def test__diameter_base_proxy__get_custom_messages__custom_dwa(self):
        #: Initial setup
        proxy = DiameterBaseProxy(self.connection)
        base = proxy.get_custom_messages()

        dwa = DiameterBaseProxy.load_dwa(self.connection)
        dwa.append(OriginStateIdAVP(64))
        dwa.append(SupportedVendorIdAVP(VENDOR_ID_3GPP))
        dwa.append(SupportedVendorIdAVP(VENDOR_ID_ETSI))

        base = proxy.get_custom_messages([dwa])

        #: Initial check
        self.assertTrue(isinstance(base.cea, CapabilitiesExchangeAnswer))
        self.assertTrue(isinstance(base.cer, CapabilitiesExchangeRequest))
        self.assertTrue(isinstance(base.dwa, DeviceWatchdogAnswer))
        self.assertTrue(isinstance(base.dwr, DeviceWatchdogRequest))
        self.assertTrue(isinstance(base.dpa, DisconnectPeerAnswer))
        self.assertTrue(isinstance(base.dpr, DisconnectPeerRequest))

        ##: Check Capabilities-Exchange-Answer

        #: Check Diameter Header
        self.assertEqual(base.cea.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cea.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.cea.header.length.hex(), "000088")
        self.assertEqual(base.cea.header.get_length(), 136)
        self.assertEqual(base.cea.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cea.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cea.__repr__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 7 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.cea.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[0].vendor_id)
        self.assertEqual(base.cea.avps[0].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[0].get_length(), 12)
        self.assertEqual(base.cea.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.cea.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.cea.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[1].vendor_id)
        self.assertEqual(base.cea.avps[1].length.hex(), "000016")
        self.assertEqual(base.cea.avps[1].get_length(), 22)
        self.assertEqual(base.cea.avps[1].data, b"client.network")
        self.assertEqual(base.cea.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cea.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[2].vendor_id)
        self.assertEqual(base.cea.avps[2].length.hex(), "00000f")
        self.assertEqual(base.cea.avps[2].get_length(), 15)
        self.assertEqual(base.cea.avps[2].data, b"network")
        self.assertEqual(base.cea.avps[2].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cea.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[3].vendor_id)
        self.assertEqual(base.cea.avps[3].length.hex(), "00000e")
        self.assertEqual(base.cea.avps[3].get_length(), 14)
        self.assertEqual(base.cea.avps[3].data.hex(), "00017f000001")
        self.assertEqual(base.cea.avps[3].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cea.avps[3].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cea.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[4].vendor_id)
        self.assertEqual(base.cea.avps[4].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[4].get_length(), 12)
        self.assertEqual(base.cea.avps[4].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cea.avps[4].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cea.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[5].vendor_id)
        self.assertEqual(base.cea.avps[5].length.hex(), "000017")
        self.assertEqual(base.cea.avps[5].get_length(), 23)
        self.assertEqual(base.cea.avps[5].data, b"Python bromelia")
        self.assertEqual(base.cea.avps[5].get_padding_length(), 1)

        #: Auth-Application-Id AVP
        self.assertEqual(base.cea.auth_application_id_avp.dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[6].vendor_id)
        self.assertEqual(base.cea.avps[6].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[6].get_length(), 12)
        self.assertEqual(base.cea.avps[6].data, DIAMETER_APPLICATION_DEFAULT)
        self.assertIsNone(base.cea.avps[6].get_padding_length())


        ##: Check Capabilities-Exchange-Request

        #: Check Diameter Header
        self.assertEqual(base.cer.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cer.header.flags, FLAG_REQUEST)
        self.assertEqual(base.cer.header.length.hex(), "00007c")
        self.assertEqual(base.cer.header.get_length(), 124)
        self.assertEqual(base.cer.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cer.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cer.__repr__(), "<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 6 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.cer.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cer.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[0].vendor_id)
        self.assertEqual(base.cer.avps[0].length.hex(), "000016")
        self.assertEqual(base.cer.avps[0].get_length(), 22)
        self.assertEqual(base.cer.avps[0].data, b"client.network")
        self.assertEqual(base.cer.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cer.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cer.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[1].vendor_id)
        self.assertEqual(base.cer.avps[1].length.hex(), "00000f")
        self.assertEqual(base.cer.avps[1].get_length(), 15)
        self.assertEqual(base.cer.avps[1].data, b"network")
        self.assertEqual(base.cer.avps[1].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cer.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cer.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[2].vendor_id)
        self.assertEqual(base.cer.avps[2].length.hex(), "00000e")
        self.assertEqual(base.cer.avps[2].get_length(), 14)
        self.assertEqual(base.cer.avps[2].data.hex(), "00017f000001")
        self.assertEqual(base.cer.avps[2].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cer.avps[2].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cer.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cer.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[3].vendor_id)
        self.assertEqual(base.cer.avps[3].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[3].get_length(), 12)
        self.assertEqual(base.cer.avps[3].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cer.avps[3].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cer.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cer.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[4].vendor_id)
        self.assertEqual(base.cer.avps[4].length.hex(), "000017")
        self.assertEqual(base.cer.avps[4].get_length(), 23)
        self.assertEqual(base.cer.avps[4].data, b"Python bromelia")
        self.assertEqual(base.cer.avps[4].get_padding_length(), 1)

        #: Firmware-Revision AVP
        self.assertEqual(base.cer.firmware_revision_avp.dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].code, FIRMWARE_REVISION_AVP_CODE)
        self.assertEqual(base.cer.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[5].vendor_id)
        self.assertEqual(base.cer.avps[5].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[5].get_length(), 12)
        self.assertEqual(base.cer.avps[5].data, FIRMWARE_VERSION)
        self.assertIsNone(base.cer.avps[5].get_padding_length())


        ##: Check Device-Watchdog-Answer

        #: Check Diameter Header
        self.assertEqual(base.dwa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dwa.header.length.hex(), "00006c")
        self.assertEqual(base.dwa.header.get_length(), 108)
        self.assertEqual(base.dwa.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwa.__repr__(), "<Diameter Message: 280 [DWA], 0 [Diameter common message], 6 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dwa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dwa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dwa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[0].vendor_id)
        self.assertEqual(base.dwa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dwa.avps[0].get_length(), 12)
        self.assertEqual(base.dwa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dwa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dwa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[1].vendor_id)
        self.assertEqual(base.dwa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dwa.avps[1].get_length(), 22)
        self.assertEqual(base.dwa.avps[1].data, b"client.network")
        self.assertEqual(base.dwa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[2].vendor_id)
        self.assertEqual(base.dwa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dwa.avps[2].get_length(), 15)
        self.assertEqual(base.dwa.avps[2].data, b"network")
        self.assertEqual(base.dwa.avps[2].get_padding_length(), 1)

        #: Origin-State-Id AVP
        self.assertEqual(base.dwa.origin_state_id_avp.dump().hex(), "000001164000000c00000040")
        self.assertEqual(base.dwa.avps[3].dump().hex(), "000001164000000c00000040")
        self.assertEqual(base.dwa.avps[3].code, ORIGIN_STATE_ID_AVP_CODE)
        self.assertEqual(base.dwa.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[3].vendor_id)
        self.assertEqual(base.dwa.avps[3].length.hex(), "00000c")
        self.assertEqual(base.dwa.avps[3].get_length(), 12)
        self.assertEqual(base.dwa.avps[3].data.hex(), "00000040")
        self.assertIsNone(base.dwa.avps[3].get_padding_length())

        #: Supported-Vendor-Id AVP
        self.assertEqual(base.dwa.supported_vendor_id_avp.dump().hex(), "000001094000000c000028af")
        self.assertEqual(base.dwa.avps[4].dump().hex(), "000001094000000c000028af")
        self.assertEqual(base.dwa.avps[4].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(base.dwa.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[4].vendor_id)
        self.assertEqual(base.dwa.avps[4].length.hex(), "00000c")
        self.assertEqual(base.dwa.avps[4].get_length(), 12)
        self.assertEqual(base.dwa.avps[4].data, VENDOR_ID_3GPP)
        self.assertIsNone(base.dwa.avps[4].get_padding_length())

        #: Supported-Vendor-Id AVP
        self.assertEqual(base.dwa.supported_vendor_id_avp__1.dump().hex(), "000001094000000c000032db")
        self.assertEqual(base.dwa.avps[5].dump().hex(), "000001094000000c000032db")
        self.assertEqual(base.dwa.avps[5].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(base.dwa.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[5].vendor_id)
        self.assertEqual(base.dwa.avps[5].length.hex(), "00000c")
        self.assertEqual(base.dwa.avps[5].get_length(), 12)
        self.assertEqual(base.dwa.avps[5].data, VENDOR_ID_ETSI)
        self.assertIsNone(base.dwa.avps[5].get_padding_length())


        ##: Check Device-Watchdog-Request

        #: Check Diameter Header
        self.assertEqual(base.dwr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dwr.header.length.hex(), "00003c")
        self.assertEqual(base.dwr.header.get_length(), 60)
        self.assertEqual(base.dwr.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwr.__repr__(), "<Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 2 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dwr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[0].vendor_id)
        self.assertEqual(base.dwr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dwr.avps[0].get_length(), 22)
        self.assertEqual(base.dwr.avps[0].data, b"client.network")
        self.assertEqual(base.dwr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[1].vendor_id)
        self.assertEqual(base.dwr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dwr.avps[1].get_length(), 15)
        self.assertEqual(base.dwr.avps[1].data, b"network")
        self.assertEqual(base.dwr.avps[1].get_padding_length(), 1)


        ##: Check Disconnect-Peer-Answer

        #: Check Diameter Header
        self.assertEqual(base.dpa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dpa.header.length.hex(), "000048")
        self.assertEqual(base.dpa.header.get_length(), 72)
        self.assertEqual(base.dpa.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpa.__repr__(), "<Diameter Message: 282 [DPA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dpa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dpa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dpa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[0].vendor_id)
        self.assertEqual(base.dpa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dpa.avps[0].get_length(), 12)
        self.assertEqual(base.dpa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dpa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dpa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[1].vendor_id)
        self.assertEqual(base.dpa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dpa.avps[1].get_length(), 22)
        self.assertEqual(base.dpa.avps[1].data, b"client.network")
        self.assertEqual(base.dpa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[2].vendor_id)
        self.assertEqual(base.dpa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dpa.avps[2].get_length(), 15)
        self.assertEqual(base.dpa.avps[2].data, b"network")
        self.assertEqual(base.dpa.avps[2].get_padding_length(), 1)


        ##: Check Disconnect-Peer-Request

        #: Check Diameter Header
        self.assertEqual(base.dpr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dpr.header.length.hex(), "000048")
        self.assertEqual(base.dpr.header.get_length(), 72)
        self.assertEqual(base.dpr.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpr.__repr__(), "<Diameter Message: 282 [DPR] REQ, 0 [Diameter common message], 3 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dpr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[0].vendor_id)
        self.assertEqual(base.dpr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dpr.avps[0].get_length(), 22)
        self.assertEqual(base.dpr.avps[0].data, b"client.network")
        self.assertEqual(base.dpr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[1].vendor_id)
        self.assertEqual(base.dpr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dpr.avps[1].get_length(), 15)
        self.assertEqual(base.dpr.avps[1].data, b"network")
        self.assertEqual(base.dpr.avps[1].get_padding_length(), 1)

    def test__diameter_base_proxy__get_custom_messages__custom_dwr(self):
        #: Initial setup
        proxy = DiameterBaseProxy(self.connection)
        base = proxy.get_custom_messages()

        dwr = DiameterBaseProxy.load_dwr(self.connection)
        dwr.append(OriginStateIdAVP(64))
        dwr.append(SupportedVendorIdAVP(VENDOR_ID_3GPP))
        dwr.append(SupportedVendorIdAVP(VENDOR_ID_ETSI))

        base = proxy.get_custom_messages([dwr])

        #: Initial check
        self.assertTrue(isinstance(base.cea, CapabilitiesExchangeAnswer))
        self.assertTrue(isinstance(base.cer, CapabilitiesExchangeRequest))
        self.assertTrue(isinstance(base.dwa, DeviceWatchdogAnswer))
        self.assertTrue(isinstance(base.dwr, DeviceWatchdogRequest))
        self.assertTrue(isinstance(base.dpa, DisconnectPeerAnswer))
        self.assertTrue(isinstance(base.dpr, DisconnectPeerRequest))

        ##: Check Capabilities-Exchange-Answer

        #: Check Diameter Header
        self.assertEqual(base.cea.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cea.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.cea.header.length.hex(), "000088")
        self.assertEqual(base.cea.header.get_length(), 136)
        self.assertEqual(base.cea.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cea.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cea.__repr__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 7 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.cea.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[0].vendor_id)
        self.assertEqual(base.cea.avps[0].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[0].get_length(), 12)
        self.assertEqual(base.cea.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.cea.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.cea.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[1].vendor_id)
        self.assertEqual(base.cea.avps[1].length.hex(), "000016")
        self.assertEqual(base.cea.avps[1].get_length(), 22)
        self.assertEqual(base.cea.avps[1].data, b"client.network")
        self.assertEqual(base.cea.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cea.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[2].vendor_id)
        self.assertEqual(base.cea.avps[2].length.hex(), "00000f")
        self.assertEqual(base.cea.avps[2].get_length(), 15)
        self.assertEqual(base.cea.avps[2].data, b"network")
        self.assertEqual(base.cea.avps[2].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cea.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[3].vendor_id)
        self.assertEqual(base.cea.avps[3].length.hex(), "00000e")
        self.assertEqual(base.cea.avps[3].get_length(), 14)
        self.assertEqual(base.cea.avps[3].data.hex(), "00017f000001")
        self.assertEqual(base.cea.avps[3].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cea.avps[3].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cea.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[4].vendor_id)
        self.assertEqual(base.cea.avps[4].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[4].get_length(), 12)
        self.assertEqual(base.cea.avps[4].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cea.avps[4].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cea.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[5].vendor_id)
        self.assertEqual(base.cea.avps[5].length.hex(), "000017")
        self.assertEqual(base.cea.avps[5].get_length(), 23)
        self.assertEqual(base.cea.avps[5].data, b"Python bromelia")
        self.assertEqual(base.cea.avps[5].get_padding_length(), 1)

        #: Auth-Application-Id AVP
        self.assertEqual(base.cea.auth_application_id_avp.dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[6].vendor_id)
        self.assertEqual(base.cea.avps[6].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[6].get_length(), 12)
        self.assertEqual(base.cea.avps[6].data, DIAMETER_APPLICATION_DEFAULT)
        self.assertIsNone(base.cea.avps[6].get_padding_length())


        ##: Check Capabilities-Exchange-Request

        #: Check Diameter Header
        self.assertEqual(base.cer.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cer.header.flags, FLAG_REQUEST)
        self.assertEqual(base.cer.header.length.hex(), "00007c")
        self.assertEqual(base.cer.header.get_length(), 124)
        self.assertEqual(base.cer.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cer.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cer.__repr__(), "<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 6 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.cer.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cer.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[0].vendor_id)
        self.assertEqual(base.cer.avps[0].length.hex(), "000016")
        self.assertEqual(base.cer.avps[0].get_length(), 22)
        self.assertEqual(base.cer.avps[0].data, b"client.network")
        self.assertEqual(base.cer.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cer.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cer.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[1].vendor_id)
        self.assertEqual(base.cer.avps[1].length.hex(), "00000f")
        self.assertEqual(base.cer.avps[1].get_length(), 15)
        self.assertEqual(base.cer.avps[1].data, b"network")
        self.assertEqual(base.cer.avps[1].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cer.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cer.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[2].vendor_id)
        self.assertEqual(base.cer.avps[2].length.hex(), "00000e")
        self.assertEqual(base.cer.avps[2].get_length(), 14)
        self.assertEqual(base.cer.avps[2].data.hex(), "00017f000001")
        self.assertEqual(base.cer.avps[2].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cer.avps[2].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cer.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cer.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[3].vendor_id)
        self.assertEqual(base.cer.avps[3].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[3].get_length(), 12)
        self.assertEqual(base.cer.avps[3].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cer.avps[3].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cer.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cer.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[4].vendor_id)
        self.assertEqual(base.cer.avps[4].length.hex(), "000017")
        self.assertEqual(base.cer.avps[4].get_length(), 23)
        self.assertEqual(base.cer.avps[4].data, b"Python bromelia")
        self.assertEqual(base.cer.avps[4].get_padding_length(), 1)

        #: Firmware-Revision AVP
        self.assertEqual(base.cer.firmware_revision_avp.dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].code, FIRMWARE_REVISION_AVP_CODE)
        self.assertEqual(base.cer.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[5].vendor_id)
        self.assertEqual(base.cer.avps[5].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[5].get_length(), 12)
        self.assertEqual(base.cer.avps[5].data, FIRMWARE_VERSION)
        self.assertIsNone(base.cer.avps[5].get_padding_length())


        ##: Check Device-Watchdog-Answer

        #: Check Diameter Header
        self.assertEqual(base.dwa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dwa.header.length.hex(), "000048")
        self.assertEqual(base.dwa.header.get_length(), 72)
        self.assertEqual(base.dwa.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwa.__repr__(), "<Diameter Message: 280 [DWA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dwa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dwa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dwa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[0].vendor_id)
        self.assertEqual(base.dwa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dwa.avps[0].get_length(), 12)
        self.assertEqual(base.dwa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dwa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dwa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[1].vendor_id)
        self.assertEqual(base.dwa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dwa.avps[1].get_length(), 22)
        self.assertEqual(base.dwa.avps[1].data, b"client.network")
        self.assertEqual(base.dwa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[2].vendor_id)
        self.assertEqual(base.dwa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dwa.avps[2].get_length(), 15)
        self.assertEqual(base.dwa.avps[2].data, b"network")
        self.assertEqual(base.dwa.avps[2].get_padding_length(), 1)


        ##: Check Device-Watchdog-Request

        #: Check Diameter Header
        self.assertEqual(base.dwr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dwr.header.length.hex(), "000060")
        self.assertEqual(base.dwr.header.get_length(), 96)
        self.assertEqual(base.dwr.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwr.__repr__(), "<Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 5 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dwr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[0].vendor_id)
        self.assertEqual(base.dwr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dwr.avps[0].get_length(), 22)
        self.assertEqual(base.dwr.avps[0].data, b"client.network")
        self.assertEqual(base.dwr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[1].vendor_id)
        self.assertEqual(base.dwr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dwr.avps[1].get_length(), 15)
        self.assertEqual(base.dwr.avps[1].data, b"network")
        self.assertEqual(base.dwr.avps[1].get_padding_length(), 1)

        #: Origin-State-Id AVP
        self.assertEqual(base.dwr.origin_state_id_avp.dump().hex(), "000001164000000c00000040")
        self.assertEqual(base.dwr.avps[2].dump().hex(), "000001164000000c00000040")
        self.assertEqual(base.dwr.avps[2].code, ORIGIN_STATE_ID_AVP_CODE)
        self.assertEqual(base.dwr.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[2].vendor_id)
        self.assertEqual(base.dwr.avps[2].length.hex(), "00000c")
        self.assertEqual(base.dwr.avps[2].get_length(), 12)
        self.assertEqual(base.dwr.avps[2].data.hex(), "00000040")
        self.assertIsNone(base.dwr.avps[2].get_padding_length())

        #: Supported-Vendor-Id AVP
        self.assertEqual(base.dwr.supported_vendor_id_avp.dump().hex(), "000001094000000c000028af")
        self.assertEqual(base.dwr.avps[3].dump().hex(), "000001094000000c000028af")
        self.assertEqual(base.dwr.avps[3].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(base.dwr.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[3].vendor_id)
        self.assertEqual(base.dwr.avps[3].length.hex(), "00000c")
        self.assertEqual(base.dwr.avps[3].get_length(), 12)
        self.assertEqual(base.dwr.avps[3].data, VENDOR_ID_3GPP)
        self.assertIsNone(base.dwr.avps[3].get_padding_length())

        #: Supported-Vendor-Id AVP
        self.assertEqual(base.dwr.supported_vendor_id_avp__1.dump().hex(), "000001094000000c000032db")
        self.assertEqual(base.dwr.avps[4].dump().hex(), "000001094000000c000032db")
        self.assertEqual(base.dwr.avps[4].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(base.dwr.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[4].vendor_id)
        self.assertEqual(base.dwr.avps[4].length.hex(), "00000c")
        self.assertEqual(base.dwr.avps[4].get_length(), 12)
        self.assertEqual(base.dwr.avps[4].data, VENDOR_ID_ETSI)
        self.assertIsNone(base.dwr.avps[4].get_padding_length())


        ##: Check Disconnect-Peer-Answer

        #: Check Diameter Header
        self.assertEqual(base.dpa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dpa.header.length.hex(), "000048")
        self.assertEqual(base.dpa.header.get_length(), 72)
        self.assertEqual(base.dpa.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpa.__repr__(), "<Diameter Message: 282 [DPA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dpa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dpa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dpa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[0].vendor_id)
        self.assertEqual(base.dpa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dpa.avps[0].get_length(), 12)
        self.assertEqual(base.dpa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dpa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dpa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[1].vendor_id)
        self.assertEqual(base.dpa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dpa.avps[1].get_length(), 22)
        self.assertEqual(base.dpa.avps[1].data, b"client.network")
        self.assertEqual(base.dpa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[2].vendor_id)
        self.assertEqual(base.dpa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dpa.avps[2].get_length(), 15)
        self.assertEqual(base.dpa.avps[2].data, b"network")
        self.assertEqual(base.dpa.avps[2].get_padding_length(), 1)


        ##: Check Disconnect-Peer-Request

        #: Check Diameter Header
        self.assertEqual(base.dpr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dpr.header.length.hex(), "000048")
        self.assertEqual(base.dpr.header.get_length(), 72)
        self.assertEqual(base.dpr.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpr.__repr__(), "<Diameter Message: 282 [DPR] REQ, 0 [Diameter common message], 3 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dpr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[0].vendor_id)
        self.assertEqual(base.dpr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dpr.avps[0].get_length(), 22)
        self.assertEqual(base.dpr.avps[0].data, b"client.network")
        self.assertEqual(base.dpr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[1].vendor_id)
        self.assertEqual(base.dpr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dpr.avps[1].get_length(), 15)
        self.assertEqual(base.dpr.avps[1].data, b"network")
        self.assertEqual(base.dpr.avps[1].get_padding_length(), 1)

    def test__diameter_base_proxy__get_custom_messages__custom_dpa(self):
        #: Initial setup
        proxy = DiameterBaseProxy(self.connection)
        base = proxy.get_custom_messages()

        dpa = DiameterBaseProxy.load_dpa(self.connection)
        dpa.append(OriginStateIdAVP(64))
        dpa.append(SupportedVendorIdAVP(VENDOR_ID_3GPP))
        dpa.append(SupportedVendorIdAVP(VENDOR_ID_ETSI))

        base = proxy.get_custom_messages([dpa])

        #: Initial check
        self.assertTrue(isinstance(base.cea, CapabilitiesExchangeAnswer))
        self.assertTrue(isinstance(base.cer, CapabilitiesExchangeRequest))
        self.assertTrue(isinstance(base.dwa, DeviceWatchdogAnswer))
        self.assertTrue(isinstance(base.dwr, DeviceWatchdogRequest))
        self.assertTrue(isinstance(base.dpa, DisconnectPeerAnswer))
        self.assertTrue(isinstance(base.dpr, DisconnectPeerRequest))

        ##: Check Capabilities-Exchange-Answer

        #: Check Diameter Header
        self.assertEqual(base.cea.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cea.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.cea.header.length.hex(), "000088")
        self.assertEqual(base.cea.header.get_length(), 136)
        self.assertEqual(base.cea.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cea.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cea.__repr__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 7 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.cea.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[0].vendor_id)
        self.assertEqual(base.cea.avps[0].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[0].get_length(), 12)
        self.assertEqual(base.cea.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.cea.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.cea.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[1].vendor_id)
        self.assertEqual(base.cea.avps[1].length.hex(), "000016")
        self.assertEqual(base.cea.avps[1].get_length(), 22)
        self.assertEqual(base.cea.avps[1].data, b"client.network")
        self.assertEqual(base.cea.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cea.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[2].vendor_id)
        self.assertEqual(base.cea.avps[2].length.hex(), "00000f")
        self.assertEqual(base.cea.avps[2].get_length(), 15)
        self.assertEqual(base.cea.avps[2].data, b"network")
        self.assertEqual(base.cea.avps[2].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cea.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[3].vendor_id)
        self.assertEqual(base.cea.avps[3].length.hex(), "00000e")
        self.assertEqual(base.cea.avps[3].get_length(), 14)
        self.assertEqual(base.cea.avps[3].data.hex(), "00017f000001")
        self.assertEqual(base.cea.avps[3].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cea.avps[3].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cea.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[4].vendor_id)
        self.assertEqual(base.cea.avps[4].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[4].get_length(), 12)
        self.assertEqual(base.cea.avps[4].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cea.avps[4].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cea.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[5].vendor_id)
        self.assertEqual(base.cea.avps[5].length.hex(), "000017")
        self.assertEqual(base.cea.avps[5].get_length(), 23)
        self.assertEqual(base.cea.avps[5].data, b"Python bromelia")
        self.assertEqual(base.cea.avps[5].get_padding_length(), 1)

        #: Auth-Application-Id AVP
        self.assertEqual(base.cea.auth_application_id_avp.dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[6].vendor_id)
        self.assertEqual(base.cea.avps[6].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[6].get_length(), 12)
        self.assertEqual(base.cea.avps[6].data, DIAMETER_APPLICATION_DEFAULT)
        self.assertIsNone(base.cea.avps[6].get_padding_length())


        ##: Check Capabilities-Exchange-Request

        #: Check Diameter Header
        self.assertEqual(base.cer.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cer.header.flags, FLAG_REQUEST)
        self.assertEqual(base.cer.header.length.hex(), "00007c")
        self.assertEqual(base.cer.header.get_length(), 124)
        self.assertEqual(base.cer.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cer.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cer.__repr__(), "<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 6 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.cer.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cer.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[0].vendor_id)
        self.assertEqual(base.cer.avps[0].length.hex(), "000016")
        self.assertEqual(base.cer.avps[0].get_length(), 22)
        self.assertEqual(base.cer.avps[0].data, b"client.network")
        self.assertEqual(base.cer.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cer.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cer.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[1].vendor_id)
        self.assertEqual(base.cer.avps[1].length.hex(), "00000f")
        self.assertEqual(base.cer.avps[1].get_length(), 15)
        self.assertEqual(base.cer.avps[1].data, b"network")
        self.assertEqual(base.cer.avps[1].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cer.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cer.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[2].vendor_id)
        self.assertEqual(base.cer.avps[2].length.hex(), "00000e")
        self.assertEqual(base.cer.avps[2].get_length(), 14)
        self.assertEqual(base.cer.avps[2].data.hex(), "00017f000001")
        self.assertEqual(base.cer.avps[2].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cer.avps[2].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cer.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cer.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[3].vendor_id)
        self.assertEqual(base.cer.avps[3].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[3].get_length(), 12)
        self.assertEqual(base.cer.avps[3].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cer.avps[3].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cer.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cer.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[4].vendor_id)
        self.assertEqual(base.cer.avps[4].length.hex(), "000017")
        self.assertEqual(base.cer.avps[4].get_length(), 23)
        self.assertEqual(base.cer.avps[4].data, b"Python bromelia")
        self.assertEqual(base.cer.avps[4].get_padding_length(), 1)

        #: Firmware-Revision AVP
        self.assertEqual(base.cer.firmware_revision_avp.dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].code, FIRMWARE_REVISION_AVP_CODE)
        self.assertEqual(base.cer.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[5].vendor_id)
        self.assertEqual(base.cer.avps[5].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[5].get_length(), 12)
        self.assertEqual(base.cer.avps[5].data, FIRMWARE_VERSION)
        self.assertIsNone(base.cer.avps[5].get_padding_length())


        ##: Check Device-Watchdog-Answer

        #: Check Diameter Header
        self.assertEqual(base.dwa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dwa.header.length.hex(), "000048")
        self.assertEqual(base.dwa.header.get_length(), 72)
        self.assertEqual(base.dwa.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwa.__repr__(), "<Diameter Message: 280 [DWA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dwa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dwa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dwa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[0].vendor_id)
        self.assertEqual(base.dwa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dwa.avps[0].get_length(), 12)
        self.assertEqual(base.dwa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dwa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dwa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[1].vendor_id)
        self.assertEqual(base.dwa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dwa.avps[1].get_length(), 22)
        self.assertEqual(base.dwa.avps[1].data, b"client.network")
        self.assertEqual(base.dwa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[2].vendor_id)
        self.assertEqual(base.dwa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dwa.avps[2].get_length(), 15)
        self.assertEqual(base.dwa.avps[2].data, b"network")
        self.assertEqual(base.dwa.avps[2].get_padding_length(), 1)


        ##: Check Device-Watchdog-Request

        #: Check Diameter Header
        self.assertEqual(base.dwr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dwr.header.length.hex(), "00003c")
        self.assertEqual(base.dwr.header.get_length(), 60)
        self.assertEqual(base.dwr.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwr.__repr__(), "<Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 2 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dwr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[0].vendor_id)
        self.assertEqual(base.dwr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dwr.avps[0].get_length(), 22)
        self.assertEqual(base.dwr.avps[0].data, b"client.network")
        self.assertEqual(base.dwr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[1].vendor_id)
        self.assertEqual(base.dwr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dwr.avps[1].get_length(), 15)
        self.assertEqual(base.dwr.avps[1].data, b"network")
        self.assertEqual(base.dwr.avps[1].get_padding_length(), 1)


        ##: Check Disconnect-Peer-Answer

        #: Check Diameter Header
        self.assertEqual(base.dpa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dpa.header.length.hex(), "00006c")
        self.assertEqual(base.dpa.header.get_length(), 108)
        self.assertEqual(base.dpa.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpa.__repr__(), "<Diameter Message: 282 [DPA], 0 [Diameter common message], 6 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dpa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dpa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dpa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[0].vendor_id)
        self.assertEqual(base.dpa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dpa.avps[0].get_length(), 12)
        self.assertEqual(base.dpa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dpa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dpa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[1].vendor_id)
        self.assertEqual(base.dpa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dpa.avps[1].get_length(), 22)
        self.assertEqual(base.dpa.avps[1].data, b"client.network")
        self.assertEqual(base.dpa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[2].vendor_id)
        self.assertEqual(base.dpa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dpa.avps[2].get_length(), 15)
        self.assertEqual(base.dpa.avps[2].data, b"network")
        self.assertEqual(base.dpa.avps[2].get_padding_length(), 1)

        #: Origin-State-Id AVP
        self.assertEqual(base.dpa.origin_state_id_avp.dump().hex(), "000001164000000c00000040")
        self.assertEqual(base.dpa.avps[3].dump().hex(), "000001164000000c00000040")
        self.assertEqual(base.dpa.avps[3].code, ORIGIN_STATE_ID_AVP_CODE)
        self.assertEqual(base.dpa.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[3].vendor_id)
        self.assertEqual(base.dpa.avps[3].length.hex(), "00000c")
        self.assertEqual(base.dpa.avps[3].get_length(), 12)
        self.assertEqual(base.dpa.avps[3].data.hex(), "00000040")
        self.assertIsNone(base.dpa.avps[3].get_padding_length())

        #: Supported-Vendor-Id AVP
        self.assertEqual(base.dpa.supported_vendor_id_avp.dump().hex(), "000001094000000c000028af")
        self.assertEqual(base.dpa.avps[4].dump().hex(), "000001094000000c000028af")
        self.assertEqual(base.dpa.avps[4].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(base.dpa.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[4].vendor_id)
        self.assertEqual(base.dpa.avps[4].length.hex(), "00000c")
        self.assertEqual(base.dpa.avps[4].get_length(), 12)
        self.assertEqual(base.dpa.avps[4].data, VENDOR_ID_3GPP)
        self.assertIsNone(base.dpa.avps[4].get_padding_length())

        #: Supported-Vendor-Id AVP
        self.assertEqual(base.dpa.supported_vendor_id_avp__1.dump().hex(), "000001094000000c000032db")
        self.assertEqual(base.dpa.avps[5].dump().hex(), "000001094000000c000032db")
        self.assertEqual(base.dpa.avps[5].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(base.dpa.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[5].vendor_id)
        self.assertEqual(base.dpa.avps[5].length.hex(), "00000c")
        self.assertEqual(base.dpa.avps[5].get_length(), 12)
        self.assertEqual(base.dpa.avps[5].data, VENDOR_ID_ETSI)
        self.assertIsNone(base.dpa.avps[5].get_padding_length())


        ##: Check Disconnect-Peer-Request

        #: Check Diameter Header
        self.assertEqual(base.dpr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dpr.header.length.hex(), "000048")
        self.assertEqual(base.dpr.header.get_length(), 72)
        self.assertEqual(base.dpr.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpr.__repr__(), "<Diameter Message: 282 [DPR] REQ, 0 [Diameter common message], 3 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dpr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[0].vendor_id)
        self.assertEqual(base.dpr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dpr.avps[0].get_length(), 22)
        self.assertEqual(base.dpr.avps[0].data, b"client.network")
        self.assertEqual(base.dpr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[1].vendor_id)
        self.assertEqual(base.dpr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dpr.avps[1].get_length(), 15)
        self.assertEqual(base.dpr.avps[1].data, b"network")
        self.assertEqual(base.dpr.avps[1].get_padding_length(), 1)

    def test__diameter_base_proxy__get_custom_messages__custom_dpr(self):
        #: Initial setup
        proxy = DiameterBaseProxy(self.connection)
        base = proxy.get_custom_messages()

        dpr = DiameterBaseProxy.load_dpr(self.connection)
        dpr.append(OriginStateIdAVP(64))
        dpr.append(SupportedVendorIdAVP(VENDOR_ID_3GPP))
        dpr.append(SupportedVendorIdAVP(VENDOR_ID_ETSI))

        base = proxy.get_custom_messages([dpr])

        #: Initial check
        self.assertTrue(isinstance(base.cea, CapabilitiesExchangeAnswer))
        self.assertTrue(isinstance(base.cer, CapabilitiesExchangeRequest))
        self.assertTrue(isinstance(base.dwa, DeviceWatchdogAnswer))
        self.assertTrue(isinstance(base.dwr, DeviceWatchdogRequest))
        self.assertTrue(isinstance(base.dpa, DisconnectPeerAnswer))
        self.assertTrue(isinstance(base.dpr, DisconnectPeerRequest))

        ##: Check Capabilities-Exchange-Answer

        #: Check Diameter Header
        self.assertEqual(base.cea.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cea.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.cea.header.length.hex(), "000088")
        self.assertEqual(base.cea.header.get_length(), 136)
        self.assertEqual(base.cea.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cea.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cea.__repr__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 7 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.cea.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[0].vendor_id)
        self.assertEqual(base.cea.avps[0].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[0].get_length(), 12)
        self.assertEqual(base.cea.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.cea.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.cea.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[1].vendor_id)
        self.assertEqual(base.cea.avps[1].length.hex(), "000016")
        self.assertEqual(base.cea.avps[1].get_length(), 22)
        self.assertEqual(base.cea.avps[1].data, b"client.network")
        self.assertEqual(base.cea.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cea.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[2].vendor_id)
        self.assertEqual(base.cea.avps[2].length.hex(), "00000f")
        self.assertEqual(base.cea.avps[2].get_length(), 15)
        self.assertEqual(base.cea.avps[2].data, b"network")
        self.assertEqual(base.cea.avps[2].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cea.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[3].vendor_id)
        self.assertEqual(base.cea.avps[3].length.hex(), "00000e")
        self.assertEqual(base.cea.avps[3].get_length(), 14)
        self.assertEqual(base.cea.avps[3].data.hex(), "00017f000001")
        self.assertEqual(base.cea.avps[3].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cea.avps[3].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cea.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[4].vendor_id)
        self.assertEqual(base.cea.avps[4].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[4].get_length(), 12)
        self.assertEqual(base.cea.avps[4].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cea.avps[4].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cea.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[5].vendor_id)
        self.assertEqual(base.cea.avps[5].length.hex(), "000017")
        self.assertEqual(base.cea.avps[5].get_length(), 23)
        self.assertEqual(base.cea.avps[5].data, b"Python bromelia")
        self.assertEqual(base.cea.avps[5].get_padding_length(), 1)

        #: Auth-Application-Id AVP
        self.assertEqual(base.cea.auth_application_id_avp.dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(base.cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(base.cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cea.avps[6].vendor_id)
        self.assertEqual(base.cea.avps[6].length.hex(), "00000c")
        self.assertEqual(base.cea.avps[6].get_length(), 12)
        self.assertEqual(base.cea.avps[6].data, DIAMETER_APPLICATION_DEFAULT)
        self.assertIsNone(base.cea.avps[6].get_padding_length())


        ##: Check Capabilities-Exchange-Request

        #: Check Diameter Header
        self.assertEqual(base.cer.header.version, DIAMETER_VERSION)
        self.assertEqual(base.cer.header.flags, FLAG_REQUEST)
        self.assertEqual(base.cer.header.length.hex(), "00007c")
        self.assertEqual(base.cer.header.get_length(), 124)
        self.assertEqual(base.cer.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(base.cer.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.cer.__repr__(), "<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 6 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.cer.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.cer.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.cer.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[0].vendor_id)
        self.assertEqual(base.cer.avps[0].length.hex(), "000016")
        self.assertEqual(base.cer.avps[0].get_length(), 22)
        self.assertEqual(base.cer.avps[0].data, b"client.network")
        self.assertEqual(base.cer.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.cer.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.cer.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.cer.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[1].vendor_id)
        self.assertEqual(base.cer.avps[1].length.hex(), "00000f")
        self.assertEqual(base.cer.avps[1].get_length(), 15)
        self.assertEqual(base.cer.avps[1].data, b"network")
        self.assertEqual(base.cer.avps[1].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(base.cer.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(base.cer.avps[2].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(base.cer.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[2].vendor_id)
        self.assertEqual(base.cer.avps[2].length.hex(), "00000e")
        self.assertEqual(base.cer.avps[2].get_length(), 14)
        self.assertEqual(base.cer.avps[2].data.hex(), "00017f000001")
        self.assertEqual(base.cer.avps[2].get_ip_address(), "127.0.0.1")
        self.assertEqual(base.cer.avps[2].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(base.cer.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(base.cer.avps[3].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(base.cer.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[3].vendor_id)
        self.assertEqual(base.cer.avps[3].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[3].get_length(), 12)
        self.assertEqual(base.cer.avps[3].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(base.cer.avps[3].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(base.cer.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(base.cer.avps[4].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(base.cer.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[4].vendor_id)
        self.assertEqual(base.cer.avps[4].length.hex(), "000017")
        self.assertEqual(base.cer.avps[4].get_length(), 23)
        self.assertEqual(base.cer.avps[4].data, b"Python bromelia")
        self.assertEqual(base.cer.avps[4].get_padding_length(), 1)

        #: Firmware-Revision AVP
        self.assertEqual(base.cer.firmware_revision_avp.dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(base.cer.avps[5].code, FIRMWARE_REVISION_AVP_CODE)
        self.assertEqual(base.cer.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.cer.avps[5].vendor_id)
        self.assertEqual(base.cer.avps[5].length.hex(), "00000c")
        self.assertEqual(base.cer.avps[5].get_length(), 12)
        self.assertEqual(base.cer.avps[5].data, FIRMWARE_VERSION)
        self.assertIsNone(base.cer.avps[5].get_padding_length())


        ##: Check Device-Watchdog-Answer

        #: Check Diameter Header
        self.assertEqual(base.dwa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dwa.header.length.hex(), "000048")
        self.assertEqual(base.dwa.header.get_length(), 72)
        self.assertEqual(base.dwa.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwa.__repr__(), "<Diameter Message: 280 [DWA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dwa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dwa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dwa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[0].vendor_id)
        self.assertEqual(base.dwa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dwa.avps[0].get_length(), 12)
        self.assertEqual(base.dwa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dwa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dwa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[1].vendor_id)
        self.assertEqual(base.dwa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dwa.avps[1].get_length(), 22)
        self.assertEqual(base.dwa.avps[1].data, b"client.network")
        self.assertEqual(base.dwa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwa.avps[2].vendor_id)
        self.assertEqual(base.dwa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dwa.avps[2].get_length(), 15)
        self.assertEqual(base.dwa.avps[2].data, b"network")
        self.assertEqual(base.dwa.avps[2].get_padding_length(), 1)


        ##: Check Device-Watchdog-Request

        #: Check Diameter Header
        self.assertEqual(base.dwr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dwr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dwr.header.length.hex(), "00003c")
        self.assertEqual(base.dwr.header.get_length(), 60)
        self.assertEqual(base.dwr.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(base.dwr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dwr.__repr__(), "<Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 2 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dwr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dwr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dwr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[0].vendor_id)
        self.assertEqual(base.dwr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dwr.avps[0].get_length(), 22)
        self.assertEqual(base.dwr.avps[0].data, b"client.network")
        self.assertEqual(base.dwr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dwr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dwr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dwr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dwr.avps[1].vendor_id)
        self.assertEqual(base.dwr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dwr.avps[1].get_length(), 15)
        self.assertEqual(base.dwr.avps[1].data, b"network")
        self.assertEqual(base.dwr.avps[1].get_padding_length(), 1)


        ##: Check Disconnect-Peer-Answer

        #: Check Diameter Header
        self.assertEqual(base.dpa.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpa.header.flags, FLAG_RESPONSE)
        self.assertEqual(base.dpa.header.length.hex(), "000048")
        self.assertEqual(base.dpa.header.get_length(), 72)
        self.assertEqual(base.dpa.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpa.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpa.__repr__(), "<Diameter Message: 282 [DPA], 0 [Diameter common message], 3 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(base.dpa.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(base.dpa.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(base.dpa.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[0].vendor_id)
        self.assertEqual(base.dpa.avps[0].length.hex(), "00000c")
        self.assertEqual(base.dpa.avps[0].get_length(), 12)
        self.assertEqual(base.dpa.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(base.dpa.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(base.dpa.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpa.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpa.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[1].vendor_id)
        self.assertEqual(base.dpa.avps[1].length.hex(), "000016")
        self.assertEqual(base.dpa.avps[1].get_length(), 22)
        self.assertEqual(base.dpa.avps[1].data, b"client.network")
        self.assertEqual(base.dpa.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpa.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpa.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpa.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpa.avps[2].vendor_id)
        self.assertEqual(base.dpa.avps[2].length.hex(), "00000f")
        self.assertEqual(base.dpa.avps[2].get_length(), 15)
        self.assertEqual(base.dpa.avps[2].data, b"network")
        self.assertEqual(base.dpa.avps[2].get_padding_length(), 1)


        ##: Check Disconnect-Peer-Request

        #: Check Diameter Header
        self.assertEqual(base.dpr.header.version, DIAMETER_VERSION)
        self.assertEqual(base.dpr.header.flags, FLAG_REQUEST)
        self.assertEqual(base.dpr.header.length.hex(), "00006c")
        self.assertEqual(base.dpr.header.get_length(), 108)
        self.assertEqual(base.dpr.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(base.dpr.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(base.dpr.__repr__(), "<Diameter Message: 282 [DPR] REQ, 0 [Diameter common message], 6 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(base.dpr.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(base.dpr.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(base.dpr.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[0].vendor_id)
        self.assertEqual(base.dpr.avps[0].length.hex(), "000016")
        self.assertEqual(base.dpr.avps[0].get_length(), 22)
        self.assertEqual(base.dpr.avps[0].data, b"client.network")
        self.assertEqual(base.dpr.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(base.dpr.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(base.dpr.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(base.dpr.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[1].vendor_id)
        self.assertEqual(base.dpr.avps[1].length.hex(), "00000f")
        self.assertEqual(base.dpr.avps[1].get_length(), 15)
        self.assertEqual(base.dpr.avps[1].data, b"network")
        self.assertEqual(base.dpr.avps[1].get_padding_length(), 1)

        #: Origin-State-Id AVP
        self.assertEqual(base.dpr.origin_state_id_avp.dump().hex(), "000001164000000c00000040")
        self.assertEqual(base.dpr.avps[3].dump().hex(), "000001164000000c00000040")
        self.assertEqual(base.dpr.avps[3].code, ORIGIN_STATE_ID_AVP_CODE)
        self.assertEqual(base.dpr.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[3].vendor_id)
        self.assertEqual(base.dpr.avps[3].length.hex(), "00000c")
        self.assertEqual(base.dpr.avps[3].get_length(), 12)
        self.assertEqual(base.dpr.avps[3].data.hex(), "00000040")
        self.assertIsNone(base.dpr.avps[3].get_padding_length())

        #: Supported-Vendor-Id AVP
        self.assertEqual(base.dpr.supported_vendor_id_avp.dump().hex(), "000001094000000c000028af")
        self.assertEqual(base.dpr.avps[4].dump().hex(), "000001094000000c000028af")
        self.assertEqual(base.dpr.avps[4].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(base.dpr.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[4].vendor_id)
        self.assertEqual(base.dpr.avps[4].length.hex(), "00000c")
        self.assertEqual(base.dpr.avps[4].get_length(), 12)
        self.assertEqual(base.dpr.avps[4].data, VENDOR_ID_3GPP)
        self.assertIsNone(base.dpr.avps[4].get_padding_length())

        #: Supported-Vendor-Id AVP
        self.assertEqual(base.dpr.supported_vendor_id_avp__1.dump().hex(), "000001094000000c000032db")
        self.assertEqual(base.dpr.avps[5].dump().hex(), "000001094000000c000032db")
        self.assertEqual(base.dpr.avps[5].code, SUPPORTED_VENDOR_ID_AVP_CODE)
        self.assertEqual(base.dpr.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(base.dpr.avps[5].vendor_id)
        self.assertEqual(base.dpr.avps[5].length.hex(), "00000c")
        self.assertEqual(base.dpr.avps[5].get_length(), 12)
        self.assertEqual(base.dpr.avps[5].data, VENDOR_ID_ETSI)
        self.assertIsNone(base.dpr.avps[5].get_padding_length())


# @unittest.SkipTest
class TestDiameterBaseProxyWithOneApplicationId(unittest.TestCase):
    def setUp(self):
        config = {
                "MODE": "CLIENT",
                "TRANSPORT_TYPE": "TCP",
                "APPLICATIONS": [{
                                    "vendor_id": VENDOR_ID_3GPP,
                                    "app_id": DIAMETER_APPLICATION_Cx
                }],
                "LOCAL_NODE_HOSTNAME": "client.network",
                "LOCAL_NODE_REALM": "network",
                "LOCAL_NODE_IP_ADDRESS": "127.0.0.1",
                "LOCAL_NODE_PORT": None,
                "PEER_NODE_HOSTNAME": "server.network",
                "PEER_NODE_REALM": "network",
                "PEER_NODE_IP_ADDRESS": "127.0.0.1",
                "PEER_NODE_PORT": None,
                "WATCHDOG_TIMEOUT": 30
            }
        self.connection = _convert_config_to_connection_obj(config)

    def test__load_cea(self):
        cea = DiameterBaseProxy.load_cea(self.connection)

        #: Check Diameter Header
        self.assertEqual(cea.header.version, DIAMETER_VERSION)
        self.assertEqual(cea.header.flags, FLAG_RESPONSE)
        self.assertEqual(cea.header.length.hex(), "0000a8")
        self.assertEqual(cea.header.get_length(), 168)
        self.assertEqual(cea.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(cea.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(cea.__repr__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 8 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(cea.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[0].vendor_id)
        self.assertEqual(cea.avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[0].get_length(), 12)
        self.assertEqual(cea.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(cea.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(cea.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[1].vendor_id)
        self.assertEqual(cea.avps[1].length.hex(), "000016")
        self.assertEqual(cea.avps[1].get_length(), 22)
        self.assertEqual(cea.avps[1].data, b"client.network")
        self.assertEqual(cea.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(cea.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cea.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[2].vendor_id)
        self.assertEqual(cea.avps[2].length.hex(), "00000f")
        self.assertEqual(cea.avps[2].get_length(), 15)
        self.assertEqual(cea.avps[2].data, b"network")
        self.assertEqual(cea.avps[2].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(cea.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cea.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[3].vendor_id)
        self.assertEqual(cea.avps[3].length.hex(), "00000e")
        self.assertEqual(cea.avps[3].get_length(), 14)
        self.assertEqual(cea.avps[3].data.hex(), "00017f000001")
        self.assertEqual(cea.avps[3].get_ip_address(), "127.0.0.1")
        self.assertEqual(cea.avps[3].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(cea.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cea.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[4].vendor_id)
        self.assertEqual(cea.avps[4].length.hex(), "00000c")
        self.assertEqual(cea.avps[4].get_length(), 12)
        self.assertEqual(cea.avps[4].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(cea.avps[4].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(cea.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cea.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[5].vendor_id)
        self.assertEqual(cea.avps[5].length.hex(), "000017")
        self.assertEqual(cea.avps[5].get_length(), 23)
        self.assertEqual(cea.avps[5].data, b"Python bromelia")
        self.assertEqual(cea.avps[5].get_padding_length(), 1)

        #: Auth-Application-Id AVP
        self.assertEqual(cea.auth_application_id_avp.dump().hex(), "000001024000000c00000000")
        self.assertEqual(cea.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[6].vendor_id)
        self.assertEqual(cea.avps[6].length.hex(), "00000c")
        self.assertEqual(cea.avps[6].get_length(), 12)
        self.assertEqual(cea.avps[6].data, DIAMETER_APPLICATION_DEFAULT)
        self.assertIsNone(cea.avps[6].get_padding_length())

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp.dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(cea.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(cea.avps[7].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].vendor_id)
        self.assertEqual(cea.avps[7].length.hex(), "000020")
        self.assertEqual(cea.avps[7].get_length(), 32)
        self.assertEqual(cea.avps[7].data.hex(), "0000010a4000000c000028af000001024000000c01000000")
        self.assertIsNone(cea.avps[7].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[7].avps[0].dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[7].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].avps[0].vendor_id)
        self.assertEqual(cea.avps[7].avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[7].avps[0].get_length(), 12)
        self.assertEqual(cea.avps[7].avps[0].data, VENDOR_ID_3GPP)
        self.assertIsNone(cea.avps[7].avps[0].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.dump().hex(), "000001024000000c01000000")
        self.assertEqual(cea.avps[7].avps[1].dump().hex(), "000001024000000c01000000")
        self.assertEqual(cea.avps[7].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].avps[1].vendor_id)
        self.assertEqual(cea.avps[7].avps[1].length.hex(), "00000c")
        self.assertEqual(cea.avps[7].avps[1].get_length(), 12)
        self.assertEqual(cea.avps[7].avps[1].data, DIAMETER_APPLICATION_Cx)
        self.assertIsNone(cea.avps[7].avps[1].get_padding_length())

    def test__load_cer(self):
        cer = DiameterBaseProxy.load_cer(self.connection)

        #: Check Diameter Header
        self.assertEqual(cer.header.version, DIAMETER_VERSION)
        self.assertEqual(cer.header.flags, FLAG_REQUEST)
        self.assertEqual(cer.header.length.hex(), "00009c")
        self.assertEqual(cer.header.get_length(), 156)
        self.assertEqual(cer.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(cer.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(cer.__repr__(), "<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 7 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(cer.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(cer.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(cer.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(cer.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[0].vendor_id)
        self.assertEqual(cer.avps[0].length.hex(), "000016")
        self.assertEqual(cer.avps[0].get_length(), 22)
        self.assertEqual(cer.avps[0].data, b"client.network")
        self.assertEqual(cer.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(cer.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cer.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cer.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(cer.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[1].vendor_id)
        self.assertEqual(cer.avps[1].length.hex(), "00000f")
        self.assertEqual(cer.avps[1].get_length(), 15)
        self.assertEqual(cer.avps[1].data, b"network")
        self.assertEqual(cer.avps[1].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(cer.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cer.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cer.avps[2].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(cer.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[2].vendor_id)
        self.assertEqual(cer.avps[2].length.hex(), "00000e")
        self.assertEqual(cer.avps[2].get_length(), 14)
        self.assertEqual(cer.avps[2].data.hex(), "00017f000001")
        self.assertEqual(cer.avps[2].get_ip_address(), "127.0.0.1")
        self.assertEqual(cer.avps[2].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(cer.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cer.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cer.avps[3].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cer.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[3].vendor_id)
        self.assertEqual(cer.avps[3].length.hex(), "00000c")
        self.assertEqual(cer.avps[3].get_length(), 12)
        self.assertEqual(cer.avps[3].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(cer.avps[3].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(cer.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cer.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cer.avps[4].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(cer.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[4].vendor_id)
        self.assertEqual(cer.avps[4].length.hex(), "000017")
        self.assertEqual(cer.avps[4].get_length(), 23)
        self.assertEqual(cer.avps[4].data, b"Python bromelia")
        self.assertEqual(cer.avps[4].get_padding_length(), 1)

        #: Firmware-Revision AVP
        self.assertEqual(cer.firmware_revision_avp.dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(cer.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(cer.avps[5].code, FIRMWARE_REVISION_AVP_CODE)
        self.assertEqual(cer.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[5].vendor_id)
        self.assertEqual(cer.avps[5].length.hex(), "00000c")
        self.assertEqual(cer.avps[5].get_length(), 12)
        self.assertEqual(cer.avps[5].data, FIRMWARE_VERSION)
        self.assertIsNone(cer.avps[5].get_padding_length())

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(cer.vendor_specific_application_id_avp.dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(cer.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(cer.avps[6].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cer.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[6].vendor_id)
        self.assertEqual(cer.avps[6].length.hex(), "000020")
        self.assertEqual(cer.avps[6].get_length(), 32)
        self.assertEqual(cer.avps[6].data.hex(), "0000010a4000000c000028af000001024000000c01000000")
        self.assertIsNone(cer.avps[6].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(cer.vendor_specific_application_id_avp.vendor_id_avp.dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cer.avps[6].avps[0].dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cer.avps[6].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cer.avps[6].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[6].avps[0].vendor_id)
        self.assertEqual(cer.avps[6].avps[0].length.hex(), "00000c")
        self.assertEqual(cer.avps[6].avps[0].get_length(), 12)
        self.assertEqual(cer.avps[6].avps[0].data, VENDOR_ID_3GPP)
        self.assertIsNone(cer.avps[6].avps[0].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(cer.vendor_specific_application_id_avp.auth_application_id_avp.dump().hex(), "000001024000000c01000000")
        self.assertEqual(cer.avps[6].avps[1].dump().hex(), "000001024000000c01000000")
        self.assertEqual(cer.avps[6].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cer.avps[6].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[6].avps[1].vendor_id)
        self.assertEqual(cer.avps[6].avps[1].length.hex(), "00000c")
        self.assertEqual(cer.avps[6].avps[1].get_length(), 12)
        self.assertEqual(cer.avps[6].avps[1].data, DIAMETER_APPLICATION_Cx)
        self.assertIsNone(cer.avps[6].avps[1].get_padding_length())


# @unittest.SkipTest
class TestDiameterBaseProxyWithTwoApplicationsId(unittest.TestCase):
    def setUp(self):
        config = {
                "MODE": "CLIENT",
                "TRANSPORT_TYPE": "TCP",
                "APPLICATIONS": [
                                    {
                                        "vendor_id": VENDOR_ID_3GPP,
                                        "app_id": DIAMETER_APPLICATION_Cx
                                    },
                                    {
                                        "vendor_id": VENDOR_ID_3GPP,
                                        "app_id": DIAMETER_APPLICATION_Rx
                                    }
                ],
                "LOCAL_NODE_HOSTNAME": "client.network",
                "LOCAL_NODE_REALM": "network",
                "LOCAL_NODE_IP_ADDRESS": "127.0.0.1",
                "LOCAL_NODE_PORT": None,
                "PEER_NODE_HOSTNAME": "server.network",
                "PEER_NODE_REALM": "network",
                "PEER_NODE_IP_ADDRESS": "127.0.0.1",
                "PEER_NODE_PORT": None,
                "WATCHDOG_TIMEOUT": 30
            }
        self.connection = _convert_config_to_connection_obj(config)

    def test__load_cea(self):
        cea = DiameterBaseProxy.load_cea(self.connection)

        #: Check Diameter Header
        self.assertEqual(cea.header.version, DIAMETER_VERSION)
        self.assertEqual(cea.header.flags, FLAG_RESPONSE)
        self.assertEqual(cea.header.length.hex(), "0000c8")
        self.assertEqual(cea.header.get_length(), 200)
        self.assertEqual(cea.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(cea.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(cea.__repr__(), "<Diameter Message: 257 [CEA], 0 [Diameter common message], 9 AVP(s)>")

        #: Result-Code AVP
        self.assertEqual(cea.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(cea.avps[0].code, RESULT_CODE_AVP_CODE)
        self.assertEqual(cea.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[0].vendor_id)
        self.assertEqual(cea.avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[0].get_length(), 12)
        self.assertEqual(cea.avps[0].data, DIAMETER_SUCCESS)
        self.assertIsNone(cea.avps[0].get_padding_length())

        #: Origin-Host AVP
        self.assertEqual(cea.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(cea.avps[1].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(cea.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[1].vendor_id)
        self.assertEqual(cea.avps[1].length.hex(), "000016")
        self.assertEqual(cea.avps[1].get_length(), 22)
        self.assertEqual(cea.avps[1].data, b"client.network")
        self.assertEqual(cea.avps[1].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(cea.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cea.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cea.avps[2].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(cea.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[2].vendor_id)
        self.assertEqual(cea.avps[2].length.hex(), "00000f")
        self.assertEqual(cea.avps[2].get_length(), 15)
        self.assertEqual(cea.avps[2].data, b"network")
        self.assertEqual(cea.avps[2].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(cea.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cea.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cea.avps[3].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(cea.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[3].vendor_id)
        self.assertEqual(cea.avps[3].length.hex(), "00000e")
        self.assertEqual(cea.avps[3].get_length(), 14)
        self.assertEqual(cea.avps[3].data.hex(), "00017f000001")
        self.assertEqual(cea.avps[3].get_ip_address(), "127.0.0.1")
        self.assertEqual(cea.avps[3].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(cea.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cea.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cea.avps[4].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[4].vendor_id)
        self.assertEqual(cea.avps[4].length.hex(), "00000c")
        self.assertEqual(cea.avps[4].get_length(), 12)
        self.assertEqual(cea.avps[4].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(cea.avps[4].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(cea.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cea.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cea.avps[5].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(cea.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[5].vendor_id)
        self.assertEqual(cea.avps[5].length.hex(), "000017")
        self.assertEqual(cea.avps[5].get_length(), 23)
        self.assertEqual(cea.avps[5].data, b"Python bromelia")
        self.assertEqual(cea.avps[5].get_padding_length(), 1)

        #: Auth-Application-Id AVP
        self.assertEqual(cea.auth_application_id_avp.dump().hex(), "000001024000000c00000000")
        self.assertEqual(cea.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(cea.avps[6].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[6].vendor_id)
        self.assertEqual(cea.avps[6].length.hex(), "00000c")
        self.assertEqual(cea.avps[6].get_length(), 12)
        self.assertEqual(cea.avps[6].data, DIAMETER_APPLICATION_DEFAULT)
        self.assertIsNone(cea.avps[6].get_padding_length())

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp.dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(cea.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(cea.avps[7].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].vendor_id)
        self.assertEqual(cea.avps[7].length.hex(), "000020")
        self.assertEqual(cea.avps[7].get_length(), 32)
        self.assertEqual(cea.avps[7].data.hex(), "0000010a4000000c000028af000001024000000c01000000")
        self.assertIsNone(cea.avps[7].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp.vendor_id_avp.dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[7].avps[0].dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[7].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].avps[0].vendor_id)
        self.assertEqual(cea.avps[7].avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[7].avps[0].get_length(), 12)
        self.assertEqual(cea.avps[7].avps[0].data, VENDOR_ID_3GPP)
        self.assertIsNone(cea.avps[7].avps[0].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp.auth_application_id_avp.dump().hex(), "000001024000000c01000000")
        self.assertEqual(cea.avps[7].avps[1].dump().hex(), "000001024000000c01000000")
        self.assertEqual(cea.avps[7].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[7].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[7].avps[1].vendor_id)
        self.assertEqual(cea.avps[7].avps[1].length.hex(), "00000c")
        self.assertEqual(cea.avps[7].avps[1].get_length(), 12)
        self.assertEqual(cea.avps[7].avps[1].data, DIAMETER_APPLICATION_Cx)
        self.assertIsNone(cea.avps[7].avps[1].get_padding_length())

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp__1.dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000014")
        self.assertEqual(cea.avps[8].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000014")
        self.assertEqual(cea.avps[8].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].vendor_id)
        self.assertEqual(cea.avps[8].length.hex(), "000020")
        self.assertEqual(cea.avps[8].get_length(), 32)
        self.assertEqual(cea.avps[8].data.hex(), "0000010a4000000c000028af000001024000000c01000014")
        self.assertIsNone(cea.avps[8].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp__1.vendor_id_avp.dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[8].avps[0].dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cea.avps[8].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].avps[0].vendor_id)
        self.assertEqual(cea.avps[8].avps[0].length.hex(), "00000c")
        self.assertEqual(cea.avps[8].avps[0].get_length(), 12)
        self.assertEqual(cea.avps[8].avps[0].data, VENDOR_ID_3GPP)
        self.assertIsNone(cea.avps[8].avps[0].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(cea.vendor_specific_application_id_avp__1.auth_application_id_avp.dump().hex(), "000001024000000c01000014")
        self.assertEqual(cea.avps[8].avps[1].dump().hex(), "000001024000000c01000014")
        self.assertEqual(cea.avps[8].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cea.avps[8].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cea.avps[8].avps[1].vendor_id)
        self.assertEqual(cea.avps[8].avps[1].length.hex(), "00000c")
        self.assertEqual(cea.avps[8].avps[1].get_length(), 12)
        self.assertEqual(cea.avps[8].avps[1].data, DIAMETER_APPLICATION_Rx)
        self.assertIsNone(cea.avps[8].avps[1].get_padding_length())

    def test__load_cer(self):
        cer = DiameterBaseProxy.load_cer(self.connection)

        #: Check Diameter Header
        self.assertEqual(cer.header.version, DIAMETER_VERSION)
        self.assertEqual(cer.header.flags, FLAG_REQUEST)
        self.assertEqual(cer.header.length.hex(), "0000bc")
        self.assertEqual(cer.header.get_length(), 188)
        self.assertEqual(cer.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(cer.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        self.assertEqual(cer.__repr__(), "<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 8 AVP(s)>")

        #: Origin-Host AVP
        self.assertEqual(cer.origin_host_avp.dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(cer.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(cer.avps[0].code, ORIGIN_HOST_AVP_CODE)
        self.assertEqual(cer.avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[0].vendor_id)
        self.assertEqual(cer.avps[0].length.hex(), "000016")
        self.assertEqual(cer.avps[0].get_length(), 22)
        self.assertEqual(cer.avps[0].data, b"client.network")
        self.assertEqual(cer.avps[0].get_padding_length(), 2)

        #: Origin-Realm AVP
        self.assertEqual(cer.origin_realm_avp.dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cer.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(cer.avps[1].code, ORIGIN_REALM_AVP_CODE)
        self.assertEqual(cer.avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[1].vendor_id)
        self.assertEqual(cer.avps[1].length.hex(), "00000f")
        self.assertEqual(cer.avps[1].get_length(), 15)
        self.assertEqual(cer.avps[1].data, b"network")
        self.assertEqual(cer.avps[1].get_padding_length(), 1)

        #: Host-IP-Address AVP
        self.assertEqual(cer.host_ip_address_avp.dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cer.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(cer.avps[2].code, HOST_IP_ADDRESS_AVP_CODE)
        self.assertEqual(cer.avps[2].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[2].vendor_id)
        self.assertEqual(cer.avps[2].length.hex(), "00000e")
        self.assertEqual(cer.avps[2].get_length(), 14)
        self.assertEqual(cer.avps[2].data.hex(), "00017f000001")
        self.assertEqual(cer.avps[2].get_ip_address(), "127.0.0.1")
        self.assertEqual(cer.avps[2].get_padding_length(), 2)

        #: Vendor-Id AVP
        self.assertEqual(cer.vendor_id_avp.dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cer.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(cer.avps[3].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cer.avps[3].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[3].vendor_id)
        self.assertEqual(cer.avps[3].length.hex(), "00000c")
        self.assertEqual(cer.avps[3].get_length(), 12)
        self.assertEqual(cer.avps[3].data, VENDOR_ID_DEFAULT)
        self.assertIsNone(cer.avps[3].get_padding_length())

        #: Product-Name AVP
        self.assertEqual(cer.product_name_avp.dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cer.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(cer.avps[4].code, PRODUCT_NAME_AVP_CODE)
        self.assertEqual(cer.avps[4].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[4].vendor_id)
        self.assertEqual(cer.avps[4].length.hex(), "000017")
        self.assertEqual(cer.avps[4].get_length(), 23)
        self.assertEqual(cer.avps[4].data, b"Python bromelia")
        self.assertEqual(cer.avps[4].get_padding_length(), 1)

        #: Firmware-Revision AVP
        self.assertEqual(cer.firmware_revision_avp.dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(cer.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(cer.avps[5].code, FIRMWARE_REVISION_AVP_CODE)
        self.assertEqual(cer.avps[5].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_NOT_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[5].vendor_id)
        self.assertEqual(cer.avps[5].length.hex(), "00000c")
        self.assertEqual(cer.avps[5].get_length(), 12)
        self.assertEqual(cer.avps[5].data, FIRMWARE_VERSION)
        self.assertIsNone(cer.avps[5].get_padding_length())

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(cer.vendor_specific_application_id_avp.dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(cer.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(cer.avps[6].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cer.avps[6].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[6].vendor_id)
        self.assertEqual(cer.avps[6].length.hex(), "000020")
        self.assertEqual(cer.avps[6].get_length(), 32)
        self.assertEqual(cer.avps[6].data.hex(), "0000010a4000000c000028af000001024000000c01000000")
        self.assertIsNone(cer.avps[6].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(cer.vendor_specific_application_id_avp.vendor_id_avp.dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cer.avps[6].avps[0].dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cer.avps[6].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cer.avps[6].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[6].avps[0].vendor_id)
        self.assertEqual(cer.avps[6].avps[0].length.hex(), "00000c")
        self.assertEqual(cer.avps[6].avps[0].get_length(), 12)
        self.assertEqual(cer.avps[6].avps[0].data, VENDOR_ID_3GPP)
        self.assertIsNone(cer.avps[6].avps[0].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(cer.vendor_specific_application_id_avp.auth_application_id_avp.dump().hex(), "000001024000000c01000000")
        self.assertEqual(cer.avps[6].avps[1].dump().hex(), "000001024000000c01000000")
        self.assertEqual(cer.avps[6].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cer.avps[6].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[6].avps[1].vendor_id)
        self.assertEqual(cer.avps[6].avps[1].length.hex(), "00000c")
        self.assertEqual(cer.avps[6].avps[1].get_length(), 12)
        self.assertEqual(cer.avps[6].avps[1].data, DIAMETER_APPLICATION_Cx)
        self.assertIsNone(cer.avps[6].avps[1].get_padding_length())

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(cer.vendor_specific_application_id_avp__1.dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000014")
        self.assertEqual(cer.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000014")
        self.assertEqual(cer.avps[7].code, VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cer.avps[7].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[7].vendor_id)
        self.assertEqual(cer.avps[7].length.hex(), "000020")
        self.assertEqual(cer.avps[7].get_length(), 32)
        self.assertEqual(cer.avps[7].data.hex(), "0000010a4000000c000028af000001024000000c01000014")
        self.assertIsNone(cer.avps[7].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Vendor-Id AVP
        self.assertEqual(cer.vendor_specific_application_id_avp__1.vendor_id_avp.dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cer.avps[7].avps[0].dump().hex(), "0000010a4000000c000028af")
        self.assertEqual(cer.avps[7].avps[0].code, VENDOR_ID_AVP_CODE)
        self.assertEqual(cer.avps[7].avps[0].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[7].avps[0].vendor_id)
        self.assertEqual(cer.avps[7].avps[0].length.hex(), "00000c")
        self.assertEqual(cer.avps[7].avps[0].get_length(), 12)
        self.assertEqual(cer.avps[7].avps[0].data, VENDOR_ID_3GPP)
        self.assertIsNone(cer.avps[7].avps[0].get_padding_length())

        #: Vendor-Specific-Application-Id AVP > Auth-Application-Id AVP
        self.assertEqual(cer.vendor_specific_application_id_avp__1.auth_application_id_avp.dump().hex(), "000001024000000c01000014")
        self.assertEqual(cer.avps[7].avps[1].dump().hex(), "000001024000000c01000014")
        self.assertEqual(cer.avps[7].avps[1].code, AUTH_APPLICATION_ID_AVP_CODE)
        self.assertEqual(cer.avps[7].avps[1].flags, FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED)
        self.assertIsNone(cer.avps[7].avps[1].vendor_id)
        self.assertEqual(cer.avps[7].avps[1].length.hex(), "00000c")
        self.assertEqual(cer.avps[7].avps[1].get_length(), 12)
        self.assertEqual(cer.avps[7].avps[1].data, DIAMETER_APPLICATION_Rx)
        self.assertIsNone(cer.avps[7].avps[1].get_padding_length())


if __name__ == "__main__":
    unittest.main()
