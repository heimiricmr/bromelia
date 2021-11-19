# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_gx.messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages for 3GPP Gx
    Application Id.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import platform
import socket

from .avps import *

from .._internal_utils import show_warn
from ..base import DiameterRequest, DiameterAnswer
from ..constants import *

show_warn("messages", "etsi_3gpp_gx")


class CreditControlAnswer(DiameterAnswer):
    """Implementation of CC-Answer (CCA) command as per 
    clause 5.6.3 of ETSI TS 129 212 V15.3.0 (2018-07).

    The CC-Answer is indicated by the Command Code field 
    set to 272 and Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_gx.messages import CreditControlAnswer as CCA
        >>> cca = CCA()
        >>> cca
        <Diameter Message: 272 [CCA] PXY, 16777238 [3GPP Gx], 7 AVP(s)>    
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "cc_request_type": CcRequestTypeAVP,
                    "cc_request_number": CcRequestNumberAVP,
    }
    optionals = { 
                    # "drmp": DrmpAVP,
                    "result_code": ResultCodeAVP,
                    "experimental_result": ExperimentalResultAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    # "oc_olr": OcOlrAVP,
                    "supported_features": SupportedFeaturesAVP,
                    # "bearer_control_mode": BearerControlModeAVP,
                    "event_trigger": EventTriggerAVP,
                    # "event_report_indication": EventReportIndicationAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "redirect_host": RedirectHostAVP,
                    "redirect_host_usage": RedirectHostUsageAVP,
                    "redirect_max_cache_time": RedirectMaxCacheTimeAVP,
                    # "charging_rule_remove": ChargingRuleRemoveAVP,
                    "charging_rule_install": ChargingRuleInstallAVP,
                    # "charging_information": ChargingInformationAVP,
                    "online": OnlineAVP,
                    "offline": OfflineAVP,
                    "qos_information": QosInformationAVP,
                    # "revalidation_time": RevalidationTimeAVP,
                    "default_eps_bearer_qos": DefaultEpsBearerQosAVP,
                    # "default_qos_information": DefaultQosInformationAVP,
                    "bearer_usage": BearerUsageAVP,
                    # "usage_monitoring_information": UsageMonitoringInformationAVP,
                    # "csg_information_reporting": CsgInformationReportingAVP,
                    # "user_csg_information": UserCsgInformationAVP,
                    # "pra_install": PraInstallAVP,
                    # "pra_remove": PraRemoveAVP,
                    # "presence_reporting_area_information": PresenceReportingAreaInformationAVP,
                    # "session_release_cause": SessionReleaseCauseAVP,
                    # "nbifom_support": NbifomSupportAVP,
                    # "nbifom_mode": NbifomModeAVP,
                    # "default_access": DefaultAccessAVP,
                    # "ran_rule_support": RanRuleSupportAVP,
                    # "routing_rule_report": RoutingRuleReportAVP,
                    # "conditional_policy_information": ConditionalPolicyInformationAVP,
                    # "removal_of_access": RemovalOfAccessAVP,
                    "ip_can_type": IpCanTypeAVP,
                    "error_message": ErrorMessageAVP,
                    # "error_reporting": ErrorReportingAVP,
                    "failed_avp": FailedAvpAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
                    # "load": LoadAVP
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 auth_application_id=DIAMETER_APPLICATION_Gx,
                 origin_host=platform.node(),
                 origin_realm=socket.getfqdn(),
                 result_code=DIAMETER_SUCCESS,
                 experimental_result=None,
                 cc_request_type=CC_REQUEST_TYPE_INITIAL_REQUEST,
                 cc_request_number=0,
                 oc_supported_features=None,
                 oc_olr=None,
                 supported_features=None,
                 bearer_control_mode=None,
                 event_trigger=None,
                 event_report_indication=None,
                 origin_state_id=None,
                 redirect_host=None,
                 redirect_host_usage=None,
                 redirect_max_cache_time=None,
                 charging_rule_remove=None,
                 charging_rule_install=None,
                 charging_information=None,
                 online=None,
                 offline=None,
                 qos_information=None,
                 revalidation_time=None,
                 default_eps_bearer_qos=None,
                 default_qos_information=None,
                 bearer_usage=None,
                 usage_monitoring_information=None,
                 csg_information_reporting=None,
                 user_csg_information=None,
                 pra_install=None,
                 pra_remove=None,
                 presence_reporting_area_information=None,
                 session_release_cause=None,
                 nbifom_support=None,
                 nbifom_mode=None,
                 default_access=None,
                 ran_rule_support=None,
                 routing_rule_report=None,
                 conditional_policy_information=None,
                 removal_of_access=None,
                 ip_can_type=None,
                 error_message=None,
                 error_reporting_host=None,
                 failed_avp=None,
                 proxy_info=None,
                 route_record=None,
                 load=None,
                 **kwargs):

        DiameterAnswer.__init__(self,
                                 command_code=CC_MESSAGE,
                                 application_id=DIAMETER_APPLICATION_Gx)

        DiameterAnswer._load(self, locals())


class CreditControlRequest(DiameterRequest):
    """Implementation of CC-Request (CCR) command as per 
    clause 5.6.2 of ETSI TS 129 212 V15.3.0 (2018-07).

    The CC-Request is indicated by the Command Code field 
    set to 272 and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.etsi_3gpp_gx.messages import CreditControlRequest as CCR
        >>> from bromelia.constants import *
        >>> ccr_avps = {
        ...     "destination_realm": "remote",
        ...     "cc_request_type": CC_REQUEST_TYPE_INITIAL_REQUEST,
        ...     "cc_request_number": 1,
        ... }
        >>> ccr = CCR(**ccr_avps)
        >>> ccr
        <Diameter Message: 272 [CCR] REQ|PXY, 16777238 [3GPP Gx], 7 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "cc_request_type": CcRequestTypeAVP,
                    "cc_request_number": CcRequestNumberAVP,
    }
    optionals = {
                    # "drmp": DrmpAVP,
                    # "credit_management_status": CreditManagementStatusAVP,
                    "destination_host": DestinationHostAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "subscription_id": SubscriptionIdAVP,
                    # "oc_supported_features": OcSupportedAVP,
                    "supported_features": SupportedFeaturesAVP,
                    # "tdf_information": TdfInformationAVP,
                    "network_request_support": NetworkRequestSupportAVP,
                    # "packet_filter_information": PacketFilterInformationAVP,
                    # "packet_filter_operation": PacketFilterOperationAVP,
                    # "bearer_identifier": BearerIdentifierAVP,
                    # "bearer_operation": BearerOperationAVP,
                    # "dynamic_address_flag": DynamicAddressFlagAVP,
                    # "dynamic_address_flag_extension": DynamicAddressFlagExtensionAVP,
                    # "pdn_connection_charging_id": PdnConnectionChargingIdAVP,
                    "framed_ip_address": FramedIpAddressAVP,
                    "framed_ipv6_prefix": FramedIpv6PrefixAVP,
                    "ip_can_type": IpCanTypeAVP,
                    # "x3gpp_rat_type": X3gppRatTypeAVP,
                    "an_trusted": AnTrustedAVP,
                    "rat_type": RatTypeAVP,
                    "termination_cause": TerminationCauseAVP,
                    "user_equipment_info": UserEquipmentInfoAVP,
                    "qos_information": QosInformationAVP,
                    # "qos_negotiation": QosNegotiationAVP,
                    # "qos_upgrade": QosUpgradeAVP,
                    "default_eps_bearer_qos": DefaultEpsBearerQosAVP,
                    # "default_qos_information": DefaultQosInformationAVP,
                    "an_gw_address": AnGwAddressAVP,
                    # "an_gw_status": AnGwStatusAVP,
                    # "x3gpp_sgsn_mcc_mnc": X3gppSgsnMccMncAVP,
                    # "x3gpp_sgsn_address": X3gppSgsnAddressAVP,
                    # "x3gpp_sgsn_ipv6_address": X3gppSgsnIpv6AddressAVP,
                    # "x3gpp_ggsn_address": X3gppGgsnAddressAVP,
                    # "x3gpp_ggsn_ipv6_address": X3gppGgsnIpv6AddressAVP,
                    # "x3gpp_selection_mode": X3gppSelectionModeAVP,
                    # "rai": RaiAVP,
                    # "x3gpp_user_location_info": X3gppUserLocationInfoAVP,
                    # "fixed_user_location_info": FixedUserLocationInfoAVP,
                    # "user_location_info_time": UserLocationInfoTimeAVP,
                    # "user_csg_information": UserCsgInformationAVP,
                    # "twan_identifier": TwanIdentifierAVP,
                    # "x3gpp_ms_timezone": X3gppMsTimezoneAVP,
                    # "ran_nas_release_cause": RanNasReleaseCauseAVP,
                    "x3gpp_charging_characteristics": X3gppChargingCharacteristicsAVP,
                    "called_station_id": CalledStationIdAVP,
                    # "pdn_connection_id": PdnConnectionIdAVP,
                    "bearer_usage": BearerUsageAVP,
                    "online": OnlineAVP,
                    "offline": OfflineAVP,
                    # "tft_packet_filter_information": TftPacketFilterInformationAVP,
                    "charging_rule_report": ChargingRuleReportAVP,
                    # "application_detection_information": ApplicationDetectionInformationAVP,
                    "event_trigger": EventTriggerAVP,
                    # "event_report_indication": EventReportIndicationAVP,
                    "access_network_charging_address": AccessNetworkChargingAddressAVP,
                    "access_network_charging_identifier_gx": AccessNetworkChargingIdentifierGxAVP,
                    # "coa_information": CoaInformationAVP,
                    # "usage_monitoring_information": UsageMonitoringInformationAVP,
                    # "nbifom_support": NbifomSupportAVP,
                    # "nbifom_mode": NbifomModeAVP,
                    # "default_access": DefaultAccessAVP,
                    # "origination_time_stamp": OriginationTimeStampAVP,
                    # "maximum_wait_time": MaximumWaitTimeAVP,
                    # "access_availability_change_reason": AccessAvailabilityChangeReasonAVP,
                    # "routing_rule_install": RoutingRuleInstallAVP,
                    # "routing_rule_remove": RoutingRuleRemoveAVP,
                    # "henb_local_ip_address": HenbLocalIpAddressAVP,
                    "ue_local_ip_address": UeLocalIpAddressAVP,
                    # "udp_source_port": UdpSourcePortAVP,
                    # "tcp_source_port": TcpLocalIpAddressAVP,
                    # "presence_reporting_area_information": PresenceReportingAreaInformationAVP,
                    # "logical_access_id": LogicalAccessIdAVP,
                    # "physical_access_id": PhysicalAccessIdAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
                    # "x3gpp_ps_data_off_status": X3gppPsDataOffStatusAVP
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 auth_application_id=DIAMETER_APPLICATION_Gx,
                 origin_host=platform.node(),
                 origin_realm=socket.getfqdn(),
                 destination_realm=None,
                 cc_request_type=CC_REQUEST_TYPE_INITIAL_REQUEST,
                 cc_request_number=0,
                 credit_management_status=None,
                 destination_host=None,
                 origin_state_id=None,
                 subscription_id=None,
                 oc_supported_features=None,
                 supported_features=None,
                 tdf_information=None,
                 network_request_support=None,
                 packet_filter_information=None,
                 packet_filter_operation=None,
                 bearer_identifier=None,
                 bearer_operation=None,
                 dynamic_address_flag=None,
                 dynamic_address_flag_extension=None,
                 pdn_connection_charging_id=None,
                 framed_ip_address=None,
                 framed_ipv6_prefix=None,
                 ip_can_type=None,
                 x3gpp_rat_type=None,
                 an_trusted=None,
                 rat_type=None,
                 termination_cause=None,
                 user_equipment_info=None,
                 qos_information=None,
                 qos_negotiation=None,
                 qos_upgrade=None,
                 default_eps_bearer_qos=None,
                 default_qos_information=None,
                 an_gw_address=None,
                 an_gw_status=None,
                 x3gpp_sgsn_mcc_mnc=None,
                 x3gpp_sgsn_address=None,
                 x3gpp_sgsn_ipv6_address=None,
                 x3gpp_ggsn_address=None,
                 x3gpp_ggsn_ipv6_address=None,
                 x3gpp_selection_mode=None,
                 rai=None,
                 x3gpp_user_location_info=None,
                 fixed_user_location_info=None,
                 user_location_info_time=None,
                 user_csg_information=None,
                 twan_identifier=None,
                 x3gpp_ms_timezone=None,
                 ran_nas_release_cause=None,
                 x3gpp_charging_characteristics=None,
                 called_station_id=None,
                 pdn_connection_id=None,
                 bearer_usage=None,
                 online=None,
                 offline=None,
                 tft_packet_filter_information=None,
                 charging_rule_report=None,
                 application_detection_information=None,
                 event_trigger=None,
                 event_report_indication=None,
                 access_network_charging_address=None,
                 access_network_charging_identifier_gx=None,
                 coa_information=None,
                 usage_monitoring_information=None,
                 nbifom_support=None,
                 nbifom_mode=None,
                 default_access=None,
                 origination_time_stamp=None,
                 maximum_wait_time=None,
                 access_availability_change_reason=None,
                 routing_rule_install=None,
                 routing_rule_remove=None,
                 henb_local_ip_address=None,
                 ue_local_ip_address=None,
                 udp_source_port=None,
                 tcp_source_port=None,
                 presence_reporting_area_information=None,
                 logical_access_id=None,
                 physical_access_id=None,
                 proxy_info=None,
                 route_record=None,
                 x3gpp_ps_data_off_status=None,
                 **kwargs):

        DiameterRequest.__init__(self,
                                 command_code=CC_MESSAGE,
                                 application_id=DIAMETER_APPLICATION_Gx)

        DiameterRequest._load(self, locals())


class ReAuthAnswer(DiameterAnswer):
    """Implementation of Re-Auth-Answer (RAA) command as per 
    clause 5.6.5 of ETSI TS 129 212 V15.3.0 (2018-07).

    The Re-Auth-Answer is indicated by the Command Code field 
    set to 258 and Command Flag's 'R' bit cleared.

    Usage::

        >>> from bromelia.etsi_3gpp_gx.messages import ReAuthAnswer as RAA
        >>> raa = RAA()
        >>> raa
        <Diameter Message: 258 [RAA] PXY, 16777238 [3GPP Gx], 4 AVP(s)>  
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
    }
    optionals = { 
                    # "drmp": DrmpAVP,
                    "result_code": ResultCodeAVP,
                    "experimental_result": ExperimentalResultAVP,
                    "origin_state_id": OriginStateIdAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    # "oc_olr": OcOlrAVP,
                    "ip_can_type": IpCanTypeAVP,
                    "rat_type": RatTypeAVP,
                    "an_trusted": AnTrustedAVP,
                    "an_gw_address": AnGwAddressAVP,
                    # "x3gpp_sgsn_mcc_mnc": X3gppSgsnMccMncAVP,
                    # "x3gpp_sgsn_address": X3gppSgsnAddressAVP,
                    # "x3gpp_sgsn_ipv6_address": X3gppSgsnIpv6AddressAVP,
                    # "rai": RaiAVP,
                    # "x3gpp_user_location_info": X3gppUserLocationInfoAVP,
                    # "user_location_info_time": UserLocationInfoTimeAVP,
                    # "netloc_access_support": NetlocAccessSupportAVP,
                    # "user_csg_information": UserCsgInformationAVP,
                    # "x3gpp_ms_timezone": X3gppMsTimezoneAVP,
                    # "default_qos_information": DefaultQosInformationAVP,
                    "charging_rule_report": ChargingRuleReportAVP,
                    "error_message": ErrorMessageAVP,
                    "error_reporting_host": ErrorReportingHostAVP,
                    "failed_avp": FailedAvpAVP,
                    "proxy_info": ProxyInfoAVP
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 origin_host=platform.node(),
                 origin_realm=socket.getfqdn(),
                 result_code=DIAMETER_SUCCESS,
                 experimental_result=None,
                 origin_state_id=None,
                 oc_supported_features=None,
                 oc_olr=None,
                 ip_can_type=None,
                 rat_type=None,
                 an_trusted=None,
                 an_gw_address=None,
                 x3gpp_sgsn_mcc_mnc=None,
                 x3gpp_sgsn_address=None,
                 x3gpp_sgsn_ipv6_address=None,
                 rai=None,
                 x3gpp_user_location_info=None,
                 user_location_info_time=None,
                 netloc_access_support=None,
                 user_csf_information=None,
                 x3gpp_ms_timezone=None,
                 default_qos_information=None,
                 charging_rule_report=None,
                 error_message=None,
                 error_reporting_host=None,
                 failed_avp=None,
                 proxy_info=None,
                 **kwargs):

        DiameterAnswer.__init__(self,
                                 command_code=RE_AUTH_MESSAGE,
                                 application_id=DIAMETER_APPLICATION_Gx)

        DiameterAnswer._load(self, locals())


class ReAuthRequest(DiameterRequest):
    """Implementation of Re-Auth-Request (RAR) command as per 
    clause 5.6.4 of ETSI TS 129 212 V15.3.0 (2018-07).

    The Re-Auth-Request is indicated by the Command Code field 
    set to 258 and the 'R' bit set in the Command Flags field.

    Usage::

        >>> from bromelia.etsi_3gpp_gx.messages import ReAuthRequest as RAR
        >>> rar_avps = {
        ...     "destination_realm": "remote"
        ... }
        >>> rar = RAR(**rar_avps)
        >>> rar
        <Diameter Message: 258 [RAR] REQ|PXY, 16777238 [3GPP Gx], 6 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "re_auth_request_type": ReAuthRequestTypeAVP,
    }
    optionals = {
                    # "drmp": DrmpAVP,
                    # "session_release_cause": SessionReleaseCauseAVP,
                    "origin_state_id": OriginStateIdAVP,
                    # "oc_supported_features": OcSupportedFeaturesAVP,
                    "event_trigger": EventTriggerAVP,
                    # "event_report_indication": EventReportIndicationAVP,
                    # "charging_rule_remove": ChargingRuleRemoveAVP,
                    "charging_rule_install": ChargingRuleInstallAVP,
                    "default_eps_bearer_qos": DefaultEpsBearerQosAVP,
                    "qos_information": QosInformationAVP,
                    # "default_qos_information": DefaultQosInformationAVP,
                    # "revalidation_time": RevalidationTimeAVP,
                    # "usage_monitoring_information": UsageMonitoringInformationAVP,
                    # "pcscf_restoration_indication": PcscfRestorationIndicationAVP,
                    # "conditional_policy_information": ConditionalPolicyInformationAVP,
                    # "removal_of_access": RemovalOfAccessAVP,
                    "ip_can_type": IpCanTypeAVP,
                    # "pra_install": PraInstallAVP,
                    # "pra_remove": PraRemoveAVP,
                    # "csg_information_reporting": CsgInformationReportingAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP
    }

    def __init__(self,
                 session_id=platform.node(),
                 drmp=None,
                 auth_application_id=DIAMETER_APPLICATION_Gx,
                 origin_host=platform.node(),
                 origin_realm=socket.getfqdn(),
                 destination_realm=None,
                 destination_host=None,
                 re_auth_request_type=RE_AUTH_REQUEST_TYPE_AUTHORIZE_ONLY,
                 session_release_cause=None,
                 origin_state_id=None,
                 oc_supported_features=None,
                 event_trigger=None,
                 event_report_indication=None,
                 charging_rule_remove=None,
                 charging_rule_install=None,
                 default_eps_bearer_qos=None,
                 qos_information=None,
                 default_qos_information=None,
                 revalidation_time=None,
                 usage_monitoring_information=None,
                 pcscf_restoration_indication=None,
                 conditional_policy_information=None,
                 removal_of_access=None,
                 ip_can_type=None,
                 pra_install=None,
                 pra_remove=None,
                 csg_information_reporting=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterRequest.__init__(self,
                                 command_code=RE_AUTH_MESSAGE,
                                 application_id=DIAMETER_APPLICATION_Gx)

        DiameterRequest._load(self, locals())
