# -*- coding: utf-8 -*-
"""
    bromelia.lib.etsi_3gpp_s6b.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP S6b Application Id.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ...avps.etsi_3gpp.ts_129_229 import SupportedFeaturesAVP
from ...avps.etsi_3gpp.ts_129_229 import VisitedNetworkIdentifierAVP

from ...avps.etsi_3gpp.ts_129_272 import ApnConfigurationAVP
from ...avps.etsi_3gpp.ts_129_272 import ServiceSelectionAVP

from ...avps.etsi_3gpp.ts_129_273 import Mip6FeatureVectorAVP

from ...avps.ietf.rfc5447 import Mip6AgentInfoAVP

from ...avps.ietf.rfc6733 import AuthApplicationIdAVP
from ...avps.ietf.rfc6733 import AuthRequestTypeAVP
from ...avps.ietf.rfc6733 import DestinationRealmAVP
from ...avps.ietf.rfc6733 import OriginHostAVP
from ...avps.ietf.rfc6733 import OriginRealmAVP
from ...avps.ietf.rfc6733 import RedirectHostAVP
from ...avps.ietf.rfc6733 import ResultCodeAVP
from ...avps.ietf.rfc6733 import SessionIdAVP
from ...avps.ietf.rfc6733 import SessionTimeoutAVP
from ...avps.ietf.rfc6733 import UserNameAVP