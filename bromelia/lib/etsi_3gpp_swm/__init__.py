# -*- coding: utf-8 -*-
"""
    bromelia.lib.etsi_3gpp_swm
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    A Python package with APIs for handling 3GPP SWm Application Id in the
    bromelia Python Library context.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from .avps import *

from .definitions import *

from .messages import AbortSessionAnswer as ASA
from .messages import AbortSessionRequest as ASR

from .messages import DiameterEapAnswer as DEA
from .messages import DiameterEapRequest as DER