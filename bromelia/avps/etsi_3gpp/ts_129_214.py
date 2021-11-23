# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp.ts_129_214
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in ETSI TS 129 214.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ...base import DiameterAVP
from ...constants.etsi_3gpp.ts_129_214 import *
from ...types import *


class MaxRequestedBandwidthDlAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Max-Requested-Bandwidth-DL AVP in Section 5.3.14 
    of ETSI TS 129 214 V15.4.0 (2018-07).

    The Max-Requested-Bandwidth-DL AVP (AVP Code 515) is of type Unsigned32.
    """
    code = MAX_REQUESTED_BANDWIDTH_DL_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             MaxRequestedBandwidthDlAVP.code,
                             MaxRequestedBandwidthDlAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class MaxRequestedBandwidthUlAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Max-Requested-Bandwidth-UL AVP in Section 5.3.15 
    of ETSI TS 129 214 V15.4.0 (2018-07).

    The Max-Requested-Bandwidth-UL AVP (AVP Code 516) is of type Unsigned32.
    """
    code = MAX_REQUESTED_BANDWIDTH_UL_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             MaxRequestedBandwidthUlAVP.code,
                             MaxRequestedBandwidthUlAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AbortCauseAVP(DiameterAVP, EnumeratedType):
    """Implementation of Abort-Cause AVP in Section 5.3.1 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Abort-Cause AVP (AVP Code 500) is of type Enumerated.
    """
    code = ABORT_CAUSE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                ABORT_CAUSE_BEARER_RELEASED,
                ABORT_CAUSE_INSUFFICIENT_SERVER_RESOURCES,
                ABORT_CAUSE_INSUFFICIENT_BEARER_RESOURCES,
                ABORT_CAUSE_PS_TO_CS_HANDOVER,
                ABORT_CAUSE_SPONSORED_DATA_CONNECTIVITY_DISALLOWED,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AbortCauseAVP.code,
                             AbortCauseAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AfApplicationIdentifierAVP(DiameterAVP, OctetStringType):
    """Implementation of AF-Application-identifier AVP in Section 5.3.5  
    of ETSI TS 129 214 V15.4.0 (2018-07).

    The AF-Application-identifier AVP (AVP Code 504) is of type OctetString.
    """
    code = AF_APPLICATION_IDENTIFIER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AfApplicationIdentifierAVP.code,
                             AfApplicationIdentifierAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AfChargingIdentifierAVP(DiameterAVP, OctetStringType):
    """Implementation of AF-Charging-identifier AVP in Section 5.3.6  
    of ETSI TS 129 214 V15.4.0 (2018-07).

    The AF-Charging-identifier AVP (AVP Code 505) is of type OctetString.
    """
    code = AF_CHARGING_IDENTIFIER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AfChargingIdentifierAVP.code,
                             AfChargingIdentifierAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class FlowDescriptionAVP(DiameterAVP, OctetStringType):
    """Implementation of Flow-Description AVP in Section 5.38 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Flow-Description AVP (AVP Code 507) is of type IPFilterRule.
    """
    code = FLOW_DESCRIPTION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             FlowDescriptionAVP.code,
                             FlowDescriptionAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class FlowNumberAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Flow-Number AVP in Section 5.3.9 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Flow-Number AVP (AVP Code 509) is of type Unsigned32.
    """
    code = FLOW_NUMBER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             FlowNumberAVP.code,
                             FlowNumberAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)
 

class FlowStatusAVP(DiameterAVP, EnumeratedType):
    """Implementation of Flow-Status AVP in Section 5.3.11 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Flow-Status AVP (AVP Code 511) is of type Enumerated.
    """
    code = FLOW_STATUS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                FLOW_STATUS_ENABLED_UPLINK,
                FLOW_STATUS_ENABLED_DOWNLINK,
                FLOW_STATUS_ENABLED,
                FLOW_STATUS_DISABLED,
                FLOW_STATUS_REMOVED,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             FlowStatusAVP.code,
                             FlowStatusAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class FlowUsageAVP(DiameterAVP, EnumeratedType):
    """Implementation of Flow-Usage AVP in Section 5.3.12 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Flow-Usage AVP (AVP Code 512) is of type Enumerated.
    """
    code = FLOW_USAGE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                FLOW_USAGE_NO_INFORMATION,
                FLOW_USAGE_RTCP,
                FLOW_USAGE_AF_SIGNALLING,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             FlowUsageAVP.code,
                             FlowUsageAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SpecificActionAVP(DiameterAVP, EnumeratedType):
    """Implementation of Specific-Action AVP in Section 5.3.13 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Specific-Action AVP (AVP Code 513) is of type Enumerated.
    """
    code = SPECIFIC_ACTION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                SPECIFIC_ACTION_CHARGING_CORRELATION_EXCHANGE,
                SPECIFIC_ACTION_INDICATION_OF_LOSS_OF_BEARER,
                SPECIFIC_ACTION_INDICATION_OF_RECOVERY_OF_BEARER,
                SPECIFIC_ACTION_INDICATION_OF_RELEASE_OF_BEARER,
                SPECIFIC_ACTION_IP_CAN_CHANGE,
                SPECIFIC_ACTION_INDICATION_OF_OUT_OF_CREDIT,
                SPECIFIC_ACTION_INDICATION_OF_SUCCESSFUL_RESOURCES_ALLOCATION,
                SPECIFIC_ACTION_INDICATION_OF_FAILED_RESOURCES_ALLOCATION,
                SPECIFIC_ACTION_INDICATION_OF_LIMITED_PCC_DEPLOYMENT,
                SPECIFIC_ACTION_USAGE_REPORT,
                SPECIFIC_ACTION_ACCESS_NETWORK_INFO_REPORT,
                SPECIFIC_ACTION_INDICATION_OF_RECOVERY_FROM_LIMITED_PCC_DEPLOYMENT,
                SPECIFIC_ACTION_INDICATION_OF_ACCESS_NETWORK_INFO_REPORTING_FAILURE,
                SPECIFIC_ACTION_INDICATION_OF_TRANSFER_POLICY_EXPIRED,
                SPECIFIC_ACTION_PLMN_CHANGE,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SpecificActionAVP.code,
                             SpecificActionAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class MediaComponentDescriptionAVP(DiameterAVP, GroupedType):
    """Implementation of Media-Component-Description AVP in Section 5.3.16 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Media-Component-Description AVP (AVP Code 517) is of type Grouped.
    """
    code = MEDIA_COMPONENT_DESCRIPTION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):        
        DiameterAVP.__init__(self, 
                             MediaComponentDescriptionAVP.code,
                             MediaComponentDescriptionAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class MediaComponentNumberAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Media-Component-Number AVP in Section 5.3.17 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Media-Component-Number AVP (AVP Code 518) is of type Unsigned32.
    """
    code = MEDIA_COMPONENT_NUMBER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             MediaComponentNumberAVP.code,
                             MediaComponentNumberAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class MediaSubComponentAVP(DiameterAVP, GroupedType):
    """Implementation of Media-Sub-Component AVP in Section 5.3.18 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Media-Sub-Component AVP (AVP Code 519) is of type Grouped.
    """
    code = MEDIA_SUB_COMPONENT_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):        
        DiameterAVP.__init__(self, 
                             MediaSubComponentAVP.code,
                             MediaSubComponentAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class MediaTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Media-Type AVP in Section 5.3.19 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Media-Type AVP (AVP Code 520) is of type Enumerated.
    """
    code = MEDIA_TYPE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP
 
    values = [
                MEDIA_TYPE_AUDIO,
                MEDIA_TYPE_VIDEO,
                MEDIA_TYPE_DATA,
                MEDIA_TYPE_APPLICATION,
                MEDIA_TYPE_CONTROL,
                MEDIA_TYPE_TEXT,
                MEDIA_TYPE_MESSAGE,
                MEDIA_TYPE_OTHER,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             MediaTypeAVP.code,
                             MediaTypeAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ServiceInfoStatusAVP(DiameterAVP, EnumeratedType):
    """Implementation of Service-Info-Status AVP in Section 5.3.25 of 
    ETSI TS 129 214 V15.4.0 (2018-07).

    The Service-Info-Status AVP (AVP Code 527) is of type Enumerated.
    """
    code = SERVICE_INFO_STATUS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP
 
    values = [
                SERVICE_INFO_STATUS_FINAL_SERVICE_INFORMATION,
                SERVICE_INFO_STATUS_PRELIMINARY_SERVICE_INFORMATION,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ServiceInfoStatusAVP.code,
                             ServiceInfoStatusAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AccessNetworkChargingAddressAVP(DiameterAVP, AddressType):
    """Implementation of Access-Network-Charging-Address AVP in Section 5.3.2 of 
    ETSI 3GPP TS 29.214 V8.14.0 (2012-12).

    The Access-Network-Charging-Address AVP (AVP Code 501) is of type Address.
    """
    code = ACCESS_NETWORK_CHARGING_ADDRESS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AccessNetworkChargingAddressAVP.code,
                             AccessNetworkChargingAddressAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        AddressType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AccessNetworkChargingIdentifierValueAVP(DiameterAVP, OctetStringType):
    """Implementation of Access-Network-Charging-Identifier-Value AVP in 
    Section 5.3.4 of ETSI 3GPP TS 29.214 V8.14.0 (2012-12).

    The Access-Network-Charging-Identifier-Value AVP (AVP Code 503) is of 
    type OctetString.
    """
    code = ACCESS_NETWORK_CHARGING_IDENTIFIER_VALUE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AccessNetworkChargingIdentifierValueAVP.code,
                             AccessNetworkChargingIdentifierValueAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)
