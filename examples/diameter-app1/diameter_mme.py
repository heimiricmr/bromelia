# -*- coding: utf-8 -*-
"""
    examples.diameter_mme
    ~~~~~~~~~~~~~~~~~~~~~

    This module contains an example on how to setup a dummy MME
	by using the Diameter class features of bromelia library.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import os
import sys

basedir = os.path.dirname(os.path.abspath(__file__))
examples_dir = os.path.dirname(basedir)
bromelia_dir = os.path.dirname(examples_dir)

sys.path.insert(0, bromelia_dir)

from bromelia import Diameter
from bromelia import DiameterRequest
from bromelia.avps import *
from bromelia.lib.etsi_3gpp_s6a import *
from bromelia.lib.etsi_3gpp_swm import *

LOCAL_HOSTNAME = "mme.epc.mynetwork.com"
LOCAL_REALM = "epc.mynetwork.com"
REMOTE_HOSTNAME = "hss.epc.mynetwork.com"
REMOTE_REALM = "epc.mynetwork.com"

#: Basic Diameter object config
config = {
            "MODE": "CLIENT",
            "APPLICATIONS": [{
                                "vendor_id": VENDOR_ID_3GPP, 
                                "app_id": DIAMETER_APPLICATION_S6a_S6d
            }],
            "LOCAL_NODE_HOSTNAME": LOCAL_HOSTNAME,
            "LOCAL_NODE_REALM": LOCAL_REALM,
            "LOCAL_NODE_IP_ADDRESS": "127.0.0.1",
            "LOCAL_NODE_PORT": 3868,
            "PEER_NODE_HOSTNAME": REMOTE_HOSTNAME,
            "PEER_NODE_REALM": REMOTE_REALM,
            "PEER_NODE_IP_ADDRESS": "127.0.0.1",
            "PEER_NODE_PORT": 3870,
            "WATCHDOG_TIMEOUT": 30
}

app = Diameter(config=config)

#: Basic DiameterAVPs for ULR message
avps = [
            SessionIdAVP(LOCAL_HOSTNAME),
            AuthSessionStateAVP(NO_STATE_MAINTAINED),
            OriginHostAVP(LOCAL_HOSTNAME),
            OriginRealmAVP(LOCAL_REALM),
            DestinationRealmAVP(REMOTE_REALM),
            UserNameAVP("123456789123456"),
            RatTypeAVP(RAT_TYPE_EUTRAN),
            UlrFlagsAVP(3)
]

#: Create ULR message
ulr = DiameterRequest(command_code=316, application_id=16777251)
ulr.extend(avps)

#: Setup Diameter connection, send ULR & receive ULA
with app.context():
    while app.is_open():
        ula = app.send_message(ulr)
        break