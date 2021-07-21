# -*- coding: utf-8 -*-
"""
    bromelia.config
    ~~~~~~~~~~~~~~~

    This module contains configuration structures.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import logging
import os

BASEDIR = os.getcwd()

#: Configs for statemachine.py module
STATE_MACHINE_TICKER = 0.0001

CLOSED = "Closed"
WAIT_CONN_ACK = "Wait-Conn-Ack"
WAIT_I_CEA = "Wait-I-CEA"
WAIT_CONN_ACK_ELECT = "Wait-Conn-Ack/Elect"
WAIT_RETURNS = "Wait-Returns"
I_OPEN = "I-Open"
R_OPEN = "R-Open"
OPEN = "Open"
CLOSING = "Closing"

#: Configs for setup.py module
SEND_BUFFER_MAXIMUM_SIZE = 4096*64
LISTENING_TICKER = 0.01
WAITING_CONN_TIMER = 2
SLEEP_TIMER = 4

#: Configs for bromelia.py module
BROMELIA_TICKER = STATE_MACHINE_TICKER
BROMELIA_LOADING_TICKER = 0.1
SEND_THRESHOLD_TICKER = 0.05
PROCESS_TIMER = 0.001

REQUEST_THRESHOLD = 10
ANSWER_THRESHOLD = 10
SEND_THRESHOLD = 30

#: Configs for transport.py module
TRACKING_SOCKET_EVENTS_TIMEOUT = 1

class Config(dict):
    def __init__(self, defaults=None):
        dict.__init__(self, defaults or {})


class DiameterLogging(object):
    LOGGING_FORMAT = "%(asctime)s [%(levelname)s] [%(process)d] "\
                    "[%(thread)d:%(threadName)s] %(module)s [%(name)s] "\
                    "[%(funcName)s]: %(message)s"

    LOGGING_DATE_FMT = "%Y-%m-%d %H:%M:%S,uuu"
    LOGGING_PATH = os.path.join(BASEDIR, f"dsa_{os.getpid()}.log")

    def __init__(self, debug=False, is_logging=False):
        if debug:
            DiameterLogging.LOGGING_LEVEL = logging.DEBUG
        else:
            DiameterLogging.LOGGING_LEVEL = logging.INFO

        if is_logging:
            logging.basicConfig(level=DiameterLogging.LOGGING_LEVEL,
                                format=DiameterLogging.LOGGING_FORMAT,
                                filename=DiameterLogging.LOGGING_PATH,
                                filemode="a")
