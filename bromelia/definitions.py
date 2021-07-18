# -*- coding: utf-8 -*-
"""
    bromelia.definitions
    ~~~~~~~~~~~~~~~~~~~~

    Defines handy dictionaries that are used within the library. It contains
    two dictionaries based on IANA's definitions.

    For more information, please refer to links below:
    https://www.iana.org/assignments/aaa-parameters/aaa-parameters.xhtml
    https://www.iana.org/assignments/radius-types/radius-types.xhtml

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

diameter_command_codes = [
                            {
                                "id": 257,
                                "long_name": "CER / CEA",
                                "ref": "[RFC6733]",
                                "short_name": "CER/CEA"

                            },
                            {
                                "id": 258,
                                "long_name": "RAR / RAA",
                                "ref": "[RFC6733]",
                                "short_name": "RAR/RAA"

                            },
                            {
                                "id": 260,
                                "long_name": "AMR / AMA",
                                "ref": "[RFC4004]",
                                "short_name": "AMR/AMA"
                            },
                            {
                                "id": 261,
                                "long_name": "Unassigned",
                                "ref": "",
                                "short_name": ""
                            },
                            {
                                "id": 262,
                                "long_name": "HAR / HAA",
                                "ref": "[RFC4004]",
                                "short_name": "HAR/HAA"
                            },
                            {
                                "id": 265,
                                "long_name": "AAR / AAA",
                                "ref": "[RFC7155]",
                                "short_name": "AAR/AAA"
                            },
                            {
                                "id": 268,
                                "long_name": "DER / DEA",
                                "ref": "[RFC4072]",
                                "short_name": "DER/DEA"
                            },
                            {
                                "id": 271,
                                "long_name": "ACR / ACA",
                                "ref": "[RFC6733]",
                                "short_name": "ACR/ACA"
                            },
                            {
                                "id": 272,
                                "long_name": "CCR / CCA",
                                "ref": "[RFC8506]",
                                "short_name": "CCR/CCA"
                            },
                            {
                                "id": 273,
                                "long_name": "Unassigned",
                                "ref": "",
                                "short_name": ""
                            },
                            {
                                "id": 274,
                                "long_name": "ASR / ASA",
                                "ref": "[RFC6733]",
                                "short_name": "ASR/ASA"
                            },
                            {
                                "id": 275,
                                "long_name": "STR / STA",
                                "ref": "[RFC6733]",
                                "short_name": "STR/STA"
                            },
                            {
                                "id": 280,
                                "long_name": "DWR / DWA",
                                "ref": "[RFC6733]",
                                "short_name": "DWR/DWA"
                            },
                            {
                                "id": 281,
                                "long_name": "Unassigned",
                                "ref": "",
                                "short_name": ""
                            },
                            {
                                "id": 282,
                                "long_name": "DPR / DPA",
                                "ref": "[RFC6733]",
                                "short_name": "DPR/DPA"
                            },
                            {
                                "id": 283,
                                "long_name": "UAR / UAA",
                                "ref": "[RFC4740]",
                                "short_name": "UAR/UAA"
                            },
                            {
                                "id": 284,
                                "long_name": "SAR / SAA",
                                "ref": "[RFC4740]",
                                "short_name": "SAR/SAA"
                            },
                            {
                                "id": 285,
                                "long_name": "LIR / LIA",
                                "ref": "[RFC4740]",
                                "short_name": "LIR/LIA"
                            },
                            {
                                "id": 286,
                                "long_name": "MAR / MAA",
                                "ref": "[RFC4740]",
                                "short_name": "MAR/MAA"
                            },
                            {
                                "id": 287,
                                "long_name": "RTR / RTA",
                                "ref": "[RFC4740]",
                                "short_name": "RTR/RTA"
                            },
                            {
                                "id": 288,
                                "long_name": "PPR / PPA",
                                "ref": "[RFC4740]",
                                "short_name": "PPR/PPA"
                            },
                            {
                                "id": 314,
                                "long_name": "PDR / PDA",
                                "ref": "[RFC5224]",
                                "short_name": "PDR/PDA"
                            },
                            {
                                "id": 315,
                                "long_name": "Policy-Install-Request (PIR)/Policy-Install-Answer (PIA)",
                                "ref": "[ITU-T Rec. Q.3303.3][RFC5431]",
                                "short_name": ""
                            },
                            {
                                "id": 316,
                                "long_name": "3GPP-Update-Location-Request/Answer (ULR/ULA)",
                                "ref": "[3GPP TS 29.272][RFC5516]",
                                "short_name": "ULR/ULA"
                            },
                            {
                                "id": 317,
                                "long_name": "3GPP-Cancel-Location-Request/Answer (CLR/CLA)",
                                "ref": "[3GPP TS 29.272][RFC5516]",
                                "short_name": "CLR/CLA"
                            },
                            {
                                "id": 318,
                                "long_name": "3GPP-Authentication-Information-Request/Answer (AIR/AIA)",
                                "ref": "[3GPP TS 29.272][RFC5516]",
                                "short_name": "AIR/AIA"
                            },
                            {
                                "id": 319,
                                "long_name": "3GPP-Insert-Subscriber-Data-Request/Answer (IDR/IDA)",
                                "ref": "[3GPP TS 29.272][RFC5516]",
                                "short_name": "IDR/IDA"
                            },
                            {
                                "id": 320,
                                "long_name": "3GPP-Delete-Subscriber-Data-Request/Answer (DSR/DSA)",
                                "ref": "[3GPP TS 29.272][RFC5516]",
                                "short_name": "DSR/DSA"
                            },
                            {
                                "id": 321,
                                "long_name": "3GPP-Purge-UE-Request/Answer (PUR/PUA)",
                                "ref": "[3GPP TS 29.272][RFC5516]",
                                "short_name": "PUR/PUA"
                            },
                            {
                                "id": 322,
                                "long_name": "3GPP-Reset-Request/Answer (RSR/RSA)",
                                "ref": "[3GPP TS 29.272][RFC5516]",
                                "short_name": "RSR/RSA"
                            },
                            {
                                "id": 323,
                                "long_name": "3GPP-Notify-Request/Answer (NOR/NOA)",
                                "ref": "[3GPP TS 29.272][RFC5516]",
                                "short_name": "NOR/NOA"
                            },
                            {
                                "id": 324,
                                "long_name": "3GPP-ME-Identity-Check-Request/Answer (ECR/ECA)",
                                "ref": "[3GPP TS 29.272][RFC5516]",
                                "short_name": "ECR/ECA"
                            },
                            {
                                "id": 325,
                                "long_name": "MIP6-Request/Answer (MIR/MIA)",
                                "ref": "[RFC5778]",
                                "short_name": "MIR/MIA"
                            },
                            {
                                "id": 326,
                                "long_name": "QoS-Authorization-Request/QoS-Authorization-Answer (QAR/QAA)",
                                "ref": "[RFC5866]",
                                "short_name": "QAR/QAA"
                            },
                            {
                                "id": 327,
                                "long_name": "QoS-Install-Request/QoS-Install-Answer (QIR/QIA)",
                                "ref": "[RFC5866]",
                                "short_name": "QIR/QIA"
                            },
                            {
                                "id": 328,
                                "long_name": "Capabilities-Update-Request/Capabilities-Update-Answer (CUR/CUA)",
                                "ref": "[RFC6737]",
                                "short_name": "CUR/CUA"
                            },
                            {
                                "id": 329,
                                "long_name": "IKEv2-SK-Request/Answer (ISR/ISA)",
                                "ref": "[RFC6738]",
                                "short_name": "ISR/ISA"
                            },
                            {
                                "id": 330,
                                "long_name": "NAT-Control-Request/Answer (NCR/NCA)",
                                "ref": "[RFC6736]",
                                "short_name": "NCR/NCA"
                            },
                            {
                                "id": 8388608,
                                "long_name": "WIMAX-HRPD-SFF Request/Answer",
                                "ref": "[3GPP2 X.S0058-0 v1.0][Avi_Lior]",
                                "short_name": ""
                            },
                            {
                                "id": 8388609,
                                "long_name": "WiMAX-Diameter-EAP-Request/Answer (WDER/WDEA) WDE",
                                "ref": "[WiMAX Release 1.5][Avi_Lior]",
                                "short_name": ""
                            },
                            {
                                "id": 8388610,
                                "long_name": "WiMAX-Change-of-Authorization-Request/Answer (WCAR/WCAA) WCA",
                                "ref": "[WiMAX Release 1.5][Avi_Lior]",
                                "short_name": ""
                            },
                            {
                                "id": 8388611,
                                "long_name": "WiMAX-Reauthentication-Request/Answer (WRAR/WRAA) WRA",
                                "ref": "[WiMAX Release 1.5][Avi_Lior]",
                                "short_name": ""
                            },
                            {
                                "id": 8388612,
                                "long_name": "WiMAX-Session-Termination-Request/Answer (WSTR/WSTA) WST",
                                "ref": "[WiMAX Release 1.5][Avi_Lior]",
                                "short_name": ""
                            },
                            {
                                "id": 8388613,
                                "long_name": "WiMAX-Abort-Session-Request/Answer (WASR/WASA) WAS",
                                "ref": "[WiMAX Release 1.5][Avi_Lior]",
                                "short_name": ""
                            },
                            {
                                "id": 8388614,
                                "long_name": "WiMAX-Home-Agent-IPv4-Request/Answer (WHA4R/WHA4A) WHA4",
                                "ref": "[WiMAX Release 1.5][Avi_Lior]",
                                "short_name": ""
                            },
                            {
                                "id": 8388615,
                                "long_name": "WiMAX-Home-Agent-IPv6-Request/Answer (WHA6R/WHA6A) WHA6",
                                "ref": "[WiMAX Release 1.5][Avi_Lior]",
                                "short_name": ""
                            },
                            {
                                "id": 8388616,
                                "long_name": "WiMAX-DHCP-Request/Answer (WDHCPR/WDHCPA) WDHCP",
                                "ref": "[WiMAX Release 1.5][Avi_Lior]",
                                "short_name": ""
                            },
                            {
                                "id": 8388617,
                                "long_name": "WiMAX-LAA-Request/Answer (WLAAR/WLAA) WLAA",
                                "ref": "[WiMAX Release 1.5][Avi_Lior]",
                                "short_name": ""
                            },
                            {
                                "id": 8388618,
                                "long_name": "WiMAX-Location-Accounting-Request/Answer (WLACR/WLACA) WLAC",
                                "ref": "[WiMAX Release 1.5][Avi_Lior]",
                                "short_name": ""
                            },
                            {
                                "id": 8388619,
                                "long_name": "WiMAX-Location-Measurement-Query-Request/Answer (WLMQR/WLMQA) WLMQ",
                                "ref": "[WiMAX Release 1.5][Avi_Lior]",
                                "short_name": ""
                            },
                            {
                                "id": 8388620,
                                "long_name": "3GPP-Provide-Location-Request/Answer (PLR/PLA)",
                                "ref": "[3GPP TS 29.172][Kimmo_Kymalainen]",
                                "short_name": "PLR/PLA"
                            },
                            {
                                "id": 8388621,
                                "long_name": "3GPP-Location-Report-Request/Answer (LRR/LRA)",
                                "ref": "[3GPP TS 29.172][Kimmo_Kymalainen]",
                                "short_name": "LRR/LRA"
                            },
                            {
                                "id": 8388622,
                                "long_name": "3GPP-LCS-Routing-Info-Request/Answer (RIR/RIA)",
                                "ref": "[3GPP TS 29.173][Kimmo_Kymalainen]",
                                "short_name": "RIR/RIA"
                            },
                            {
                                "id": 8388623,
                                "long_name": "Notif-Request/Answer (NFR/NFA)",
                                "ref": "[Tomas_Menzl]",
                                "short_name": "NFR/NFA"
                            },
                            {
                                "id": 8388624,
                                "long_name": "Msg-Interface-Request/Answer (MIFR/MIFA)",
                                "ref": "[Tomas_Menzl]",
                                "short_name": ""
                            },
                            {
                                "id": 8388625,
                                "long_name": "Mobile-Application-Request/Answer (MAPR/MAPA)",
                                "ref": "[Tomas_Menzl]",
                                "short_name": ""
                            },
                            {
                                "id": 8388626,
                                "long_name": "Update Location Request/Answer (ULR / ULA)",
                                "ref": "[3GPP2 publication X.S0057][Avi_Lior]",
                                "short_name": "ULR/ULA"
                            },
                            {
                                "id": 8388627,
                                "long_name": "Cancel Location Request/Answer (CLR CLA)",
                                "ref": "[3GPP2 publication X.S0057][Avi_Lior]",
                                "short_name": ""
                            },
                            {
                                "id": 8388628,
                                "long_name": "Juniper-Sync-Event (JSE)",
                                "ref": "[Aleksey_Romanov]",
                                "short_name": ""
                            },
                            {
                                "id": 8388629,
                                "long_name": "Juniper-Session-Discovery (JSD)",
                                "ref": "[Aleksey_Romanov]",
                                "short_name": ""
                            },
                            {
                                "id": 8388630,
                                "long_name": "Query Profile Request Answer (QPR/QPA)",
                                "ref": "[3GPP2 publication X.S0057A E-UTRAN eHRPD7][Avi_Lior]",
                                "short_name": "QPR/QPA"
                            },
                            {
                                "id": 8388631,
                                "long_name": "Subscription Information Application (SIR/SIA)",
                                "ref": "[Lars_Anglert]",
                                "short_name": "SIR/SIA"
                            },
                            {
                                "id": 8388632,
                                "long_name": "Distributed Charging Request/Diameter Charging Answer (DCR/DCA)",
                                "ref": "[Lars_Anglert]",
                                "short_name": "DCR/DCA"
                            },
                            {
                                "id": 8388633,
                                "long_name": "Ericsson Spending Limit Request/Answer (SLR/SLA)",
                                "ref": "[Lars_Anglert]",
                                "short_name": "SLR/SLA"
                            },
                            {
                                "id": 8388634,
                                "long_name": "Ericsson Spending Status Notification Request/Answer (SNR/SNA)",
                                "ref": "[Lars_Anglert]",
                                "short_name": "SNR/SNA"
                            },
                            {
                                "id": 8388635,
                                "long_name": "Spending-Limit-Request/Answer (SLR/SLA)",
                                "ref": "[3GPP TS 29.219][Kimmo_Kymalainen]",
                                "short_name": "SLR/SLA"
                            },
                            {
                                "id": 8388636,
                                "long_name": "Spending-Status-Notification-Request/Answer (SNR/SNA)",
                                "ref": "[3GPP TS 29.219][Kimmo_Kymalainen]",
                                "short_name": "SNR/SNA"
                            },
                            {
                                "id": 8388637,
                                "long_name": "TDF-Session-Request/Answer (TSR/TSA)",
                                "ref": "[3GPP TS 29.212][Kimmo_Kymalainen]",
                                "short_name": "TSR/TSA"
                            },
                            {
                                "id": 8388638,
                                "long_name": "3GPP-Update-VCSG-Location-Request/Answer (UVR/UVA)",
                                "ref": "[3GPP TS 29.272][Kimmo_Kymalainen]",
                                "short_name": "UVR/UVA"
                            },
                            {
                                "id": 8388639,
                                "long_name": "Device-Action-Request/Answer (DAR/DAA)",
                                "ref": "[3GPP TS 29.368][Kimmo_Kymalainen]",
                                "short_name": "DAR/DAA"
                            },
                            {
                                "id": 8388640,
                                "long_name": "Device-Notification-Request/Answer (DNR/DNA)",
                                "ref": "[3GPP TS 29.368][Kimmo_Kymalainen]",
                                "short_name": "DNR/DNA"
                            },
                            {
                                "id": 8388641,
                                "long_name": "Subscriber-Information-Request/Answer (SIR/SIA)",
                                "ref": "[3GPP TS 29.336][Kimmo_Kymalainen]",
                                "short_name": "SIR/SIA"
                            },
                            {
                                "id": 8388642,
                                "long_name": "Cancel-VCSG-Location-Request/Answer (CVR/CVA)",
                                "ref": "[3GPP TS 29.272][Kimmo_Kymalainen]",
                                "short_name": "CVR/CVA"
                            },
                            {
                                "id": 8388643,
                                "long_name": "Device-Trigger-Request/Answer (DTR/DTA)",
                                "ref": "[3GPP TS 29.337][Kimmo_Kymalainen]",
                                "short_name": "DTR/DTA"
                            },
                            {
                                "id": 8388644,
                                "long_name": "Delivery-Report-Request/Answer (DRR/DRA)",
                                "ref": "[3GPP TS 29.337][Kimmo_Kymalainen]",
                                "short_name": "DRR/DRA"
                            },
                            {
                                "id": 8388645,
                                "long_name": "MO-Forward-Short-Message Request/Answer (OFR/OFA)",
                                "ref": "[3GPP TS 29.338][Kimmo_Kymalainen]",
                                "short_name": "OFR/OFA"
                            },
                            {
                                "id": 8388646,
                                "long_name": "MT-Forward-Short-Message Request/Answer (TFR/TFA)",
                                "ref": "[3GPP TS 29.338][Kimmo_Kymalainen]",
                                "short_name": "TFR/TFA"
                            },
                            {
                                "id": 8388647,
                                "long_name": "Send-Routing-Info-for-SM-Request/Answer (SRR/SRA)",
                                "ref": "[3GPP TS 29.338][Kimmo_Kymalainen]",
                                "short_name": "SRR/SRA"
                            },
                            {
                                "id": 8388648,
                                "long_name": "Alert-Service-Centre-Request/Answer (ALR/ALA)",
                                "ref": "[3GPP TS 29.338][Kimmo_Kymalainen]",
                                "short_name": "ALR/ALA"
                            },
                            {
                                "id": 8388649,
                                "long_name": "Report-SM-Delivery-Status-Request/Answer (RDR/RDA)",
                                "ref": "[3GPP TS 29.338][Kimmo_Kymalainen]",
                                "short_name": "RDR/RDA"
                            },
                            {
                                "id": 8388650,
                                "long_name": "NSN Cancel-LocationMS-Request/Answer (CLR/CLA)",
                                "ref": "[Hannes_Tschofenig]",
                                "short_name": "CLR/CLA"
                            },
                            {
                                "id": 8388651,
                                "long_name": "NSN User-DataMS-Request/Answer (UDR/UDA)",
                                "ref": "[Hannes_Tschofenig]",
                                "short_name": "UDR/UDA"
                            },
                            {
                                "id": 8388652,
                                "long_name": "NSN Profile-UpdateMS-Request/Answer (PUR/PUA)",
                                "ref": "[Hannes_Tschofenig]",
                                "short_name": "PUR/PUA"
                            },
                            {
                                "id": 8388653,
                                "long_name": "NSN Subscribe-NotificationsMS-Request/Answer (SNR/SNA)",
                                "ref": "[Hannes_Tschofenig]",
                                "short_name": "SNR/SNA"
                            },
                            {
                                "id": 8388654,
                                "long_name": "NSN Push-NotificationMS-Request/Answer (PNR/PNA)",
                                "ref": "[Hannes_Tschofenig]",
                                "short_name": "PNR/PNA"
                            },
                            {
                                "id": 8388655,
                                "long_name": "Get Gateway Request/Answer (GGR/GGA)",
                                "ref": "[Steve_Donovan]",
                                "short_name": "GGR/GGA"
                            },
                            {
                                "id": 8388656,
                                "long_name": "Trigger-Establishment-Request/Answer (TER/TEA)",
                                "ref": "[3GPP TS 29.215][Kimmo_Kymalainen]",
                                "short_name": "TER/TEA"
                            },
                            {
                                "id": 8388657,
                                "long_name": "Ericsson Binding-Data-Request/Answer (BDR/BDA)",
                                "ref": "[Klaus_Turina]",
                                "short_name": "BDR/BDA"
                            },
                            {
                                "id": 8388658,
                                "long_name": "3GPP2 Subscriber-Information-Request/Answer (SIR/SIA)",
                                "ref": "[3GPP2 X.S0068][Jun_Wang]",
                                "short_name": "SIR/SIA"
                            },
                            {
                                "id": 8388659,
                                "long_name": "Verizon Session Data Recovery Request/Answer (SDR/SDA)",
                                "ref": "[Niranjan_Avula]",
                                "short_name": "SDR/SDA"
                            },
                            {
                                "id": 8388660,
                                "long_name": "Nokia Core Service Request/Answer (CSR/CSA)",
                                "ref": "[Timo_Perala]",
                                "short_name": "CSR/CSA"
                            },
                            {
                                "id": 8388661,
                                "long_name": "Nokia Extended Command Request/Answer (ECR/ECA)",
                                "ref": "[Timo_Perala]",
                                "short_name": "ECR/ECA"
                            },
                            {
                                "id": 8388662,
                                "long_name": "GCS-Action-Request/Answer (GAR/GAA)",
                                "ref": "[3GPP TS 29.468][Kimmo_Kymalainen]",
                                "short_name": "GAR/GAA"
                            },
                            {
                                "id": 8388663,
                                "long_name": "GCS-Notification-Request/Answer (GNR/GNA)",
                                "ref": "[3GPP TS 29.468][Kimmo_Kymalainen]",
                                "short_name": "GNR/GNA"
                            },
                            {
                                "id": 8388664,
                                "long_name": "ProSe-Subscriber-Information-Request/Answer (PIR/PIA)",
                                "ref": "[3GPP TS 29.344][Kimmo_Kymalainen]",
                                "short_name": "PIR/PIA"
                            },
                            {
                                "id": 8388665,
                                "long_name": "Update-ProSe-Subscriber-Data-Request/Answer (UPR/UPA)",
                                "ref": "[3GPP TS 29.344][Kimmo_Kymalainen]",
                                "short_name": "UPR/UPA"
                            },
                            {
                                "id": 8388666,
                                "long_name": "ProSe-Notify-Request/Answer (PNR/PNA)",
                                "ref": "[3GPP TS 29.344][Kimmo_Kymalainen]",
                                "short_name": "PNR/PNA"
                            },
                            {
                                "id": 8388667,
                                "long_name": "Reset-Request/Answer (RSR/RSA)",
                                "ref": "[3GPP TS 29.344][Kimmo_Kymalainen]",
                                "short_name": "RSR/RSA"
                            },
                            {
                                "id": 8388668,
                                "long_name": "ProSe-Authorization-Request/Answer (PAR/PAA)",
                                "ref": "[3GPP TS 29.345][Kimmo_Kymalainen]",
                                "short_name": "PAR/PAA"
                            },
                            {
                                "id": 8388669,
                                "long_name": "ProSe-Discovery-Request/Answer (PDR/PDA)",
                                "ref": "[3GPP TS 29.345][Kimmo_Kymalainen]",
                                "short_name": "PDR/PDA"
                            },
                            {
                                "id": 8388670,
                                "long_name": "ProSe-Match-Request/Answer (PMR/PMA)",
                                "ref": "[3GPP TS 29.345][Kimmo_Kymalainen]",
                                "short_name": "PMR/PMA"
                            },
                            {
                                "id": 8388671,
                                "long_name": "ProSe-Match-Report-Info-Request/Answer (PIR/PIA)",
                                "ref": "[3GPP TS 29.345][Kimmo_Kymalainen]",
                                "short_name": "PIR/PIA"
                            },
                            {
                                "id": 8388672,
                                "long_name": "ProSe-Proximity-Request/Answer (PRR/PRA)",
                                "ref": "[3GPP TS 29.345][Kimmo_Kymalainen]",
                                "short_name": "PRR/PRA"
                            },
                            {
                                "id": 8388673,
                                "long_name": "ProSe-Location-Update-Request (PLR/PLA)",
                                "ref": "[3GPP TS 29.345][Kimmo_Kymalainen]",
                                "short_name": "PLR/PLA"
                            },
                            {
                                "id": 8388674,
                                "long_name": "ProSe-Alert-Request/Answer (ALR/ALA)",
                                "ref": "[3GPP TS 29.345][Kimmo_Kymalainen]",
                                "short_name": "ALR/ALA"
                            },
                            {
                                "id": 8388675,
                                "long_name": "ProSe-Cancellation-Request/Answer (RPR/RPA)",
                                "ref": "[3GPP TS 29.345][Kimmo_Kymalainen]",
                                "short_name": "RPR/RPA"
                            },
                            {
                                "id": 8388676,
                                "long_name": "ProXimity-Action-Request/Answer (PXR/PXA)",
                                "ref": "[3GPP TS 29.343][Kimmo_Kymalainen]",
                                "short_name": "PXR/PXA"
                            },
                            {
                                "id": 8388677,
                                "long_name": "Rivada Xd DSC-Registration-Request/Answer (DDRR/DDRA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388678,
                                "long_name": "Rivada Xd Heart-Beat-Request/Answer (DHBR/DHBA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388679,
                                "long_name": "Rivada Xd Cell-Info-Transfer-Request/Answer (DCTR/DCTA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388680,
                                "long_name": "Rivada Xd Cell-Info-Notification-Request/Answer (DCNR/DCNA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388681,
                                "long_name": "Rivada Xd Cell-Info-Modification-Request/Answer (DIMR/DIMA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388682,
                                "long_name": "Rivada Xd Cell-Info-Modification-Notification-Request/Answer (DINR/DINA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388683,
                                "long_name": "Rivada Xd Resource-Allocation-Request/Answer (DRAR/DRAA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388684,
                                "long_name": "Rivada Xd Resource-Allocation-Notification-Request/Answer (DANR/DANA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388685,
                                "long_name": "Rivada Xd Resource-Modification-Request/Answer (DRMR/DRMA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388686,
                                "long_name": "Rivada Xd Resource-Modification-Notification-Request/Answer (DMNR/DMNA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388687,
                                "long_name": "Rivada Xd Resource-Hold-Request/Answer (DRHR/DRHA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388688,
                                "long_name": "Rivada Xd Resource-Hold-Notification-Request/Answer (DHNR/DHNA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388689,
                                "long_name": "Rivada Xd Resource-Resume-Request/Answer (DRSR/DRSA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388690,
                                "long_name": "Rivada Xd Resource-Resume-Notification-Request/Answer (DSNR/DSNA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388691,
                                "long_name": "Rivada Xd Resource-Usage-Update-Request/Answer (DRUR/DRUA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388692,
                                "long_name": "Rivada Xd Resource-Usage-Notification-Request/Answer (DUNR/DUNA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388693,
                                "long_name": "Rivada Xd Resource-Release-Request/Answer (DRRR/DRRA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388694,
                                "long_name": "Rivada Xd Resource-Release-Notification-Request/Answer (DRNR/DRNA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388695,
                                "long_name": "Rivada Xm Resource-Allocation-Request/Answer (MRAR/MRAA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388696,
                                "long_name": "Rivada Xm Resource-Hold-Request/Answer (MRHR/MRHA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388697,
                                "long_name": "Rivada Xm Resource-Release-Request/Answer (MRRR/MRRA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388698,
                                "long_name": "Rivada Xm Resource-Modify-Request/Answer (MRMR/MRMA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388699,
                                "long_name": "Rivada Xm Resource-Allocation-Notify-Request/Answer (MANR/MANA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388700,
                                "long_name": "Rivada Xm Resource-Resume-Request/Answer (MRSR/MRSA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388701,
                                "long_name": "Rivada Xm Add-UE-Context-Request/Answer (MAUR/MAUA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388702,
                                "long_name": "Rivada Xm Update-UE-Context-Request/Answer (MUUR/MUUA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388703,
                                "long_name": "Rivada Xm Delete-UE-Context-Request/Answer (MDUR/MDUA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388704,
                                "long_name": "Rivada Xm Detach-UE-Request/Answer (MDTR/MDTA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388705,
                                "long_name": "Rivada Xm Page-UE-Request/Answer (MPUR/MPUA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388706,
                                "long_name": "Rivada Xm Heart-Beat-Request/Answer (MHBR/MHBA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388707,
                                "long_name": "Rivada Xa DPC-Registration-Request/Answer (ADRR/ADRA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388708,
                                "long_name": "Rivada Xa Heart-Beat-Request/Answer (AHBR/AHBA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388709,
                                "long_name": "Rivada Xa Resource-Allocation-Request/Answer (ARAR/ARAA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388710,
                                "long_name": "Rivada Xa Resource-Release-Request/Answer (ARRR/ARRA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388711,
                                "long_name": "Rivada Xa Resource-Release-Notification-Request/Answer (ARNR/ARNA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388712,
                                "long_name": "Rivada Xh User-Data-Request/Answer (HUDR/HUDA)",
                                "ref": "[Vincent_D_Onofrio]",
                                "short_name": ""
                            },
                            {
                                "id": 8388713,
                                "long_name": "ProSe-Initial-Location-Information-Request/Answer (PSR/PSA)",
                                "ref": "[3GPP TS 29.344][Kimmo_Kymalainen]",
                                "short_name": "PSR/PSA"
                            },
                            {
                                "id": 8388714,
                                "long_name": "Nokia Session-Sync-Request/Answer (SSR/SSA)",
                                "ref": "[Timo_Perala]",
                                "short_name": "SSR/SSA"
                            },
                            {
                                "id": 8388715,
                                "long_name": "Nokia Session-Mass-Sync-Request/Answer (SMR/SMA)",
                                "ref": "[Timo_Perala]",
                                "short_name": "SMR/SMA"
                            },
                            {
                                "id": 8388716,
                                "long_name": "Nokia Fetch-Session-Request/Answer (FSR/FSA)",
                                "ref": "[Timo_Perala]",
                                "short_name": "FSR/FSA"
                            },
                            {
                                "id": 8388717,
                                "long_name": "Ericsson Trace-Report-Request/Answer (TRR/TRA)",
                                "ref": "[Gerhard_Schmidt-Krschka]",
                                "short_name": "TRR/TRA"
                            },
                            {
                                "id": 8388718,
                                "long_name": "Configuration-Information-Request/Answer (CIR/CIA)",
                                "ref": "[3GPP TS 29.336][Kimmo_Kymalainen]",
                                "short_name": "CIR/CIA"
                            },
                            {
                                "id": 8388719,
                                "long_name": "Reporting-Information-Request/Answer (RIR/RIA)",
                                "ref": "[3GPP TS 29.336][Kimmo_Kymalainen]",
                                "short_name": "RIR/RIA"
                            },
                            {
                                "id": 8388720,
                                "long_name": "Non-Aggregated-RUCI-Report-Request/Answer (NRR/NRA)",
                                "ref": "[3GPP TS 29.217][Kimmo_Kymalainen]",
                                "short_name": "NRR/NRA"
                            },
                            {
                                "id": 8388721,
                                "long_name": "Aggregated-RUCI-Report-Request/Answer (ARR/ARA)",
                                "ref": "[3GPP TS 29.217][Kimmo_Kymalainen]",
                                "short_name": "ARR/ARA"
                            },
                            {
                                "id": 8388722,
                                "long_name": "Modify-Uecontext-Request/Answer (MUR/MUA)",
                                "ref": "[3GPP TS 29.217][Kimmo_Kymalainen]",
                                "short_name": "MUR/MUA"
                            },
                            {
                                "id": 8388723,
                                "long_name": "Background-Data-Transfer-Request/Answer (BTR/BTA)",
                                "ref": "[3GPP TS 29.154][Kimmo_Kymalainen]",
                                "short_name": "BTR/BTA"
                            },
                            {
                                "id": 8388724,
                                "long_name": "Network-Status-Request/Answer (NSR/NSA)",
                                "ref": "[3GPP TS 29.153][Kimmo_Kymalainen]",
                                "short_name": "NSR/NSA"
                            },
                            {
                                "id": 8388725,
                                "long_name": "Network-Status-Continuous-Report-Request/Answer (NCR/NCA)",
                                "ref": "[3GPP TS 29.153][Kimmo_Kymalainen]",
                                "short_name": "NCR/NCA"
                            },
                            {
                                "id": 8388726,
                                "long_name": "NIDD-Information-Request/Answer (NIR/NIA)",
                                "ref": "[3GPP TS 29.336][Kimmo_Kymalainen]",
                                "short_name": "NIR/NIA"
                            },
                            {
                                "id": 8388727,
                                "long_name": "ProXimity-Application-Request/Answer (XAR/XAA)",
                                "ref": "[3GPP TS 29.343][Kimmo_Kymalainen]",
                                "short_name": "XAR/XAA"
                            },
                            {
                                "id": 8388728,
                                "long_name": "Data-Pull-Request/Answer (DPR/DPA)",
                                "ref": "[3GPP TS 29.283][Kimmo_Kymalainen]",
                                "short_name": "DPR/DPA"
                            },
                            {
                                "id": 8388729,
                                "long_name": "Data-Update-Request/Answer (DMR/DMA)",
                                "ref": "[3GPP TS 29.283][Kimmo_Kymalainen]",
                                "short_name": "DMR/DMA"
                            },
                            {
                                "id": 8388730,
                                "long_name": "Notification-Data-Request/Answer (NDR/NDA)",
                                "ref": "[3GPP TS 29.283][Kimmo_Kymalainen]",
                                "short_name": "NDR/NDA"
                            },
                            {
                                "id": 8388731,
                                "long_name": "TSSF-Notification-Request/Answer (TNR/TNA)",
                                "ref": "[3GPP TS 29.212][Kimmo_Kymalainen]",
                                "short_name": "TNR/TNA"
                            },
                            {
                                "id": 8388732,
                                "long_name": "Connection-Management-Request/Answer (CMR/CMA)",
                                "ref": "[3GPP TS 29.128][Kimmo_Kymalainen]",
                                "short_name": "CMR/CMA"
                            },
                            {
                                "id": 8388733,
                                "long_name": "MO-Data-Request/Answer (ODR/ODA)",
                                "ref": "[3GPP TS 29.128][Kimmo_Kymalainen]",
                                "short_name": "ODR/ODA"
                            },
                            {
                                "id": 8388734,
                                "long_name": "MT-Data-Request/Answer (TDR/TDA)",
                                "ref": "[3GPP TS 29.128][Kimmo_Kymalainen]",
                                "short_name": "TDR/TDA"
                            },
                            {
                                "id": 8388735,
                                "long_name": "Event-Configuration-Request/Answer (ECR/ECA)",
                                "ref": "[3GPP TS 29.154][Kimmo_Kymalainen]",
                                "short_name": "ECR/ECA"
                            },
                            {
                                "id": 8388736,
                                "long_name": "Event-Reporting-Request/Answer (ERR/ERA)",
                                "ref": "[3GPP TS 29.154][Kimmo_Kymalainen]",
                                "short_name": "ERR/ERA"
                            },
                            {
                                "id": 8388737,
                                "long_name": "DESS-DTLS-Handshake-Client-Request/Response",
                                "ref": "[GSMA PRD FS.19][Wayne_Cutler]",
                                "short_name": ""
                            },
                            {
                                "id": 8388738,
                                "long_name": "DESS-DTLS-Handshake-Server-Request/Response",
                                "ref": "[GSMA PRD FS.19][Wayne_Cutler]",
                                "short_name": ""
                            },
                            {
                                "id": 16777214,
                                "long_name": "Experimental code",
                                "ref": "[RFC6733]",
                                "short_name": ""
                            },
                            {
                                "id": 16777215,
                                "long_name": "Experimental code",
                                "ref": "[RFC6733]",
                                "short_name": ""
                            }
]

diameter_application_ids = [
                                {
                                    "id": 0,
                                    "long_name": "Diameter common message",
                                    "ref": "[RFC6733]"
                                },
                                {
                                    "id": 1,
                                    "long_name": "NASREQ",
                                    "ref": "[RFC7155]"
                                },
                                {
                                    "id": 2,
                                    "long_name": "Mobile IPv4",
                                    "ref": "[RFC4004]"
                                },
                                {
                                    "id": 3,
                                    "long_name": "Diameter base accounting",
                                    "ref": "[RFC6733]"
                                },
                                {
                                    "id": 4,
                                    "long_name": "Diameter Credit Control",
                                    "ref": "[RFC8506]"
                                },
                                {
                                    "id": 5,
                                    "long_name": "Diameter EAP",
                                    "ref": "[RFC4072]"
                                },
                                {
                                    "id": 6,
                                    "long_name": "Diameter Session Initiation Protocol (SIP) Application",
                                    "ref": "[RFC4740]"
                                },
                                {
                                    "id": 7,
                                    "long_name": "Diameter Mobile IPv6 IKE (MIP6I)",
                                    "ref": "[RFC5778]"
                                },
                                {
                                    "id": 8,
                                    "long_name": "Diameter Mobile IPv6 Auth (MIP6A)",
                                    "ref": "[RFC5778]"
                                },
                                {
                                    "id": 9,
                                    "long_name": "Diameter QoS application",
                                    "ref": "[RFC5866]"
                                },
                                {
                                    "id": 10,
                                    "long_name": "Diameter Capabilities Update",
                                    "ref": "[RFC6737]"
                                },
                                {
                                    "id": 11,
                                    "long_name": "Diameter IKE SK (IKESK)",
                                    "ref": "[RFC6738]"
                                },
                                {
                                    "id": 12,
                                    "long_name": "Diameter NAT Control Application",
                                    "ref": "[RFC6736]"
                                },
                                {
                                    "id": 13,
                                    "long_name": "Diameter ERP",
                                    "ref": "[RFC6942]"
                                },
                                {
                                    "id": 16777216,
                                    "long_name": "3GPP Cx",
                                    "ref": "[3GPP TS 29.228][3GPP TS 29.229]"
                                },
                                {
                                    "id": 16777217,
                                    "long_name": "3GPP Sh",
                                    "ref": "[3GPP TS 29.328][3GPP TS 29.329]"
                                },
                                {
                                    "id": 16777218,
                                    "long_name": "3GPP Re",
                                    "ref": "[3GPP TS 32.296][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777219,
                                    "long_name": "3GPP Wx",
                                    "ref": "[3GPP TS 29.234][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777220,
                                    "long_name": "3GPP Zn",
                                    "ref": "[3GPP TS 29.109][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777221,
                                    "long_name": "3GPP Zh",
                                    "ref": "[3GPP TS 29.109][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777222,
                                    "long_name": "3GPP Gq",
                                    "ref": "[3GPP TS 29.209][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777223,
                                    "long_name": "3GPP Gmb",
                                    "ref": "[3GPP TS 29.061][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777224,
                                    "long_name": "3GPP Gx",
                                    "ref": "[3GPP TS 29.210][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777225,
                                    "long_name": "3GPP Gx over Gy",
                                    "ref": "[3GPP TS 29.210][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777226,
                                    "long_name": "3GPP MM10",
                                    "ref": "[3GPP TS 29.140][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777227,
                                    "long_name": "Ericsson MSI",
                                    "ref": "[German_Blanco]"
                                },
                                {
                                    "id": 16777228,
                                    "long_name": "Ericsson Zx",
                                    "ref": "[German_Blanco]"
                                },
                                {
                                    "id": 16777229,
                                    "long_name": "3GPP Rx",
                                    "ref": "[3GPP TS 29.211][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777230,
                                    "long_name": "3GPP Pr",
                                    "ref": "[3GPP TS 29.234][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777231,
                                    "long_name": "ETSI e4",
                                    "ref": "[ETSI ES 283 034]"
                                },
                                {
                                    "id": 16777232,
                                    "long_name": "Ericsson Charging-CIP",
                                    "ref": "[Bjorn_Almen]"
                                },
                                {
                                    "id": 16777233,
                                    "long_name": "Ericsson Mm",
                                    "ref": "[German_Blanco]"
                                },
                                {
                                    "id": 16777234,
                                    "long_name": "Vodafone Gx+",
                                    "ref": "[Torsten_Oertel]"
                                },
                                {
                                    "id": 16777235,
                                    "long_name": "ITU-T Rs",
                                    "ref": "[ITU-T Recommendation Q.3301.1]"
                                },
                                {
                                    "id": 16777236,
                                    "long_name": "3GPP Rx",
                                    "ref": "[3GPP TS 29.214][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777237,
                                    "long_name": "3GPP2 Ty",
                                    "ref": "[AC_Mahendran]"
                                },
                                {
                                    "id": 16777238,
                                    "long_name": "3GPP Gx",
                                    "ref": "[3GPP TS 29.212][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777239,
                                    "long_name": "Juniper Cluster",
                                    "ref": "[Vitaly_Dzhitenov]"
                                },
                                {
                                    "id": 16777240,
                                    "long_name": "Juniper Policy-Control-AAA",
                                    "ref": "[Steffen_Ries]"
                                },
                                {
                                    "id": 16777241,
                                    "long_name": "iptego USPI",
                                    "ref": "[Christian_Schubert]"
                                },
                                {
                                    "id": 16777242,
                                    "long_name": "Covergence-specific SIP routing",
                                    "ref": "[Martin_Del_Vecchio]"
                                },
                                {
                                    "id": 16777243,
                                    "long_name": "Policy Processing",
                                    "ref": "[OMA PEEM V1.0][Michael_Brenner]"
                                },
                                {
                                    "id": 16777244,
                                    "long_name": "Juniper Policy-Control-JSRC",
                                    "ref": "[Jun_Chang]"
                                },
                                {
                                    "id": 16777245,
                                    "long_name": "ITU-T S-TC1",
                                    "ref": "[ITU-T Recommendation Q.3221][Kwihoon_Kim]"
                                },
                                {
                                    "id": 16777246,
                                    "long_name": "NSN Unified Charging Trigger Function (UCTF)",
                                    "ref": "[http://www.3gpp.org/ftp/Specs/][Dan_D_Albuquerque]"
                                },
                                {
                                    "id": 16777247,
                                    "long_name": "3GPP2 CAN Access Authentication and Authorization",
                                    "ref": "[ftp://ftp.3gpp2.org/TSGX/Projects/][Avi_Lior]"
                                },
                                {
                                    "id": 16777248,
                                    "long_name": "3GPP2 WLAN Interworking Access Authentication and         \nAuthorization",
                                    "ref": "[ftp://ftp.3gpp2.org/TSGX/Projects/][Avi_Lior]"
                                },
                                {
                                    "id": 16777249,
                                    "long_name": "3GPP2 WLAN Interworking Accounting",
                                    "ref": "[ftp://ftp.3gpp2.org/TSGX/Projects/][Avi_Lior]"
                                },
                                {
                                    "id": 16777250,
                                    "long_name": "3GPP Sta",
                                    "ref": "[3GPP TS 29.273][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777251,
                                    "long_name": "3GPP S6a",
                                    "ref": "[3GPP TS 29.272][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777252,
                                    "long_name": "3GPP S13",
                                    "ref": "[3GPP TS 29.272][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777253,
                                    "long_name": "ETSI Re",
                                    "ref": "[ETSI TS 183 060][Shicheng_Hu]"
                                },
                                {
                                    "id": 16777254,
                                    "long_name": "ETSI GOCAP",
                                    "ref": "[ETSI ES 283 039][Shicheng_Hu]"
                                },
                                {
                                    "id": 16777255,
                                    "long_name": "SLg",
                                    "ref": "[3GPP TS 29.172][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777256,
                                    "long_name": "ITU-T Rw",
                                    "ref": "[ITU-T Rec. Q.3303.3][RFC5431]"
                                },
                                {
                                    "id": 16777257,
                                    "long_name": "ETSI a4",
                                    "ref": "[Shicheng_Hu]"
                                },
                                {
                                    "id": 16777258,
                                    "long_name": "ITU-T Rt",
                                    "ref": "[ITU-T Rec. Q.3305.1][Tom_Taylor]"
                                },
                                {
                                    "id": 16777259,
                                    "long_name": "CARA",
                                    "ref": "[Sachin_Rathee]"
                                },
                                {
                                    "id": 16777260,
                                    "long_name": "CAMA",
                                    "ref": "[Sachin_Rathee]"
                                },
                                {
                                    "id": 16777261,
                                    "long_name": "Femtocell extension to Diameter EAP Application",
                                    "ref": "[Vitaly_Dzhitenov]"
                                },
                                {
                                    "id": 16777262,
                                    "long_name": "ITU-T Ru",
                                    "ref": "[ITU-T Rec. Q.nacp.Ru Q.nacp.Ru][Hyungseok_Chung]"
                                },
                                {
                                    "id": 16777263,
                                    "long_name": "ITU-T Ng",
                                    "ref": "[ITU-T Rec. Q.nacp.Ru Q.nacp.Ru][Kwihoon_Kim]"
                                },
                                {
                                    "id": 16777264,
                                    "long_name": "3GPP SWm",
                                    "ref": "[3GPP TS 29.273][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777265,
                                    "long_name": "3GPP SWx",
                                    "ref": "[3GPP TS 29.273][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777266,
                                    "long_name": "3GPP Gxx",
                                    "ref": "[3GPP TS 29.212][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777267,
                                    "long_name": "3GPP S9",
                                    "ref": "[3GPP TS 29.215][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777268,
                                    "long_name": "3GPP Zpn",
                                    "ref": "[3GPP TS 29.109][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777269,
                                    "long_name": "Ericsson HSI",
                                    "ref": "[German_Blanco]"
                                },
                                {
                                    "id": 16777270,
                                    "long_name": "Juniper-Example",
                                    "ref": "[Aleksey_Romanov]"
                                },
                                {
                                    "id": 16777271,
                                    "long_name": "ITU-T Ri",
                                    "ref": "[ITU-T Rec. Q.3307.1][Michiaki_Hayashi]"
                                },
                                {
                                    "id": 16777272,
                                    "long_name": "3GPP S6b",
                                    "ref": "[3GPP TS 29.273][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777273,
                                    "long_name": "Juniper JGx",
                                    "ref": "[Claudio_Lordello]"
                                },
                                {
                                    "id": 16777274,
                                    "long_name": "ITU-T Rd",
                                    "ref": "[ITU-T Rec. Q.3306.1][Janusz_Pieczerak]"
                                },
                                {
                                    "id": 16777275,
                                    "long_name": "ADMI Notification Application",
                                    "ref": "[Tomas_Menzl]"
                                },
                                {
                                    "id": 16777276,
                                    "long_name": "ADMI Messaging Interface Application",
                                    "ref": "[Tomas_Menzl]"
                                },
                                {
                                    "id": 16777277,
                                    "long_name": "Peter-Service VSI",
                                    "ref": "[Alexey_Grishin]"
                                },
                                {
                                    "id": 16777278,
                                    "long_name": "ETSI Rr request model",
                                    "ref": "[ETSI TS 183 071][Miguel_Angel_Reina_Ortega]"
                                },
                                {
                                    "id": 16777279,
                                    "long_name": "ETSI Rr delegated model",
                                    "ref": "[ETSI TS 183 071][Miguel_Angel_Reina_Ortega]"
                                },
                                {
                                    "id": 16777280,
                                    "long_name": "WIMAX HRPD Interworking",
                                    "ref": "[3GPP2 X.S0058-0 v1.0][Avi_Lior]"
                                },
                                {
                                    "id": 16777281,
                                    "long_name": "WiMAX Network Access Authentication and Authorization Diameter Application (WNAAADA)",
                                    "ref": "[WiMAX Release 1.5][Avi_Lior]"
                                },
                                {
                                    "id": 16777282,
                                    "long_name": "WiMAX Network Accounting Diameter Application (WNADA)",
                                    "ref": "[WiMAX Release 1.5][Avi_Lior]"
                                },
                                {
                                    "id": 16777283,
                                    "long_name": "WiMAX MIP4 Diameter Application (WM4DA)",
                                    "ref": "[WiMAX Release 1.5][Avi_Lior]"
                                },
                                {
                                    "id": 16777284,
                                    "long_name": "WiMAX MIP6 Diameter Application (WM6DA)",
                                    "ref": "[WiMAX Release 1.5][Avi_Lior]"
                                },
                                {
                                    "id": 16777285,
                                    "long_name": "WiMAX DHCP Diameter Application (WDDA)",
                                    "ref": "[WiMAX Release 1.5][Avi_Lior]"
                                },
                                {
                                    "id": 16777286,
                                    "long_name": "WiMAX-Location-Authentication-Authorization Diameter Application (WLAADA)",
                                    "ref": "[WiMAX Release 1.5][Avi_Lior]"
                                },
                                {
                                    "id": 16777287,
                                    "long_name": "WiMAX-Policy-and-Charging-Control-R3-Policies Diameter Application (WiMAX PCC-R3-P)",
                                    "ref": "[WiMAX Release 1.5][Avi_Lior]"
                                },
                                {
                                    "id": 16777288,
                                    "long_name": "WiMAX-Policy-and-Charging-Control-R3-OFfline-Charging Diameter Application (WiMAX PCC-R3-OFC)",
                                    "ref": "[WiMAX Release 1.5][Avi_Lior]"
                                },
                                {
                                    "id": 16777289,
                                    "long_name": "WiMAX-Policy-and-Charging-Control-R3-Offline-Charging-Prime Diameter Application (WiMAX PCC-R3-OFC-PRIME)",
                                    "ref": "[WiMAX Release 1.5][Avi_Lior]"
                                },
                                {
                                    "id": 16777290,
                                    "long_name": "WiMAX-Policy-and-Charging-Control-R3-Online-Charging Diameter Application (WiMAX PCC-R3-OC)",
                                    "ref": "[WiMAX Release 1.5][Avi_Lior]"
                                },
                                {
                                    "id": 16777291,
                                    "long_name": "3GPP SLh",
                                    "ref": "[3GPP TS 29.173][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777292,
                                    "long_name": "3GPP SGmb",
                                    "ref": "[3GPP TS 29.061][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777293,
                                    "long_name": "CMDI - Cloudmark Diameter Interface",
                                    "ref": "[Sanjiv_Parikh]"
                                },
                                {
                                    "id": 16777294,
                                    "long_name": "Camiant DRMA",
                                    "ref": "[Tarek_Abou-Assali][Michael_Mercurio]"
                                },
                                {
                                    "id": 16777295,
                                    "long_name": "PiLTE Interworking Diameter Application",
                                    "ref": "[3GPP2 publication X.S0057][Avi_Lior]"
                                },
                                {
                                    "id": 16777296,
                                    "long_name": "Juniper-Sessions-Recovery (JSR)",
                                    "ref": "[Aleksey_Romanov]"
                                },
                                {
                                    "id": 16777297,
                                    "long_name": "Vedicis LiveProxy",
                                    "ref": "[Francois-Frederic_Ozog]"
                                },
                                {
                                    "id": 16777298,
                                    "long_name": "Pi*3GPP2 Diameter Application",
                                    "ref": "[3GPP2 publication X.S0057A E-UTRAN eHRPD][Avi_Lior]"
                                },
                                {
                                    "id": 16777299,
                                    "long_name": "Sandvine Rf+",
                                    "ref": "[Yoni_Eitan]"
                                },
                                {
                                    "id": 16777300,
                                    "long_name": "Subscription Information Application",
                                    "ref": "[Lars_Anglert]"
                                },
                                {
                                    "id": 16777301,
                                    "long_name": "Ericsson Charging-DCIP",
                                    "ref": "[Lars_Anglert]"
                                },
                                {
                                    "id": 16777302,
                                    "long_name": "3GPP Sy",
                                    "ref": "[3GPP TS 29.219][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777303,
                                    "long_name": "3GPP Sd",
                                    "ref": "[3GPP TS 29.212][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777304,
                                    "long_name": "Ericsson Sy",
                                    "ref": "[Lars_Anglert]"
                                },
                                {
                                    "id": 16777305,
                                    "long_name": "HP DTD",
                                    "ref": "[Chiranjeev_Agrawal][J_V_Kishore]"
                                },
                                {
                                    "id": 16777306,
                                    "long_name": "M9 interface between MLM-PE(P) and MLM-PE(C)",
                                    "ref": "[ITU-T Q5/Sg11][Jin_Seek_Choi]"
                                },
                                {
                                    "id": 16777307,
                                    "long_name": "ITU-T M13",
                                    "ref": "[ITU-T Q.3230][Kwihoon_Kim]"
                                },
                                {
                                    "id": 16777308,
                                    "long_name": "3GPP S7a",
                                    "ref": "[3GPP TS 29.272][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777309,
                                    "long_name": "3GPP Tsp",
                                    "ref": "[3GPP TS 29.368][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777310,
                                    "long_name": "3GPP S6m",
                                    "ref": "[3GPP TS 29.336][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777311,
                                    "long_name": "3GPP T4",
                                    "ref": "[3GPP TS 29.337][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777312,
                                    "long_name": "3GPP S6c",
                                    "ref": "[3GPP TS 29.338][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777313,
                                    "long_name": "3GPP SGd",
                                    "ref": "[3GPP TS 29.338][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777314,
                                    "long_name": "Intrado-SLg",
                                    "ref": "[Scott_Luallin]"
                                },
                                {
                                    "id": 16777315,
                                    "long_name": "Ericsson Diameter Signalling Controller Application (DSC)",
                                    "ref": "[Klaus_Turina]"
                                },
                                {
                                    "id": 16777316,
                                    "long_name": "Verizon-Femto-Loc",
                                    "ref": "[Niranjan_Avula]"
                                },
                                {
                                    "id": 16777317,
                                    "long_name": "Nokia Siemens Networks (NSN) Hd Application",
                                    "ref": "[Hannes_Tschofenig]"
                                },
                                {
                                    "id": 16777318,
                                    "long_name": "3GPP S15",
                                    "ref": "[3GPP TS 29.212][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777319,
                                    "long_name": "3GPP S9a",
                                    "ref": "[3GPP TS 29.215][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777320,
                                    "long_name": "3GPP S9a*",
                                    "ref": "[3GPP TS 29.215][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777321,
                                    "long_name": "Gateway Location Application",
                                    "ref": "[Steve_Donovan]"
                                },
                                {
                                    "id": 16777322,
                                    "long_name": "Verizon Session Recovery",
                                    "ref": "[Niranjan_Avula]"
                                },
                                {
                                    "id": 16777323,
                                    "long_name": "3GPP2 M1 Interface",
                                    "ref": "[3GPP2 X.S0068][Jun_Wang]"
                                },
                                {
                                    "id": 16777324,
                                    "long_name": "MAGIC Client Interface Protocol (CIP)",
                                    "ref": "[ARINC 839][Paul_Prisaznuk][Manfred_Benten]"
                                },
                                {
                                    "id": 16777325,
                                    "long_name": "ITU-T Nc",
                                    "ref": "[ITU-T Rec. Q.nacp.Nc][Kwihoon_Kim]"
                                },
                                {
                                    "id": 16777326,
                                    "long_name": "ITU-T Ne",
                                    "ref": "[ITU-T Rec. Q.nacp.Ne][Kwihoon_Kim]"
                                },
                                {
                                    "id": 16777327,
                                    "long_name": "Ericsson Sx",
                                    "ref": "[Irene_Martin]"
                                },
                                {
                                    "id": 16777328,
                                    "long_name": "Nokia Service Extension, NSE",
                                    "ref": "[Timo_Perala]"
                                },
                                {
                                    "id": 16777329,
                                    "long_name": "Rivada Xd",
                                    "ref": "[Vincent_D_Onofrio]"
                                },
                                {
                                    "id": 16777330,
                                    "long_name": "Rivada Xm",
                                    "ref": "[Vincent_D_Onofrio]"
                                },
                                {
                                    "id": 16777331,
                                    "long_name": "Rivada Xh",
                                    "ref": "[Vincent_D_Onofrio]"
                                },
                                {
                                    "id": 16777332,
                                    "long_name": "Rivada Xf",
                                    "ref": "[Vincent_D_Onofrio]"
                                },
                                {
                                    "id": 16777333,
                                    "long_name": "Rivada Xp",
                                    "ref": "[Vincent_D_Onofrio]"
                                },
                                {
                                    "id": 16777334,
                                    "long_name": "Rivada Xa",
                                    "ref": "[Vincent_D_Onofrio]"
                                },
                                {
                                    "id": 16777335,
                                    "long_name": "3GPP MB2-C",
                                    "ref": "[3GPP TS 29.468][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777336,
                                    "long_name": "3GPP PC4a",
                                    "ref": "[3GPP TS 29.344][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777337,
                                    "long_name": "3GPP PC2",
                                    "ref": "[3GPP TS 29.343][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777338,
                                    "long_name": "Juniper Domain Policy",
                                    "ref": "[Vitaly_Dzhitenov]"
                                },
                                {
                                    "id": 16777339,
                                    "long_name": "Host Observer",
                                    "ref": "[Laimutis_Slecpenka]"
                                },
                                {
                                    "id": 16777340,
                                    "long_name": "3GPP PC6/PC7",
                                    "ref": "[3GPP TS 29.345][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777341,
                                    "long_name": "Nokia Sdr Application",
                                    "ref": "[Timo_Perala]"
                                },
                                {
                                    "id": 16777342,
                                    "long_name": "3GPP Np",
                                    "ref": "[3GPP TS 29.217][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777343,
                                    "long_name": "Sandvine Location Relay Service",
                                    "ref": "[Inian_Vasanth]"
                                },
                                {
                                    "id": 16777344,
                                    "long_name": "Sandvine Fairshare Traffic Management Service",
                                    "ref": "[Inian_Vasanth]"
                                },
                                {
                                    "id": 16777345,
                                    "long_name": "3GPP S6t",
                                    "ref": "[3GPP TS 29.336][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777346,
                                    "long_name": "3GPP T6a/T6b",
                                    "ref": "[3GPP TS 29.128][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777347,
                                    "long_name": "3GPP Ns",
                                    "ref": "[3GPP TS 29.153][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777348,
                                    "long_name": "3GPP Nt",
                                    "ref": "[3GPP TS 29.154][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777349,
                                    "long_name": "3GPP St",
                                    "ref": "[3GPP TS 29.212][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777350,
                                    "long_name": "3GPP PC2",
                                    "ref": "[3GPP TS 29.343][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777351,
                                    "long_name": "3GPP Diameter Data Management",
                                    "ref": "[3GPP TS 29.283][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777352,
                                    "long_name": "ITU-T M1",
                                    "ref": "[ITU-T Recommendation Q.nacp.M1][Kwihoon_Kim]"
                                },
                                {
                                    "id": 16777353,
                                    "long_name": "ITU-T M2",
                                    "ref": "[ITU-T Recommendation Q.nacp.M2][Kwihoon_Kim]"
                                },
                                {
                                    "id": 16777354,
                                    "long_name": "Verizon-NLS-WDS",
                                    "ref": "[Niranjan_Avula]"
                                },
                                {
                                    "id": 16777355,
                                    "long_name": "3GPP V4",
                                    "ref": "[3GPP TS 29.388][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777356,
                                    "long_name": "3GPP V6",
                                    "ref": "[3GPP TS 29.389][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777357,
                                    "long_name": "OMN Adapt Application",
                                    "ref": "[Jarda_Nedved]"
                                },
                                {
                                    "id": 16777358,
                                    "long_name": "3GPP Nta",
                                    "ref": "[3GPP TS 29.154][Kimmo_Kymalainen]"
                                },
                                {
                                    "id": 16777359,
                                    "long_name": "Ericsson Charging - SBI Policy",
                                    "ref": "[S.Dhanalakshmi]"
                                },
                                {
                                    "id": 16777360,
                                    "long_name": "GSMA-DESS",
                                    "ref": "[GSMA PRD FS.19][Wayne_Cutler]"
                                },
                                {
                                    "id": 4294967295,
                                    "long_name": "Relay",
                                    "ref": "[RFC6733]"
                                }
]

diameter_avps = [
                    {
                        "name": "User-Name",
                        "id": 1
                    },
                    {
                        "name": "User-Password",
                        "id": 2
                    },
                    {
                        "name": "CHAP-Password",
                        "id": 3
                    },
                    {
                        "name": "NAS-IP-Address",
                        "id": 4
                    },
                    {
                        "name": "NAS-Port",
                        "id": 5
                    },
                    {
                        "name": "Service-Type",
                        "id": 6
                    },
                    {
                        "name": "Framed-Protocol",
                        "id": 7
                    },
                    {
                        "name": "Framed-IP-Address",
                        "id": 8
                    },
                    {
                        "name": "Framed-IP-Netmask",
                        "id": 9
                    },
                    {
                        "name": "Framed-Routing",
                        "id": 10
                    },
                    {
                        "name": "Filter-Id",
                        "id": 11
                    },
                    {
                        "name": "Framed-MTU",
                        "id": 12
                    },
                    {
                        "name": "Framed-Compression",
                        "id": 13
                    },
                    {
                        "name": "Login-IP-Host",
                        "id": 14
                    },
                    {
                        "name": "Login-Service",
                        "id": 15
                    },
                    {
                        "name": "Login-TCP-Port",
                        "id": 16
                    },
                    {
                        "name": "Unassigned",
                        "id": 17
                    },
                    {
                        "name": "Reply-Message",
                        "id": 18
                    },
                    {
                        "name": "Callback-Number",
                        "id": 19
                    },
                    {
                        "name": "Callback-Id",
                        "id": 20
                    },
                    {
                        "name": "Unassigned",
                        "id": 21
                    },
                    {
                        "name": "Framed-Route",
                        "id": 22
                    },
                    {
                        "name": "Framed-IPX-Network",
                        "id": 23
                    },
                    {
                        "name": "State",
                        "id": 24
                    },
                    {
                        "name": "Class",
                        "id": 25
                    },
                    {
                        "name": "Vendor-Specific",
                        "id": 26
                    },
                    {
                        "name": "Session-Timeout",
                        "id": 27
                    },
                    {
                        "name": "Idle-Timeout",
                        "id": 28
                    },
                    {
                        "name": "Termination-Action",
                        "id": 29
                    },
                    {
                        "name": "Called-Station-Id",
                        "id": 30
                    },
                    {
                        "name": "Calling-Station-Id",
                        "id": 31
                    },
                    {
                        "name": "NAS-Identifier",
                        "id": 32
                    },
                    {
                        "name": "Proxy-State",
                        "id": 33
                    },
                    {
                        "name": "Login-LAT-Service",
                        "id": 34
                    },
                    {
                        "name": "Login-LAT-Node",
                        "id": 35
                    },
                    {
                        "name": "Login-LAT-Group",
                        "id": 36
                    },
                    {
                        "name": "Framed-AppleTalk-Link",
                        "id": 37
                    },
                    {
                        "name": "Framed-AppleTalk-Network",
                        "id": 38
                    },
                    {
                        "name": "Framed-AppleTalk-Zone",
                        "id": 39
                    },
                    {
                        "name": "Acct-Status-Type",
                        "id": 40
                    },
                    {
                        "name": "Acct-Delay-Time",
                        "id": 41
                    },
                    {
                        "name": "Acct-Input-Octets",
                        "id": 42
                    },
                    {
                        "name": "Acct-Output-Octets",
                        "id": 43
                    },
                    {
                        "name": "Acct-Session-Id",
                        "id": 44
                    },
                    {
                        "name": "Acct-Authentic",
                        "id": 45
                    },
                    {
                        "name": "Acct-Session-Time",
                        "id": 46
                    },
                    {
                        "name": "Acct-Input-Packets",
                        "id": 47
                    },
                    {
                        "name": "Acct-Output-Packets",
                        "id": 48
                    },
                    {
                        "name": "Acct-Terminate-Cause",
                        "id": 49
                    },
                    {
                        "name": "Acct-Multi-Session-Id",
                        "id": 50
                    },
                    {
                        "name": "Acct-Link-Count",
                        "id": 51
                    },
                    {
                        "name": "Acct-Input-Gigawords",
                        "id": 52
                    },
                    {
                        "name": "Acct-Output-Gigawords",
                        "id": 53
                    },
                    {
                        "name": "Unassigned",
                        "id": 54
                    },
                    {
                        "name": "Event-Timestamp",
                        "id": 55
                    },
                    {
                        "name": "Egress-VLANID",
                        "id": 56
                    },
                    {
                        "name": "Ingress-Filters",
                        "id": 57
                    },
                    {
                        "name": "Egress-VLAN-Name",
                        "id": 58
                    },
                    {
                        "name": "User-Priority-Table",
                        "id": 59
                    },
                    {
                        "name": "CHAP-Challenge",
                        "id": 60
                    },
                    {
                        "name": "NAS-Port-Type",
                        "id": 61
                    },
                    {
                        "name": "Port-Limit",
                        "id": 62
                    },
                    {
                        "name": "Login-LAT-Port",
                        "id": 63
                    },
                    {
                        "name": "Tunnel-Type",
                        "id": 64
                    },
                    {
                        "name": "Tunnel-Medium-Type",
                        "id": 65
                    },
                    {
                        "name": "Tunnel-Client-Endpoint",
                        "id": 66
                    },
                    {
                        "name": "Tunnel-Server-Endpoint",
                        "id": 67
                    },
                    {
                        "name": "Acct-Tunnel-Connection",
                        "id": 68
                    },
                    {
                        "name": "Tunnel-Password",
                        "id": 69
                    },
                    {
                        "name": "ARAP-Password",
                        "id": 70
                    },
                    {
                        "name": "ARAP-Features",
                        "id": 71
                    },
                    {
                        "name": "ARAP-Zone-Access",
                        "id": 72
                    },
                    {
                        "name": "ARAP-Security",
                        "id": 73
                    },
                    {
                        "name": "ARAP-Security-Data",
                        "id": 74
                    },
                    {
                        "name": "Password-Retry",
                        "id": 75
                    },
                    {
                        "name": "Prompt",
                        "id": 76
                    },
                    {
                        "name": "Connect-Info",
                        "id": 77
                    },
                    {
                        "name": "Configuration-Token",
                        "id": 78
                    },
                    {
                        "name": "EAP-Message",
                        "id": 79
                    },
                    {
                        "name": "Message-Authenticator",
                        "id": 80
                    },
                    {
                        "name": "Tunnel-Private-Group-ID",
                        "id": 81
                    },
                    {
                        "name": "Tunnel-Assignment-ID",
                        "id": 82
                    },
                    {
                        "name": "Tunnel-Preference",
                        "id": 83
                    },
                    {
                        "name": "ARAP-Challenge-Response",
                        "id": 84
                    },
                    {
                        "name": "Acct-Interim-Interval",
                        "id": 85
                    },
                    {
                        "name": "Acct-Tunnel-Packets-Lost",
                        "id": 86
                    },
                    {
                        "name": "NAS-Port-Id",
                        "id": 87
                    },
                    {
                        "name": "Framed-Pool",
                        "id": 88
                    },
                    {
                        "name": "CUI",
                        "id": 89
                    },
                    {
                        "name": "Tunnel-Client-Auth-ID",
                        "id": 90
                    },
                    {
                        "name": "Tunnel-Server-Auth-ID",
                        "id": 91
                    },
                    {
                        "name": "NAS-Filter-Rule",
                        "id": 92
                    },
                    {
                        "name": "Unassigned",
                        "id": 93
                    },
                    {
                        "name": "Originating-Line-Info",
                        "id": 94
                    },
                    {
                        "name": "NAS-IPv6-Address",
                        "id": 95
                    },
                    {
                        "name": "Framed-Interface-Id",
                        "id": 96
                    },
                    {
                        "name": "Framed-IPv6-Prefix",
                        "id": 97
                    },
                    {
                        "name": "Login-IPv6-Host",
                        "id": 98
                    },
                    {
                        "name": "Framed-IPv6-Route",
                        "id": 99
                    },
                    {
                        "name": "Framed-IPv6-Pool",
                        "id": 100
                    },
                    {
                        "name": "Error-Cause Attribute",
                        "id": 101
                    },
                    {
                        "name": "EAP-Key-Name",
                        "id": 102
                    },
                    {
                        "name": "Digest-Response",
                        "id": 103
                    },
                    {
                        "name": "Digest-Realm",
                        "id": 104
                    },
                    {
                        "name": "Digest-Nonce",
                        "id": 105
                    },
                    {
                        "name": "Digest-Response-Auth",
                        "id": 106
                    },
                    {
                        "name": "Digest-Nextnonce",
                        "id": 107
                    },
                    {
                        "name": "Digest-Method",
                        "id": 108
                    },
                    {
                        "name": "Digest-URI",
                        "id": 109
                    },
                    {
                        "name": "Digest-Qop",
                        "id": 110
                    },
                    {
                        "name": "Digest-Algorithm",
                        "id": 111
                    },
                    {
                        "name": "Digest-Entity-Body-Hash",
                        "id": 112
                    },
                    {
                        "name": "Digest-CNonce",
                        "id": 113
                    },
                    {
                        "name": "Digest-Nonce-Count",
                        "id": 114
                    },
                    {
                        "name": "Digest-Username",
                        "id": 115
                    },
                    {
                        "name": "Digest-Opaque",
                        "id": 116
                    },
                    {
                        "name": "Digest-Auth-Param",
                        "id": 117
                    },
                    {
                        "name": "Digest-AKA-Auts",
                        "id": 118
                    },
                    {
                        "name": "Digest-Domain",
                        "id": 119
                    },
                    {
                        "name": "Digest-Stale",
                        "id": 120
                    },
                    {
                        "name": "Digest-HA1",
                        "id": 121
                    },
                    {
                        "name": "SIP-AOR",
                        "id": 122
                    },
                    {
                        "name": "Delegated-IPv6-Prefix",
                        "id": 123
                    },
                    {
                        "name": "MIP6-Feature-Vector",
                        "id": 124
                    },
                    {
                        "name": "MIP6-Home-Link-Prefix",
                        "id": 125
                    },
                    {
                        "name": "Operator-Name",
                        "id": 126
                    },
                    {
                        "name": "Location-Information",
                        "id": 127
                    },
                    {
                        "name": "Location-Data",
                        "id": 128
                    },
                    {
                        "name": "Basic-Location-Policy-Rules",
                        "id": 129
                    },
                    {
                        "name": "Extended-Location-Policy-Rules",
                        "id": 130
                    },
                    {
                        "name": "Location-Capable",
                        "id": 131
                    },
                    {
                        "name": "Requested-Location-Info",
                        "id": 132
                    },
                    {
                        "name": "Framed-Management-Protocol",
                        "id": 133
                    },
                    {
                        "name": "Management-Transport-Protection",
                        "id": 134
                    },
                    {
                        "name": "Management-Policy-Id",
                        "id": 135
                    },
                    {
                        "name": "Management-Privilege-Level",
                        "id": 136
                    },
                    {
                        "name": "PKM-SS-Cert",
                        "id": 137
                    },
                    {
                        "name": "PKM-CA-Cert",
                        "id": 138
                    },
                    {
                        "name": "PKM-Config-Settings",
                        "id": 139
                    },
                    {
                        "name": "PKM-Cryptosuite-List",
                        "id": 140
                    },
                    {
                        "name": "PKM-SAID",
                        "id": 141
                    },
                    {
                        "name": "PKM-SA-Descriptor",
                        "id": 142
                    },
                    {
                        "name": "PKM-Auth-Key",
                        "id": 143
                    },
                    {
                        "name": "DS-Lite-Tunnel-Name",
                        "id": 144
                    },
                    {
                        "name": "Mobile-Node-Identifier",
                        "id": 145
                    },
                    {
                        "name": "Service-Selection",
                        "id": 146
                    },
                    {
                        "name": "PMIP6-Home-LMA-IPv6-Address",
                        "id": 147
                    },
                    {
                        "name": "PMIP6-Visited-LMA-IPv6-Address",
                        "id": 148
                    },
                    {
                        "name": "PMIP6-Home-LMA-IPv4-Address",
                        "id": 149
                    },
                    {
                        "name": "PMIP6-Visited-LMA-IPv4-Address",
                        "id": 150
                    },
                    {
                        "name": "PMIP6-Home-HN-Prefix",
                        "id": 151
                    },
                    {
                        "name": "PMIP6-Visited-HN-Prefix",
                        "id": 152
                    },
                    {
                        "name": "PMIP6-Home-Interface-ID",
                        "id": 153
                    },
                    {
                        "name": "PMIP6-Visited-Interface-ID",
                        "id": 154
                    },
                    {
                        "name": "PMIP6-Home-IPv4-HoA",
                        "id": 155
                    },
                    {
                        "name": "PMIP6-Visited-IPv4-HoA",
                        "id": 156
                    },
                    {
                        "name": "PMIP6-Home-DHCP4-Server-Address",
                        "id": 157
                    },
                    {
                        "name": "PMIP6-Visited-DHCP4-Server-Address",
                        "id": 158
                    },
                    {
                        "name": "PMIP6-Home-DHCP6-Server-Address",
                        "id": 159
                    },
                    {
                        "name": "PMIP6-Visited-DHCP6-Server-Address",
                        "id": 160
                    },
                    {
                        "name": "PMIP6-Home-IPv4-Gateway",
                        "id": 161
                    },
                    {
                        "name": "PMIP6-Visited-IPv4-Gateway",
                        "id": 162
                    },
                    {
                        "name": "EAP-Lower-Layer",
                        "id": 163
                    },
                    {
                        "name": "GSS-Acceptor-Service-Name",
                        "id": 164
                    },
                    {
                        "name": "GSS-Acceptor-Host-Name",
                        "id": 165
                    },
                    {
                        "name": "GSS-Acceptor-Service-Specifics",
                        "id": 166
                    },
                    {
                        "name": "GSS-Acceptor-Realm-Name",
                        "id": 167
                    },
                    {
                        "name": "Framed-IPv6-Address",
                        "id": 168
                    },
                    {
                        "name": "DNS-Server-IPv6-Address",
                        "id": 169
                    },
                    {
                        "name": "Route-IPv6-Information",
                        "id": 170
                    },
                    {
                        "name": "Delegated-IPv6-Prefix-Pool",
                        "id": 171
                    },
                    {
                        "name": "Stateful-IPv6-Address-Pool",
                        "id": 172
                    },
                    {
                        "name": "IPv6-6rd-Configuration",
                        "id": 173
                    },
                    {
                        "name": "Allowed-Called-Station-Id",
                        "id": 174
                    },
                    {
                        "name": "EAP-Peer-Id",
                        "id": 175
                    },
                    {
                        "name": "EAP-Server-Id",
                        "id": 176
                    },
                    {
                        "name": "Mobility-Domain-Id",
                        "id": 177
                    },
                    {
                        "name": "Preauth-Timeout",
                        "id": 178
                    },
                    {
                        "name": "Network-Id-Name",
                        "id": 179
                    },
                    {
                        "name": "EAPoL-Announcement",
                        "id": 180
                    },
                    {
                        "name": "WLAN-HESSID",
                        "id": 181
                    },
                    {
                        "name": "WLAN-Venue-Info",
                        "id": 182
                    },
                    {
                        "name": "WLAN-Venue-Language",
                        "id": 183
                    },
                    {
                        "name": "WLAN-Venue-Name",
                        "id": 184
                    },
                    {
                        "name": "WLAN-Reason-Code",
                        "id": 185
                    },
                    {
                        "name": "WLAN-Pairwise-Cipher",
                        "id": 186
                    },
                    {
                        "name": "WLAN-Group-Cipher",
                        "id": 187
                    },
                    {
                        "name": "WLAN-AKM-Suite",
                        "id": 188
                    },
                    {
                        "name": "WLAN-Group-Mgmt-Cipher",
                        "id": 189
                    },
                    {
                        "name": "WLAN-RF-Band",
                        "id": 190
                    },
                    {
                        "name": "Unassigned",
                        "id": 191
                    },
                    {
                        "name": "Extended-Attribute-1",
                        "id": 241
                    },
                    {
                        "name": "Extended-Attribute-2",
                        "id": 242
                    },
                    {
                        "name": "Extended-Attribute-3",
                        "id": 243
                    },
                    {
                        "name": "Extended-Attribute-4",
                        "id": 244
                    },
                    {
                        "name": "Extended-Attribute-5",
                        "id": 245
                    },
                    {
                        "name": "Extended-Attribute-6",
                        "id": 246
                    },
                    {
                        "name": "Host-IP-Address",
                        "id": 257
                    },
                    {
                        "name": "Auth-Application-Id",
                        "id": 258
                    },
                    {
                        "name": "Acct-Application-Id",
                        "id": 259
                    },
                    {
                        "name": "Vendor-Specific-Application-Id",
                        "id": 260
                    },
                    {
                        "name": "Redirect-Host-Usage",
                        "id": 261
                    },
                    {
                        "name": "Redirect-Max-Cache-Time",
                        "id": 262
                    },
                    {
                        "name": "Session-Id",
                        "id": 263
                    },
                    {
                        "name": "Origin-Host",
                        "id": 264
                    },
                    {
                        "name": "Supported-Vendor-Id",
                        "id": 265
                    },
                    {
                        "name": "Vendor-Id",
                        "id": 266
                    },
                    {
                        "name": "Firmware-Revision",
                        "id": 267
                    },
                    {
                        "name": "Result-Code",
                        "id": 268
                    },
                    {
                        "name": "Product-Name",
                        "id": 269
                    },
                    {
                        "name": "Session-Binding",
                        "id": 270
                    },
                    {
                        "name": "Session-Server-Failover",
                        "id": 271
                    },
                    {
                        "name": "Multi-Round-Time-Out",
                        "id": 272
                    },
                    {
                        "name": "Disconnect-Cause",
                        "id": 273
                    },
                    {
                        "name": "Auth-Request-Type",
                        "id": 274
                    },
                    {
                        "name": "Auth-Grace-Period",
                        "id": 276
                    },
                    {
                        "name": "Auth-Session-State",
                        "id": 277
                    },
                    {
                        "name": "Origin-State-Id",
                        "id": 278
                    },
                    {
                        "name": "Failed-AVP",
                        "id": 279
                    },
                    {
                        "name": "Proxy-Host",
                        "id": 280
                    },
                    {
                        "name": "Error-Message",
                        "id": 281
                    },
                    {
                        "name": "Route-Record",
                        "id": 282
                    },
                    {
                        "name": "Destination-Realm",
                        "id": 283
                    },
                    {
                        "name": "Proxy-Info",
                        "id": 284
                    },
                    {
                        "name": "Re-Auth-Request-Type",
                        "id": 285
                    },
                    {
                        "name": "Accounting-Sub-Session-Id",
                        "id": 287
                    },
                    {
                        "name": "Authorization-Lifetime",
                        "id": 291
                    },
                    {
                        "name": "Redirect-Host",
                        "id": 292
                    },
                    {
                        "name": "Destination-Host",
                        "id": 293
                    },
                    {
                        "name": "Error-Reporting-Host",
                        "id": 294
                    },
                    {
                        "name": "Termination-Cause",
                        "id": 295
                    },
                    {
                        "name": "Origin-Realm",
                        "id": 296
                    },
                    {
                        "name": "Experimental-Result",
                        "id": 297
                    },
                    {
                        "name": "Experimental-Result-Code",
                        "id": 298
                    },
                    {
                        "name": "Inband-Security-Id",
                        "id": 299
                    },
                    {
                        "name": "E2E-Sequence",
                        "id": 300
                    },
                    {
                        "name": "DRMP",
                        "id": 301
                    },
                    {
                        "name": "MIP-FA-to-HA-SPI",
                        "id": 318
                    },
                    {
                        "name": "MIP-FA-to-MN-SPI",
                        "id": 319
                    },
                    {
                        "name": "MIP-Reg-Request",
                        "id": 320
                    },
                    {
                        "name": "MIP-Reg-Reply",
                        "id": 321
                    },
                    {
                        "name": "MIP-MN-AAA-Auth",
                        "id": 322
                    },
                    {
                        "name": "MIP-HA-to-FA-SPI",
                        "id": 323
                    },
                    {
                        "name": "MIP-MN-to-FA-MSA",
                        "id": 325
                    },
                    {
                        "name": "MIP-FA-to-MN-MSA",
                        "id": 326
                    },
                    {
                        "name": "MIP-FA-to-HA-MSA",
                        "id": 328
                    },
                    {
                        "name": "MIP-HA-to-FA-MSA",
                        "id": 329
                    },
                    {
                        "name": "MIP-MN-to-HA-MSA",
                        "id": 331
                    },
                    {
                        "name": "MIP-HA-to-MN-MSA",
                        "id": 332
                    },
                    {
                        "name": "MIP-Mobile-Node-Address",
                        "id": 333
                    },
                    {
                        "name": "MIP-Home-Agent-Address",
                        "id": 334
                    },
                    {
                        "name": "MIP-Nonce",
                        "id": 335
                    },
                    {
                        "name": "MIP-Candidate-Home-Agent-Host",
                        "id": 336
                    },
                    {
                        "name": "MIP-Feature-Vector",
                        "id": 337
                    },
                    {
                        "name": "MIP-Auth-Input-Data-Length",
                        "id": 338
                    },
                    {
                        "name": "MIP-Authenticator-Length",
                        "id": 339
                    },
                    {
                        "name": "MIP-Authenticator-Offset",
                        "id": 340
                    },
                    {
                        "name": "MIP-MN-AAA-SPI",
                        "id": 341
                    },
                    {
                        "name": "MIP-Filter-Rule",
                        "id": 342
                    },
                    {
                        "name": "MIP-Session-Key",
                        "id": 343
                    },
                    {
                        "name": "MIP-FA-Challenge",
                        "id": 344
                    },
                    {
                        "name": "MIP-Algorithm-Type",
                        "id": 345
                    },
                    {
                        "name": "MIP-Replay-Mode",
                        "id": 346
                    },
                    {
                        "name": "MIP-Originating-Foreign-AAA",
                        "id": 347
                    },
                    {
                        "name": "MIP-Home-Agent-Host",
                        "id": 348
                    },
                    {
                        "name": "Accounting-Input-Octets",
                        "id": 363
                    },
                    {
                        "name": "Accounting-Output-Octets",
                        "id": 364
                    },
                    {
                        "name": "Accounting-Input-Packets",
                        "id": 365
                    },
                    {
                        "name": "Accounting-Output-Packets",
                        "id": 366
                    },
                    {
                        "name": "MIP-MSA-Lifetime",
                        "id": 367
                    },
                    {
                        "name": "SIP-Accounting-Information",
                        "id": 368
                    },
                    {
                        "name": "SIP-Accounting-Server-URI",
                        "id": 369
                    },
                    {
                        "name": "SIP-Credit-Control-Server-URI",
                        "id": 370
                    },
                    {
                        "name": "SIP-Server-URI",
                        "id": 371
                    },
                    {
                        "name": "SIP-Server-Capabilities",
                        "id": 372
                    },
                    {
                        "name": "SIP-Mandatory-Capability",
                        "id": 373
                    },
                    {
                        "name": "SIP-Optional-Capability",
                        "id": 374
                    },
                    {
                        "name": "SIP-Server-Assignment-Type",
                        "id": 375
                    },
                    {
                        "name": "SIP-Auth-Data-Item",
                        "id": 376
                    },
                    {
                        "name": "SIP-Authentication-Scheme",
                        "id": 377
                    },
                    {
                        "name": "SIP-Item-Number",
                        "id": 378
                    },
                    {
                        "name": "SIP-Authenticate",
                        "id": 379
                    },
                    {
                        "name": "SIP-Authorization",
                        "id": 380
                    },
                    {
                        "name": "SIP-Authentication-Info",
                        "id": 381
                    },
                    {
                        "name": "SIP-Number-Auth-Items",
                        "id": 382
                    },
                    {
                        "name": "SIP-Deregistration-Reason",
                        "id": 383
                    },
                    {
                        "name": "SIP-Reason-Code",
                        "id": 384
                    },
                    {
                        "name": "SIP-Reason-Info",
                        "id": 385
                    },
                    {
                        "name": "SIP-Visited-Network-Id",
                        "id": 386
                    },
                    {
                        "name": "SIP-User-Authorization-Type",
                        "id": 387
                    },
                    {
                        "name": "SIP-Supported-User-Data-Type",
                        "id": 388
                    },
                    {
                        "name": "SIP-User-Data",
                        "id": 389
                    },
                    {
                        "name": "SIP-User-Data-Type",
                        "id": 390
                    },
                    {
                        "name": "SIP-User-Data-Contents",
                        "id": 391
                    },
                    {
                        "name": "SIP-User-Data-Already-Available",
                        "id": 392
                    },
                    {
                        "name": "SIP-Method",
                        "id": 393
                    },
                    {
                        "name": "NAS-Filter-Rule",
                        "id": 400
                    },
                    {
                        "name": "Tunneling",
                        "id": 401
                    },
                    {
                        "name": "CHAP-Auth",
                        "id": 402
                    },
                    {
                        "name": "CHAP-Algorithm",
                        "id": 403
                    },
                    {
                        "name": "CHAP-Ident",
                        "id": 404
                    },
                    {
                        "name": "CHAP-Response",
                        "id": 405
                    },
                    {
                        "name": "Accounting-Auth-Method",
                        "id": 406
                    },
                    {
                        "name": "QoS-Filter-Rule",
                        "id": 407
                    },
                    {
                        "name": "Origin-AAA-Protocol",
                        "id": 408
                    },
                    {
                        "name": "CC-Correlation-Id",
                        "id": 411
                    },
                    {
                        "name": "CC-Input-Octets",
                        "id": 412
                    },
                    {
                        "name": "CC-Money",
                        "id": 413
                    },
                    {
                        "name": "CC-Output-Octets",
                        "id": 414
                    },
                    {
                        "name": "CC-Request-Number",
                        "id": 415
                    },
                    {
                        "name": "CC-Request-Type",
                        "id": 416
                    },
                    {
                        "name": "CC-Service-Specific-Units",
                        "id": 417
                    },
                    {
                        "name": "CC-Session-Failover",
                        "id": 418
                    },
                    {
                        "name": "CC-Sub-Session-Id",
                        "id": 419
                    },
                    {
                        "name": "CC-Time",
                        "id": 420
                    },
                    {
                        "name": "CC-Total-Octets",
                        "id": 421
                    },
                    {
                        "name": "Check-Balance-Result",
                        "id": 422
                    },
                    {
                        "name": "Cost-Information",
                        "id": 423
                    },
                    {
                        "name": "Cost-Unit",
                        "id": 424
                    },
                    {
                        "name": "Currency-Code",
                        "id": 425
                    },
                    {
                        "name": "Credit-Control",
                        "id": 426
                    },
                    {
                        "name": "Credit-Control-Failure-Handling",
                        "id": 427
                    },
                    {
                        "name": "Direct-Debiting-Failure-Handling",
                        "id": 428
                    },
                    {
                        "name": "Exponent",
                        "id": 429
                    },
                    {
                        "name": "Final-Unit-Indication",
                        "id": 430
                    },
                    {
                        "name": "Granted-Service-Unit",
                        "id": 431
                    },
                    {
                        "name": "Rating-Group",
                        "id": 432
                    },
                    {
                        "name": "Redirect-Address-Type",
                        "id": 433
                    },
                    {
                        "name": "Redirect-Server",
                        "id": 434
                    },
                    {
                        "name": "Redirect-Server-Address",
                        "id": 435
                    },
                    {
                        "name": "Requested-Action",
                        "id": 436
                    },
                    {
                        "name": "Requested-Service-Unit",
                        "id": 437
                    },
                    {
                        "name": "Restriction-Filter-Rule",
                        "id": 438
                    },
                    {
                        "name": "Service-Identifier",
                        "id": 439
                    },
                    {
                        "name": "Service-Parameter-Info",
                        "id": 440
                    },
                    {
                        "name": "Service-Parameter-Type",
                        "id": 441
                    },
                    {
                        "name": "Service-Parameter-Value",
                        "id": 442
                    },
                    {
                        "name": "Subscription-Id",
                        "id": 443
                    },
                    {
                        "name": "Subscription-Id-Data",
                        "id": 444
                    },
                    {
                        "name": "Unit-Value",
                        "id": 445
                    },
                    {
                        "name": "Used-Service-Unit",
                        "id": 446
                    },
                    {
                        "name": "Value-Digits",
                        "id": 447
                    },
                    {
                        "name": "Validity-Time",
                        "id": 448
                    },
                    {
                        "name": "Final-Unit-Action",
                        "id": 449
                    },
                    {
                        "name": "Subscription-Id-Type",
                        "id": 450
                    },
                    {
                        "name": "Tariff-Time-Change",
                        "id": 451
                    },
                    {
                        "name": "Tariff-Change-Usage",
                        "id": 452
                    },
                    {
                        "name": "G-S-U-Pool-Identifier",
                        "id": 453
                    },
                    {
                        "name": "CC-Unit-Type",
                        "id": 454
                    },
                    {
                        "name": "Multiple-Services-Indicator",
                        "id": 455
                    },
                    {
                        "name": "Multiple-Services-Credit-Control",
                        "id": 456
                    },
                    {
                        "name": "G-S-U-Pool-Reference",
                        "id": 457
                    },
                    {
                        "name": "User-Equipment-Info",
                        "id": 458
                    },
                    {
                        "name": "User-Equipment-Info-Type",
                        "id": 459
                    },
                    {
                        "name": "User-Equipment-Info-Value",
                        "id": 460
                    },
                    {
                        "name": "Service-Context-Id",
                        "id": 461
                    },
                    {
                        "name": "EAP-Payload",
                        "id": 462
                    },
                    {
                        "name": "EAP-Reissued-Payload",
                        "id": 463
                    },
                    {
                        "name": "EAP-Master-Session-Key",
                        "id": 464
                    },
                    {
                        "name": "Accounting-EAP-Auth-Method",
                        "id": 465
                    },
                    {
                        "name": "Accounting-Record-Type",
                        "id": 480
                    },
                    {
                        "name": "Accounting-Realtime-Required",
                        "id": 483
                    },
                    {
                        "name": "Accounting-Record-Number",
                        "id": 485
                    },
                    {
                        "name": "MIP6-Agent-Info",
                        "id": 486
                    },
                    {
                        "name": "MIP-Careof-Address",
                        "id": 487
                    },
                    {
                        "name": "MIP-Authenticator",
                        "id": 488
                    },
                    {
                        "name": "MIP-MAC-Mobility-Data",
                        "id": 489
                    },
                    {
                        "name": "MIP-Timestamp",
                        "id": 490
                    },
                    {
                        "name": "MIP-MN-HA-SPI",
                        "id": 491
                    },
                    {
                        "name": "MIP-MN-HA-MSA",
                        "id": 492
                    },
                    {
                        "name": "Service-Selection",
                        "id": 493
                    },
                    {
                        "name": "MIP6-Auth-Mode",
                        "id": 494
                    },
                    {
                        "name": "TMOD-1",
                        "id": 495
                    },
                    {
                        "name": "Token-Rate",
                        "id": 496
                    },
                    {
                        "name": "Bucket-Depth",
                        "id": 497
                    },
                    {
                        "name": "Peak-Traffic-Rate",
                        "id": 498
                    },
                    {
                        "name": "Minimum-Policed-Unit",
                        "id": 499
                    },
                    {
                        "name": "Maximum-Packet-Size",
                        "id": 500
                    },
                    {
                        "name": "TMOD-2",
                        "id": 501
                    },
                    {
                        "name": "Bandwidth",
                        "id": 502
                    },
                    {
                        "name": "PHB-Class",
                        "id": 503
                    },
                    {
                        "name": "PMIP6-DHCP-Server-Address",
                        "id": 504
                    },
                    {
                        "name": "PMIP6-IPv4-Home-Address",
                        "id": 505
                    },
                    {
                        "name": "Mobile-Node-Identifier",
                        "id": 506
                    },
                    {
                        "name": "Service-Configuration",
                        "id": 507
                    },
                    {
                        "name": "QoS-Resources",
                        "id": 508
                    },
                    {
                        "name": "Filter-Rule",
                        "id": 509
                    },
                    {
                        "name": "Filter-Rule-Precedence",
                        "id": 510
                    },
                    {
                        "name": "Classifier",
                        "id": 511
                    },
                    {
                        "name": "Classifier-ID",
                        "id": 512
                    },
                    {
                        "name": "Protocol",
                        "id": 513
                    },
                    {
                        "name": "Direction",
                        "id": 514
                    },
                    {
                        "name": "From-Spec",
                        "id": 515
                    },
                    {
                        "name": "To-Spec",
                        "id": 516
                    },
                    {
                        "name": "Negated",
                        "id": 517
                    },
                    {
                        "name": "IP-Address",
                        "id": 518
                    },
                    {
                        "name": "IP-Address-Range",
                        "id": 519
                    },
                    {
                        "name": "IP-Address-Start",
                        "id": 520
                    },
                    {
                        "name": "IP-Address-End",
                        "id": 521
                    },
                    {
                        "name": "IP-Address-Mask",
                        "id": 522
                    },
                    {
                        "name": "IP-Mask-Bit-Mask-Width",
                        "id": 523
                    },
                    {
                        "name": "MAC-Address",
                        "id": 524
                    },
                    {
                        "name": "MAC-Address-Mask",
                        "id": 525
                    },
                    {
                        "name": "MAC-Address-Mask-Pattern",
                        "id": 526
                    },
                    {
                        "name": "EUI64-Address",
                        "id": 527
                    },
                    {
                        "name": "EUI64-Address-Mask",
                        "id": 528
                    },
                    {
                        "name": "EUI64-Address-Mask-Pattern",
                        "id": 529
                    },
                    {
                        "name": "Port",
                        "id": 530
                    },
                    {
                        "name": "Port-Range",
                        "id": 531
                    },
                    {
                        "name": "Port-Start",
                        "id": 532
                    },
                    {
                        "name": "Port-End",
                        "id": 533
                    },
                    {
                        "name": "Use-Assigned-Address",
                        "id": 534
                    },
                    {
                        "name": "Diffserv-Code-Point",
                        "id": 535
                    },
                    {
                        "name": "Fragmentation-Flag",
                        "id": 536
                    },
                    {
                        "name": "IP-Option",
                        "id": 537
                    },
                    {
                        "name": "IP-Option-Type",
                        "id": 538
                    },
                    {
                        "name": "IP-Option-Value",
                        "id": 539
                    },
                    {
                        "name": "TCP-Option",
                        "id": 540
                    },
                    {
                        "name": "TCP-Option-Type",
                        "id": 541
                    },
                    {
                        "name": "TCP-Option-Value",
                        "id": 542
                    },
                    {
                        "name": "TCP-Flags",
                        "id": 543
                    },
                    {
                        "name": "TCP-Flag-Type",
                        "id": 544
                    },
                    {
                        "name": "ICMP-Type",
                        "id": 545
                    },
                    {
                        "name": "ICMP-Type-Number",
                        "id": 546
                    },
                    {
                        "name": "ICMP-Code",
                        "id": 547
                    },
                    {
                        "name": "ETH-Option",
                        "id": 548
                    },
                    {
                        "name": "ETH-Proto-Type",
                        "id": 549
                    },
                    {
                        "name": "ETH-Ether-Type",
                        "id": 550
                    },
                    {
                        "name": "ETH-SAP",
                        "id": 551
                    },
                    {
                        "name": "VLAN-ID-Range",
                        "id": 552
                    },
                    {
                        "name": "S-VID-Start",
                        "id": 553
                    },
                    {
                        "name": "S-VID-End",
                        "id": 554
                    },
                    {
                        "name": "C-VID-Start",
                        "id": 555
                    },
                    {
                        "name": "C-VID-End",
                        "id": 556
                    },
                    {
                        "name": "User-Priority-Range",
                        "id": 557
                    },
                    {
                        "name": "Low-User-Priority",
                        "id": 558
                    },
                    {
                        "name": "High-User-Priority",
                        "id": 559
                    },
                    {
                        "name": "Time-Of-Day-Condition",
                        "id": 560
                    },
                    {
                        "name": "Time-Of-Day-Start",
                        "id": 561
                    },
                    {
                        "name": "Time-Of-Day-End",
                        "id": 562
                    },
                    {
                        "name": "Day-Of-Week-Mask",
                        "id": 563
                    },
                    {
                        "name": "Day-Of-Month-Mask",
                        "id": 564
                    },
                    {
                        "name": "Month-Of-Year-Mask",
                        "id": 565
                    },
                    {
                        "name": "Absolute-Start-Time",
                        "id": 566
                    },
                    {
                        "name": "Absolute-Start-Fractional-Seconds",
                        "id": 567
                    },
                    {
                        "name": "Absolute-End-Time",
                        "id": 568
                    },
                    {
                        "name": "Absolute-End-Fractional-Seconds",
                        "id": 569
                    },
                    {
                        "name": "Timezone-Flag",
                        "id": 570
                    },
                    {
                        "name": "Timezone-Offset",
                        "id": 571
                    },
                    {
                        "name": "Treatment-Action",
                        "id": 572
                    },
                    {
                        "name": "QoS-Profile-Id",
                        "id": 573
                    },
                    {
                        "name": "QoS-Profile-Template",
                        "id": 574
                    },
                    {
                        "name": "QoS-Semantics",
                        "id": 575
                    },
                    {
                        "name": "QoS-Parameters",
                        "id": 576
                    },
                    {
                        "name": "Excess-Treatment",
                        "id": 577
                    },
                    {
                        "name": "QoS-Capability",
                        "id": 578
                    },
                    {
                        "name": "QoS-Authorization-Data",
                        "id": 579
                    },
                    {
                        "name": "Bound-Auth-Session-Id",
                        "id": 580
                    },
                    {
                        "name": "Key",
                        "id": 581
                    },
                    {
                        "name": "Key-Type",
                        "id": 582
                    },
                    {
                        "name": "Keying-Material",
                        "id": 583
                    },
                    {
                        "name": "Key-Lifetime",
                        "id": 584
                    },
                    {
                        "name": "Key-SPI",
                        "id": 585
                    },
                    {
                        "name": "Key-Name",
                        "id": 586
                    },
                    {
                        "name": "IKEv2-Nonces",
                        "id": 587
                    },
                    {
                        "name": "Ni",
                        "id": 588
                    },
                    {
                        "name": "Nr",
                        "id": 589
                    },
                    {
                        "name": "IKEv2-Identity",
                        "id": 590
                    },
                    {
                        "name": "Initiator-Identity",
                        "id": 591
                    },
                    {
                        "name": "ID-Type",
                        "id": 592
                    },
                    {
                        "name": "Identification-Data",
                        "id": 593
                    },
                    {
                        "name": "Responder-Identity",
                        "id": 594
                    },
                    {
                        "name": "NC-Request-Type",
                        "id": 595
                    },
                    {
                        "name": "NAT-Control-Install",
                        "id": 596
                    },
                    {
                        "name": "NAT-Control-Remove",
                        "id": 597
                    },
                    {
                        "name": "NAT-Control-Definition",
                        "id": 598
                    },
                    {
                        "name": "NAT-Internal-Address",
                        "id": 599
                    },
                    {
                        "name": "NAT-External-Address",
                        "id": 600
                    },
                    {
                        "name": "Max-NAT-Bindings",
                        "id": 601
                    },
                    {
                        "name": "NAT-Control-Binding-Template",
                        "id": 602
                    },
                    {
                        "name": "Duplicate-Session-Id",
                        "id": 603
                    },
                    {
                        "name": "NAT-External-Port-Style",
                        "id": 604
                    },
                    {
                        "name": "NAT-Control-Record",
                        "id": 605
                    },
                    {
                        "name": "NAT-Control-Binding-Status",
                        "id": 606
                    },
                    {
                        "name": "Current-NAT-Bindings",
                        "id": 607
                    },
                    {
                        "name": "Dual-Priority",
                        "id": 608
                    },
                    {
                        "name": "Preemption-Priority",
                        "id": 609
                    },
                    {
                        "name": "Defending-Priority",
                        "id": 610
                    },
                    {
                        "name": "Admission-Priority",
                        "id": 611
                    },
                    {
                        "name": "SIP-Resource-Priority",
                        "id": 612
                    },
                    {
                        "name": "SIP-Resource-Priority-Namespace",
                        "id": 613
                    },
                    {
                        "name": "SIP-Resource-Priority-Value",
                        "id": 614
                    },
                    {
                        "name": "Application-Level-Resource-Priority",
                        "id": 615
                    },
                    {
                        "name": "ALRP-Namespace",
                        "id": 616
                    },
                    {
                        "name": "ALRP-Value",
                        "id": 617
                    },
                    {
                        "name": "ERP-RK-Request",
                        "id": 618
                    },
                    {
                        "name": "ERP-Realm",
                        "id": 619
                    },
                    {
                        "name": "Redirect-Realm",
                        "id": 620
                    },
                    {
                        "name": "OC-Supported-Features",
                        "id": 621
                    },
                    {
                        "name": "OC-Feature-Vector",
                        "id": 622
                    },
                    {
                        "name": "OC-OLR",
                        "id": 623
                    },
                    {
                        "name": "OC-Sequence-Number",
                        "id": 624
                    },
                    {
                        "name": "OC-Validity-Duration",
                        "id": 625
                    },
                    {
                        "name": "OC-Report-Type",
                        "id": 626
                    },
                    {
                        "name": "OC-Reduction-Percentage",
                        "id": 627
                    },
                    {
                        "name": "ECN-IP-Codepoint",
                        "id": 628
                    },
                    {
                        "name": "Congestion-Treatment",
                        "id": 629
                    },
                    {
                        "name": "Flow-Count",
                        "id": 630
                    },
                    {
                        "name": "Packet-Count",
                        "id": 631
                    },
                    {
                        "name": "IP-Prefix-Length",
                        "id": 632
                    },
                    {
                        "name": "Border-Router-Name",
                        "id": 633
                    },
                    {
                        "name": "64-Multicast-Attributes",
                        "id": 634
                    },
                    {
                        "name": "ASM-mPrefix64",
                        "id": 635
                    },
                    {
                        "name": "SSM-mPrefix64",
                        "id": 636
                    },
                    {
                        "name": "Tunnel-Source-Pref-Or-Addr",
                        "id": 637
                    },
                    {
                        "name": "Tunnel-Source-IPv6-Address",
                        "id": 638
                    },
                    {
                        "name": "Port-Set-Identifier",
                        "id": 639
                    },
                    {
                        "name": "Lw4o6-Binding",
                        "id": 640
                    },
                    {
                        "name": "Lw4o6-External-IPv4-Addr",
                        "id": 641
                    },
                    {
                        "name": "MAP-E-Attributes",
                        "id": 642
                    },
                    {
                        "name": "MAP-Mesh-Mode",
                        "id": 643
                    },
                    {
                        "name": "MAP-Mapping-Rule",
                        "id": 644
                    },
                    {
                        "name": "Rule-IPv4-Addr-Or-Prefix",
                        "id": 645
                    },
                    {
                        "name": "Rule-IPv6-Prefix",
                        "id": 646
                    },
                    {
                        "name": "EA-Field-Length",
                        "id": 647
                    },
                    {
                        "name": "OC-Peer-Algo",
                        "id": 648
                    },
                    {
                        "name": "SourceID",
                        "id": 649
                    },
                    {
                        "name": "Load",
                        "id": 650
                    },
                    {
                        "name": "Load-Type",
                        "id": 651
                    },
                    {
                        "name": "Load-Value",
                        "id": 652
                    },
                    {
                        "name": "User-Equipment-Info-Extension",
                        "id": 653
                    },
                    {
                        "name": "User-Equipment-Info-IMEISV",
                        "id": 654
                    },
                    {
                        "name": "User-Equipment-Info-MAC",
                        "id": 655
                    },
                    {
                        "name": "User-Equipment-Info-EUI64",
                        "id": 656
                    },
                    {
                        "name": "User-Equipment-Info-ModifiedEUI64",
                        "id": 657
                    },
                    {
                        "name": "User-Equipment-Info-IMEI",
                        "id": 658
                    },
                    {
                        "name": "Subscription-Id-Extension",
                        "id": 659
                    },
                    {
                        "name": "Subscription-Id-E164",
                        "id": 660
                    },
                    {
                        "name": "Subscription-Id-IMSI",
                        "id": 661
                    },
                    {
                        "name": "Subscription-Id-SIP-URI",
                        "id": 662
                    },
                    {
                        "name": "Subscription-Id-NAI",
                        "id": 663
                    },
                    {
                        "name": "Subscription-Id-Private",
                        "id": 664
                    },
                    {
                        "name": "Redirect-Server-Extension",
                        "id": 665
                    },
                    {
                        "name": "Redirect-Address-IPAddress",
                        "id": 666
                    },
                    {
                        "name": "Redirect-Address-URL",
                        "id": 667
                    },
                    {
                        "name": "Redirect-Address-SIP-URI",
                        "id": 668
                    },
                    {
                        "name": "QoS-Final-Unit-Indication",
                        "id": 669
                    },
                    {
                        "name": "OC-Maximum-Rate",
                        "id": 670
                    }
]
