# -*- coding: utf-8 -*-
"""
    bromelia.avps.ietf.rfc5447
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in IETF RFC 5447.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..ietf.rfc6733 import DestinationHostAVP
from ..ietf.rfc6733 import DestinationRealmAVP
from ...base import DiameterAVP
from ...constants.ietf.rfc5447 import *
from ...types import *


class MipHomeAgentHostAVP(DiameterAVP, GroupedType):
    """Implementation of MIP-Home-Agent-Host AVP in both Section 7.3.43 of
    ETSI TS 129 272 V15.10.0 (2020-01) and Section 4.2.3 of IETF RFC 5447.

    The MIP-Home-Agent-Host AVP (AVP Code 348) is of type Grouped.
    """
    code = MIP_HOME_AGENT_HOST_AVP_CODE
    vendor_id = None

    mandatory = {
                    "destination_host": DestinationHostAVP,
                    "destination_realm": DestinationRealmAVP,
    }
    optionals = {}

    def __init__(self, data):
        DiameterAVP.__init__(self, MipHomeAgentHostAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)


class Mip6AgentInfoAVP(DiameterAVP, GroupedType):
    """Implementation of MIP6-Agent-Info AVP in both Section 7.3.45 of
    ETSI TS 129 272 V15.10.0 (2020-01) and Section 4.2.1 of IETF RFC 5447.

    The MIP6-Agent-Info AVP (AVP Code 486) is of type Grouped.
    """
    code = MIP6_AGENT_INFO_AVP_CODE
    vendor_id = None

    mandatory = {}
    optionals = {
                    # "mip_home_agent_address": MipHomeAgentAddressAVP,
                    "mip_home_agent_host": MipHomeAgentHostAVP,
                    # "mip_home_link_prefix": MipHomeLinkPrefixAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, Mip6AgentInfoAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)