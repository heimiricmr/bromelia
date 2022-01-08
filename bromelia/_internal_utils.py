# -*- coding: utf-8 -*-
"""
    bromelia._internal_utils
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Defines utility functions that are consumed internally by the library.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import datetime
import ipaddress
import logging
import re
import os
import struct
import yaml
from collections import namedtuple

from .definitions import diameter_application_ids
from .definitions import diameter_avps
from .definitions import diameter_command_codes
from .exceptions import InvalidConfigKey
from .exceptions import InvalidConfigValue


LocalNode = namedtuple("LocalNode", [
                                        "host_name",
                                        "realm",
                                        "ip_address",
                                        "port"
                                    ]
)
PeerNode = namedtuple("PeerNode", [
                                        "host_name",
                                        "realm",
                                        "ip_address",
                                        "port"
                                    ]
)
Connection = namedtuple("Connection", [
                                        "name",
                                        "mode",
                                        "local_node",
                                        "peer_node",
                                        "application_ids",
                                        "watchdog_timeout"
                                    ]
)
config_mask = [
                "MODE",
                "APPLICATIONS",
                "LOCAL_NODE_HOSTNAME",
                "LOCAL_NODE_REALM",
                "LOCAL_NODE_IP_ADDRESS",
                "LOCAL_NODE_PORT",
                "PEER_NODE_HOSTNAME",
                "PEER_NODE_REALM",
                "PEER_NODE_IP_ADDRESS",
                "PEER_NODE_PORT",
                "WATCHDOG_TIMEOUT"
]


def convert_to_1_byte(content: int) -> bytes:
    return struct.pack(">B", content)


def convert_to_2_bytes(content: int) -> bytes:
    return struct.pack(">H", content)


def convert_to_3_bytes(content: int) -> bytes:
    return content.to_bytes(3, byteorder="big")


def convert_to_4_bytes(content: int) -> bytes:
    return struct.pack(">L", content)


def convert_to_6_bytes(content: int) -> bytes:
    return content.to_bytes(6, byteorder="big")


def convert_to_8_bytes(content: int) -> bytes:
    return struct.pack(">q", content)


def convert_to_integer_from_bytes(bytes: bytes) -> int:
    return int.from_bytes(bytes, byteorder="big")


def header_representation(header) -> dict:
    cmd_code = header.command_code
    application_id = header.application_id
    
    cmd_code_str, cmd_code_int = command_code_look_up(cmd_code)

    flag_representation = ""
    if header.is_request():
        flag_representation += " REQ|"
        cmd_code_str = cmd_code_str[:3]
    else:
        flag_representation += " "
        cmd_code_str = cmd_code_str[4:]

    if header.is_proxiable():
        flag_representation += "PXY|"

    if header.is_error():
        flag_representation += "ERR|"

    application_id = header.application_id
    app_id_str, app_id_int = application_id_look_up(application_id)

    return {
                "cmd_code_str": cmd_code_str,
                "cmd_code_int": cmd_code_int,
                "flag_representation": flag_representation[:-1],
                "app_id_str": app_id_str,
                "app_id_int": app_id_int
    }


def application_id_look_up(application_id: bytes) -> tuple[str, str]:
    if not application_id:
        return "", "Unknown"
    
    for application in diameter_application_ids:
        if application["id"] == convert_to_integer_from_bytes(application_id):
            return application["long_name"], application["id"]
    return "", "Unknown"


def command_code_look_up(command_code: bytes) -> tuple[str, str]:
    if not command_code:
        return "", "Unknown"

    for code in diameter_command_codes:
        if code["id"] == convert_to_integer_from_bytes(command_code):
            return code["short_name"], code["id"]
    return "", "Unknown"


def avp_look_up(avp) -> str:
    if not avp.get_vendor_id():
        if avp.get_code() == 0:
            return "Unknown"

        for diameter_avp in diameter_avps:
            if diameter_avp["id"] == avp.get_code():
                return diameter_avp["name"]

    return "Unknown"



def _convert_config_to_connection_obj(config) -> Connection:
    for key in config.keys():
        if key not in config_mask:
            raise InvalidConfigKey(f"Invalid config key '{key}' found")

    for key, value in config.items():
        if key == "MODE":
            if value not in ["CLIENT", "SERVER"]:
                raise InvalidConfigValue(f"Invalid config value '{value}' "\
                                         f"found for config key '{key}'. It "\
                                         f"MUST be either 'CLIENT' or 'SERVER'")

            mode = value

        elif key == "APPLICATIONS":
            if value:
                for app in value:
                    app_keys = app.keys()
                    if not [key for key in app_keys if key in ["vendor_id", "app_id"]]:
                        raise InvalidConfigValue(f"Invalid config value "\
                                                 f"found for config key "\
                                                 f"'{key}'. It MUST be a "\
                                                 f"dictionary with "\
                                                 f"'vendor_id' and 'app_id' "\
                                                 f"keys")

                    for key in app_keys:
                        if not isinstance(app[key], bytes):
                            raise InvalidConfigValue(f"Invalid config value "\
                                                     f"'{value}' found for "\
                                                     f"config key '{key}'. It "\
                                                     f"MUST be a dictionary "\
                                                     f"with byte value in "\
                                                     f"each key")


            application_ids = value

        elif key == "LOCAL_NODE_HOSTNAME":
            local_node_host_name = value
        elif key == "LOCAL_NODE_REALM":
            local_node_realm = value
        elif key == "LOCAL_NODE_IP_ADDRESS":
            try:
                ipaddress.IPv4Address(value)
                local_node_ip_address = value

            except ipaddress.AddressValueError:
                raise InvalidConfigValue(f"Invalid config value '{value}' "\
                                         f"found for config key '{key}'. It "\
                                         f"MUST correspond to a valid IPv4 "\
                                         f"address format")

        elif key == "LOCAL_NODE_PORT":
            local_node_port = value

        elif key == "PEER_NODE_HOSTNAME":
            peer_node_host_name = value
        elif key == "PEER_NODE_REALM":
            peer_node_realm = value
        elif key == "PEER_NODE_IP_ADDRESS":
            try:
                ipaddress.IPv4Address(value)
                peer_node_ip_address = value

            except ipaddress.AddressValueError:
                raise InvalidConfigValue(f"Invalid config value '{value}' "\
                                         f"found for config key '{key}'. It "\
                                         f"MUST correspond to a valid IPv4 "\
                                         f"address format")

        elif key == "PEER_NODE_PORT":
            peer_node_port = value

        elif key == "WATCHDOG_TIMEOUT":
            if not isinstance(value, int):
                raise InvalidConfigValue(f"Invalid config value '{value}' "\
                                         f"found for config key '{key}'. It "\
                                         f"MUST be 'int'")

            watchdog_timeout = value

    local_node = LocalNode(host_name=local_node_host_name,
                           realm=local_node_realm,
                           ip_address=local_node_ip_address,
                           port=local_node_port
    )

    peer_node = PeerNode(host_name=peer_node_host_name,
                         realm=peer_node_realm,
                         ip_address=peer_node_ip_address,
                         port=peer_node_port
    )

    connection = Connection(name="bromelia",
                            mode=mode,
                            application_ids=application_ids,
                            local_node=local_node,
                            peer_node=peer_node,
                            watchdog_timeout=watchdog_timeout)

    return connection


def _convert_file_to_config(filepath: str = None, variables_dictionary: dict = globals()) -> list:
    if not filepath:
        filepath = os.path.join(os.getcwd(), "config.yaml")

    try:
        if os.path.exists(filepath):
            with open(filepath, "r") as config_file:
                from_config_file = yaml.load(config_file, Loader=yaml.FullLoader)

    except Exception as e:
        logging.exception(f"_convert_file_to_config - exception: {e}")

    if from_config_file["api_version"] != "v1":
        raise

    configs = list()

    for spec in from_config_file["spec"]:
        for application in spec["applications"]:
            vendor_id = application["vendor_id"]
            app_id = application["app_id"]

            application["vendor_id"] = variables_dictionary[vendor_id]
            application["app_id"] = variables_dictionary[app_id]

        configs.append({
                            "MODE": spec["mode"].upper(),
                            "APPLICATIONS": spec["applications"],
                            "LOCAL_NODE_HOSTNAME": spec["local"]["hostname"],
                            "LOCAL_NODE_REALM": spec["local"]["realm"],
                            "LOCAL_NODE_IP_ADDRESS": spec["local"]["ip_address"],
                            "LOCAL_NODE_PORT": spec["local"]["port"],
                            "PEER_NODE_HOSTNAME": spec["peer"]["hostname"],
                            "PEER_NODE_REALM": spec["peer"]["realm"],
                            "PEER_NODE_IP_ADDRESS": spec["peer"]["ip_address"],
                            "PEER_NODE_PORT": spec["peer"]["port"],
                            "WATCHDOG_TIMEOUT": spec["watchdog_timeout"]
        })

    return configs


def get_app_ids(apps: list) -> str:
    text = ""
    for index, app in enumerate(apps):
        app_name = application_id_look_up(app['app_id'])[0]
        text += f"{app_name};"
        if index == (len(apps) - 1):
            return text[:-1]


def get_app_name(filepath: str = None) -> str:
    if not filepath:
        filepath = os.path.join(os.getcwd(), "config.yaml")

    try:
        if os.path.exists(filepath):
            with open(filepath, "r") as config_file:
                from_config_file = yaml.load(config_file, Loader=yaml.FullLoader)

    except Exception as e:
        logging.exception(f"_convert_file_to_config - exception: {e}")

    if from_config_file["api_version"] != "v1":
        raise

    return from_config_file["name"]


def get_logging_filename(app_name: str = None) -> str:
    if app_name is None:
        name = "dsa"
    else:
        if not isinstance(app_name, str) or app_name == "":
            name = "dsa"
        else:
            pattern = re.findall(r"[\-\+\*\/\\\!\@\#\$\%\&\\(\)\=\~\[\]\{\}]", app_name)
            if pattern:
                raise Exception("Invalid symbol found")

            name = app_name.lower()

    now = datetime.datetime.now()

    #: The filename has the follow format:
    #: log-{name}-{year}-{month}-{day}-{hour}-{minute}-{second}-UTC{utc}-pid_{pid}.log
    return f"log-{name}-"\
           f"{str(now.year).zfill(2)}-"\
           f"{str(now.month).zfill(2)}-"\
           f"{str(now.day).zfill(2)}-"\
           f"{str(now.hour).zfill(2)}-"\
           f"{str(now.minute).zfill(2)}-"\
           f"{str(now.second).zfill(2)}-"\
           f"UTC{str(now.astimezone())[-6:-3]}-"\
           f"pid_{os.getpid()}.log"


def get_avp_name_formatted(key: str) -> str:
    pattern = re.findall(r"(.*)__(\d*)", key)
    if pattern:
        key = pattern[0][0]
        idx = pattern[0][1]
        return f"{key}_avp__{idx}"

    return f"{key}_avp"


class SessionHandler:
    init = 0
    id = 0
    optional = "bromelia"


    def __init__(self):
        SessionHandler.reset()


    @staticmethod
    def get_session_id(data: str, previous: str = None) -> str:
        #: Returns high, low and optional values in order to fulfill the 
        #: recommended format: 
        #: <DiameterIdentity>;<high 32 bits>;<low 32 bits>[;<optional value>]

        SessionHandler._verify_session_id(previous, current=data)

        high = SessionHandler.init
        low = SessionHandler.id
        optional = SessionHandler.optional

        return f"{data};{high};{low};{optional}"


    @staticmethod
    def reset() -> None:
        diff = datetime.datetime.utcnow() - datetime.datetime(1900, 1, 1, 0, 0, 0)
        SessionHandler.init = diff.days*24*60*60 + diff.seconds
        SessionHandler.id = 0


    @staticmethod
    def _verify_session_id(previous: str, current: str) -> None:
        if previous is not None:
            _previous = previous.split(";")

            if _previous:
                if current == _previous[0]:
                    SessionHandler.id += 1
                    return

            SessionHandler.reset()
            return
        
        SessionHandler.id += 1


SessionHandler()