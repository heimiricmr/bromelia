# -*- coding: utf-8 -*-
"""
    examples.bromelia_hss
    ~~~~~~~~~~~~~~~~~~~~~

    This module contains an example on how to setup a dummy HSS
	by using the Bromelia class features of bromelia library.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import os
import sys

basedir = os.path.dirname(os.path.abspath(__file__))
examples_dir = os.path.dirname(basedir)
bromelia_dir = os.path.dirname(examples_dir)

sys.path.insert(0, bromelia_dir)

from bromelia import Bromelia
from bromelia.avps import *
from bromelia.constants import *
from bromelia.lib.etsi_3gpp_s6a import *
from bromelia.lib.etsi_3gpp_s6a import CLA # CancelLocationAnswer
from bromelia.lib.etsi_3gpp_s6a import CLR # CancelLocationRequest

#: Application initialization 
config_file = os.path.join(basedir, "bromelia_hss_config.yaml")

app = Bromelia(config_file=config_file)
app.load_messages_into_application_id([CLA, CLR], DIAMETER_APPLICATION_S6a)

CLR = app.s6a.CLR   #: Creating CLR alias

if __name__ == "__main__":
    app.run()   #: It will be blocked until connection has been established

    clr = CLR(user_name="123456789012345",
              clr_flags=2,
              destination_host=app.configs[0]["PEER_NODE_HOSTNAME"],
              supported_features=[
                                    VendorIdAVP(VENDOR_ID_3GPP),
                                    FeatureListIdAVP(1),
                                    FeatureListAVP(134217728)])

    cla = app.send_message(clr)
