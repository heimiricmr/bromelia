# List of DiameterAVP objects

|name|code|type|spec|section|path|#|class_name
|----|----|----|----|-------|----|-|----------
|1|`Subscription-Id-Data`|444|UTF8String|IETF RFC 4006|8.48|[avps.ietf.rfc4006](../bromelia/avps/ietf/rfc4006.py#L17)|SubscriptionIdDataAVP
|2|`Subscription-Id-Type`|450|Enumerated|IETF RFC 4006|8.47|[avps.ietf.rfc4006](../bromelia/avps/ietf/rfc4006.py#L32)|SubscriptionIdTypeAVP
|3|`Subscription-Id`|443|Grouped|IETF RFC 4006|8.46|[avps.ietf.rfc4006](../bromelia/avps/ietf/rfc4006.py#L55)|SubscriptionIdAVP
|4|`EAP-Payload`|462|OctetString|IETF RFC 4072|4.1.1|[avps.ietf.rfc4072](../bromelia/avps/ietf/rfc4072.py#L20)|EapPayloadAVP
|5|`EAP-Master-Session-Key`|464|OctetString|IETF RFC 4072|4.1.3|[avps.ietf.rfc4072](../bromelia/avps/ietf/rfc4072.py#L51)|EapMasterSessionKeyAVP
|6|`MIP-Home-Agent-Host`|348|Grouped|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.43|[avps.ietf.rfc5447](../bromelia/avps/ietf/rfc5447.py#L19)|MipHomeAgentHostAVP
|7|`MIP6-Agent-Info`|486|Grouped|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.45|[avps.ietf.rfc5447](../bromelia/avps/ietf/rfc5447.py#L40)|Mip6AgentInfoAVP
|8|`User-Name`|1|UTF8String|IETF RFC 6733|8.14|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L23)|UserNameAVP
|9|`Class`|25|OctetString|IETF RFC 6733|8.20|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L37)|ClassAVP
|10|`Session-Timeout`|27|Unsigned32|IETF RFC 6733|8.13|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L52)|SessionTimeoutAVP
|11|`Proxy-State`|33|OctetString|IETF RFC 6733|6.7.4|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L66)|ProxyStateAVP
|12|`Acct-Session-Id`|44|OctetString|IETF RFC 6733|9.8.4|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L80)|AcctSessionIdAVP
|13|`Acct-Multi-Session-Id`|50|UTF8String|IETF RFC 6733|9.8.5|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L95)|AcctMultiSessionIdAVP
|14|`Event-Timestamp`|55|Time|IETF RFC 6733|8.21|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L118)|EventTimestampAVP
|15|`Acct-Interim-Interval`|85|Unsigned32|IETF RFC 6733|9.8.2|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L132)|AcctInterimIntervalAVP
|16|`Host-IP-Address`|257|Address|IETF RFC 6733|5.3.5|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L147)|HostIpAddressAVP
|17|`Auth-Application-Id`|258|Unsigned32|IETF RFC 6733|6.8|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L161)|AuthApplicationIdAVP
|18|`Acct-Application-Id`|259|Unsigned32|IETF RFC 6733|6.9|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L176)|AcctApplicationIdAVP
|19|`Vendor-Id`|266|Unsigned32|IETF RFC 6733|5.3.3|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L191)|VendorIdAVP
|20|`Vendor-Specific-Application-Id`|260|Grouped|IETF RFC 6733|6.11|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L205)|VendorSpecificApplicationIdAVP
|21|`Redirect-Host-Usage`|261|Enumerated|IETF RFC 6733|6.13|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L228)|RedirectHostUsageAVP
|22|`Redirect-Max-Cache-Time`|262|Unsigned32|IETF RFC 6733|6.14|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L253)|RedirectMaxCacheTimeAVP
|23|`Session-Id`|263|UTF8String|IETF RFC 6733|8.8|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L268)|SessionIdAVP
|24|`Origin-Host`|264|DiameterIdentity|IETF RFC 6733|6.3|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L303)|OriginHostAVP
|25|`Supported-Vendor-Id`|265|Unsigned32|IETF RFC 6733|5.3.6|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L317)|SupportedVendorIdAVP
|26|`Firmware-Revision`|267|Unsigned32|IETF RFC 6733|5.3.4|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L332)|FirmwareRevisionAVP
|27|`Result-Code`|268|Unsigned32|IETF RFC 6733|7.1|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L346)|ResultCodeAVP
|28|`Product-Name`|269|UTF8String|IETF RFC 6733|5.3.7|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L396)|ProductNameAVP
|29|`Session-Binding`|270|Unsigned32|IETF RFC 6733|8.17|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L409)|SessionBindingAVP
|30|`Session-Server-Failover`|271|Enumerated|IETF RFC 6733|8.18|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L423)|SessionServerFailoverAVP
|31|`Multi-Round-Time-Out`|272|Unsigned32|IETF RFC 6733|8.19|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L445)|MultiRoundTimeOutAVP
|32|`Disconnect-Cause`|273|Enumerated|IETF RFC 6733|5.4.3|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L460)|DisconnectCauseAVP
|33|`Auth-Request-Type`|274|Enumerated|IETF RFC 6733|8.7|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L481)|AuthRequestTypeAVP
|34|`Auth-Grace-Period`|276|Unsigned32|IETF RFC 6733|8.10|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L501)|AuthGracePeriodAVP
|35|`Auth-Session-State`|277|Enumerated|IETF RFC 6733|8.11|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L516)|AuthSessionStateAVP
|36|`Origin-State-Id`|278|Unsigned32|IETF RFC 6733|8.16|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L536)|OriginStateIdAVP
|37|`Failed-AVP`|279|Grouped|IETF RFC 6733|7.5|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L550)|FailedAvpAVP
|38|`Proxy-Host`|280|DiameterIdentity|IETF RFC 6733|6.7.3|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L567)|ProxyHostAVP
|39|`Error-Message`|281|UTF8String|IETF RFC 6733|7.3|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L581)|ErrorMessageAVP
|40|`Route-Record`|282|DiameterIdentity|IETF RFC 6733|6.7.1|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L594)|RouteRecordAVP
|41|`Destination-Realm`|283|DiameterIdentity|IETF RFC 6733|6.6|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L608)|DestinationRealmAVP
|42|`Proxy-Info`|284|Grouped|IETF RFC 6733|6.7.2|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L622)|ProxyInfoAVP
|43|`Re-Auth-Request-Type`|285|Enumerated|IETF RFC 6733|8.12|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L642)|ReAuthRequestTypeAVP
|44|`Accounting-Sub-Session-Id`|287|Unsigned64|IETF RFC 6733|9.8.6|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L662)|AccountingSubSessionIdAVP
|45|`Authorization-Lifetime`|291|Unsigned32|IETF RFC 6733|8.9|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L677)|AuthorizationLifetimeAVP
|46|`Redirect-Host`|292|DiameterURI|IETF RFC 6733|6.12|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L692)|RedirectHostAVP
|47|`Destination-Host`|293|DiameterIdentity|IETF RFC 6733|6.5|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L706)|DestinationHostAVP
|48|`Error-Reporting-Host`|294|DiameterIdentity|IETF RFC 6733|7.4|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L720)|ErrorReportingHostAVP
|49|`Termination-Cause`|295|Enumerated|IETF RFC 6733|8.47|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L734)|TerminationCauseAVP
|50|`Origin-Realm`|296|DiameterIdentity|IETF RFC 6733|6.4|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L760)|OriginRealmAVP
|51|`Experimental-Result-Code`|298|Unsigned32|IETF RFC 6733|7.7|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L774)|ExperimentalResultCodeAVP
|52|`Experimental-Result`|297|Grouped|IETF RFC 6733|7.6|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L789)|ExperimentalResultAVP
|53|`Inband-Security-Id`|299|Unsigned32|IETF RFC 6733|6.10|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L809)|InbandSecurityIdAVP
|54|`Accounting-Record-Type`|480|Enumerated|IETF RFC 6733|9.8.1|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L823)|AccountingRecordTypeAVP
|55|`Accounting-Realtime-Required`|483|Enumerated|IETF RFC 6733|9.8.7|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L845)|AccountingRealtimeRequiredAVP
|56|`Accounting-Record-Number`|485|Unsigned32|IETF RFC 6733|9.8.3|[avps.ietf.rfc6733](../bromelia/avps/ietf/rfc6733.py#L866)|AccountingRecordNumberAVP
|57|`Framed-IP-Address`|8|Address|IETF RFC 7155|4.4.10.5.1|[avps.ietf.rfc7155](../bromelia/avps/ietf/rfc7155.py#L17)|FramedIpAddressAVP
|58|`Called-Station-Id`|30|UTF8String|IETF RFC 7155|4.2.5|[avps.ietf.rfc7155](../bromelia/avps/ietf/rfc7155.py#L47)|CalledStationIdAVP
|59|`Framed-IPv6-Prefix`|97|OctetString|IETF RFC 7155|4.4.10.5.6|[avps.ietf.rfc7155](../bromelia/avps/ietf/rfc7155.py#L62)|FramedIpv6PrefixAVP
|60|`Calling-Station-Id`|31|UTF8String|IETF RFC 7155|4.2.6|[avps.ietf.rfc7155](../bromelia/avps/ietf/rfc7155.py#L77)|CallingStationIdAVP
|61|`CC-Request-Number`|415|Unsigned32|IETF RFC 8506|8.2|[avps.ietf.rfc8506](../bromelia/avps/ietf/rfc8506.py#L17)|CcRequestNumberAVP
|62|`CC-Request-Type`|416|Enumerated|IETF RFC 8506|8.3|[avps.ietf.rfc8506](../bromelia/avps/ietf/rfc8506.py#L34)|CcRequestTypeAVP
|63|`Rating-Group`|432|Unsigned32|IETF RFC 8506|8.29|[avps.ietf.rfc8506](../bromelia/avps/ietf/rfc8506.py#L58)|RatingGroupAVP
|64|`Service-Identifier`|439|Unsigned32|IETF RFC 8506|8.28|[avps.ietf.rfc8506](../bromelia/avps/ietf/rfc8506.py#L75)|ServiceIdentifierAVP
|65|`User-Equipment-Info`|458|Grouped|IETF RFC 8506|8.49|[avps.ietf.rfc8506](../bromelia/avps/ietf/rfc8506.py#L92)|UserEquipmentInfoAVP
|66|`User-Equipment-Info-Type`|459|Enumerated|IETF RFC 8506|8.50|[avps.ietf.rfc8506](../bromelia/avps/ietf/rfc8506.py#L109)|UserEquipmentInfoTypeAVP
|67|`User-Equipment-Info-Value`|460|OctetString|IETF RFC 8506|8.51|[avps.ietf.rfc8506](../bromelia/avps/ietf/rfc8506.py#L133)|UserEquipmentInfoValueAVP
|68|`3GPP-Charging-Characteristics`|13|UTF8String|ETSI TS 129 061 V10.11.0 (2014-10)|16.4.7.2|[avps.etsi_3gpp.ts_129_061](../bromelia/avps/etsi_3gpp/ts_129_061.py#L17)|X3gppChargingCharacteristicsAVP
|69|`Priority-Level`|1406|Unsigned32|ETSI TS 129 212 V12.6.0 (2014-10)|5.3.45|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L17)|PriorityLevelAVP
|70|`Pre-emption-Capability`|1047|Enumerated|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.46|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L34)|PreEmptionCapabilityAVP
|71|`Pre-emption-Vulnerability`|1048|Enumerated|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.47|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L57)|PreEmptionVulnerabilityAVP
|72|`QoS-Class-Identifier`|1028|Enumerated|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.17|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L80)|QosClassIdentifierAVP
|73|`RAT-Type`|1032|Enumerated|3GPP TS 29.212|5.3.31|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L120)|RatTypeAVP
|74|`UE-Local-IP-Address AVP`|2805|Address|ETSI TS 129 212 V15.9.0 (2020-01)|5.3.5|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L151)|UeLocalIpAddressAVP
|75|`Precedence`|1010|Unsigned32|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.11|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L168)|PrecedenceAVP
|76|`Reporting-Level`|1011|Enumerated|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.12|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L186)|ReportingLevelAVP
|77|`IP-CAN-Type`|1027|Enumerated|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.27|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L210)|IpCanTypeAVP
|78|`AN-GW-Address`|1050|Address|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.49|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L241)|AnGwAddressAVP
|79|`Charging-Correlation-Indicator`|1073|Enumerated|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.67|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L258)|ChargingCorrelationIndicatorAVP
|80|`Bearer-Usage`|1000|Enumerated|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.1|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L279)|BearerUsageAVP
|81|`Charging-Rule-Install`|1001|Grouped|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.2|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L302)|ChargingRuleInstallAVP
|82|`Charging-Rule-Definition`|1003|Grouped|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.4|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L320)|ChargingRuleDefinitionAVP
|83|`Charging-Rule-Name`|1005|OctetString|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.6|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L338)|ChargingRuleNameAVP
|84|`Event-Trigger`|1006|Enumerated|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.7|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L356)|EventTriggerAVP
|85|`Metering-Method`|1007|Enumerated|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.8|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L426)|MeteringMethodAVP
|86|`Offline`|1008|Enumerated|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.9|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L451)|OfflineAVP
|87|`Online`|1009|Enumerated|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.10|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L474)|OnlineAVP
|88|`QoS-Information`|1016|Grouped|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.16|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L497)|QosInformationAVP
|89|`Charging-Rule-Report`|1018|Grouped|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.18|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L515)|ChargingRuleReportAVP
|90|`PCC-Rule-Status`|1019|Enumerated|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.19|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L533)|PccRuleStatusAVP
|91|`Access-Network-Charging-Identifier-Gx`|1022|Grouped|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.22|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L557)|AccessNetworkChargingIdentifierGxAVP
|92|`Network-Request-Support`|1024|Enumerated|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.24|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L576)|NetworkRequestSupportAVP
|93|`Guaranteed-Bitrate-DL`|1025|Unsigned32|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.25|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L599)|GuaranteedBitrateDlAVP
|94|`Guaranteed-Bitrate-UL`|1026|Unsigned32|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.26|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L617)|GuaranteedBitrateUlAVP
|95|`Rule-Failure-Code`|1031|Enumerated|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.38|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L635)|RuleFailureCodeAVP
|96|`APN-Aggregate-Max-Bitrate-DL`|1040|Unsigned32|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.39|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L682)|ApnAggregateMaxBitrateDlAVP
|97|`APN-Aggregate-Max-Bitrate-UL`|1041|Unsigned32|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.40|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L699)|ApnAggregateMaxBitrateUlAVP
|98|`Default-EPS-Bearer-QoS`|1049|Grouped|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.48|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L716)|DefaultEpsBearerQosAVP
|99|`Flow-Information`|1058|Grouped|ETSI TS 129 212 V15.3.0 (2018-07)|5.3.53|[avps.etsi_3gpp.ts_129_212](../bromelia/avps/etsi_3gpp/ts_129_212.py#L733)|FlowInformationAVP
|100|`Max-Requested-Bandwidth-DL`|515|Unsigned32|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.14|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L17)|MaxRequestedBandwidthDlAVP
|101|`Max-Requested-Bandwidth-UL`|516|Unsigned32|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.15|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L35)|MaxRequestedBandwidthUlAVP
|102|`Abort-Cause`|500|Enumerated|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.1|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L53)|AbortCauseAVP
|103|`AF-Application-identifier`|504|OctetString|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.5|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L79)|AfApplicationIdentifierAVP
|104|`AF-Charging-identifier`|505|OctetString|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.6|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L97)|AfChargingIdentifierAVP
|105|`Flow-Description`|507|IPFilterRule|ETSI TS 129 214 V15.4.0 (2018-07)|5.38|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L115)|FlowDescriptionAVP
|106|`Flow-Number`|509|Unsigned32|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.9|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L133)|FlowNumberAVP
|107|`Flow-Status`|511|Enumerated|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.11|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L151)|FlowStatusAVP
|108|`Flow-Usage`|512|Enumerated|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.12|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L177)|FlowUsageAVP
|109|`Specific-Action`|513|Enumerated|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.13|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L201)|SpecificActionAVP
|110|`Media-Component-Description`|517|Grouped|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.16|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L237)|MediaComponentDescriptionAVP
|111|`Media-Component-Number`|518|Unsigned32|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.17|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L255)|MediaComponentNumberAVP
|112|`Media-Sub-Component`|519|Grouped|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.18|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L273)|MediaSubComponentAVP
|113|`Media-Type`|520|Enumerated|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.19|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L291)|MediaTypeAVP
|114|`Service-Info-Status`|527|Enumerated|ETSI TS 129 214 V15.4.0 (2018-07)|5.3.25|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L320)|ServiceInfoStatusAVP
|115|`Access-Network-Charging-Address`|501|Address|ETSI 3GPP TS 29.214 V8.14.0 (2012-12)|5.3.2|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L343)|AccessNetworkChargingAddressAVP
|116|`Access-Network-Charging-Identifier-Value`|503|OctetString|ETSI 3GPP TS 29.214 V8.14.0 (2012-12)|5.3.4|[avps.etsi_3gpp.ts_129_214](../bromelia/avps/etsi_3gpp/ts_129_214.py#L361)|AccessNetworkChargingIdentifierValueAVP
|117|`Feature-List-ID`|629|Unsigned32|ETSI TS 129 229 V14.3.0 (2019-10)|6.3.30|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L19)|FeatureListIdAVP
|118|`Feature-List`|630|Unsigned32|ETSI TS 129 229 V14.3.0 (2019-10)|6.3.31|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L36)|FeatureListAVP
|119|`Supported-Features`|628|Grouped|ETSI TS 129 229 V14.3.0 (2019-10)|6.3.29|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L53)|SupportedFeaturesAVP
|120|`Visited-Network-Identifier`|600|OctetString|ETSI TS 129 229 V15.2.0 (2019-10)|6.3.1|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L77)|VisitedNetworkIdentifierAVP
|121|`SIP-Number-Auth-Items`|607|Unsigned32|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.8|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L95)|SipNumberAuthItemsAVP
|122|`Authentication-Scheme`|608|UTF8String|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.9|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L113)|SipAuthenticationSchemeAVP
|123|`SIP-Authenticate`|609|OctetString|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.10|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L131)|SipAuthenticateAVP
|124|`SIP-Authorization`|610|OctetString|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.11|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L149)|SipAuthorizationAVP
|125|`Confidentiality-Key`|625|OctetString|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.27|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L167)|ConfidentialityKeyAVP
|126|`Integrity-Key`|626|OctetString|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.28|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L185)|IntegrityKeyAVP
|127|`SIP-Auth-Data-Item`|612|Grouped|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.13|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L203)|SipAuthDataItemAVP
|128|`Server-Assignment-Type`|614|Enumerated|ETSI TS 129 229 V16.2.0 (2020-11)|6.3.15|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L236)|ServerAssignmentTypeAVP
|129|`Reason-Code`|616|Enumerated|ETSI TS 129 229 V11.3.0 (2013-04)|6.3.17|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L272)|ReasonCodeAVP
|130|`Reason-Info`|617|UTF8String|ETSI TS 129 229 V11.3.0 (2013-04)|6.3.18|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L297)|ReasonInfoAVP
|131|`Deregistration-Reason`|615|Grouped|ETSI TS 129 229 V11.3.0 (2013-04)|6.3.16|[avps.etsi_3gpp.ts_129_229](../bromelia/avps/etsi_3gpp/ts_129_229.py#L315)|DeregistrationReasonAVP
|132|`STN-SR`|1433|OctetString|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.39|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L35)|StnSrAVP
|133|`AMBR`|1435|Grouped|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.41|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L68)|AmbrAVP
|134|`Subscriber-Status`|1424|Enumerated|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.29|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L95)|SubscriberStatusAVP
|135|`Context-Identifier`|1423|Unsigned32|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.27|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L118)|ContextIdentifierAVP
|136|`PDN-Type`|1456|Enumerated|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.62|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L135)|PdnTypeAVP
|137|`Service-Selection`|493|UTF8String|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.36|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L159)|ServiceSelectionAVP
|138|`Allocation-Retention-Priority`|1034|Grouped|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.40|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L176)|AllocationRetentionPriorityAVP
|139|`EPS-Subscribed-QoS-Profile`|1431|Grouped|ETSI TS 129 272 V15.10.0 (2020-01) |7.3.37|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L202)|EpsSubscribedQosProfileAVP
|140|`VPLMN-Dynamic-Address-Allowed`|1432|Enumerated|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.38|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L226)|VplmnDynamicAddressAllowedAVP
|141|`PDN-GW-Allocation-Type`|1438|Enumerated|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.44|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L251)|PdnGwAllocationTypeAVP
|142|`APN-Configuration`|1430|Grouped|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.35|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L274)|ApnConfigurationAVP
|143|`All-APN-Configurations-Included-Indicator`|1428|Enumerated|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.33|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L322)|AllApnConfigurationsIncludedIndicatorAVP
|144|`APN-Configuration-Profile`|1429|Grouped|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.34|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L346)|ApnConfigurationProfileAVP
|145|`UE-Usage-Type`|1680|Unsigned32|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.202|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L373)|UeUsageTypeAVP
|146|`Operator-Determined-Barring`|1425|Unsigned32|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.30|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L390)|OperatorDeterminedBarringAVP
|147|`Subscription-Data`|1400|Grouped|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.2|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L408)|SubscriptionDataAVP
|148|`IMEI`|1402|UTF8String|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.4|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L470)|ImeiAVP
|149|`Number-Of-Requested-Vectors`|1410|Unsigned32|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.14|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L488)|NumberOfRequestedVectorsAVP
|150|`Re-Synchronization-Info`|1411|OctetString|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.15|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L506)|ReSynchronizationInfoAVP
|151|`Immediate-Response-Preferred`|1412|Unsigned32|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.16|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L524)|ImmediateResponsePreferredAVP
|152|`Requested-EUTRAN-Authentication-Info`|1408|Grouped|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.11|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L542)|RequestedEutranAuthenticationInfoAVP
|153|`Software-Version`|1403|UTF8String|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.5|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L568)|SoftwareVersionAVP
|154|`Terminal-Information`|1401|Grouped|ETSI TS 129 272 V15.10.0 (2020-01)|5.3.14|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L586)|TerminalInformationAVP
|155|`Equipment-Status`|1445|Enumerated|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.51|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L611)|EquipmentStatusAVP
|156|`ULR-Flags`|1405|Unsigned32|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.7|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L635)|UlrFlagsAVP
|157|`ULA-Flags`|1406|Unsigned32|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.8|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L653)|UlaFlagsAVP
|158|`AIR-Flags`|1679|Unsigned32|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.201|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L671)|AirFlagsAVP
|159|`NOR-Flags`|1443|Unsigned32|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.49|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L688)|NorFlagsAVP
|160|`PUR-Flags`|1635|Unsigned32|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.149|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L706)|PurFlagsAVP
|161|`PUA-Flags`|1442|Unsigned32|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.49|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L723)|PuaFlagsAVP
|162|`Alert-Reason`|1434|Enumerated|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.83|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L741)|AlertReasonAVP
|163|`Error-Diagnostic`|1614|Enumerated|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.128|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L763)|ErrorDiagnosticAVP
|164|`Visited-PLMN-Id`|1407|OctetString|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.9|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L788)|VisitedPlmnIdAVP
|165|`Item-Number`|1419|Unsigned32|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.23|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L806)|ItemNumberAVP
|166|`RAND`|1447|OctetString|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.53|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L824)|RandAVP
|167|`XRES`|1448|OctetString|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.54|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L842)|XresAVP
|168|`AUTN`|1449|OctetString|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.55|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L860)|AutnAVP
|169|`KASME`|1450|OctetString|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.56|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L878)|KasmeAVP
|170|`E-UTRAN-Vector`|1414|Grouped|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.18|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L896)|EUtranVectorAVP
|171|`Authentication-Info`|1413|Grouped|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.17|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L923)|AuthenticationInfoAVP
|172|`Homogeneous-Support-of-IMS-Voice-Over-PS-Sessions`|1493|Enumerated|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.107|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L948)|HomogeneousSupportOfImsVoiceOverPsSessionsAVP
|173|`UE-SRVCC-Capability`|1615|Enumerated|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.130|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L971)|UeSrvccCapabilityAVP
|174|`Supported-Services`|3143|Grouped|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.199|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L993)|SupportedServicesAVP
|175|`Supported-Monitoring-Events`|3144|Unsigned64|ETSI TS 129 272 V15.10.0 (2020-01)|7.3.200|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L1010)|SupportedMonitoringEventsAVP
|176|`Cancellation-Type`|1420|Enumerated|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.24|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L1027)|CancellationTypeAVP
|177|`CLR-Flags`|1638|Unsigned32|ETSI TS 129 272 V15.4.0 (2018-07)|7.3.152|[avps.etsi_3gpp.ts_129_272](../bromelia/avps/etsi_3gpp/ts_129_272.py#L1053)|ClrFlagsAVP
|178|`Mobile-Node-Identifier`|506|UTF8String|ETSI TS 129 273 V15.4.0 (2019-10)|5.2.3.2|[avps.etsi_3gpp.ts_129_273](../bromelia/avps/etsi_3gpp/ts_129_273.py#L26)|MobileNodeIdentifierAVP
|179|`Non-3GPP-IP-Access`|1501|Enumerated|ETSI TS 129 273 V14.5.0 (2019-10)|8.2.3.3|[avps.etsi_3gpp.ts_129_273](../bromelia/avps/etsi_3gpp/ts_129_273.py#L43)|Non3gppIpAccessAVP
|180|`MIP6-Feature-Vector`|124|Unsigned64|ETSI TS 129 273 V14.3.0 (2017-07)|9.2.3.2.3|[avps.etsi_3gpp.ts_129_273](../bromelia/avps/etsi_3gpp/ts_129_273.py#L66)|Mip6FeatureVectorAVP
|181|`Non-3GPP-Ip-Access-APN`|1502|Enumerated|ETSI TS 129 273 V14.3.0 (2017-07)|8.2.3.4|[avps.etsi_3gpp.ts_129_273](../bromelia/avps/etsi_3gpp/ts_129_273.py#L81)|Non3gppIpAccessApnAVP
|182|`Non-3GPP-User-Data`|1500|Grouped|ETSI TS 129 273 V14.3.0 (2017-07)|8.2.3.1|[avps.etsi_3gpp.ts_129_273](../bromelia/avps/etsi_3gpp/ts_129_273.py#L104)|Non3gppUserDataAVP
|183|`AN-Trusted`|1503|Enumerated|ETSI TS 129 273 V12.5.0 (2014-10)|5.2.3.9|[avps.etsi_3gpp.ts_129_273](../bromelia/avps/etsi_3gpp/ts_129_273.py#L142)|AnTrustedAVP
|184|`MSISDN`|701|OctetString|ETSI TS 129 329 V15.1.0 (2018-07)|6.3.2|[avps.etsi_3gpp.ts_129_329](../bromelia/avps/etsi_3gpp/ts_129_329.py#L18)|MsisdnAVP
|185|`Reservation-Priority`|458|Enumerated|ETSI TS 183 017 V2.3.1 (2008-09)|7.3.9|[avps.etsi_3gpp.ts_183_017](../bromelia/avps/etsi_3gpp/ts_183_017.py#L17)|ReservationPriorityAVP
