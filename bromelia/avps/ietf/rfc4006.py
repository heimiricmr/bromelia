# -*- coding: utf-8 -*-
"""
    bromelia.avps.ietf.rfc4006
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in IETF RFC 4006.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..ietf.rfc8506 import RatingGroupAVP
from ..ietf.rfc6733 import ResultCodeAVP

from ...base import DiameterAVP
from ...constants.ietf.rfc4006 import *
from ...types import *


class CcSessionFailoverAVP(DiameterAVP, EnumeratedType):
    """Implementation of CC-Session-Failover AVP in Section 8.4 of 
    IETF RFC 4006.

    The CC-Session-Failover AVP (AVP Code 418) is of type Enumerated.
    """
    code = CC_SESSION_FAILOVER_AVP_CODE
    vendor_id = None

    values = [
                CC_SESSION_FAILOVER_NOT_SUPPORTED,
                CC_SESSION_FAILOVER_SUPPORTED
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, CcSessionFailoverAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class ValueDigitsAVP(DiameterAVP, Unsigned64Type):
    """Implementation of Value-Digits AVP in Section 8.10 of IETF RFC 4006.

    The Value-Digits AVP (AVP Code 447) is of type Integer64.
    """
    code = VALUE_DIGITS_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, ValueDigitsAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned64Type.__init__(self, data=data)


class ExponentAVP(DiameterAVP, Integer32Type):
    """Implementation of Exponent AVP in Section 8.9 of IETF RFC 4006.

    The Exponent AVP (AVP Code 429) is of type Integer32.
    """
    code = EXPONENT_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, ExponentAVP.code)
        # DiameterAVP.set_mandatory_bit(self, True) CHECK
        Integer32Type.__init__(self, data=data)


class UnitValueAVP(DiameterAVP, GroupedType):
    """Implementation of Unit-Value AVP in Section 8.8 of IETF RFC 4006.

    The Unit-Value AVP (AVP Code 425) is of type Grouped.
    """
    code = UNIT_VALUE_AVP_CODE
    vendor_id = None

    mandatory = {
                    "value_digits": ValueDigitsAVP,
    }
    optionals = {
                    "exponent": ExponentAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, UnitValueAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)


class CurrencyCodeAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Currency-Code AVP in Section 8.11 of IETF RFC 4006.

    The Currency-Code AVP (AVP Code 425) is of type Unsigned32.
    """
    code = CURRENCY_CODE_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, CurrencyCodeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class CostUnitAVP(DiameterAVP, UTF8StringType):
    """Implementation of Cost-Unit AVP in Section 8.12 of IETF RFC 4006.

    The Cost-Unit AVP (AVP Code 424) is of type UTF8String.
    """
    code = COST_UNIT_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, CostUnitAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


class CostInformationAVP(DiameterAVP, GroupedType):
    """Implementation of Cost-Information AVP in Section 8.7 of IETF RFC 4006.

    The Cost-Information AVP (AVP Code 423) is of type Grouped.
    """
    code = COST_INFORMATION_AVP_CODE
    vendor_id = None

    mandatory = {
                    "unit_value": UnitValueAVP,
                    "currency_code": CurrencyCodeAVP,
    }
    optionals = {
                    "cost_unit": CostUnitAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, CostInformationAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)


class CreditControlFailureHandlingAVP(DiameterAVP, EnumeratedType):
    """Implementation of Credit-Control-Failure-Handling AVP in Section 8.14 of 
    IETF RFC 4006.

    The Credit-Control-Failure-Handling AVP (AVP Code 427) is of type Enumerated.
    """
    code = CREDIT_CONTROL_FAILURE_HANDLING_AVP_CODE
    vendor_id = None

    values = [
                CREDIT_CONTROL_FAILURE_HANDLING_TERMINATE,
                CREDIT_CONTROL_FAILURE_HANDLING_CONTINUE,
                CREDIT_CONTROL_FAILURE_HANDLING_RETRY_AND_TERMINATE
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, CreditControlFailureHandlingAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class DirectDebitingFailureHandlingAVP(DiameterAVP, EnumeratedType):
    """Implementation of Direct-Debiting-Failure-Handling AVP in Section 8.15 of 
    IETF RFC 4006.

    The Direct-Debiting-Failure-Handling AVP (AVP Code 428) is of type Enumerated.
    """
    code = DIRECT_DEBITING_FAILURE_HANDLING_AVP_CODE
    vendor_id = None

    values = [
                DIRECT_DEBITING_FAILURE_HANDLING_TERMINATE_OR_BUFFER,
                DIRECT_DEBITING_FAILURE_HANDLING_CONTINUE,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, DirectDebitingFailureHandlingAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class TariffTimeChangeAVP(DiameterAVP, TimeType):
    """Implementation of Tariff-Time-Change AVP in Section 8.20 of
    IETF RFC 4006.

    The Tariff-Time-Change AVP (AVP Code 451) is of type Time.
    """
    code = TARIFF_CHANGE_USAGE_AVP_CODE
    vendor_id = None

    def __init__(self, data=datetime.datetime.utcnow()):
        DiameterAVP.__init__(self, TariffTimeChangeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)    
        TimeType.__init__(self, data=data)


class CcTimeAVP(DiameterAVP, Unsigned32Type):
    """Implementation of CC-Time AVP in Section 8.21 of IETF RFC 4006.

    The CC-Time AVP (AVP Code 420) is of type Unsigned32.
    """
    code = CC_TIME_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, CcTimeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class CcTotalOctetsAVP(DiameterAVP, Unsigned64Type):
    """Implementation of CC-Total-Octets AVP in Section 8.23 of IETF RFC 4006.

    The CC-Total-Octets AVP (AVP Code 421) is of type Unsigned64.
    """
    code = CC_TOTAL_OCTETS_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, CcTotalOctetsAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned64Type.__init__(self, data=data)


class CcInputOctetsAVP(DiameterAVP, Unsigned64Type):
    """Implementation of CC-Input-Octets AVP in Section 8.24 of IETF RFC 4006.

    The CC-Input-Octets AVP (AVP Code 412) is of type Unsigned64.
    """
    code = CC_INPUT_OCTETS_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, CcInputOctetsAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned64Type.__init__(self, data=data)


class CcOutputOctetsAVP(DiameterAVP, Unsigned64Type):
    """Implementation of CC-Output-Octets AVP in Section 8.25 of IETF RFC 4006.

    The CC-Output-Octets AVP (AVP Code 414) is of type Unsigned64.
    """
    code = CC_OUTPUT_OCTETS_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, CcOutputOctetsAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned64Type.__init__(self, data=data)


class ValidityTimeAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Validity-Time AVP in Section 8.33 of IETF RFC 4006.

    The Validity-Time AVP (AVP Code 448) is of type Unsigned32.
    """
    code = VALIDITY_TIME_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, ValidityTimeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned32Type.__init__(self, data=data)


class ValueDigitsAVP(DiameterAVP, Unsigned64Type):
    """Implementation of Value-Digits AVP in Section 8.10 of IETF RFC 4006.

    The Value-Digits AVP (AVP Code 447) is of type Integer64.
    """
    code = VALUE_DIGITS_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, ValueDigitsAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        Unsigned64Type.__init__(self, data=data)


class GrantedServiceUnitAVP(DiameterAVP, GroupedType):
    """Implementation of Granted-Service-Unit AVP in Section 8.17 of
    IETF RFC 4006.

    The Granted-Service-Unit AVP (AVP Code 431) is of type Grouped.
    """
    code = GRANTED_SERVICE_UNIT_AVP_CODE
    vendor_id = None

    mandatory = {}
    optionals = {
                    "tariff_time_change": TariffTimeChangeAVP,
                    "cc_time": CcTimeAVP,
                    # "cc_money": CcMoneyAVP,
                    "cc_total_octets": CcTotalOctetsAVP,
                    "cc_input_octets": CcInputOctetsAVP,
                    "cc_output_octets": CcOutputOctetsAVP,
                    # "cc_service_specific_units": CCServiceSpecificUnitsAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, GrantedServiceUnitAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)


class RequestedServiceUnitAVP(DiameterAVP, GroupedType):
    """Implementation of Requested-Service-Unit AVP in Section 8.18 of
    IETF RFC 4006.

    The Requested-Service-Unit AVP (AVP Code 437) is of type Grouped.
    """
    code = REQUESTED_SERVICE_UNIT_AVP_CODE
    vendor_id = None

    mandatory = {}
    optionals = {
                    "cc_time": CcTimeAVP,
                    # "cc_money": CcMoneyAVP,
                    "cc_total_octets": CcTotalOctetsAVP,
                    "cc_input_octets": CcInputOctetsAVP,
                    "cc_output_octets": CcOutputOctetsAVP,
                    # "cc_service_specific_units": CCServiceSpecificUnitsAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, RequestedServiceUnitAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)


class MultipleServicesCreditControlAVP(DiameterAVP, GroupedType):
    """Implementation of Multiple-Services-Credit-Control AVP in Section 8.16 of
    IETF RFC 4006.

    The Multiple-Services-Credit-Control AVP (AVP Code 456) is of type Grouped.
    """
    code = MULTIPLE_SERVICES_CREDIT_CONTROL_AVP_CODE
    vendor_id = None

    mandatory = {}
    optionals = {
                    "granted_service_unit": GrantedServiceUnitAVP,
                    # "requested_service_unit": RequestedServiceUnitAVP,
                    # "used_service_unit": UsedServiceUnitAVP,
                    # "tariff_change_usage": TariffChangeUsageAVP,
                    # "service_identifier": ServiceIdentifierAVP,
                    "rating_group": RatingGroupAVP,
                    # "gsu_pool_reference": GSUPoolReferenceAVP,
                    "validity_time": ValidityTimeAVP,
                    "result_code": ResultCodeAVP,
                    # "final_unit_indication": FinalUnitIndicationAVP
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, MultipleServicesCreditControlAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)


class SubscriptionIdDataAVP(DiameterAVP, UTF8StringType):
    """Implementation of Subscription-Id-Data AVP in Section 8.48 of 
    IETF RFC 4006.

    The Subscription-Id-Data AVP (AVP Code 444) is of type UTF8String.
    """
    code = SUBSCRIPTION_ID_DATA_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, SubscriptionIdDataAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


class SubscriptionIdTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Subscription-Id-Type AVP in Section 8.47 of 
    IETF RFC 4006.

    The Subscription-Id-Type AVP (AVP Code 450) is of type Enumerated.
    """
    code = SUBSCRIPTION_ID_TYPE_AVP_CODE
    vendor_id = None

    values = [
                END_USER_E164,
                END_USER_IMSI,
                END_USER_SIP_URI,
                END_USER_NAI,
                END_USER_PRIVATE
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, SubscriptionIdTypeAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)


class SubscriptionIdAVP(DiameterAVP, GroupedType):
    """Implementation of Subscription-Id AVP in Section 8.46 of IETF RFC 4006.

    The Subscription-Id AVP (AVP Code 443) is of type Grouped.
    """
    code = SUBSCRIPTION_ID_AVP_CODE
    vendor_id = None

    mandatory = {
                    "subscription_id_data": SubscriptionIdDataAVP,
                    "subscription_id_type": SubscriptionIdTypeAVP,
    }
    optionals = {}

    def __init__(self, data):
        DiameterAVP.__init__(self, SubscriptionIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)