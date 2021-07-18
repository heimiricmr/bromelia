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
