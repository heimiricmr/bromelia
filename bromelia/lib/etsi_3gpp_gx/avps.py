# -*- coding: utf-8 -*-
"""
    bromelia.lib.etsi_3gpp_gx.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP Gx Application Id.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ...avps.etsi_3gpp.ts_129_061 import X3gppChargingCharacteristicsAVP

from ...avps.etsi_3gpp.ts_129_212 import AccessNetworkChargingIdentifierGxAVP
from ...avps.etsi_3gpp.ts_129_212 import AnGwAddressAVP
from ...avps.etsi_3gpp.ts_129_212 import BearerUsageAVP
from ...avps.etsi_3gpp.ts_129_212 import ChargingRuleInstallAVP
from ...avps.etsi_3gpp.ts_129_212 import ChargingRuleReportAVP
from ...avps.etsi_3gpp.ts_129_212 import DefaultEpsBearerQosAVP
from ...avps.etsi_3gpp.ts_129_212 import EventTriggerAVP
from ...avps.etsi_3gpp.ts_129_212 import IpCanTypeAVP
from ...avps.etsi_3gpp.ts_129_212 import NetworkRequestSupportAVP
from ...avps.etsi_3gpp.ts_129_212 import OfflineAVP
from ...avps.etsi_3gpp.ts_129_212 import OnlineAVP
from ...avps.etsi_3gpp.ts_129_212 import QosInformationAVP
from ...avps.etsi_3gpp.ts_129_212 import RatTypeAVP
from ...avps.etsi_3gpp.ts_129_212 import UeLocalIpAddressAVP

from ...avps.etsi_3gpp.ts_129_214 import AccessNetworkChargingAddressAVP

from ...avps.etsi_3gpp.ts_129_229 import SupportedFeaturesAVP

from ...avps.etsi_3gpp.ts_129_273 import AnTrustedAVP

from ...avps.ietf.rfc4006 import SubscriptionIdAVP

from ...avps.ietf.rfc6733 import AuthApplicationIdAVP
from ...avps.ietf.rfc6733 import DestinationHostAVP
from ...avps.ietf.rfc6733 import DestinationRealmAVP
from ...avps.ietf.rfc6733 import ErrorMessageAVP
from ...avps.ietf.rfc6733 import ErrorReportingHostAVP
from ...avps.ietf.rfc6733 import ExperimentalResultAVP
from ...avps.ietf.rfc6733 import FailedAvpAVP
from ...avps.ietf.rfc6733 import OriginHostAVP
from ...avps.ietf.rfc6733 import OriginRealmAVP
from ...avps.ietf.rfc6733 import OriginStateIdAVP
from ...avps.ietf.rfc6733 import ProxyInfoAVP
from ...avps.ietf.rfc6733 import ReAuthRequestTypeAVP
from ...avps.ietf.rfc6733 import ResultCodeAVP
from ...avps.ietf.rfc6733 import RedirectHostAVP
from ...avps.ietf.rfc6733 import RedirectHostUsageAVP
from ...avps.ietf.rfc6733 import RedirectMaxCacheTimeAVP
from ...avps.ietf.rfc6733 import RouteRecordAVP
from ...avps.ietf.rfc6733 import SessionIdAVP
from ...avps.ietf.rfc6733 import TerminationCauseAVP

from ...avps.ietf.rfc7155 import CalledStationIdAVP
from ...avps.ietf.rfc7155 import FramedIpAddressAVP
from ...avps.ietf.rfc7155 import FramedIpv6PrefixAVP

from ...avps.ietf.rfc8506 import CcRequestNumberAVP
from ...avps.ietf.rfc8506 import CcRequestTypeAVP
from ...avps.ietf.rfc8506 import UserEquipmentInfoAVP