# -*- coding: utf-8 -*-
"""
    bromelia._internal_utils
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Defines utility functions that are consumed internally by the library.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import ipaddress
import logging
import os
import struct
import yaml
from collections import namedtuple

from .exceptions import InvalidConfigKey
from .exceptions import InvalidConfigValue
from .definitions import diameter_application_ids
from .definitions import diameter_avps
from .definitions import diameter_command_codes


def convert_to_1_byte(content):
    return struct.pack(">B", content)


def convert_to_2_bytes(content):
    return struct.pack(">H", content)


def convert_to_3_bytes(content):
    return content.to_bytes(3, byteorder="big")


def convert_to_4_bytes(content):
    return struct.pack(">L", content)


def convert_to_8_bytes(content):
    return struct.pack(">q", content)


def convert_to_integer_from_bytes(integer):
    return int.from_bytes(integer, byteorder="big")


def header_representation(header):
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


def application_id_look_up(application_id):
    if not application_id:
        return "", "Unknown"
    
    for application in diameter_application_ids:
        if application["id"] == convert_to_integer_from_bytes(application_id):
            return application["long_name"], application["id"]
    return "", "Unknown"


def command_code_look_up(command_code):
    if not command_code:
        return "", "Unknown"

    for code in diameter_command_codes:
        if code["id"] == convert_to_integer_from_bytes(command_code):
            return code["short_name"], code["id"]
    return "", "Unknown"


def avp_look_up(avp):
    if not avp.get_vendor_id():
        if avp.get_code() == 0:
            return "Unknown"

        for diameter_avp in diameter_avps:
            if diameter_avp["id"] == avp.get_code():
                return diameter_avp["name"]

    return "Unknown"


def _convert_config_to_connection_obj(config):
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

    for key in config.keys():
        if key not in config_mask:
            raise InvalidConfigKey(f"Invalid config key '{key}' found")

    for key, value in config.items():
        if key == "MODE":
            if value not in ["CLIENT", "SERVER"]:
                raise InvalidConfigValue("Invalid config value '{value}' "\
                                f"found for config key '{key}'. It MUST be "\
                                "either 'CLIENT' or 'SERVER'")

            mode = value

        elif key == "APPLICATIONS":
            if value:
                for app in value:
                    app_keys = app.keys()
                    if not [key for key in app_keys if key in ["vendor_id", "app_id"]]:
                        raise InvalidConfigValue("Invalid config value "\
                                        f"found for config key '{key}'. It "\
                                        "MUST be a dictionary with "\
                                        "'vendor_id' and 'app_id' keys")

                    for key in app_keys:
                        if not isinstance(app[key], bytes):
                            raise InvalidConfigValue("Invalid config value "\
                                            f"'{value}' found for config key "\
                                            f"'{key}'. It MUST be a "\
                                            "dictionary with byte value in "\
                                            "each key")


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
                                f"found for config key '{key}'. It MUST "\
                                 "correspond to a valid IPv4 address format")

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
                                f"found for config key '{key}'. It MUST "\
                                 "correspond to a valid IPv4 address format")

        elif key == "PEER_NODE_PORT":
            peer_node_port = value

        elif key == "WATCHDOG_TIMEOUT":
            if not isinstance(value, int):
                raise InvalidConfigValue(f"Invalid config value '{value}' "\
                                f"found for config key '{key}'. It MUST be "\
                                "'int'")

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


def _convert_file_to_config(filepath=None, variables_dictionary=globals()):
    if not filepath:
        filepath = os.path.join(os.getcwd(), "config.yaml")

    try:
        if os.path.exists(filepath):
            config_file = open(filepath, "r")
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
            "WATCHDOG_TIMEOUT": 60
        })

    return configs


def get_app_ids(apps):
    text = ""
    for index, app in enumerate(apps):
        app_name = application_id_look_up(app['app_id'])[0]
        text += f"{app_name};"
        if index == (len(apps) - 1):
            return text[:-1]
