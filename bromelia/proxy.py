# -*- coding: utf-8 -*-
"""
    bromelia.proxy
    ~~~~~~~~~~~~~~

    This module contains the BaseMessages class necessary to instantiate
    the DiameterAssociation class. It allows define the set of base messages
    of Diameter protocol which will be used in a specific connection. Besides
    that, it allows to customize the base messages content as per RFC 6733.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from typing import Any, List

from ._internal_utils import Connection
from .constants import *
from .avps import AuthApplicationIdAVP
from .avps import VendorIdAVP
from .avps import VendorSpecificApplicationIdAVP
from .messages import CEA
from .messages import CER
from .messages import DWA
from .messages import DWR
from .messages import DPA
from .messages import DPR


class BaseMessages:
    def __init__(self,
                 cer: CER,
                 cea: CEA,
                 dwr: DWR,
                 dwa: DWA,
                 dpr: DPR,
                 dpa: DPA) -> None:
        self.cer = cer
        self.cea = cea
        self.dwr = dwr
        self.dwa = dwa
        self.dpr = dpr
        self.dpa = dpa


class DiameterBaseProxy:
    def __init__(self, connection: Connection) -> None:
        self.connection = connection


    def get_default_messages(self) -> BaseMessages:
        return BaseMessages(cer=DiameterBaseProxy.load_cer(self.connection),
                            cea=DiameterBaseProxy.load_cea(self.connection), 
                            dwr=DiameterBaseProxy.load_dwr(self.connection), 
                            dwa=DiameterBaseProxy.load_dwa(self.connection), 
                            dpr=DiameterBaseProxy.load_dpr(self.connection), 
                            dpa=DiameterBaseProxy.load_dpa(self.connection))


    def get_custom_messages(self, msgs: List[Any] = None) -> BaseMessages:
        base = dict()

        if msgs is not None:
            for msg in msgs:
                if isinstance(msg, CER):
                    base.update({"cer": msg})
                elif isinstance(msg, CEA):
                    base.update({"cea": msg})
                elif isinstance(msg, DWR):
                    base.update({"dwr": msg})
                elif isinstance(msg, DWA):
                    base.update({"dwa": msg})
                elif isinstance(msg, DPR):
                    base.update({"dpr": msg})
                elif isinstance(msg, DPA):
                    base.update({"dpa": msg})

        if "cea" not in base.keys():
            base.update({"cea": DiameterBaseProxy.load_cea(self.connection)})

        if "cer" not in base.keys():
            base.update({"cer": DiameterBaseProxy.load_cer(self.connection)})

        if "dwa" not in base.keys():
            base.update({"dwa": DiameterBaseProxy.load_dwa(self.connection)})

        if "dwr" not in base.keys():
            base.update({"dwr": DiameterBaseProxy.load_dwr(self.connection)})

        if "dpa" not in base.keys():
            base.update({"dpa": DiameterBaseProxy.load_dpa(self.connection)})

        if "dpr" not in base.keys():
            base.update({"dpr": DiameterBaseProxy.load_dpr(self.connection)})

        return BaseMessages(**base)


    @staticmethod
    def load_cer(connection: Connection) -> CER:
        if isinstance(connection.application_ids, dict):
            application = connection.application_ids
            avps = {
                    "origin_host": connection.local_node.host_name,
                    "origin_realm": connection.local_node.realm,
                    "host_ip_address": connection.local_node.ip_address,
                    "vendor_id": VENDOR_ID_DEFAULT,
                    "auth_application_id": application["app_id"]
            }
            cer = CER(**avps)

        elif isinstance(connection.application_ids, list):
            avps = {
                    "origin_host": connection.local_node.host_name,
                    "origin_realm": connection.local_node.realm,
                    "host_ip_address": connection.local_node.ip_address,
                    "vendor_id": VENDOR_ID_DEFAULT,
            }
            cer = CER(**avps)

            applications = connection.application_ids
            for application in applications:
                vendor_id_avp = VendorIdAVP(application["vendor_id"])
                auth_app_id_avp = AuthApplicationIdAVP(application["app_id"])

                avp = VendorSpecificApplicationIdAVP([
                                                        vendor_id_avp, 
                                                        auth_app_id_avp
                ])

                cer.append(avp)

        return cer


    @staticmethod
    def load_cea(connection: Connection) -> CEA:
        if isinstance(connection.application_ids, dict):
            application = connection.application_ids
            avps = {
                    "origin_host": connection.local_node.host_name,
                    "origin_realm": connection.local_node.realm,
                    "host_ip_address": connection.local_node.ip_address,
                    "vendor_id": VENDOR_ID_DEFAULT,
                    "auth_application_id": application["app_id"],
            }
            cea = CEA(**avps)

        elif isinstance(connection.application_ids, list):
            avps = {
                    "origin_host": connection.local_node.host_name,
                    "origin_realm": connection.local_node.realm,
                    "host_ip_address": connection.local_node.ip_address,
                    "vendor_id": VENDOR_ID_DEFAULT,
            }
            cea = CEA(**avps)

            applications = connection.application_ids
            for application in applications:
                vendor_id_avp = VendorIdAVP(application["vendor_id"])
                auth_app_id_avp = AuthApplicationIdAVP(application["app_id"])

                avp = VendorSpecificApplicationIdAVP([
                                                        vendor_id_avp, 
                                                        auth_app_id_avp
                ])

                cea.append(avp)

        return cea


    @staticmethod
    def load_dwr(connection: Connection) -> DWR:
        avps = {
                "origin_host": connection.local_node.host_name,
                "origin_realm": connection.local_node.realm,
        }            
        return DWR(**avps)


    @staticmethod
    def load_dwa(connection: Connection) -> DWA:
        avps = {
                "origin_host": connection.local_node.host_name,
                "origin_realm": connection.local_node.realm,
        }
        return DWA(**avps)


    @staticmethod
    def load_dpr(connection: Connection) -> DPR:
        avps = {
                "origin_host": connection.local_node.host_name,
                "origin_realm": connection.local_node.realm,
        }            
        return DPR(**avps)


    @staticmethod
    def load_dpa(connection: Connection) -> DPA:
        avps = {
                "origin_host": connection.local_node.host_name,
                "origin_realm": connection.local_node.realm,
        }
        return DPA(**avps)
