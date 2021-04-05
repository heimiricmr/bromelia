# -*- coding: utf-8 -*-
"""
    examples.diameter_hss
    ~~~~~~~~~~~~~~~~~~~~~

    This module contains an example on how to setup a dummy HSS
	by using the Diameter class features of bromelia library.
    
    :copyright: (c) 2020 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import os
import sys

basedir = os.path.dirname(os.path.abspath(__file__))
examples_dir = os.path.dirname(basedir)
bromelia_dir = os.path.dirname(examples_dir)

sys.path.insert(0, bromelia_dir)

from bromelia import Diameter
from bromelia import DiameterAnswer
from bromelia.avps import *
from bromelia.etsi_3gpp_s6a_s6d.avps import *
from bromelia.etsi_3gpp_swm.avps import *

LOCAL_HOSTNAME = "hss.epc.mynetwork.com"
LOCAL_REALM = "epc.mynetwork.com"
REMOTE_HOSTNAME = "mme.epc.mynetwork.com"
REMOTE_REALM = "epc.mynetwork.com"

#: Basic Diameter object config
config = {
            "MODE": "SERVER",
            "APPLICATIONS": [{
                                "vendor_id": VENDOR_ID_3GPP, 
                                "app_id": DIAMETER_APPLICATION_S6a_S6d
            }],
            "LOCAL_NODE_HOSTNAME": LOCAL_HOSTNAME,
            "LOCAL_NODE_REALM": LOCAL_REALM,
            "LOCAL_NODE_IP_ADDRESS": "127.0.0.1",
            "LOCAL_NODE_PORT": 3870,
            "PEER_NODE_HOSTNAME": REMOTE_HOSTNAME,
            "PEER_NODE_REALM": REMOTE_REALM,
            "PEER_NODE_IP_ADDRESS": "127.0.0.1",
            "PEER_NODE_PORT": 3868,
            "WATCHDOG_TIMEOUT": 30
}

app = Diameter(config=config)

#: Basic DiameterAVPs for ULR message
avp1 = ResultCodeAVP(DIAMETER_SUCCESS)
avp2 = OriginHostAVP(LOCAL_HOSTNAME)
avp3 = OriginRealmAVP(LOCAL_REALM)
avp4 = AuthSessionStateAVP(NO_STATE_MAINTAINED)
avp5 = VendorSpecificApplicationIdAVP([
                                        VendorIdAVP(VENDOR_ID_3GPP), 
                                        AuthApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)
])
avp6 = SupportedFeaturesAVP([
                                VendorIdAVP(VENDOR_ID_3GPP), 
                                FeatureListIdAVP(1), 
                                FeatureListAVP(402653191)
])
avp7 = DiameterAVP(code=1406, flags=192, vendor_id=10415, data=1) #: ULA-Flags AVP

with app.context():
    while app.is_open():
        ulr = app.get_message()
        if ulr:
            #: Basic validation and ULA message creation
            if ulr.user_name_avp.data.decode("utf-8") == "123456789123456":
                avp0 = ulr.session_id_avp
                avps = [avp0, avp1, avp2, avp3, avp4, avp5, avp6, avp7]

                ula = DiameterAnswer(header=ulr.header, avps=avps)
                app.send_message(ula)
