# -*- coding: utf-8 -*-
"""
    bromelia.lib.etsi_3gpp_swm.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP SWm Application Id.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ...avps.etsi_3gpp.ts_129_061 import X3gppChargingCharacteristicsAVP

from ...avps.etsi_3gpp.ts_129_212 import RatTypeAVP
from ...avps.etsi_3gpp.ts_129_212 import UeLocalIpAddressAVP

from ...avps.etsi_3gpp.ts_129_229 import SupportedFeaturesAVP
from ...avps.etsi_3gpp.ts_129_229 import VisitedNetworkIdentifierAVP

from ...avps.etsi_3gpp.ts_129_272 import ServiceSelectionAVP
from ...avps.etsi_3gpp.ts_129_272 import ApnConfigurationAVP

from ...avps.etsi_3gpp.ts_129_273 import MobileNodeIdentifierAVP
from ...avps.etsi_3gpp.ts_129_273 import Mip6FeatureVectorAVP

from ...avps.ietf.rfc4006 import SubscriptionIdAVP

from ...avps.ietf.rfc4072 import EapMasterSessionKeyAVP
from ...avps.ietf.rfc4072 import EapPayloadAVP

from ...avps.ietf.rfc5447 import Mip6AgentInfoAVP

from ...avps.ietf.rfc6733 import AuthApplicationIdAVP
from ...avps.ietf.rfc6733 import AuthRequestTypeAVP
from ...avps.ietf.rfc6733 import AuthSessionStateAVP
from ...avps.ietf.rfc6733 import DestinationHostAVP
from ...avps.ietf.rfc6733 import DestinationRealmAVP
from ...avps.ietf.rfc6733 import OriginHostAVP
from ...avps.ietf.rfc6733 import OriginRealmAVP
from ...avps.ietf.rfc6733 import RedirectHostAVP
from ...avps.ietf.rfc6733 import ResultCodeAVP
from ...avps.ietf.rfc6733 import SessionIdAVP
from ...avps.ietf.rfc6733 import SessionTimeoutAVP
from ...avps.ietf.rfc6733 import UserNameAVP