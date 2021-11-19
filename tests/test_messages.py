# -*- coding: utf-8 -*-
"""
    test.test_messages
    ~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages unittests.
    
    :copyright: (c) 2020 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.constants import *
from bromelia.messages import AbortSessionAnswer
from bromelia.messages import AbortSessionRequest
from bromelia.messages import CapabilitiesExchangeAnswer
from bromelia.messages import CapabilitiesExchangeRequest
from bromelia.messages import DeviceWatchdogAnswer
from bromelia.messages import DeviceWatchdogRequest
from bromelia.messages import DisconnectPeerAnswer
from bromelia.messages import DisconnectPeerRequest
from bromelia.messages import ReAuthAnswer
from bromelia.messages import ReAuthRequest
from bromelia.messages import SessionTerminationAnswer
from bromelia.messages import SessionTerminationRequest


class TestCreateMessageCER(unittest.TestCase):
    def test_default_in_my_computer(self):
        ref = "0100007c800001010000000030fa20a508db4bcd000001084000001048656e7269717565000001284000001048656e7269717565000001014000000e0001c0a80f0d00000000010a4000000c000000000000010d00000012507974686f6e207372630000000001024000000c000000000000010b0000000c00000001"

        custom_avps = {
                        "origin_host": "Henrique",
                        "origin_realm": "Henrique",
                        "host_ip_address": "192.168.15.13",
                        "vendor_id": VENDOR_ID_DEFAULT,
                        "product_name": "Python src",
                        "auth_application_id": DIAMETER_APPLICATION_DEFAULT,
                        "firmware_revision": 1
        }
        msg = CapabilitiesExchangeRequest(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])

    def test_custom_1(self):
        ref = "0100006c800001010000000030fa20a508db4bcd000001084000000b65733200000001284000000b65736d00000001014000000e00010a81f1eb00000000010a4000000c000000000000010d0000000a45530000000001024000000c010000300000010b0000000c00000001"

        custom_avps = {
                        "origin_host": "es2",
                        "origin_realm": "esm",
                        "host_ip_address": "10.129.241.235",
                        "vendor_id": VENDOR_ID_DEFAULT,
                        "product_name": "ES",
                        "auth_application_id": DIAMETER_APPLICATION_SWm,
                        "firmware_revision": 1
        }
        msg = CapabilitiesExchangeRequest(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])

    def test_custom_2(self):
        custom_avps = {
                        "origin_host": "drasm03c.mncXXX.mccYYY.3gppnetwork.org",
                        "origin_realm": "mncXXX.mccYYY.3gppnetwork.org",
                        "host_ip_address": "10.110.219.82",
                        "vendor_id": VENDOR_ID_TEKELEC,
                        "product_name": "DSR",
                        "auth_application_id": DIAMETER_APPLICATION_RELAY,
                        "firmware_revision": 529153
        }

        msg = CapabilitiesExchangeRequest(**custom_avps)
        ref = "010000ac800001010000000063fad2bd0010f9c9000001084000002e647261736d3033632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000128400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000001014000000e00010a6edb5200000000010a4000000c000001430000010d0000000b44535200000001024000000cffffffff0000010b0000000c00081301"

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])


class TestCreateMessageCEA(unittest.TestCase):
    def test_default_in_my_computer(self):
        ref = "01000090000001010000000030fa20a508db4bcd0000010c4000000c000007d1000001084000001048656e7269717565000001284000001048656e7269717565000001014000000e0001c0a80f0d00000000010a4000000c000000000000010d0000001b42726f6d656c69614170706c69636174696f6e00000001024000000c010000300000010b0000000c00000001"

        custom_avps = {
                        "origin_host": "Henrique",
                        "origin_realm": "Henrique",
                        "host_ip_address": "192.168.15.13",
                        "vendor_id": VENDOR_ID_DEFAULT,
                        "product_name": "BromeliaApplication",
                        "auth_application_id": DIAMETER_APPLICATION_SWm,
                        "firmware_revision": 1
        }
        msg = CapabilitiesExchangeAnswer(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])

    def test_custom_1(self):
        ref = "010000b8000001010000000063fad2bd0010f9c90000010c4000000c000007d1000001084000002d647261747263622e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f726700000000000128400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000001014000000e00010a9f78c400000000010a4000000c000001430000010d0000000b44535200000001024000000cffffffff0000010b0000000c00081301"

        custom_avps = {
                        "origin_host": "dratrcb.mncXXX.mccYYY.3gppnetwork.org",
                        "origin_realm": "mncXXX.mccYYY.3gppnetwork.org",
                        "host_ip_address": "10.159.120.196",
                        "vendor_id": VENDOR_ID_TEKELEC,
                        "product_name": "DSR",
                        "auth_application_id": DIAMETER_APPLICATION_RELAY,
                        "firmware_revision": 529153
        }
        msg = CapabilitiesExchangeAnswer(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])


class TestCreateMessageRAR(unittest.TestCase):
    def test_default_in_my_computer(self):
        custom_avps = {
                        "auth_application_id": DIAMETER_APPLICATION_Rx,
                        "origin_host": "Henrique",
                        "origin_realm": "Henrique",
                        "destination_realm": "mncXXX.mccYYY.3gppnetwork.org",
                        "destination_host": "pcrf.mncXXX.mccYYY.3gppnetwork.org",
                        "re_auth_request_type": RE_AUTH_REQUEST_TYPE_AUTHORIZE_AUTHENTICATE
        }
        msg = ReAuthRequest(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "c0")
        self.assertEqual(msg.header.command_code.hex(), "000102")
        self.assertEqual(msg.header.application_id.hex(), "01000014")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001084000001048656e7269717565")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000001048656e7269717565")

        #: Destination-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000011b400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Destination-Host AVP
        self.assertEqual(msg.avps[4].dump().hex(), "000001254000002a706372662e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001024000000c01000014")

        #: Re-Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "0000011d4000000c00000001")


    def test_custom_1(self):
        custom_avps = {
                        "auth_application_id": DIAMETER_APPLICATION_Gx,
                        "origin_host": "pcrf-gx",
                        "origin_realm": "pcrf-gx.operator.com",
                        "destination_realm": "mncXXX.mccYYY.3gppnetwork.org",
                        "destination_host": "pgw.mncXXX.mccYYY.3gppnetwork.org",
                        "re_auth_request_type": RE_AUTH_REQUEST_TYPE_AUTHORIZE_ONLY
        }
        msg = ReAuthRequest(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "c0")
        self.assertEqual(msg.header.command_code.hex(), "000102")
        self.assertEqual(msg.header.application_id.hex(), "01000016")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001084000000f706372662d677800")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000001c706372662d67782e6f70657261746f722e636f6d")

        #: Destination-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000011b400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Destination-Host AVP
        self.assertEqual(msg.avps[4].dump().hex(), "00000125400000297067772e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001024000000c01000016")

        #: Re-Auth-Application-Id AVP
        self.assertEqual(msg.avps[6].dump().hex(), "0000011d4000000c00000000")


class TestCreateMessageRAA(unittest.TestCase):
    def test_default_in_my_computer(self):
        custom_avps = {
                        "origin_host": "Henrique",
                        "origin_realm": "Henrique"
        }
        msg = ReAuthAnswer(**custom_avps)
        msg.header.application_id = DIAMETER_APPLICATION_Gx

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "40")
        self.assertEqual(msg.header.command_code.hex(), "000102")
        self.assertEqual(msg.header.application_id.hex(), "01000016")

        #: Result-Code AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010c4000000c000007d1")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001084000001048656e7269717565")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001284000001048656e7269717565")


    def test_custom_1(self):
        custom_avps = {
                        "origin_host": "pcrf-gx",
                        "origin_realm": "pcrf-gx.operator.com",
    					"origin_state_id": 1543977942,
        }
        msg = ReAuthAnswer(**custom_avps)
        msg.header.application_id = DIAMETER_APPLICATION_Rx

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "40")
        self.assertEqual(msg.header.command_code.hex(), "000102")
        self.assertEqual(msg.header.application_id.hex(), "01000014")

        #: Result-Code AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010c4000000c000007d1")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001084000000f706372662d677800")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001284000001c706372662d67782e6f70657261746f722e636f6d")

        #: Origin-State-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "000001164000000c5c073bd6")


class TestCreateMessageASR(unittest.TestCase):
    def test_default_in_my_computer(self):
        custom_avps = {
                        "origin_host": "Henrique",
                        "origin_realm": "Henrique",
                        "destination_realm": "ims.mncXXX.mccYYY.3gppnetwork.org",
                        "destination_host": "rx.pcsf2rj1.ims.mncXXX.mccYYY.3gppnetwork.org",
                        "auth_application_id": DIAMETER_APPLICATION_Rx,
    					"route_record": "pcrf-rx"
        }
        msg = AbortSessionRequest(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "c0")
        self.assertEqual(msg.header.command_code.hex(), "000112")
        self.assertEqual(msg.header.application_id.hex(), "01000014")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001084000001048656e7269717565")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000001048656e7269717565")

        #: Destination-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000011b40000029696d732e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Destination-Host AVP
        self.assertEqual(msg.avps[4].dump().hex(), "000001254000003572782e7063736632726a312e696d732e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001024000000c01000014")

        #: Route-Record AVP
        self.assertEqual(msg.avps[6].dump().hex(), "0000011a4000000f706372662d727800")


    def test_custom_1(self):
        custom_avps = {
                        "origin_host": "encvltapp1-ne-rx",
                        "origin_realm": "rxserver.com",
                        "destination_realm": "ims.mncXXX.mccYYY.3gppnetwork.org",
                        "destination_host": "rx.pcsf2rj1.ims.mncXXX.mccYYY.3gppnetwork.org",
                        "auth_application_id": DIAMETER_APPLICATION_Rx,
    					"route_record": "rxserver-ne-rx"
        }
        msg = AbortSessionRequest(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "c0")
        self.assertEqual(msg.header.command_code.hex(), "000112")
        self.assertEqual(msg.header.application_id.hex(), "01000014")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010840000018656e63766c74617070312d6e652d7278")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000001472787365727665722e636f6d")

        #: Destination-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000011b40000029696d732e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Destination-Host AVP
        self.assertEqual(msg.avps[4].dump().hex(), "000001254000003572782e7063736632726a312e696d732e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001024000000c01000014")

        #: Route-Record AVP
        self.assertEqual(msg.avps[6].dump().hex(), "0000011a4000001672787365727665722d6e652d72780000")


class TestCreateMessageASA(unittest.TestCase):
    def test_default_in_my_computer(self):
        custom_avps = {
                        "origin_host": "Henrique",
                        "origin_realm": "Henrique"
        }
        msg = AbortSessionAnswer(**custom_avps)
        msg.header.application_id = DIAMETER_APPLICATION_Rx

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "40")
        self.assertEqual(msg.header.command_code.hex(), "000112")
        self.assertEqual(msg.header.application_id.hex(), "01000014")

        #: Result-Code AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010c4000000c000007d1")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001084000001048656e7269717565")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001284000001048656e7269717565")


    def test_custom_1(self):
        custom_avps = {
                        "origin_host": "rx.pcsf2rj1.ims.mncXXX.mccYYY.3gppnetwork.org",
                        "origin_realm": "ims.mncXXX.mccYYY.3gppnetwork.org",
        }
        msg = AbortSessionAnswer(**custom_avps)
        msg.header.application_id = DIAMETER_APPLICATION_Rx

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "40")
        self.assertEqual(msg.header.command_code.hex(), "000112")
        self.assertEqual(msg.header.application_id.hex(), "01000014")

        #: Result-Code AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010c4000000c000007d1")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001084000003572782e7063736632726a312e696d732e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000012840000029696d732e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")


class TestCreateMessageSTR(unittest.TestCase):
    def test_default_in_my_computer(self):
        custom_avps = {
                        "session_id": "Henrique",
                        "origin_host": "Henrique",
                        "origin_realm": "Henrique",
                        "destination_realm": "mncXXX.mccYYY.3gppnetwork.org",
                        "auth_application_id": DIAMETER_APPLICATION_S6b,
                        "termination_cause": DIAMETER_LOGOUT,
                        "user_name": "my-user@nai.epc.mncXXX.mccYYY.3gppnetwork.org",
                        "destination_host": "rj4.mncXXX.mccYYY.3gppnetwork.org",
        }
        msg = SessionTerminationRequest(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "80")
        self.assertEqual(msg.header.command_code.hex(), "000113")
        self.assertEqual(msg.header.application_id.hex(), "00000000")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001084000001048656e7269717565")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001284000001048656e7269717565")

        #: Destination-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000011b400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "000001024000000c01000038")

        #: Termination-Cause AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001274000000c00000001")

        #: User-Name AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000001400000356d792d75736572406e61692e6570632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Destination-Host AVP
        self.assertEqual(msg.avps[7].dump().hex(), "0000012540000029726a342e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")


    def test_custom_1(self):
        custom_avps = {
                        "session_id": "rj01.mncXXX.mccYYY.3gppnetwork.org;460335448;12637;5b58cc42-5d03",
                        "origin_host": "rj01.mncXXX.mccYYY.3gppnetwork.org",
                        "origin_realm": "mncXXX.mccYYY.3gppnetwork.org",
                        "destination_realm": "mncXXX.mccYYY.3gppnetwork.org",
                        "auth_application_id": DIAMETER_APPLICATION_S6b,
                        "termination_cause": DIAMETER_LOGOUT,
                        "user_name": "my-user@nai.mncXXX.mccYYY.3gppnetwork.org",
                        "destination_host": "rj4.mncXXX.mccYYY.3gppnetwork.org",
                        "route_record": "rj01.mncXXX.mccYYY.3gppnetwork.org"
        }
        msg = SessionTerminationRequest(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "80")
        self.assertEqual(msg.header.command_code.hex(), "000113")
        self.assertEqual(msg.header.application_id.hex(), "00000000")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001084000002a726a30312e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "00000128400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Destination-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000011b400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[4].dump().hex(), "000001024000000c01000038")

        #: Termination-Cause AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001274000000c00000001")

        #: User-Name AVP
        self.assertEqual(msg.avps[6].dump().hex(), "00000001400000316d792d75736572406e61692e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Destination-Host AVP
        self.assertEqual(msg.avps[7].dump().hex(), "0000012540000029726a342e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: Route-Record AVP
        self.assertEqual(msg.avps[8].dump().hex(), "0000011a4000002a726a30312e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000")


class TestCreateMessageSTA(unittest.TestCase):
    def test_default_in_my_computer(self):
        ref = "010001c4c000011301000038b8e650000ba90a6b0000010740000058726a6d636b30312d73616563697330342e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f72673b3436303333353434383b31323633373b35623538636334322d35643033000001084000003a726a6d636b30312d73616563697330342e6570632e6d6e633030352e6d63633732342e336770706e6574776f726b2e6f7267000000000128400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000000000011b400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000000000012540000029726a342e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000001024000000c01000038000001274000000c0000000100000001400000316d792d75736572406e61692e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000000000011a40000036726a6d636b30312d73616563697330342e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000"

        custom_avps = {
                        "session_id": "Henrique",
                        "origin_host": "Henrique",
                        "origin_realm": "Henrique",
                        "user_name": "my-user@nai.mncXXX.mccYYY.3gppnetwork.org",
        }
        msg = SessionTerminationAnswer(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "00")
        self.assertEqual(msg.header.command_code.hex(), "000113")
        self.assertEqual(msg.header.application_id.hex(), "00000000")

        #: Result-Code AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010c4000000c000007d1")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001084000001048656e7269717565")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001284000001048656e7269717565")

        #: User-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "00000001400000316d792d75736572406e61692e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")


    def test_custom_1(self):
        custom_avps = {
                        "session_id": "rj01.mncXXX.mccYYY.3gppnetwork.org;460335448;12637;5b58cc42-5d03",
                        "origin_host": "rj01.mncXXX.mccYYY.3gppnetwork.org",
                        "origin_realm": "mncXXX.mccYYY.3gppnetwork.org",
                        "user_name": "my-user@nai.mncXXX.mccYYY.3gppnetwork.org",
        }
        msg = SessionTerminationAnswer(**custom_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "00")
        self.assertEqual(msg.header.command_code.hex(), "000113")
        self.assertEqual(msg.header.application_id.hex(), "00000000")

        #: Result-Code AVP
        self.assertEqual(msg.avps[1].dump().hex(), "0000010c4000000c000007d1")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001084000002a726a30312e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f72670000")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "00000128400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")

        #: User-Name AVP
        self.assertEqual(msg.avps[4].dump().hex(), "00000001400000316d792d75736572406e61692e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000")


class TestCreateMessageDWR(unittest.TestCase):
    def test_default_in_my_computer(self):
        ref = "01000034800001180000000030fa20a508db4bcd000001084000001048656e7269717565000001284000001048656e7269717565"

        custom_avps = {
                        "origin_host": "Henrique",
                        "origin_realm": "Henrique",
        }
        msg = DeviceWatchdogRequest(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])

    def test_custom_1(self):
        ref = "0100002c80000118000000005b86e6aa874d4be9000001084000000b65733200000001284000000b65736d00"

        custom_avps = {
                        "origin_host": "es2",
                        "origin_realm": "esm",
        }
        msg = DeviceWatchdogRequest(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])

    def test_custom_2(self):
        ref = "0100006c800001180000000063fad2be0010f9ce000001084000002e647261736d3033632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000128400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"

        custom_avps = {
                        "origin_host": "drasm03c.mncXXX.mccYYY.3gppnetwork.org",
                        "origin_realm": "mncXXX.mccYYY.3gppnetwork.org",
        }
        msg = DeviceWatchdogRequest(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])

    def test_custom_3(self):
        ref = "010000688000011800000000203db507016fe246000001084000002c6472617472632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f726700000128400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"

        custom_avps = {
                        "origin_host": "dratrc.mncXXX.mccYYY.3gppnetwork.org",
                        "origin_realm": "mncXXX.mccYYY.3gppnetwork.org",
        }
        msg = DeviceWatchdogRequest(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])


class TestCreateMessageDWA(unittest.TestCase):
    def test_default_in_my_computer(self):
        ref = "01000040000001180000000030fa20a508db4bcd0000010c4000000c000007d1000001084000001048656e7269717565000001284000001048656e7269717565"

        custom_avps = {
                        "origin_host": "Henrique",
                        "origin_realm": "Henrique",
        }
        msg = DeviceWatchdogAnswer(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])

    def test_custom_1(self):
        ref = "010000380000011800000000203dbedf01bbc8e20000010c4000000c000007d1000001084000000b65733200000001284000000b65736d00"

        custom_avps = {
                        "origin_host": "es2",
                        "origin_realm": "esm",
        }
        msg = DeviceWatchdogAnswer(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])

    def test_custom_2(self):
        ref = "010000740000011800000000a0603b774cc758ea0000010c4000000c000007d1000001084000002c6472617472632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f726700000128400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"

        custom_avps = {
                        "origin_host": "dratrc.mncXXX.mccYYY.3gppnetwork.org",
                        "origin_realm": "mncXXX.mccYYY.3gppnetwork.org",
        }
        msg = DeviceWatchdogAnswer(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])

    def test_custom_3(self):
        ref = "01000078000001180000000063fad2bf0010f9d30000010c4000000c000007d1000001084000002d647261747263622e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f726700000000000128400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"

        custom_avps = {
                        "origin_host": "dratrcb.mncXXX.mccYYY.3gppnetwork.org",
                        "origin_realm": "mncXXX.mccYYY.3gppnetwork.org",
        }
        msg = DeviceWatchdogAnswer(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])


class TestCreateMessageDPR(unittest.TestCase):
    def test_default_in_my_computer(self):
        ref = "010000408000011a000000004f8f143a0069761d000001084000001048656e7269717565000001284000001048656e7269717565000001114000000c00000000"

        custom_avps = {
                        "origin_host": "Henrique",
                        "origin_realm": "Henrique",
                        "disconnect_cause": DISCONNECT_CAUSE_REBOOTING
        }
        msg = DisconnectPeerRequest(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])

    def test_custom_1(self):
        ref = "010000788000011a000000004f8f143a0069761d000001084000002d647261747263622e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f726700000000000128400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000001114000000c00000000"

        custom_avps = {
                        "origin_host": "dratrcb.mncXXX.mccYYY.3gppnetwork.org",
                        "origin_realm": "mncXXX.mccYYY.3gppnetwork.org",
                        "disconnect_cause": DISCONNECT_CAUSE_REBOOTING
        }
        msg = DisconnectPeerRequest(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])


class TestCreateMessageDPA(unittest.TestCase):
    def test_default_in_my_computer(self):
        ref = "010000400000011a000000004f8f143a0069761d0000010c4000000c000007d1000001084000001048656e7269717565000001284000001048656e7269717565"

        custom_avps = {
                        "origin_host": "Henrique",
                        "origin_realm": "Henrique",
        }
        msg = DisconnectPeerAnswer(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])

    def test_custom_1(self):
        ref = "010000780000011a000000004f8f143a0069761d0000010c4000000c000007d1000001084000002e647261736d3033632e6d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000000128400000256d6e635858582e6d63635959592e336770706e6574776f726b2e6f7267000000"

        custom_avps = {
                        "origin_host": "drasm03c.mncXXX.mccYYY.3gppnetwork.org",
                        "origin_realm": "mncXXX.mccYYY.3gppnetwork.org"
        }
        msg = DisconnectPeerAnswer(**custom_avps)

        self.maxDiff = None
        self.assertEqual(msg.dump().hex()[:24], ref[:24])
        self.assertEqual(msg.dump().hex()[40:], ref[40:])


if __name__ == "__main__":
    unittest.main()