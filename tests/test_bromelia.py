# -*- coding: utf-8 -*-
"""
    test.test_bromelia
    ~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol bromelia unittests.
    
    :copyright: (c) 2021 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import os
import sys

testing_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(testing_dir)

sys.path.insert(0, base_dir)

from bromelia.bromelia import get_application_string_by_id   
from bromelia.bromelia import get_formatted_answer_as_per_request
from bromelia.constants import *
from bromelia.messages import CEA, CER
from bromelia.lib.etsi_3gpp_s6a import ULA, ULR


class TestGetApplicationStringById(unittest.TestCase):
    def test__get_application_string_by_id__0(self):
        self.assertIsNone(get_application_string_by_id(0))

    def test__get_application_string_by_id__DEFAULT(self):
        self.assertEqual(get_application_string_by_id(DIAMETER_APPLICATION_DEFAULT), "default")

    def test__get_application_string_by_id__Cx(self):
        self.assertEqual(get_application_string_by_id(DIAMETER_APPLICATION_Rx), "rx")

    def test__get_application_string_by_id__Sh(self):
        self.assertEqual(get_application_string_by_id(DIAMETER_APPLICATION_Sh), "sh")

    def test__get_application_string_by_id__Zh(self):
        self.assertEqual(get_application_string_by_id(DIAMETER_APPLICATION_Zh), "zh")

    def test__get_application_string_by_id__Rx(self):
        self.assertEqual(get_application_string_by_id(DIAMETER_APPLICATION_Rx), "rx")

    def test__get_application_string_by_id__Gx(self):
        self.assertEqual(get_application_string_by_id(DIAMETER_APPLICATION_Gx), "gx")

    def test__get_application_string_by_id__S6a(self):
        self.assertEqual(get_application_string_by_id(DIAMETER_APPLICATION_S6a), "s6a")

    def test__get_application_string_by_id__S13(self):
        self.assertEqual(get_application_string_by_id(DIAMETER_APPLICATION_S13), "s13")

    def test__get_application_string_by_id__SWm(self):
        self.assertEqual(get_application_string_by_id(DIAMETER_APPLICATION_SWm), "swm")

    def test__get_application_string_by_id__SWx(self):
        self.assertEqual(get_application_string_by_id(DIAMETER_APPLICATION_SWx), "swx")

    def test__get_application_string_by_id__S6b(self):
        self.assertEqual(get_application_string_by_id(DIAMETER_APPLICATION_S6b), "s6b")

    def test__get_application_string_by_id__SLh(self):
        self.assertEqual(get_application_string_by_id(DIAMETER_APPLICATION_SLh), "slh")

    def test__get_application_string_by_id__UNKNOWN(self):
        self.assertEqual(get_application_string_by_id(DIAMETER_APPLICATION_UNKNOWN), "unknown")

    def test__get_application_string_by_id__RELAY(self):
        self.assertEqual(get_application_string_by_id(DIAMETER_APPLICATION_RELAY), "relay")


class TestGetFormattedAnswerAsPerRequest(unittest.TestCase):
    def test__get_formatted_answer_as_per_request__1_no_session_id_avp(self):
        cer = CER()
        cea = CEA()

        self.assertEqual(cea.header.version, cer.header.version)
        self.assertNotEqual(cea.header.length, cer.header.length)
        self.assertNotEqual(cea.header.flags, cer.header.flags)
        self.assertEqual(cea.header.command_code, cer.header.command_code)
        self.assertEqual(cea.header.application_id, cer.header.application_id)
        self.assertNotEqual(cea.header.hop_by_hop, cer.header.hop_by_hop)       # different messages, then diff hop_by_hop
        self.assertNotEqual(cea.header.end_to_end, cer.header.end_to_end)       # different messages, then diff end_to_end

        cea = get_formatted_answer_as_per_request(cea, cer)

        self.assertEqual(cea.header.version, cer.header.version)
        self.assertNotEqual(cea.header.length, cer.header.length)
        self.assertNotEqual(cea.header.flags, cer.header.flags)
        self.assertEqual(cea.header.command_code, cer.header.command_code)
        self.assertEqual(cea.header.application_id, cer.header.application_id)
        self.assertEqual(cea.header.hop_by_hop, cer.header.hop_by_hop)          # different messages, but now same transaction
        self.assertEqual(cea.header.end_to_end, cer.header.end_to_end)          # different messages, but now same transaction

    def test__get_formatted_answer_as_per_request__2_session_id_avp(self):
        ulr = ULR(destination_realm="peernode", user_name="frodo", visited_plmn_id=bytes.fromhex("27f450"))
        ula = ULA()

        self.assertEqual(ula.header.version, ulr.header.version)
        self.assertNotEqual(ula.header.length, ulr.header.length)
        self.assertNotEqual(ula.header.flags, ulr.header.flags)
        self.assertEqual(ula.header.command_code, ulr.header.command_code)
        self.assertEqual(ula.header.application_id, ulr.header.application_id)
        self.assertNotEqual(ula.header.hop_by_hop, ulr.header.hop_by_hop)       # different messages, then diff hop_by_hop
        self.assertNotEqual(ula.header.end_to_end, ulr.header.end_to_end)       # different messages, then diff end_to_end
        self.assertNotEqual(ula.session_id_avp, ulr.session_id_avp)             # different messages, then diff session_id_avp

        ula = get_formatted_answer_as_per_request(ula, ulr)

        self.assertEqual(ula.header.version, ulr.header.version)
        self.assertNotEqual(ula.header.length, ulr.header.length)
        self.assertNotEqual(ula.header.flags, ulr.header.flags)
        self.assertEqual(ula.header.command_code, ulr.header.command_code)
        self.assertEqual(ula.header.application_id, ulr.header.application_id)
        self.assertEqual(ula.header.hop_by_hop, ulr.header.hop_by_hop)          # different messages, but now same transaction
        self.assertEqual(ula.header.end_to_end, ulr.header.end_to_end)          # different messages, but now same transaction
        self.assertEqual(ula.session_id_avp, ulr.session_id_avp)                # different messages, but now same session_id_avp


if __name__ == "__main__":
    unittest.main()