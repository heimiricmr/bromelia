# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp.ts_129_273
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in ETSI TS 129 273.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..etsi_3gpp.ts_129_061 import X3gppChargingCharacteristicsAVP
from ..etsi_3gpp.ts_129_212 import RatTypeAVP
from ..etsi_3gpp.ts_129_272 import AmbrAVP
from ..etsi_3gpp.ts_129_272 import ContextIdentifierAVP
from ..etsi_3gpp.ts_129_272 import ApnConfigurationAVP

from ..ietf.rfc4006 import SubscriptionIdAVP
from ..ietf.rfc6733 import SessionTimeoutAVP

from ...base import DiameterAVP
from ...constants.etsi_3gpp.ts_129_273 import *
from ...types import *


class MobileNodeIdentifierAVP(DiameterAVP, UTF8StringType):
    """Implementation of Mobile-Node-Identifier AVP in Section 5.2.3.2  
    of ETSI TS 129 273 V15.4.0 (2019-10).

    The Mobile-Node-Identifier AVP (AVP Code 506) is of type UTF8String.
    """
    code = MOBILE_NODE_IDENTIFIER_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             MobileNodeIdentifierAVP.code,
                             MobileNodeIdentifierAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)
        

class Non3gppIpAccessAVP(DiameterAVP, EnumeratedType):
    """Implementation of Non-3GPP-IP-Access AVP in Section 8.2.3.3 
    of ETSI TS 129 273 V14.5.0 (2019-10).

    The Non-3GPP-IP-Access AVP (AVP Code 1501) is of type Enumerated.
    """
    code = NON_3GPP_IP_ACCESS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                NON_3GPP_SUBSCRIPTION_ALLOWED,
                NON_3GPP_SUBSCRIPTION_BARRED
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             Non3gppIpAccessAVP.code,
                             Non3gppIpAccessAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class Mip6FeatureVectorAVP(DiameterAVP, Unsigned64Type):
    """Implementation of MIP6-Feature-Vector AVP in Section 9.2.3.2.3 of 
    ETSI TS 129 273 V14.3.0 (2017-07).

    The MIP6-Feature-Vector AVP (AVP Code 124) is of type Unsigned64.
    """
    code = MIP6_FEATURE_VECTOR_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, Mip6FeatureVectorAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned64Type.__init__(self, data=data)


class Non3gppIpAccessApnAVP(DiameterAVP, EnumeratedType):
    """Implementation of Non-3GPP-Ip-Access-APN AVP in Section 8.2.3.4
    of ETSI TS 129 273 V14.3.0 (2017-07).

    The Non-3GPP-Ip-Access-APN AVP (AVP Code 1502) is of type Enumerated.
    """
    code = NON_3GPP_IP_ACCESS_APN_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                NON_3GPP_APNS_ENABLE,
                NON_3GPP_APNS_DISABLE,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             Non3gppIpAccessApnAVP.code,
                             Non3gppIpAccessApnAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class Non3gppUserDataAVP(DiameterAVP, GroupedType):
    """Implementation of Non-3GPP-User-Data AVP in Section 8.2.3.1 
    of ETSI TS 129 273 V14.3.0 (2017-07).

    The Non-3GPP-User-Data AVP (AVP Code 1500) is of type Grouped.
    """
    code = NON_3GPP_USER_DATA_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    optionals = {
                    "subscription_id": SubscriptionIdAVP,
                    "non_3gpp_ip_access": Non3gppIpAccessAVP,
                    "non_3gpp_ip_access_apn": Non3gppIpAccessApnAVP,
                    "rat_type": RatTypeAVP,
                    "session_timeout": SessionTimeoutAVP,
                    "mip6_feature_vector": Mip6FeatureVectorAVP,
                    "ambr": AmbrAVP,
                    "x3gpp_charging_characteristics": X3gppChargingCharacteristicsAVP,
                    "context_identifier": ContextIdentifierAVP,
                    #"apn_oi_replacement": ApnOiReplacementAVP,
                    "apn_configuration": ApnConfigurationAVP,
                    #"trace_info": TraceInfoAVP,
                    #"twan_default_apn_context_id": TwanDefaultApnContextIdAVP,
                    #"twan_access_info": TwanAccessInfoAVP,
                    #"emergency_info": EmergencyInfoAVP,
                    #"erp_authorization": ErpAuthorizationAVP

    }

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             Non3gppUserDataAVP.code,
                             Non3gppUserDataAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AnTrustedAVP(DiameterAVP, EnumeratedType):
    """Implementation of AN-Trusted AVP in Section 5.2.3.9 of
    ETSI TS 129 273 V12.5.0 (2014-10).

    The AN-Trusted AVP (AVP Code 1503) is of type Enumerated.
    """
    code = AN_TRUSTED_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                AN_TRUSTED_TRUSTED,
                AN_TRUSTED_UNTRUSTED,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AnTrustedAVP.code,
                             AnTrustedAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)
