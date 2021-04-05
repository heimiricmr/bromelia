# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_s6a_s6d.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP S6a/S6d Application Id.
    
    :copyright: (c) 2020 Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import base64

from .._internal_utils import convert_to_1_byte
from .._internal_utils import convert_to_2_bytes
from ..avps import *
from ..constants import *
from ..exceptions import AVPAttributeValueError
from ..types import *


class SupportedFeaturesAVP(DiameterAVP, GroupedType):
    """Implementation of Supported-Features AVP in Section 6.3.29 of 
    ETSI TS 129 229 V14.3.0 (2019-10).

    The Supported-Features AVP (AVP Code 628) is of type Grouped.
    """
    code = SUPPORTED_FEATURES_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, SupportedFeaturesAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)

        if isinstance(data, bytes):
            data = DiameterAVP.load(data)
            self.avps = data

        if not isinstance(data, list):
                raise DataTypeError("GroupedType MUST have data argument "\
                                "of 'list'")

        self.data = b""

        vendor_id_avp_count = 0
        feature_list_id_avp_count = 0
        feature_list_avp_count = 0
        for avp in data:
            if isinstance(avp, VendorIdAVP):
                self.vendor_id_avp = avp
                self.data += avp.dump()
                vendor_id_avp_count += 1

            elif isinstance(avp, FeatureListIdAVP):
                self.feature_list_id_avp = avp
                self.data += avp.dump()
                feature_list_id_avp_count += 1

            elif isinstance(avp, FeatureListAVP):
                self.feature_list_id_avp = avp
                self.data += avp.dump()
                feature_list_avp_count += 1


        if vendor_id_avp_count == 0 or \
                feature_list_id_avp_count == 0 or \
                feature_list_avp_count == 0:
            
            raise AVPAttributeValueError("invalid input argument for "\
                                    "SupportedFeaturesAVP. It "\
                                    "MUST contain one VendorIdAVP, "\
                                    "one FeatureListIdAVP and one "\
                                    "FeatureListAVP objects",
                                    DIAMETER_MISSING_AVP)

        if vendor_id_avp_count > 1 or \
                feature_list_id_avp_count > 1 or \
                feature_list_avp_count > 1:

            raise AVPAttributeValueError("invalid input argument for "\
                                    "SupportedFeaturesAVP. It "\
                                    "MUST contain only one VendorIdAVP, "\
                                    "only one FeatureListIdAVP and "\
                                    "only one FeatureListAVP object",
                                    DIAMETER_AVP_OCCURS_TOO_MANY_TIMES)

        GroupedType.__init__(self, data=self.data, vendor_id=VENDOR_ID_3GPP)


class FeatureListIdAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Feature-List-ID AVP in Section 6.3.30 of
    ETSI TS 129 229 V14.3.0 (2019-10).

    The Feature-List-ID AVP (AVP Code 629) is of type Unsigned32.
    """
    code = FEATURE_LIST_ID_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, FeatureListIdAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class FeatureListAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Feature-List AVP in Section 6.3.31 of 
    ETSI TS 129 229 V14.3.0 (2019-10).

    The Feature-List AVP (AVP Code 630) is of type Unsigned32.
    """
    code = FEATURE_LIST_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, FeatureListAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class TerminalInformationAVP(DiameterAVP, GroupedType):
    """Implementation of Terminal-Information AVP in Section 5.3.14 of
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Terminal-Information AVP (AVP Code 1401) is of type Grouped.
    """
    code = TERMINAL_INFORMATION_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, TerminalInformationAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)

        if isinstance(data, bytes):
            data = DiameterAVP.load(data)
            self.avps = data

        if not isinstance(data, list):
                raise DataTypeError("GroupedType MUST have data argument "\
                                "of 'list'")

        self.data = b""

        imei_avp_count = 0
        software_version_avp_count = 0
        for avp in data:
            if isinstance(avp, ImeiAVP):
                self.imei_avp = avp
                self.data += avp.dump()
                imei_avp_count += 1

            elif isinstance(avp, SoftwareVersionAVP):
                self.software_version_avp = avp
                self.data += avp.dump()
                software_version_avp_count += 1


        if imei_avp_count > 1 or software_version_avp_count > 1:
            raise AVPAttributeValueError("invalid input argument for "\
                                    "TerminalInformationAVP. It "\
                                    "MUST contain only one ImeiAVP, "\
                                    "or only one SoftwareVersionAVP object",
                                    DIAMETER_AVP_OCCURS_TOO_MANY_TIMES)

        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ImeiAVP(DiameterAVP, UTF8StringType):
    """Implementation of IMEI AVP in Section 7.3.4 of
    ETSI TS 129 272 V15.10.0 (2020-01).

    The IMEI AVP (AVP Code 1402) is of type UTF8String.
    """
    code = IMEI_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, ImeiAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self,data=data, vendor_id=VENDOR_ID_3GPP)


class SoftwareVersionAVP(DiameterAVP, UTF8StringType):
    """Implementation of Software-Version AVP in Section 7.3.5 of
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Software-Version AVP (AVP Code 1403) is of type UTF8String.
    """
    code = SOFTWARE_VERSION_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, SoftwareVersionAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self,data=data, vendor_id=VENDOR_ID_3GPP)


class UlrFlagsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of ULR-Flags AVP in Section 7.3.7 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The ULR-Flags AVP (AVP Code 1405) is of type Unsigned32.
    """
    code = ULR_FLAGS_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, UlrFlagsAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class VisitedPlmnIdAVP(DiameterAVP, OctetStringType):
    """Implementation of Visited-PLMN-Id AVP in Section 7.3.9 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Visited-PLMN-Id AVP (AVP Code 1407) is of type OctetString.
    """
    code = VISITED_PLMN_ID_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, VisitedPlmnIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class UeSrvccCapabilityAVP(DiameterAVP, EnumeratedType):
    """Implementation of UE-SRVCC-Capability AVP in Section 7.3.130 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The UE-SRVCC-Capability AVP (AVP Code 1615) is of type Enumerated.
    """
    code = UE_SRVCC_CAPABILITY_AVP_CODE

    values = [
                UE_SRVCC_NOT_SUPPORTED,
                UE_SRVCC_SUPPORTED
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, UeSrvccCapabilityAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SupportedServicesAVP(DiameterAVP, GroupedType):
    """Implementation of Supported-Services AVP in Section 7.3.199 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Supported-Services AVP (AVP Code 3143) is of type Grouped.
    """
    code = SUPPORTED_SERVICES_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, SupportedServicesAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)

        if isinstance(data, bytes):
            data = DiameterAVP.load(data)
            self.avps = data

        if not isinstance(data, list):
                raise DataTypeError("GroupedType MUST have data argument "\
                                "of 'list'")

        self.data = b""

        supported_monitoring_events_avp_count = 0
        for avp in data:
            if isinstance(avp, SupportedMonitoringEventsAVP):
                self.supported_monitoring_events_avp = avp
                self.data += avp.dump()
                supported_monitoring_events_avp_count += 1


        if supported_monitoring_events_avp_count > 1:
            raise AVPAttributeValueError("invalid input argument for "\
                                    "SupportedServicesAVP. It "\
                                    "MUST contain only one "\
                                    "SupportedMonitoringEventsAVP object",
                                    DIAMETER_AVP_OCCURS_TOO_MANY_TIMES)

        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SupportedMonitoringEventsAVP(DiameterAVP, Unsigned64Type):
    """Implementation of Supported-Monitoring-Events AVP in Section 7.3.200 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Supported-Monitoring-Events AVP (AVP Code 3144) is of type Unsigned64.
    """
    code = SUPPORTED_MONITORING_EVENTS_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, SupportedMonitoringEventsAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned64Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class CancellationTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Cancellation-Type AVP in Section 7.3.24 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The Cancellation-Type AVP (AVP Code 1420) is of type Enumerated.
    """
    code = CANCELLATION_TYPE_AVP_CODE

    values = [
                CANCELLATION_TYPE_MME_UPDATE_PROCEDURE,
                CANCELLATION_TYPE_SGSN_UPDATE_PROCEDURE,
                CANCELLATION_TYPE_SUBSCRIPTION_WITHDRAWAL,
                CANCELLATION_TYPE_UPDATE_PROCEDURE_IWF,
                CANCELLATION_TYPE_INITIAL_ATTACH_PROCEDURE
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, CancellationTypeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ClrFlagsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of CLR-Flags AVP in Section 7.3.152 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The CLR-Flags AVP (AVP Code 1638) is of type Unsigned32.
    """
    code = CLR_FLAGS_AVP_CODE

    def __init__(self, data):
        DiameterAVP.__init__(self, ClrFlagsAVP.code)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)
