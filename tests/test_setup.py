# -*- coding: utf-8 -*-
"""
    test.test_setup
    ~~~~~~~~~~~~~~~

    This module contains the Bromelia setup unittests.

    :copyright: (c) 2021 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys
import time
import threading

from copy import copy

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.config import CLOSED, R_OPEN, I_OPEN
from bromelia.constants import *
from bromelia.setup import Diameter

# s = Diameter(config=s_config, debug=True, is_logging=True)
# c = Diameter(config=c_config, debug=True, is_logging=True)

# @unittest.SkipTest
class TestDiameterBase(unittest.TestCase):
    def setUp(self):
        self.server_config = {
                "MODE": "SERVER",
                "APPLICATIONS": [],
                "LOCAL_NODE_HOSTNAME": "server.network",
                "LOCAL_NODE_REALM": "network",
                "LOCAL_NODE_IP_ADDRESS": "127.0.0.1",
                "LOCAL_NODE_PORT": None,
                "PEER_NODE_HOSTNAME": "client.network",
                "PEER_NODE_REALM": "network",
                "PEER_NODE_IP_ADDRESS": "127.0.0.1",
                "PEER_NODE_PORT": None,
                "WATCHDOG_TIMEOUT": 30
            }

        self.client_config = {
                "MODE": "CLIENT",
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

    def test__capability_exchange_procedure_and_disconnection_procedure_from_client(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        c_config = copy(self.client_config)

        s_config["LOCAL_NODE_PORT"] = 3868
        c_config["PEER_NODE_PORT"] = 3868

        #: Instantiate Diameter objects Diameter Server and Client,
        #: respectivetly.
        s = Diameter(config=s_config)
        c = Diameter(config=c_config)

        #: It worth note Diameter object is unique across processes. There is
        #: no reason to start two or more in a single process. However, in order
        #: to allow unittests in a single process, two Diameter objects will be
        #: run by using the threading module. That's because the `start` method
        #: is blocking for Diameter objects who play role as Diameter Server.
        thr_s = threading.Thread(name="server", target=s.start)
        thr_s.start()

        #: Before run the Diameter Client, let's verify the Diameter Server
        #: state.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        time.sleep(1)

        #: Start the Diameter Client.
        thr_c = threading.Thread(name="client", target=c.start)
        thr_c.start()

        time.sleep(1)

        #: Check the Diameter Server state now is running.
        self.assertTrue(s.is_open())
        self.assertFalse(s.is_closed())
        self.assertEqual(s.get_current_state(), R_OPEN)

        #: Check the Diameter Client state now is running.
        self.assertTrue(c.is_open())
        self.assertFalse(c.is_closed())
        self.assertEqual(c.get_current_state(), I_OPEN)

        #: Close the Diameter connection from Client.
        c.close()

        time.sleep(5)   # It may be better

        #: Check the Diameter Server state now is closed.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        #: Check the Diameter Client state now is closed.
        self.assertFalse(c.is_open())
        self.assertTrue(c.is_closed())
        self.assertEqual(c.get_current_state(), CLOSED)

    def test__capability_exchange_procedure_and_disconnection_procedure_from_server(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        c_config = copy(self.client_config)

        s_config["LOCAL_NODE_PORT"] = 3869
        c_config["PEER_NODE_PORT"] = 3869

        #: Instantiate Diameter objects Diameter Server and Client,
        #: respectivetly.
        s = Diameter(config=s_config)
        c = Diameter(config=c_config)

        #: It worth note Diameter object is unique across processes. There is
        #: no reason to start two or more in a single process. However, in order
        #: to allow unittests in a single process, two Diameter objects will be
        #: run by using the threading module. That's because the `start` method
        #: is blocking for Diameter objects who play role as Diameter Server.
        thr_s = threading.Thread(name="server", target=s.start)
        thr_s.start()

        #: Before run the Diameter Client, let's verify the Diameter Server
        #: state.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        time.sleep(1)

        #: Start the Diameter Client.
        thr_c = threading.Thread(name="client", target=c.start)
        thr_c.start()

        time.sleep(1)

        #: Check the Diameter Server state now is running.
        self.assertTrue(s.is_open())
        self.assertFalse(s.is_closed())
        self.assertEqual(s.get_current_state(), R_OPEN)

        #: Check the Diameter Client state now is running.
        self.assertTrue(c.is_open())
        self.assertFalse(c.is_closed())
        self.assertEqual(c.get_current_state(), I_OPEN)

        #: Close the Diameter connection from Server.
        s.close()

        time.sleep(5)   # It may be better

        #: Check the Diameter Server state now is running.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        #: Check the Diameter Client state now is running.
        self.assertFalse(c.is_open())
        self.assertTrue(c.is_closed())
        self.assertEqual(c.get_current_state(), CLOSED)

    def test__get_base_message__cer__from_client(self):
        #: Preconditions.
        c_config = copy(self.client_config)
        c_config["PEER_NODE_PORT"] = 3870

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

    def test__get_base_message__cea__from_client(self):
        #: Preconditions.
        c_config = copy(self.client_config)
        c_config["PEER_NODE_PORT"] = 3870

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

    def test__get_base_message__dwr__from_client(self):
        #: Preconditions.
        c_config = copy(self.client_config)
        c_config["PEER_NODE_PORT"] = 3870

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Device-Watchdog-Request
        msg = base.dwr

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

    def test__get_base_message__dwa__from_client(self):
        #: Preconditions.
        c_config = copy(self.client_config)
        c_config["PEER_NODE_PORT"] = 3870

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Device-Watchdog-Answer
        msg = base.dwa

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

    def test__get_base_message__dpr__from_client(self):
        #: Preconditions.
        c_config = copy(self.client_config)
        c_config["PEER_NODE_PORT"] = 3870

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Disconnect-Peer-Request
        msg = base.dpr

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Disconnect-Cause AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001114000000c00000000")
        self.assertEqual(msg.avps[2].data, DISCONNECT_CAUSE_REBOOTING)

    def test__get_base_message__dpa__from_client(self):
        #: Preconditions.
        c_config = copy(self.client_config)
        c_config["PEER_NODE_PORT"] = 3870

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Disconnect-Peer-Answer
        msg = base.dpa

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

    def test__get_base_message__cer__from_server(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        s_config["LOCAL_NODE_PORT"] = 3870

        #: Instantiate Diameter objects Diameter Server.
        s = Diameter(config=s_config)

        #: Get the Diameter base protocol messages.
        base = s.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "00000108400000167365727665722e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"server.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

    def test__get_base_message__cea__from_server(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        s_config["LOCAL_NODE_PORT"] = 3870

        #: Instantiate Diameter objects Diameter Server.
        s = Diameter(config=s_config)

        #: Get the Diameter base protocol messages.
        base = s.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "00000108400000167365727665722e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"server.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

    def test__get_base_message__dwr__from_server(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        s_config["LOCAL_NODE_PORT"] = 3870

        #: Instantiate Diameter objects Diameter Server.
        s = Diameter(config=s_config)

        #: Get the Diameter base protocol messages.
        base = s.get_base_messages()

        #: Device-Watchdog-Request
        msg = base.dwr

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "00000108400000167365727665722e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"server.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

    def test__get_base_message__dwa__from_server(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        s_config["LOCAL_NODE_PORT"] = 3870

        #: Instantiate Diameter objects Diameter Server.
        s = Diameter(config=s_config)

        #: Get the Diameter base protocol messages.
        base = s.get_base_messages()

        #: Device-Watchdog-Answer
        msg = base.dwa

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, DEVICE_WATCHDOG_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "00000108400000167365727665722e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"server.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

    def test__get_base_message__dpr__from_server(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        s_config["LOCAL_NODE_PORT"] = 3870

        #: Instantiate Diameter objects Diameter Server.
        s = Diameter(config=s_config)

        #: Get the Diameter base protocol messages.
        base = s.get_base_messages()

        #: Disconnect-Peer-Request
        msg = base.dpr

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "00000108400000167365727665722e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"server.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Disconnect-Cause AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001114000000c00000000")
        self.assertEqual(msg.avps[2].data, DISCONNECT_CAUSE_REBOOTING)

    def test__get_base_message__dpa__from_server(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        s_config["LOCAL_NODE_PORT"] = 3870

        #: Instantiate Diameter objects Diameter Server.
        s = Diameter(config=s_config)

        #: Get the Diameter base protocol messages.
        base = s.get_base_messages()

        #: Disconnect-Peer-Answer
        msg = base.dpa

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, DISCONNECT_PEER_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "00000108400000167365727665722e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"server.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")


# @unittest.SkipTest
class TestDiameterBaseOneApplicationId(unittest.TestCase):
    def setUp(self):
        self.server_config = {
                "MODE": "SERVER",
                "APPLICATIONS": [],
                "LOCAL_NODE_HOSTNAME": "server.network",
                "LOCAL_NODE_REALM": "network",
                "LOCAL_NODE_IP_ADDRESS": "127.0.0.1",
                "LOCAL_NODE_PORT": 3870,
                "PEER_NODE_HOSTNAME": "client.network",
                "PEER_NODE_REALM": "network",
                "PEER_NODE_IP_ADDRESS": "127.0.0.1",
                "PEER_NODE_PORT": None,
                "WATCHDOG_TIMEOUT": 30
            }

        self.client_config = {
                "MODE": "CLIENT",
                "APPLICATIONS": [],
                "LOCAL_NODE_HOSTNAME": "client.network",
                "LOCAL_NODE_REALM": "network",
                "LOCAL_NODE_IP_ADDRESS": "127.0.0.1",
                "LOCAL_NODE_PORT": None,
                "PEER_NODE_HOSTNAME": "server.network",
                "PEER_NODE_REALM": "network",
                "PEER_NODE_IP_ADDRESS": "127.0.0.1",
                "PEER_NODE_PORT": 3870,
                "WATCHDOG_TIMEOUT": 30
            }

    def test__capability_exchange_procedure_and_disconnection_procedure_from_client(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        c_config = copy(self.client_config)

        s_config["LOCAL_NODE_PORT"] = 3868
        c_config["PEER_NODE_PORT"] = 3868

        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }

        s_config["APPLICATIONS"].append(app)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Server and Client,
        #: respectivetly.
        s = Diameter(config=s_config)
        c = Diameter(config=c_config)

        #: It worth note Diameter object is unique across processes. There is
        #: no reason to start two or more in a single process. However, in order
        #: to allow unittests in a single process, two Diameter objects will be
        #: run by using the threading module. That's because the `start` method
        #: is blocking for Diameter objects who play role as Diameter Server.
        thr_s = threading.Thread(name="server", target=s.start)
        thr_s.start()

        #: Before run the Diameter Client, let's verify the Diameter Server
        #: state.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        time.sleep(1)

        #: Start the Diameter Client.
        thr_c = threading.Thread(name="client", target=c.start)
        thr_c.start()

        time.sleep(1)

        #: Check the Diameter Server state now is running.
        self.assertTrue(s.is_open())
        self.assertFalse(s.is_closed())
        self.assertEqual(s.get_current_state(), R_OPEN)

        #: Check the Diameter Client state now is running.
        self.assertTrue(c.is_open())
        self.assertFalse(c.is_closed())
        self.assertEqual(c.get_current_state(), I_OPEN)

        #: Close the Diameter connection from Client.
        c.close()

        time.sleep(5)   # It may be better

        #: Check the Diameter Server state now is running.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        #: Check the Diameter Client state now is running.
        self.assertFalse(c.is_open())
        self.assertTrue(c.is_closed())
        self.assertEqual(c.get_current_state(), CLOSED)

    def test__capability_exchange_procedure_and_disconnection_procedure_from_server(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        c_config = copy(self.client_config)

        s_config["LOCAL_NODE_PORT"] = 3869
        c_config["PEER_NODE_PORT"] = 3869

        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }

        s_config["APPLICATIONS"].append(app)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Server and Client,
        #: respectivetly.
        s = Diameter(config=s_config)
        c = Diameter(config=c_config)

        #: It worth note Diameter object is unique across processes. There is
        #: no reason to start two or more in a single process. However, in order
        #: to allow unittests in a single process, two Diameter objects will be
        #: run by using the threading module. That's because the `start` method
        #: is blocking for Diameter objects who play role as Diameter Server.
        thr_s = threading.Thread(name="server", target=s.start)
        thr_s.start()

        #: Before run the Diameter Client, let's verify the Diameter Server
        #: state.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        time.sleep(1)

        #: Start the Diameter Client.
        thr_c = threading.Thread(name="client", target=c.start)
        thr_c.start()

        time.sleep(1)

        #: Check the Diameter Server state now is running.
        self.assertTrue(s.is_open())
        self.assertFalse(s.is_closed())
        self.assertEqual(s.get_current_state(), R_OPEN)

        #: Check the Diameter Client state now is running.
        self.assertTrue(c.is_open())
        self.assertFalse(c.is_closed())
        self.assertEqual(c.get_current_state(), I_OPEN)

        #: Close the Diameter connection from Server.
        s.close()

        time.sleep(5)   # It may be better

        #: Check the Diameter Server state now is running.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        #: Check the Diameter Client state now is running.
        self.assertFalse(c.is_open())
        self.assertTrue(c.is_closed())
        self.assertEqual(c.get_current_state(), CLOSED)

    def test__get_base_message__cer__from_client__app_Cx(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_Cx)

    def test__get_base_message__cea__from_client__app_Cx(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_Cx)

    def test__get_base_message__cer__from_client__app_Sh(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Sh
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000001")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_Sh)

    def test__get_base_message__cea__from_client__app_Sh(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Sh
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000001")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_Sh)

    def test__get_base_message__cer__from_client__app_Zh(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Zh
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000005")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_Zh)

    def test__get_base_message__cea__from_client__app_Zh(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Zh
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000005")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_Zh)

    def test__get_base_message__cer__from_client__app_Rx(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Rx
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000014")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_Rx)

    def test__get_base_message__cea__from_client__app_Rx(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Rx
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000014")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_Rx)

    def test__get_base_message__cer__from_client__app_Gx(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Gx
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000016")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_Gx)

    def test__get_base_message__cea__from_client__app_Gx(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Gx
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000016")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_Gx)

    def test__get_base_message__cer__from_client__app_S6a(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_S6a
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000023")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_S6a)

    def test__get_base_message__cea__from_client__app_S6a(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_S6a
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000023")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_S6a)

    def test__get_base_message__cer__from_client__app_S13(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_S13
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000024")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_S13)

    def test__get_base_message__cea__from_client__app_S13(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_S13
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000024")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_S13)

    def test__get_base_message__cer__from_client__app_SWm(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_SWm
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000030")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_SWm)

    def test__get_base_message__cea__from_client__app_SWm(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_SWm
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000030")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_SWm)

    def test__get_base_message__cer__from_client__app_SWx(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_SWx
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000031")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_SWx)

    def test__get_base_message__cea__from_client__app_SWx(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_SWx
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000031")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_SWx)

    def test__get_base_message__cer__from_client__app_S6b(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_S6b
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000038")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_S6b)

    def test__get_base_message__cea__from_client__app_S6b(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_S6b
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000038")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_S6b)

    def test__get_base_message__cer__from_client__app_SLh(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_SLh
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c0100004b")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_SLh)

    def test__get_base_message__cea__from_client__app_SLh(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_SLh
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c0100004b")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_SLh)

    def test__get_base_message__cer__from_client__app_UNKNOWN(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_DEFAULT,
            "app_id": DIAMETER_APPLICATION_UNKNOWN
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c00000000000001024000000cf5c6f515")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_DEFAULT)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_UNKNOWN)

    def test__get_base_message__cea__from_client__app_UNKNOWN(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_DEFAULT,
            "app_id": DIAMETER_APPLICATION_UNKNOWN
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c00000000000001024000000cf5c6f515")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_DEFAULT)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_UNKNOWN)

    def test__get_base_message__cer__from_client__app_RELAY(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_DEFAULT,
            "app_id": DIAMETER_APPLICATION_RELAY
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c00000000000001024000000cffffffff")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_DEFAULT)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_RELAY)

    def test__get_base_message__cea__from_client__app_RELAY(self):
        #: Preconditions.
        app = {
            "vendor_id": VENDOR_ID_DEFAULT,
            "app_id": DIAMETER_APPLICATION_RELAY
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Answer
        msg = base.cea

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_RESPONSE)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Result-Code AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010c4000000c000007d1")
        self.assertEqual(msg.avps[0].data, DIAMETER_SUCCESS)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[1].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[2].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[3].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[4].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[5].data, b"Python bromelia")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000001024000000c00000000")
        self.assertEqual(msg.avps[6].data, DIAMETER_APPLICATION_DEFAULT)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c00000000000001024000000cffffffff")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_DEFAULT)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_RELAY)


# @unittest.SkipTest
class TestDiameterBaseMultipleApplicationIds(unittest.TestCase):
    def setUp(self):
        self.server_config = {
                "MODE": "SERVER",
                "APPLICATIONS": [],
                "LOCAL_NODE_HOSTNAME": "server.network",
                "LOCAL_NODE_REALM": "network",
                "LOCAL_NODE_IP_ADDRESS": "127.0.0.1",
                "LOCAL_NODE_PORT": 3870,
                "PEER_NODE_HOSTNAME": "client.network",
                "PEER_NODE_REALM": "network",
                "PEER_NODE_IP_ADDRESS": "127.0.0.1",
                "PEER_NODE_PORT": None,
                "WATCHDOG_TIMEOUT": 30
            }

        self.client_config = {
                "MODE": "CLIENT",
                "APPLICATIONS": [],
                "LOCAL_NODE_HOSTNAME": "client.network",
                "LOCAL_NODE_REALM": "network",
                "LOCAL_NODE_IP_ADDRESS": "127.0.0.1",
                "LOCAL_NODE_PORT": None,
                "PEER_NODE_HOSTNAME": "server.network",
                "PEER_NODE_REALM": "network",
                "PEER_NODE_IP_ADDRESS": "127.0.0.1",
                "PEER_NODE_PORT": 3870,
                "WATCHDOG_TIMEOUT": 30
            }

    def test__capability_exchange_procedure_and_disconnection_procedure_from_client__2_apps(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        c_config = copy(self.client_config)

        s_config["LOCAL_NODE_PORT"] = 3868
        c_config["PEER_NODE_PORT"] = 3868

        app1 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }
        app2 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Gx
        }

        s_config["APPLICATIONS"].append(app1)
        s_config["APPLICATIONS"].append(app2)

        c_config["APPLICATIONS"].append(app1)
        c_config["APPLICATIONS"].append(app2)

        #: Instantiate Diameter objects Diameter Server and Client,
        #: respectivetly.
        s = Diameter(config=s_config)
        c = Diameter(config=c_config)

        #: It worth note Diameter object is unique across processes. There is
        #: no reason to start two or more in a single process. However, in order
        #: to allow unittests in a single process, two Diameter objects will be
        #: run by using the threading module. That's because the `start` method
        #: is blocking for Diameter objects who play role as Diameter Server.
        thr_s = threading.Thread(name="server", target=s.start)
        thr_s.start()

        #: Before run the Diameter Client, let's verify the Diameter Server
        #: state.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        time.sleep(1)

        #: Start the Diameter Client.
        thr_c = threading.Thread(name="client", target=c.start)
        thr_c.start()

        time.sleep(1)

        #: Check the Diameter Server state now is running.
        self.assertTrue(s.is_open())
        self.assertFalse(s.is_closed())
        self.assertEqual(s.get_current_state(), R_OPEN)

        #: Check the Diameter Client state now is running.
        self.assertTrue(c.is_open())
        self.assertFalse(c.is_closed())
        self.assertEqual(c.get_current_state(), I_OPEN)

        #: Close the Diameter connection from Client.
        c.close()

        time.sleep(5)   # It may be better

        #: Check the Diameter Server state now is running.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        #: Check the Diameter Client state now is running.
        self.assertFalse(c.is_open())
        self.assertTrue(c.is_closed())
        self.assertEqual(c.get_current_state(), CLOSED)

    def test__capability_exchange_procedure_and_disconnection_procedure_from_server__2_apps(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        c_config = copy(self.client_config)

        s_config["LOCAL_NODE_PORT"] = 3869
        c_config["PEER_NODE_PORT"] = 3869

        app1 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }
        app2 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Gx
        }

        s_config["APPLICATIONS"].append(app1)
        s_config["APPLICATIONS"].append(app2)

        c_config["APPLICATIONS"].append(app1)
        c_config["APPLICATIONS"].append(app2)

        #: Instantiate Diameter objects Diameter Server and Client,
        #: respectivetly.
        s = Diameter(config=s_config)
        c = Diameter(config=c_config)

        #: It worth note Diameter object is unique across processes. There is
        #: no reason to start two or more in a single process. However, in order
        #: to allow unittests in a single process, two Diameter objects will be
        #: run by using the threading module. That's because the `start` method
        #: is blocking for Diameter objects who play role as Diameter Server.
        thr_s = threading.Thread(name="server", target=s.start)
        thr_s.start()

        #: Before run the Diameter Client, let's verify the Diameter Server
        #: state.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        time.sleep(1)

        #: Start the Diameter Client.
        thr_c = threading.Thread(name="client", target=c.start)
        thr_c.start()

        time.sleep(1)

        #: Check the Diameter Server state now is running.
        self.assertTrue(s.is_open())
        self.assertFalse(s.is_closed())
        self.assertEqual(s.get_current_state(), R_OPEN)

        #: Check the Diameter Client state now is running.
        self.assertTrue(c.is_open())
        self.assertFalse(c.is_closed())
        self.assertEqual(c.get_current_state(), I_OPEN)

        #: Close the Diameter connection from Server.
        s.close()

        time.sleep(5)   # It may be better

        #: Check the Diameter Server state now is running.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        #: Check the Diameter Client state now is running.
        self.assertFalse(c.is_open())
        self.assertTrue(c.is_closed())
        self.assertEqual(c.get_current_state(), CLOSED)

    def test__capability_exchange_procedure_and_disconnection_procedure_from_client__3_apps(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        c_config = copy(self.client_config)

        s_config["LOCAL_NODE_PORT"] = 3868
        c_config["PEER_NODE_PORT"] = 3868

        app1 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }
        app2 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Gx
        }
        app3 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Rx
        }

        s_config["APPLICATIONS"].append(app1)
        s_config["APPLICATIONS"].append(app2)
        s_config["APPLICATIONS"].append(app3)

        c_config["APPLICATIONS"].append(app1)
        c_config["APPLICATIONS"].append(app2)
        c_config["APPLICATIONS"].append(app3)

        #: Instantiate Diameter objects Diameter Server and Client,
        #: respectivetly.
        s = Diameter(config=s_config)
        c = Diameter(config=c_config)

        #: It worth note Diameter object is unique across processes. There is
        #: no reason to start two or more in a single process. However, in order
        #: to allow unittests in a single process, two Diameter objects will be
        #: run by using the threading module. That's because the `start` method
        #: is blocking for Diameter objects who play role as Diameter Server.
        thr_s = threading.Thread(name="server", target=s.start)
        thr_s.start()

        #: Before run the Diameter Client, let's verify the Diameter Server
        #: state.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        time.sleep(1)

        #: Start the Diameter Client.
        thr_c = threading.Thread(name="client", target=c.start)
        thr_c.start()

        time.sleep(1)

        #: Check the Diameter Server state now is running.
        self.assertTrue(s.is_open())
        self.assertFalse(s.is_closed())
        self.assertEqual(s.get_current_state(), R_OPEN)

        #: Check the Diameter Client state now is running.
        self.assertTrue(c.is_open())
        self.assertFalse(c.is_closed())
        self.assertEqual(c.get_current_state(), I_OPEN)

        #: Close the Diameter connection from Client.
        c.close()

        time.sleep(5)   # It may be better

        #: Check the Diameter Server state now is running.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        #: Check the Diameter Client state now is running.
        self.assertFalse(c.is_open())
        self.assertTrue(c.is_closed())
        self.assertEqual(c.get_current_state(), CLOSED)

    def test__capability_exchange_procedure_and_disconnection_procedure_from_server__3_apps(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        c_config = copy(self.client_config)

        s_config["LOCAL_NODE_PORT"] = 3869
        c_config["PEER_NODE_PORT"] = 3869

        app1 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }
        app2 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Gx
        }
        app3 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Rx
        }

        s_config["APPLICATIONS"].append(app1)
        s_config["APPLICATIONS"].append(app2)
        s_config["APPLICATIONS"].append(app3)

        c_config["APPLICATIONS"].append(app1)
        c_config["APPLICATIONS"].append(app2)
        c_config["APPLICATIONS"].append(app3)

        #: Instantiate Diameter objects Diameter Server and Client,
        #: respectivetly.
        s = Diameter(config=s_config)
        c = Diameter(config=c_config)

        #: It worth note Diameter object is unique across processes. There is
        #: no reason to start two or more in a single process. However, in order
        #: to allow unittests in a single process, two Diameter objects will be
        #: run by using the threading module. That's because the `start` method
        #: is blocking for Diameter objects who play role as Diameter Server.
        thr_s = threading.Thread(name="server", target=s.start)
        thr_s.start()

        #: Before run the Diameter Client, let's verify the Diameter Server
        #: state.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        time.sleep(1)

        #: Start the Diameter Client.
        thr_c = threading.Thread(name="client", target=c.start)
        thr_c.start()

        time.sleep(1)

        #: Check the Diameter Server state now is running.
        self.assertTrue(s.is_open())
        self.assertFalse(s.is_closed())
        self.assertEqual(s.get_current_state(), R_OPEN)

        #: Check the Diameter Client state now is running.
        self.assertTrue(c.is_open())
        self.assertFalse(c.is_closed())
        self.assertEqual(c.get_current_state(), I_OPEN)

        #: Close the Diameter connection from Server.
        s.close()

        time.sleep(5)   # It may be better

        #: Check the Diameter Server state now is running.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        #: Check the Diameter Client state now is running.
        self.assertFalse(c.is_open())
        self.assertTrue(c.is_closed())
        self.assertEqual(c.get_current_state(), CLOSED)

    def test__capability_exchange_procedure_and_disconnection_procedure_from_client__4_apps(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        c_config = copy(self.client_config)

        s_config["LOCAL_NODE_PORT"] = 3868
        c_config["PEER_NODE_PORT"] = 3868

        app1 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }
        app2 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Gx
        }
        app3 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Rx
        }
        app4 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Zh
        }

        s_config["APPLICATIONS"].append(app1)
        s_config["APPLICATIONS"].append(app2)
        s_config["APPLICATIONS"].append(app3)
        s_config["APPLICATIONS"].append(app4)

        c_config["APPLICATIONS"].append(app1)
        c_config["APPLICATIONS"].append(app2)
        c_config["APPLICATIONS"].append(app3)
        c_config["APPLICATIONS"].append(app4)

        #: Instantiate Diameter objects Diameter Server and Client,
        #: respectivetly.
        s = Diameter(config=s_config)
        c = Diameter(config=c_config)

        #: It worth note Diameter object is unique across processes. There is
        #: no reason to start two or more in a single process. However, in order
        #: to allow unittests in a single process, two Diameter objects will be
        #: run by using the threading module. That's because the `start` method
        #: is blocking for Diameter objects who play role as Diameter Server.
        thr_s = threading.Thread(name="server", target=s.start)
        thr_s.start()

        #: Before run the Diameter Client, let's verify the Diameter Server
        #: state.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        time.sleep(1)

        #: Start the Diameter Client.
        thr_c = threading.Thread(name="client", target=c.start)
        thr_c.start()

        time.sleep(1)

        #: Check the Diameter Server state now is running.
        self.assertTrue(s.is_open())
        self.assertFalse(s.is_closed())
        self.assertEqual(s.get_current_state(), R_OPEN)

        #: Check the Diameter Client state now is running.
        self.assertTrue(c.is_open())
        self.assertFalse(c.is_closed())
        self.assertEqual(c.get_current_state(), I_OPEN)

        #: Close the Diameter connection from Client.
        c.close()

        time.sleep(5)   # It may be better

        #: Check the Diameter Server state now is running.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        #: Check the Diameter Client state now is running.
        self.assertFalse(c.is_open())
        self.assertTrue(c.is_closed())
        self.assertEqual(c.get_current_state(), CLOSED)

    def test__capability_exchange_procedure_and_disconnection_procedure_from_server__4_apps(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        c_config = copy(self.client_config)

        s_config["LOCAL_NODE_PORT"] = 3869
        c_config["PEER_NODE_PORT"] = 3869

        app1 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }
        app2 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Gx
        }
        app3 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Rx
        }
        app4 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Zh
        }

        s_config["APPLICATIONS"].append(app1)
        s_config["APPLICATIONS"].append(app2)
        s_config["APPLICATIONS"].append(app3)
        s_config["APPLICATIONS"].append(app4)

        c_config["APPLICATIONS"].append(app1)
        c_config["APPLICATIONS"].append(app2)
        c_config["APPLICATIONS"].append(app3)
        c_config["APPLICATIONS"].append(app4)

        #: Instantiate Diameter objects Diameter Server and Client,
        #: respectivetly.
        s = Diameter(config=s_config)
        c = Diameter(config=c_config)

        #: It worth note Diameter object is unique across processes. There is
        #: no reason to start two or more in a single process. However, in order
        #: to allow unittests in a single process, two Diameter objects will be
        #: run by using the threading module. That's because the `start` method
        #: is blocking for Diameter objects who play role as Diameter Server.
        thr_s = threading.Thread(name="server", target=s.start)
        thr_s.start()

        #: Before run the Diameter Client, let's verify the Diameter Server
        #: state.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        time.sleep(1)

        #: Start the Diameter Client.
        thr_c = threading.Thread(name="client", target=c.start)
        thr_c.start()

        time.sleep(1)

        #: Check the Diameter Server state now is running.
        self.assertTrue(s.is_open())
        self.assertFalse(s.is_closed())
        self.assertEqual(s.get_current_state(), R_OPEN)

        #: Check the Diameter Client state now is running.
        self.assertTrue(c.is_open())
        self.assertFalse(c.is_closed())
        self.assertEqual(c.get_current_state(), I_OPEN)

        #: Close the Diameter connection from Server.
        s.close()

        time.sleep(5)   # It may be better

        #: Check the Diameter Server state now is running.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        #: Check the Diameter Client state now is running.
        self.assertFalse(c.is_open())
        self.assertTrue(c.is_closed())
        self.assertEqual(c.get_current_state(), CLOSED)

    def test__capability_exchange_procedure_and_disconnection_procedure_from_client__5_apps(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        c_config = copy(self.client_config)

        s_config["LOCAL_NODE_PORT"] = 3868
        c_config["PEER_NODE_PORT"] = 3868

        app1 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }
        app2 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Gx
        }
        app3 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Rx
        }
        app4 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Zh
        }
        app5 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_S6b
        }

        s_config["APPLICATIONS"].append(app1)
        s_config["APPLICATIONS"].append(app2)
        s_config["APPLICATIONS"].append(app3)
        s_config["APPLICATIONS"].append(app4)
        s_config["APPLICATIONS"].append(app5)

        c_config["APPLICATIONS"].append(app1)
        c_config["APPLICATIONS"].append(app2)
        c_config["APPLICATIONS"].append(app3)
        c_config["APPLICATIONS"].append(app4)
        c_config["APPLICATIONS"].append(app5)

        #: Instantiate Diameter objects Diameter Server and Client,
        #: respectivetly.
        s = Diameter(config=s_config)
        c = Diameter(config=c_config)

        #: It worth note Diameter object is unique across processes. There is
        #: no reason to start two or more in a single process. However, in order
        #: to allow unittests in a single process, two Diameter objects will be
        #: run by using the threading module. That's because the `start` method
        #: is blocking for Diameter objects who play role as Diameter Server.
        thr_s = threading.Thread(name="server", target=s.start)
        thr_s.start()

        #: Before run the Diameter Client, let's verify the Diameter Server
        #: state.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        time.sleep(1)

        #: Start the Diameter Client.
        thr_c = threading.Thread(name="client", target=c.start)
        thr_c.start()

        time.sleep(1)

        #: Check the Diameter Server state now is running.
        self.assertTrue(s.is_open())
        self.assertFalse(s.is_closed())
        self.assertEqual(s.get_current_state(), R_OPEN)

        #: Check the Diameter Client state now is running.
        self.assertTrue(c.is_open())
        self.assertFalse(c.is_closed())
        self.assertEqual(c.get_current_state(), I_OPEN)

        #: Close the Diameter connection from Client.
        c.close()

        time.sleep(5)   # It may be better

        #: Check the Diameter Server state now is running.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        #: Check the Diameter Client state now is running.
        self.assertFalse(c.is_open())
        self.assertTrue(c.is_closed())
        self.assertEqual(c.get_current_state(), CLOSED)

    def test__capability_exchange_procedure_and_disconnection_procedure_from_server__5_apps(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        c_config = copy(self.client_config)

        s_config["LOCAL_NODE_PORT"] = 3869
        c_config["PEER_NODE_PORT"] = 3869

        app1 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }
        app2 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Gx
        }
        app3 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Rx
        }
        app4 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Zh
        }
        app5 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_S6b
        }

        s_config["APPLICATIONS"].append(app1)
        s_config["APPLICATIONS"].append(app2)
        s_config["APPLICATIONS"].append(app3)
        s_config["APPLICATIONS"].append(app4)
        s_config["APPLICATIONS"].append(app5)

        c_config["APPLICATIONS"].append(app1)
        c_config["APPLICATIONS"].append(app2)
        c_config["APPLICATIONS"].append(app3)
        c_config["APPLICATIONS"].append(app4)
        c_config["APPLICATIONS"].append(app5)

        #: Instantiate Diameter objects Diameter Server and Client,
        #: respectivetly.
        s = Diameter(config=s_config)
        c = Diameter(config=c_config)

        #: It worth note Diameter object is unique across processes. There is
        #: no reason to start two or more in a single process. However, in order
        #: to allow unittests in a single process, two Diameter objects will be
        #: run by using the threading module. That's because the `start` method
        #: is blocking for Diameter objects who play role as Diameter Server.
        thr_s = threading.Thread(name="server", target=s.start)
        thr_s.start()

        #: Before run the Diameter Client, let's verify the Diameter Server
        #: state.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        time.sleep(1)

        #: Start the Diameter Client.
        thr_c = threading.Thread(name="client", target=c.start)
        thr_c.start()

        time.sleep(1)

        #: Check the Diameter Server state now is running.
        self.assertTrue(s.is_open())
        self.assertFalse(s.is_closed())
        self.assertEqual(s.get_current_state(), R_OPEN)

        #: Check the Diameter Client state now is running.
        self.assertTrue(c.is_open())
        self.assertFalse(c.is_closed())
        self.assertEqual(c.get_current_state(), I_OPEN)

        #: Close the Diameter connection from Server.
        s.close()

        time.sleep(5)   # It may be better

        #: Check the Diameter Server state now is running.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        #: Check the Diameter Client state now is running.
        self.assertFalse(c.is_open())
        self.assertTrue(c.is_closed())
        self.assertEqual(c.get_current_state(), CLOSED)

    def test__get_base_message__cer__from_client__2_apps(self):
        #: Preconditions.
        app1 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }
        app2 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Sh
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app1)
        c_config["APPLICATIONS"].append(app2)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_Cx)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000001")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_Sh)

    def test__get_base_message__cer__from_client__3_apps(self):
        #: Preconditions.
        app1 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }
        app2 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Sh
        }
        app3 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Zh
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app1)
        c_config["APPLICATIONS"].append(app2)
        c_config["APPLICATIONS"].append(app3)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_Cx)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000001")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_Sh)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[8].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000005")
        self.assertEqual(msg.avps[8].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[8].auth_application_id_avp.data, DIAMETER_APPLICATION_Zh)

    def test__get_base_message__cer__from_client__4_apps(self):
        #: Preconditions.
        app1 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }
        app2 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Sh
        }
        app3 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Zh
        }
        app4 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Rx
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app1)
        c_config["APPLICATIONS"].append(app2)
        c_config["APPLICATIONS"].append(app3)
        c_config["APPLICATIONS"].append(app4)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_Cx)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000001")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_Sh)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[8].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000005")
        self.assertEqual(msg.avps[8].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[8].auth_application_id_avp.data, DIAMETER_APPLICATION_Zh)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[9].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000014")
        self.assertEqual(msg.avps[9].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[9].auth_application_id_avp.data, DIAMETER_APPLICATION_Rx)

    def test__get_base_message__cer__from_client__5_apps(self):
        #: Preconditions.
        app1 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Cx
        }
        app2 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Sh
        }
        app3 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Zh
        }
        app4 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Rx
        }
        app5 = {
            "vendor_id": VENDOR_ID_3GPP,
            "app_id": DIAMETER_APPLICATION_Gx
        }

        c_config = copy(self.client_config)
        c_config["APPLICATIONS"].append(app1)
        c_config["APPLICATIONS"].append(app2)
        c_config["APPLICATIONS"].append(app3)
        c_config["APPLICATIONS"].append(app4)
        c_config["APPLICATIONS"].append(app5)

        #: Instantiate Diameter objects Diameter Client.
        c = Diameter(config=c_config)

        #: Get the Diameter base protocol messages.
        base = c.get_base_messages()

        #: Capability-Exchange-Request
        msg = base.cer

        #: Diameter Header
        self.assertEqual(msg.header.version, DIAMETER_VERSION)
        self.assertEqual(msg.header.flags, FLAG_REQUEST)
        self.assertEqual(msg.header.command_code, CAPABILITIES_EXCHANGE_MESSAGE)
        self.assertEqual(msg.header.application_id, DIAMETER_APPLICATION_DEFAULT)

        #: Origin-Host AVP
        self.assertEqual(msg.avps[0].dump().hex(), "0000010840000016636c69656e742e6e6574776f726b0000")
        self.assertEqual(msg.avps[0].data, b"client.network")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001284000000f6e6574776f726b00")
        self.assertEqual(msg.avps[1].data, b"network")

        #: Host-IP-Address AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001014000000e00017f0000010000")
        self.assertEqual(msg.avps[2].get_ip_address(), "127.0.0.1")

        #: Vendor-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010a4000000c00000000")
        self.assertEqual(msg.avps[3].data, VENDOR_ID_DEFAULT)

        #: Product-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000010d00000017507974686f6e2062726f6d656c696100")
        self.assertEqual(msg.avps[4].data, b"Python bromelia")

        #: Firmware-Revision AVP
        self.assertEqual(msg.avps[5].dump().hex(), "0000010b0000000c00000001")
        self.assertEqual(msg.avps[5].data, FIRMWARE_VERSION)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000000")
        self.assertEqual(msg.avps[6].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[6].auth_application_id_avp.data, DIAMETER_APPLICATION_Cx)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[7].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000001")
        self.assertEqual(msg.avps[7].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[7].auth_application_id_avp.data, DIAMETER_APPLICATION_Sh)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[8].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000005")
        self.assertEqual(msg.avps[8].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[8].auth_application_id_avp.data, DIAMETER_APPLICATION_Zh)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[9].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000014")
        self.assertEqual(msg.avps[9].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[9].auth_application_id_avp.data, DIAMETER_APPLICATION_Rx)

        #: Vendor-Specific-Application-Id AVP
        self.assertEqual(msg.avps[10].dump().hex(), "00000104400000200000010a4000000c000028af000001024000000c01000016")
        self.assertEqual(msg.avps[10].vendor_id_avp.data, VENDOR_ID_3GPP)
        self.assertEqual(msg.avps[10].auth_application_id_avp.data, DIAMETER_APPLICATION_Gx)

# @unittest.SkipTest
class TestDiameterBaseSpecificClientPort(unittest.TestCase):
    def setUp(self):
        self.server_config = {
                "MODE": "SERVER",
                "APPLICATIONS": [],
                "LOCAL_NODE_HOSTNAME": "server.network",
                "LOCAL_NODE_REALM": "network",
                "LOCAL_NODE_IP_ADDRESS": "127.0.0.1",
                "LOCAL_NODE_PORT": None,
                "PEER_NODE_HOSTNAME": "client.network",
                "PEER_NODE_REALM": "network",
                "PEER_NODE_IP_ADDRESS": "127.0.0.1",
                "PEER_NODE_PORT": None,
                "WATCHDOG_TIMEOUT": 30
            }

        self.client_config = {
                "MODE": "CLIENT",
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

    def test__capability_exchange_procedure_and_disconnection_procedure_from_client_with_specific_client_port(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        c_config = copy(self.client_config)

        s_config["LOCAL_NODE_PORT"] = 3868
        c_config["LOCAL_NODE_PORT"] = 3869
        c_config["PEER_NODE_PORT"] = 3868

        #: Instantiate Diameter objects Diameter Server and Client,
        #: respectivetly.
        s = Diameter(config=s_config)
        c = Diameter(config=c_config)

        #: It worth note Diameter object is unique across processes. There is
        #: no reason to start two or more in a single process. However, in order
        #: to allow unittests in a single process, two Diameter objects will be
        #: run by using the threading module. That's because the `start` method
        #: is blocking for Diameter objects who play role as Diameter Server.
        thr_s = threading.Thread(name="server", target=s.start)
        thr_s.start()

        #: Before run the Diameter Client, let's verify the Diameter Server
        #: state.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        time.sleep(1)

        #: Start the Diameter Client.
        thr_c = threading.Thread(name="client", target=c.start)
        thr_c.start()

        time.sleep(1)

        #: Check the Diameter Server state now is running.
        self.assertTrue(s.is_open())
        self.assertFalse(s.is_closed())
        self.assertEqual(s.get_current_state(), R_OPEN)

        #: Check the Diameter Client state now is running.
        self.assertTrue(c.is_open())
        self.assertFalse(c.is_closed())
        self.assertEqual(c.get_current_state(), I_OPEN)

        #: Check that client is bound to expected local port
        self.assertEqual(c._association.transport.sock.getsockname()[1], c_config["LOCAL_NODE_PORT"])

        #: Close the Diameter connection from Client.
        c.close()

        time.sleep(5)   # It may be better

        #: Check the Diameter Server state now is closed.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        #: Check the Diameter Client state now is closed.
        self.assertFalse(c.is_open())
        self.assertTrue(c.is_closed())
        self.assertEqual(c.get_current_state(), CLOSED)

    def test__capability_exchange_procedure_and_disconnection_procedure_from_server_with_specific_client_port(self):
        #: Preconditions.
        s_config = copy(self.server_config)
        c_config = copy(self.client_config)

        s_config["LOCAL_NODE_PORT"] = 3870
        c_config["LOCAL_NODE_PORT"] = 3871
        c_config["PEER_NODE_PORT"] = 3870

        #: Instantiate Diameter objects Diameter Server and Client,
        #: respectivetly.
        s = Diameter(config=s_config)
        c = Diameter(config=c_config)

        #: It worth note Diameter object is unique across processes. There is
        #: no reason to start two or more in a single process. However, in order
        #: to allow unittests in a single process, two Diameter objects will be
        #: run by using the threading module. That's because the `start` method
        #: is blocking for Diameter objects who play role as Diameter Server.
        thr_s = threading.Thread(name="server", target=s.start)
        thr_s.start()

        #: Before run the Diameter Client, let's verify the Diameter Server
        #: state.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        time.sleep(1)

        #: Start the Diameter Client.
        thr_c = threading.Thread(name="client", target=c.start)
        thr_c.start()

        time.sleep(1)

        #: Check the Diameter Server state now is running.
        self.assertTrue(s.is_open())
        self.assertFalse(s.is_closed())
        self.assertEqual(s.get_current_state(), R_OPEN)

        #: Check the Diameter Client state now is running.
        self.assertTrue(c.is_open())
        self.assertFalse(c.is_closed())
        self.assertEqual(c.get_current_state(), I_OPEN)

        #: Check that client is bound to expected local port
        self.assertEqual(c._association.transport.sock.getsockname()[1], c_config["LOCAL_NODE_PORT"])

        #: Close the Diameter connection from Server.
        s.close()

        time.sleep(5)   # It may be better

        #: Check the Diameter Server state now is running.
        self.assertFalse(s.is_open())
        self.assertTrue(s.is_closed())
        self.assertEqual(s.get_current_state(), CLOSED)

        #: Check the Diameter Client state now is running.
        self.assertFalse(c.is_open())
        self.assertTrue(c.is_closed())
        self.assertEqual(c.get_current_state(), CLOSED)


if __name__ == "__main__":
    unittest.main()
