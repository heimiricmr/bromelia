from ..._internal_utils import convert_to_4_bytes


#: Diameter AVPs
LOW_BALANCE_INDICATION_AVP_CODE = convert_to_4_bytes(2020)
REMAINING_BALANCE_AVP_CODE = convert_to_4_bytes(2021)

#: List of Low-Balance-Indication AVP values.
#: For more information, please refer to Section 7.2.97 of
#: ETSI TS 132 299 V14.3.0 (2017-04).
LOW_BALANCE_INDICATION_NOT_APPLICABLE = convert_to_4_bytes(0)
LOW_BALANCE_INDICATION_YES = convert_to_4_bytes(1)
