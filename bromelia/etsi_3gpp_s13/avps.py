# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_s13.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP S13/S13' Application Id.
    
    :copyright: (c) 2021-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from .._internal_utils import show_warn

show_warn("avps", "etsi_3gpp_s13")

from ..avps.etsi_3gpp.ts_129_272 import TerminalInformationAVP
from ..avps.etsi_3gpp.ts_129_272 import EquipmentStatusAVP

from ..avps.ietf.rfc6733 import AuthApplicationIdAVP
from ..avps.ietf.rfc6733 import AuthSessionStateAVP
from ..avps.ietf.rfc6733 import DestinationHostAVP
from ..avps.ietf.rfc6733 import DestinationRealmAVP
from ..avps.ietf.rfc6733 import ExperimentalResultAVP
from ..avps.ietf.rfc6733 import FailedAvpAVP
from ..avps.ietf.rfc6733 import OriginHostAVP
from ..avps.ietf.rfc6733 import OriginRealmAVP
from ..avps.ietf.rfc6733 import ProxyInfoAVP
from ..avps.ietf.rfc6733 import ResultCodeAVP
from ..avps.ietf.rfc6733 import RouteRecordAVP
from ..avps.ietf.rfc6733 import SessionIdAVP
from ..avps.ietf.rfc6733 import UserNameAVP
from ..avps.ietf.rfc6733 import VendorIdAVP
from ..avps.ietf.rfc6733 import VendorSpecificApplicationIdAVP