# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_s13.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP S13/S13' Application Id.
    
    :copyright: (c) 2021-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..avps import *
from ..base import *
from ..constants import *
from ..types import *


class ImeiAVP(DiameterAVP, UTF8StringType):
    """Implementation of IMEI AVP in Section 7.3.4 of
    ETSI TS 129 272 V15.10.0 (2020-01).

    The IMEI AVP (AVP Code 1402) is of type UTF8String.
    """
    code = IMEI_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ImeiAVP.code,
                             ImeiAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SoftwareVersionAVP(DiameterAVP, UTF8StringType):
    """Implementation of Software-Version AVP in Section 7.3.5 of
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Software-Version AVP (AVP Code 1403) is of type UTF8String.
    """
    code = SOFTWARE_VERSION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SoftwareVersionAVP.code,
                             SoftwareVersionAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class TerminalInformationAVP(DiameterAVP, GroupedType):
    """Implementation of Terminal-Information AVP in Section 5.3.14 of
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Terminal-Information AVP (AVP Code 1401) is of type Grouped.
    """
    code = TERMINAL_INFORMATION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {}
    optionals = {
                    "imei": ImeiAVP,
                    # "x3gpp2_meid": x3gpp2MeidAVP,
                    "software_version": SoftwareVersionAVP       
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             TerminalInformationAVP.code,
                             TerminalInformationAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class EquipmentStatusAVP(DiameterAVP, EnumeratedType):
    """Implementation of Equipment-Status AVP in Section 7.3.51 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The Equipment-Status AVP (AVP Code 1445) is of type Enumerated.
    """
    code = EQUIPMENT_STATUS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                EQUIPMENT_STATUS_WHITELISTED,
                EQUIPMENT_STATUS_BLACKLISTED,
                EQUIPMENT_STATUS_GREYLISTED
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             EquipmentStatusAVP.code,
                             EquipmentStatusAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)