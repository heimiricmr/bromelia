# -*- coding: utf-8 -*-
"""
    bromelia.lib.etsi_3gpp_swx
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    A Python package with APIs for handling 3GPP SWx Application Id in the
    bromelia Python Library context.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from .avps import *

from .messages import MultimediaAuthAnswer as MAA
from .messages import MultimediaAuthRequest as MAR

from .messages import RegistrationTerminationAnswer as RTA
from .messages import RegistrationTerminationRequest as RTR

from .messages import ServerAssignmentAnswer as SAA
from .messages import ServerAssignmentRequest as SAR