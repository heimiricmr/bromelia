# List of DiameterAVP objects

|name|code|type|spec|section|path|#|class_name
|----|----|----|----|-------|----|-|----------
|`User-Name`|1|UTF8String| IETF RFC 6733|8.14|[avps.py](../bromelia/avps.py)|1|UserNameAVP
|`Class`|25|OctetString| IETF RFC 6733|8.2|[avps.py](../bromelia/avps.py)|2|ClassAVP
|`Session-Timeout`|27|Unsigned32| IETF RFC 6733|8.13|[avps.py](../bromelia/avps.py)|3|SessionTimeoutAVP
|`Calling-Station-Id`|31|UTF8String| IETF RFC 7155|4.2.6|[avps.py](../bromelia/avps.py)|4|CallingStationIdAVP
|`Proxy-State`|33|OctetString| IETF RFC 6733|6.7.4|[avps.py](../bromelia/avps.py)|5|ProxyStateAVP
|`Acct-Session-Id`|44|OctetString| IETF RFC 6733|9.8.4|[avps.py](../bromelia/avps.py)|6|AcctSessionIdAVP
|`Acct-Multi-Session-Id`|50|UTF8String| IETF RFC 6733|9.8.5|[avps.py](../bromelia/avps.py)|7|AcctMultiSessionIdAVP
|`Event-Timestamp`|55|Time| IETF RFC 6733|8.21|[avps.py](../bromelia/avps.py)|8|EventTimestampAVP
|`Acct-Interim-Interval`|85|Unsigned32| IETF RFC 6733|9.8.2|[avps.py](../bromelia/avps.py)|9|AcctInterimIntervalAVP
|`Host-IP-Address`|257|Address| IETF RFC 3588|5.3.5|[avps.py](../bromelia/avps.py)|10|HostIpAddressAVP
|`Auth-Application-Id`|258|Unsigned32| IETF RFC 3588|6.8|[avps.py](../bromelia/avps.py)|11|AuthApplicationIdAVP
|`Acct-Application-Id`|259|Unsigned32| IETF RFC 6733|6.9|[avps.py](../bromelia/avps.py)|12|AcctApplicationIdAVP
|`Vendor-Specific-Application-Id`|260|Grouped| IETF RFC 6733|6.11|[avps.py](../bromelia/avps.py)|14 (13)|VendorSpecificApplicationIdAVP
|`Redirect-Host-Usage`|261|Enumerated| IETF RFC 6733|6.13|[avps.py](../bromelia/avps.py)|15 (14)|RedirectHostUsageAVP
|`Redirect-Max-Cache-Time`|262|Unsigned32| IETF RFC 6733|6.14|[avps.py](../bromelia/avps.py)|16 (15)|RedirectMaxCacheTimeAVP
|`Session-Id`|263|UTF8String| IETF RFC 3588|8.8|[avps.py](../bromelia/avps.py)|17 (16)|SessionIdAVP
|`Origin-Host`|264|DiameterIdentity| IETF RFC 3588|6.3|[avps.py](../bromelia/avps.py)|18 (17)|OriginHostAVP
|`Supported-Vendor-Id`|265|Unsigned32| IETF RFC 6733|5.3.6|[avps.py](../bromelia/avps.py)|19 (18)|SupportedVendorIdAVP
|`Vendor-Id`|266|Unsigned32| IETF RFC 3588|5.3.3|[avps.py](../bromelia/avps.py)|13 (19)|VendorIdAVP
|`Firmware-Revision`|267|Unsigned32| IETF RFC 3588|5.3.4|[avps.py](../bromelia/avps.py)|20|FirmwareRevisionAVP
|`Result-Code`|268|Unsigned32| IETF RFC 3588|7.1|[avps.py](../bromelia/avps.py)|21|ResultCodeAVP
|`Product-Name`|269|UTF8String| IETF RFC 3588|5.3.7|[avps.py](../bromelia/avps.py)|22|ProductNameAVP
|`Session-Binding`|270|Unsigned32| IETF RFC 6733|8.17|[avps.py](../bromelia/avps.py)|23|SessionBindingAVP
|`Session-Server-Failover`|271|Enumerated| IETF RFC 6733|8.18|[avps.py](../bromelia/avps.py)|24|SessionServerFailoverAVP
|`Multi-Round-Time-Out`|272|Unsigned32| IETF RFC 6733|8.19|[avps.py](../bromelia/avps.py)|25|MultiRoundTimeOutAVP
|`Disconnect-Cause`|273|Enumerated| IETF RFC 3588|5.4.3|[avps.py](../bromelia/avps.py)|26|DisconnectCauseAVP
|`Auth-Request-Type`|274|Enumerated| IETF RFC 3588|8.7|[avps.py](../bromelia/avps.py)|27|AuthRequestTypeAVP
|`Auth-Grace-Period`|276|Unsigned32| IETF RFC 6733|8.1|[avps.py](../bromelia/avps.py)|28|AuthGracePeriodAVP
|`Auth-Session-State`|277|Enumerated| IETF RFC 3588|8.11|[avps.py](../bromelia/avps.py)|29|AuthSessionStateAVP
|`Origin-State-Id`|278|Unsigned32| IETF RFC 6733|8.16|[avps.py](../bromelia/avps.py)|30|OriginStateIdAVP
|`Failed-AVP`|279|Grouped| IETF RFC 6733|7.5|[avps.py](../bromelia/avps.py)|31|FailedAvpAVP
|`Proxy-Host`|280|DiameterIdentity| IETF RFC 6733|6.7.3|[avps.py](../bromelia/avps.py)|32|ProxyHostAVP
|`Error-Message`|281|UTF8String| IETF RFC 6733|7.3|[avps.py](../bromelia/avps.py)|33|ErrorMessageAVP
|`Route-Record`|282|DiameterIdentity| IETF RFC 6733|6.7.1|[avps.py](../bromelia/avps.py)|34|RouteRecordAVP
|`Destination-Realm`|283|DiameterIdentity| IETF RFC 3588|6.6|[avps.py](../bromelia/avps.py)|35|DestinationRealmAVP
|`Proxy-Info`|284|Grouped| IETF RFC 6733|6.7.2|[avps.py](../bromelia/avps.py)|36|ProxyInfoAVP
|`Re-Auth-Request-Type`|285|Enumerated| IETF RFC 6733|8.12|[avps.py](../bromelia/avps.py)|37|ReAuthRequestTypeAVP
|`Accounting-Sub-Session-Id`|287|Unsigned64| IETF RFC 6733|9.8.6|[avps.py](../bromelia/avps.py)|38|AccountingSubSessionIdAVP
|`Authorization-Lifetime`|291|Unsigned32| IETF RFC 6733|8.9|[avps.py](../bromelia/avps.py)|39|AuthorizationLifetimeAVP
|`Redirect-Host`|292|DiameterURI| IETF RFC 6733|6.12|[avps.py](../bromelia/avps.py)|40|RedirectHostAVP
|`Destination-Host`|293|DiameterIdentity| IETF RFC 3588|6.5|[avps.py](../bromelia/avps.py)|41|DestinationHostAVP
|`Error-Reporting-Host`|294|DiameterIdentity| IETF RFC 6733|7.4|[avps.py](../bromelia/avps.py)|42|ErrorReportingHostAVP
|`Termination-Cause`|295|Enumerated| IETF RFC 6733|8.47|[avps.py](../bromelia/avps.py)|43|TerminationCauseAVP
|`Origin-Realm`|296|DiameterIdentity| IETF RFC 3588|6.4|[avps.py](../bromelia/avps.py)|44|OriginRealmAVP
|`Experimental-Result`|297|Grouped| IETF RFC 6733|7.6|[avps.py](../bromelia/avps.py)|45|ExperimentalResultAVP
|`Experimental-Result-Code`|298|Unsigned32| IETF RFC 6733|7.7|[avps.py](../bromelia/avps.py)|46|ExperimentalResultCodeAVP
|`Inband-Security-Id`|299|Unsigned32| IETF RFC 6733|6.1|[avps.py](../bromelia/avps.py)|47|InbandSecurityIdAVP
|`MIP-Home-Agent-Host`|348|Grouped|IETF RFC 5447|4.2.3|[avps.py](../bromelia/avps.py)|48|MipHomeAgentHostAVP
|`Subscription-Id`|443|Grouped| IETF RFC 4006|8.46|[avps.py](../bromelia/avps.py)|49|SubscriptionIdAVP
|`Subscription-Id-Data`|444|UTF8String| IETF RFC 4006|8.48|[avps.py](../bromelia/avps.py)|50|SubscriptionIdDataAVP
|`Subscription-Id-Type`|450|Enumerated| IETF RFC 4006|8.47|[avps.py](../bromelia/avps.py)|51|SubscriptionIdTypeAVP
|`EAP-Payload`|462|OctetString| IETF RFC 4072|4.1.1|[avps.py](../bromelia/avps.py)|52|EapPayloadAVP
|`EAP-Master-Session-Key`|464|OctetString| IETF RFC 4072|4.1.3|[avps.py](../bromelia/avps.py)|53|EapMasterSessionKeyAVP
|`Accounting-Record-Type`|480|Enumerated| IETF RFC 6733|9.8.1|[avps.py](../bromelia/avps.py)|54|AccountingRecordTypeAVP
|`Accounting-Realtime-Required`|483|Enumerated| IETF RFC 6733|9.8.7|[avps.py](../bromelia/avps.py)|55|AccoutingRealtimeRequiredAVP
|`Accounting-Record-Number`|485|Unsigned32| IETF RFC 6733|9.8.3|[avps.py](../bromelia/avps.py)|56|AccountingRecordNumberAVP
|`MIP6-Agent-Info`|486|Grouped| IETF RFC 5447|4.2.1|[avps.py](../bromelia/avps.py)|57|Mip6AgentInfoAVP
|`3GPP-Charging-Characteristics`|13|UTF8String|ETSI TS 129 061 V10.11.0 (2014-10)|16.4.7.2|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|1|X3gppChargingCharacteristicsAVP
|`Service-Selection`|493|UTF8String|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.36|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|2|ServiceSelectionAVP
|`Mobile-Node-Identifier`|506|UTF8String|ETSI TS 129 273 V15.4.0 (2019-10)|5.2.3.2|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|3|MobileNodeIdentifierAVP
|`Max-Requested-Bandwidth-DL`|515|Unsigned32|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.14|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|4|MaxRequestedBandwidthDlAVP
|`Max-Requested-Bandwidth-UL`|516|Unsigned32|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.15|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|5|MaxRequestedBandwidthUlAVP
|`Visited-Network-Identifier`|600|OctetString|ETSI TS 129 229 V15.2.0 (2019-10)|6.3.1 |[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|6|VisitedNetworkIdentifierAVP
|`QoS-Class-Identifier`|1028|Enumerated|ETSI TS 129 212 V12.6.0 (2014-10)|5.3.17|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|7|QosClassIdentifierAVP
|RAT-Type AVP|1032|Enumerated|ETSI TS 129 212|5.3.31|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|8|RatTypeAVP
|`Allocation-Retention-Priority`|1034|Grouped|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.40|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|9|AllocationRetentionPriorityAVP
|`Priority-Level`|1406|Unsigned32|ETSI TS 129 212 V12.6.0 (2014-10)|5.3.45|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|10|PriorityLevelAVP
|`Context-Identifier`|1423|Unsigned32|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.27|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|11|ContextIdentifierAVP
|`APN-Configuration`|1430|Grouped|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.35|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|12|ApnConfigurationAVP
|`EPS-Subscribed-QoS-Profile`|1431|Grouped|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.37|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|13|EpsSubscribedQosProfileAVP
|`VPLMN-Dynamic-Address-Allowed`|1432|Enumerated|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.38|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|14|VplmnDynamicAddressAllowedAVP
|`AMBR`|1435|Grouped|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.41|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|15|AmbrAVP
|`PDN-GW-Allocation-Type`|1438|Enumerated|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.44|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|16|PdnGwAllocationTypeAVP
|`PDN-Type`|1456|Enumerated|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.62|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|17|PdnTypeAVP
|`Non-3GPP-IP-Access`|1501|Enumerated|ETSI TS 129 273 V14.5.0 (2019-10)|8.2.3.3|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|18|Non3gppIpAccessAVP
|`UE-Local-IP-Address`|2805|Address|ETSI TS 129 212 V15.9.0 (2020-01)|5.3.5|[etsi_3gpp_swm/avps.py](../bromelia/etsi_3gpp_swm/avps.py)|19|UeLocalIpAddressAVP
|`SIP-Number-Auth-Items`|607|Unsigned32|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.8|[etsi_3gpp_swx/avps.py](../bromelia/etsi_3gpp_swx/avps.py)|1|SipNumberAuthItemsAVP
|`Authentication-Scheme`|608|UTF8String|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.9|[etsi_3gpp_swx/avps.py](../bromelia/etsi_3gpp_swx/avps.py)|2|SipAuthenticationSchemeAVP
|`SIP-Authenticate`|609|OctetString|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.10|[etsi_3gpp_swx/avps.py](../bromelia/etsi_3gpp_swx/avps.py)|3|SipAuthenticateAVP
|`SIP-Authorization`|610|OctetString|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.11 |[etsi_3gpp_swx/avps.py](../bromelia/etsi_3gpp_swx/avps.py)|4|SipAuthorizationAVP
|`Confidentiality-Key`|625|OctetString|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.27 |[etsi_3gpp_swx/avps.py](../bromelia/etsi_3gpp_swx/avps.py)|5|ConfidentialityKeyAVP
|`Integrity-Key`|626|OctetString|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.28|[etsi_3gpp_swx/avps.py](../bromelia/etsi_3gpp_swx/avps.py)|6|IntegrityKeyAVP
|`SIP-Auth-Data-Item`|612|Grouped|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.13 |[etsi_3gpp_swx/avps.py](../bromelia/etsi_3gpp_swx/avps.py)|7|SipAuthDataItemAVP
|`Non-3GPP-Ip-Access`|1501|Enumerated|ETSI TS 129 273 V14.3.0 (2017-07)|8.2.3.3|[etsi_3gpp_swx/avps.py](../bromelia/etsi_3gpp_swx/avps.py)|8|Non3gppIpAccessAVP
|`Non-3GPP-Ip-Access-APN`|1502|Enumerated|ETSI TS 129 273 V14.3.0 (2017-07)|8.2.3.4|[etsi_3gpp_swx/avps.py](../bromelia/etsi_3gpp_swx/avps.py)|9|Non3gppIpAccessApnAVP
|`Non-3GPP-User-Data`|1500|Grouped|ETSI TS 129 273 V14.3.0 (2017-07)|8.2.3.1|[etsi_3gpp_swx/avps.py](../bromelia/etsi_3gpp_swx/avps.py)|10|Non3gppUserDataAVP
|`Server-Assignment-Type`|614|Enumerated|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.15|[etsi_3gpp_swx/avps.py](../bromelia/etsi_3gpp_swx/avps.py)|11|ServerAssignmentTypeAVP
|`Reason-Code`|616|Enumerated|ETSI TS 129 229 V11.3.0 (2013-04)|6.3.17|[etsi_3gpp_swx/avps.py](../bromelia/etsi_3gpp_swx/avps.py)|12|ReasonCodeAVP
|`Reason-Info`|617|UTF8String|ETSI TS 129 229 V11.3.0 (2013-04)|6.3.18|[etsi_3gpp_swx/avps.py](../bromelia/etsi_3gpp_swx/avps.py)|13|ReasonInfoAVP
|`Deregistration-Reason`|615|Grouped|ETSI TS 129 229 V11.3.0 (2013-04)|6.3.16 |[etsi_3gpp_swx/avps.py](../bromelia/etsi_3gpp_swx/avps.py)|14|DeregistrationReasonAVP
|`Supported-Features`|628|Grouped|ETSI TS 129 229 V14.3.0 (2019-10)|6.3.29 |[etsi_3gpp_s6a_s6d/avps.py](../bromelia/etsi_3gpp_s6a_s6d/avps.py)|1|SupportedFeaturesAVP
|`Feature-List-ID`|629|Unsigned32|ETSI TS 129 229 V14.3.0 (2019-10)|6.3.30|[etsi_3gpp_s6a_s6d/avps.py](../bromelia/etsi_3gpp_s6a_s6d/avps.py)|2|FeatureListIdAVP
|`Feature-List`|630|Unsigned32|ETSI TS 129 229 V14.3.0 (2019-10)|6.3.31|[etsi_3gpp_s6a_s6d/avps.py](../bromelia/etsi_3gpp_s6a_s6d/avps.py)|3|FeatureListAVP
|`Terminal-Information`|1401|Grouped|ETSI TS 129 272 V15.10.0 (2020-01)|5.3.14|[etsi_3gpp_s6a_s6d/avps.py](../bromelia/etsi_3gpp_s6a_s6d/avps.py)|4|TerminalInformationAVP
|`IMEI`|1402|UTF8String|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.4|[etsi_3gpp_s6a_s6d/avps.py](../bromelia/etsi_3gpp_s6a_s6d/avps.py)|5|ImeiAVP
|`Software-Version`|1403|UTF8String|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.5|[etsi_3gpp_s6a_s6d/avps.py](../bromelia/etsi_3gpp_s6a_s6d/avps.py)|6|SoftwareVersionAVP
|`ULR-Flags`|1405|Unsigned32|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.7 |[etsi_3gpp_s6a_s6d/avps.py](../bromelia/etsi_3gpp_s6a_s6d/avps.py)|7|UlrFlagsAVP
|`Visited-PLMN-Id`|1407|OctetString|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.9 |[etsi_3gpp_s6a_s6d/avps.py](../bromelia/etsi_3gpp_s6a_s6d/avps.py)|8|VisitedPlmnIdAVP
|`UE-SRVCC-Capability`|1615|Enumerated|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.130 |[etsi_3gpp_s6a_s6d/avps.py](../bromelia/etsi_3gpp_s6a_s6d/avps.py)|9|UeSrvccCapabilityAVP
|`Supported-Services`|3143|Grouped|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.199 |[etsi_3gpp_s6a_s6d/avps.py](../bromelia/etsi_3gpp_s6a_s6d/avps.py)|10|SupportedServicesAVP
|`Supported-Monitoring-Events`|3144|Unsigned64|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.200 |[etsi_3gpp_s6a_s6d/avps.py](../bromelia/etsi_3gpp_s6a_s6d/avps.py)|11|SupportedMonitoringEventsAVP
|`Cancellation-Type`|1420|Enumerated|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.24 |[etsi_3gpp_s6a_s6d/avps.py](../bromelia/etsi_3gpp_s6a_s6d/avps.py)|12|CancellationTypeAVP
|`CLR-Flags`|1638|Unsigned32|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.152|[etsi_3gpp_s6a_s6d/avps.py](../bromelia/etsi_3gpp_s6a_s6d/avps.py)|13|ClrFlagsAVP
|`MIP6-Feature-Vector`|124|Unsigned64|ETSI TS 129 273 V14.3.0 (2017-07)|9.2.3.2.3|[etsi_3gpp_s6b/avps.py](../bromelia/etsi_3gpp_s6b/avps.py)|1|Mip6FeatureVectorAVP
