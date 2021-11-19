# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_rx.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP Rx Application Id.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from .._internal_utils import show_warn

show_warn("avps", "etsi_3gpp_rx")

from ..avps.etsi_3gpp.ts_129_212 import RatTypeAVP
from ..avps.etsi_3gpp.ts_129_212 import UeLocalIpAddressAVP
from ..avps.etsi_3gpp.ts_129_212 import AnGwAddressAVP
from ..avps.etsi_3gpp.ts_129_212 import IpCanTypeAVP

from ..avps.etsi_3gpp.ts_129_214 import AbortCauseAVP
from ..avps.etsi_3gpp.ts_129_214 import AfApplicationIdentifierAVP
from ..avps.etsi_3gpp.ts_129_214 import AfChargingIdentifierAVP
from ..avps.etsi_3gpp.ts_129_214 import SpecificActionAVP
from ..avps.etsi_3gpp.ts_129_214 import MediaComponentDescriptionAVP
from ..avps.etsi_3gpp.ts_129_214 import ServiceInfoStatusAVP
from ..avps.etsi_3gpp.ts_129_214 import AccessNetworkChargingAddressAVP

from ..avps.etsi_3gpp.ts_129_229 import SupportedFeaturesAVP

from ..avps.etsi_3gpp.ts_129_273 import AnTrustedAVP

from ..avps.etsi_3gpp.ts_183_017 import ReservationPriorityAVP

from ..avps.ietf.rfc4006 import SubscriptionIdAVP

from ..avps.ietf.rfc6733 import AuthApplicationIdAVP
from ..avps.ietf.rfc6733 import AuthSessionStateAVP
from ..avps.ietf.rfc6733 import ClassAVP
from ..avps.ietf.rfc6733 import DestinationHostAVP
from ..avps.ietf.rfc6733 import DestinationRealmAVP
from ..avps.ietf.rfc6733 import ErrorMessageAVP
from ..avps.ietf.rfc6733 import ErrorReportingHostAVP
from ..avps.ietf.rfc6733 import ExperimentalResultAVP
from ..avps.ietf.rfc6733 import FailedAvpAVP
from ..avps.ietf.rfc6733 import OriginHostAVP
from ..avps.ietf.rfc6733 import OriginRealmAVP
from ..avps.ietf.rfc6733 import OriginStateIdAVP
from ..avps.ietf.rfc6733 import ProxyInfoAVP
from ..avps.ietf.rfc6733 import ResultCodeAVP
from ..avps.ietf.rfc6733 import SessionIdAVP
from ..avps.ietf.rfc6733 import RedirectHostAVP
from ..avps.ietf.rfc6733 import RedirectHostUsageAVP
from ..avps.ietf.rfc6733 import RedirectMaxCacheTimeAVP
from ..avps.ietf.rfc6733 import RouteRecordAVP
from ..avps.ietf.rfc6733 import TerminationCauseAVP

from ..avps.ietf.rfc7155 import FramedIpAddressAVP
from ..avps.ietf.rfc7155 import CalledStationIdAVP
from ..avps.ietf.rfc7155 import FramedIpv6PrefixAVP

from ..avps.ietf.rfc8506 import UserEquipmentInfoAVP