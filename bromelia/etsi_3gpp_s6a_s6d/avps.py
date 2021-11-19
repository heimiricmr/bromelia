# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_s6a_s6d.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP S6a/S6d Application Id.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from .._internal_utils import show_warn

show_warn("avps", "etsi_3gpp_s6a_s6d", "etsi_3gpp_s6a")

from ..avps.etsi_3gpp.ts_129_212 import RatTypeAVP

from ..avps.etsi_3gpp.ts_129_229 import SupportedFeaturesAVP
from ..avps.etsi_3gpp.ts_129_229 import VisitedNetworkIdentifierAVP

from ..avps.etsi_3gpp.ts_129_272 import ContextIdentifierAVP
from ..avps.etsi_3gpp.ts_129_272 import ServiceSelectionAVP
from ..avps.etsi_3gpp.ts_129_272 import UeUsageTypeAVP
from ..avps.etsi_3gpp.ts_129_272 import SubscriptionDataAVP
from ..avps.etsi_3gpp.ts_129_272 import RequestedEutranAuthenticationInfoAVP
from ..avps.etsi_3gpp.ts_129_272 import TerminalInformationAVP
from ..avps.etsi_3gpp.ts_129_272 import UlrFlagsAVP
from ..avps.etsi_3gpp.ts_129_272 import UlaFlagsAVP
from ..avps.etsi_3gpp.ts_129_272 import AirFlagsAVP
from ..avps.etsi_3gpp.ts_129_272 import NorFlagsAVP
from ..avps.etsi_3gpp.ts_129_272 import PurFlagsAVP
from ..avps.etsi_3gpp.ts_129_272 import PuaFlagsAVP
from ..avps.etsi_3gpp.ts_129_272 import AlertReasonAVP
from ..avps.etsi_3gpp.ts_129_272 import ErrorDiagnosticAVP
from ..avps.etsi_3gpp.ts_129_272 import VisitedPlmnIdAVP
from ..avps.etsi_3gpp.ts_129_272 import AuthenticationInfoAVP
from ..avps.etsi_3gpp.ts_129_272 import HomogeneousSupportOfImsVoiceOverPsSessionsAVP
from ..avps.etsi_3gpp.ts_129_272 import UeSrvccCapabilityAVP
from ..avps.etsi_3gpp.ts_129_272 import SupportedServicesAVP
from ..avps.etsi_3gpp.ts_129_272 import CancellationTypeAVP
from ..avps.etsi_3gpp.ts_129_272 import ClrFlagsAVP

from ..avps.ietf.rfc5447 import Mip6AgentInfoAVP

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