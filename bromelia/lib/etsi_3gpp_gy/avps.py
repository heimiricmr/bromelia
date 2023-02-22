# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_gy.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP Gy Application Id.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ...avps.etsi_3gpp.ts_132_299 import LowBalanceIndicationAVP
from ...avps.etsi_3gpp.ts_132_299 import RemainingBalanceAVP

from ...avps.ietf.rfc4006 import CcSessionFailoverAVP
from ...avps.ietf.rfc4006 import CostInformationAVP
from ...avps.ietf.rfc4006 import CreditControlFailureHandlingAVP
from ...avps.ietf.rfc4006 import DirectDebitingFailureHandlingAVP
from ...avps.ietf.rfc4006 import MultipleServicesCreditControlAVP
from ...avps.ietf.rfc4006 import RequestedServiceUnitAVP
from ...avps.ietf.rfc4006 import SubscriptionIdAVP

from ...avps.ietf.rfc6733 import AcctMultiSessionIdAVP
from ...avps.ietf.rfc6733 import AuthApplicationIdAVP
from ...avps.ietf.rfc6733 import DestinationHostAVP
from ...avps.ietf.rfc6733 import DestinationRealmAVP
from ...avps.ietf.rfc6733 import EventTimestampAVP
from ...avps.ietf.rfc6733 import FailedAvpAVP
from ...avps.ietf.rfc6733 import OriginHostAVP
from ...avps.ietf.rfc6733 import OriginRealmAVP
from ...avps.ietf.rfc6733 import OriginStateIdAVP
from ...avps.ietf.rfc6733 import ProxyInfoAVP
from ...avps.ietf.rfc6733 import ResultCodeAVP
from ...avps.ietf.rfc6733 import RedirectHostAVP
from ...avps.ietf.rfc6733 import RedirectHostUsageAVP
from ...avps.ietf.rfc6733 import RedirectMaxCacheTimeAVP
from ...avps.ietf.rfc6733 import RouteRecordAVP
from ...avps.ietf.rfc6733 import SessionIdAVP
from ...avps.ietf.rfc6733 import TerminationCauseAVP
from ...avps.ietf.rfc6733 import UserNameAVP

from ...avps.ietf.rfc8506 import CcRequestNumberAVP
from ...avps.ietf.rfc8506 import CcRequestTypeAVP
from ...avps.ietf.rfc8506 import ServiceIdentifierAVP
from ...avps.ietf.rfc8506 import UserEquipmentInfoAVP