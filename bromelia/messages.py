# -*- coding: utf-8 -*-
"""
    bromelia.messages
    ~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol base messages.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from .lib.ietf_rfc6733.messages import AbortSessionAnswer as ASA
from .lib.ietf_rfc6733.messages import AbortSessionRequest as ASR

from .lib.ietf_rfc6733.messages import CapabilitiesExchangeAnswer as CEA
from .lib.ietf_rfc6733.messages import CapabilitiesExchangeRequest as CER

from .lib.ietf_rfc6733.messages import DeviceWatchdogAnswer as DWA
from .lib.ietf_rfc6733.messages import DeviceWatchdogRequest as DWR

from .lib.ietf_rfc6733.messages import DisconnectPeerAnswer as DPA
from .lib.ietf_rfc6733.messages import DisconnectPeerRequest as DPR

from .lib.ietf_rfc6733.messages import ReAuthAnswer as RAA
from .lib.ietf_rfc6733.messages import ReAuthRequest as RAR

from .lib.ietf_rfc6733.messages import SessionTerminationAnswer as STA
from .lib.ietf_rfc6733.messages import SessionTerminationRequest as STR

from .lib.ietf_rfc6733.messages import *