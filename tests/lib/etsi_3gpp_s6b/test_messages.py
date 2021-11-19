# -*- coding: utf-8 -*-
"""
    tests.etsi_3gpp_s6b.test_messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages unittests 
	for 3GPP S6b Diameter Application Id.
    
    :copyright: (c) 2020 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import os
import sys
import unittest

base_dir = "/Users/henriquemr/Public/SWE/diameter_bromelia/bromelia"
sys.path.insert(0, base_dir)

from bromelia.avps.etsi_3gpp.ts_129_212 import UeLocalIpAddressAVP
from bromelia.avps.ietf.rfc5447 import MipHomeAgentHostAVP
from bromelia.avps.ietf.rfc6733 import OriginStateIdAVP
from bromelia.avps.ietf.rfc6733 import DestinationHostAVP
from bromelia.avps.ietf.rfc6733 import RouteRecordAVP
from bromelia.constants import *
from bromelia.lib.etsi_3gpp_s6b import *


class TestCreateMessageAAA(unittest.TestCase):
    def test_aaa__1(self):
        aaa_avps = {
            "mip6_feature_vector": 70368744177664,
            "session_timeout": 10800,
        }

        msg = AAA(**aaa_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "40")
        self.assertEqual(msg.header.command_code.hex(), "000109")
        self.assertEqual(msg.header.application_id.hex(), "01000038")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001024000000c01000038")

        #: Auth-Request-Type AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001124000000c00000002")

        #: Result-Code AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010c4000000c000007d1")

        #: MIP6-Feature-Vector AVP
        self.assertEqual(msg.avps[6].dump().hex(), "0000007c400000100000400000000000")

        #: Session-Timeout AVP
        self.assertEqual(msg.avps[7].dump().hex(), "0000001b4000000c00002a30")

    def test_aaa__2(self):
        aaa_avps = {
            "origin_host": "pgw0",
            "origin_realm": "local",
            "destination_realm": "remote",
            "mip6_feature_vector": 70368744177664,
            "session_timeout": 10800,
        }

        msg = AAA(**aaa_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "40")
        self.assertEqual(msg.header.command_code.hex(), "000109")
        self.assertEqual(msg.header.application_id.hex(), "01000038")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001024000000c01000038")

        #: Auth-Request-Type AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001124000000c00000002")

        #: Result-Code AVP
        self.assertEqual(msg.avps[3].dump().hex(), "0000010c4000000c000007d1")

        #: MIP6-Feature-Vector AVP
        self.assertEqual(msg.avps[6].dump().hex(), "0000007c400000100000400000000000")

        #: Session-Timeout AVP
        self.assertEqual(msg.avps[7].dump().hex(), "0000001b4000000c00002a30")


class TestCreateMessageAAR(unittest.TestCase):
    def test_aar__1(self):
        aar_avps = {
            "destination_realm": "remote",
            "user_name": "frodo",
        }

        msg = AAR(**aar_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "c0")
        self.assertEqual(msg.header.command_code.hex(), "000109")
        self.assertEqual(msg.header.application_id.hex(), "01000038")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001024000000c01000038")

        #: Destination-Realm AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000011b4000000e72656d6f74650000")

        #: Auth-Request-Type AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001124000000c00000002")

        #: User-Name AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000000014000000d66726f646f000000")


    def test_aar__2(self):
        aar_avps = {
            "origin_host": "pgw0",
            "origin_realm": "local",
            "destination_realm": "remote",
            "user_name": "frodo",
        }

        msg = AAR(**aar_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "c0")
        self.assertEqual(msg.header.command_code.hex(), "000109")
        self.assertEqual(msg.header.application_id.hex(), "01000038")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001024000000c01000038")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001084000000c70677730")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001284000000d6c6f63616c000000")

        #: Destination-Realm AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000011b4000000e72656d6f74650000")

        #: Auth-Request-Type AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001124000000c00000002")

        #: User-Name AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000000014000000d66726f646f000000")


    def test_aar__3(self):
        aar_avps = {
            "origin_host": "pgw0",
            "origin_realm": "local",
            "destination_realm": "remote",
            "origin_state_id": OriginStateIdAVP(1530156152),
            "user_name": "frodo",
            "mip6_agent_info": [
                                    MipHomeAgentHostAVP([
                                                            DestinationRealmAVP("remote"),
                                                            DestinationHostAVP("pgw0.topon.remote")
                                                        ])
            ],
            "visited_network_identifier": "mncXXX.mccYYY.3gppnetwork.org",
            "mip6_feature_vector": 70368744177664,
            "service_selection": "ims",
            "ue_local_ip_address": UeLocalIpAddressAVP("127.0.1.1"),
            "route_record": RouteRecordAVP("hop0"),
            "destination_host": DestinationHostAVP("aaa0")
        }

        msg = AAR(**aar_avps)

        #: Diameter Header
        self.assertEqual(msg.header.version.hex(), "01")
        self.assertEqual(msg.header.flags.hex(), "c0")
        self.assertEqual(msg.header.command_code.hex(), "000109")
        self.assertEqual(msg.header.application_id.hex(), "01000038")

        #: Origin-Host AVP
        self.assertEqual(msg.avps[1].dump().hex(), "000001024000000c01000038")

        #: Origin-Realm AVP
        self.assertEqual(msg.avps[2].dump().hex(), "000001084000000c70677730")

        #: Auth-Application-Id AVP
        self.assertEqual(msg.avps[3].dump().hex(), "000001284000000d6c6f63616c000000")

        #: Destination-Realm AVP
        self.assertEqual(msg.avps[4].dump().hex(), "0000011b4000000e72656d6f74650000")

        #: Auth-Request-Type AVP
        self.assertEqual(msg.avps[5].dump().hex(), "000001124000000c00000002")

        #: User-Name AVP
        self.assertEqual(msg.avps[6].dump().hex(), "000000014000000d66726f646f000000")


if __name__ == "__main__":
    unittest.main()