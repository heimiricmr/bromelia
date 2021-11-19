# -*- coding: utf-8 -*-
"""
    bromelia.lib.etsi_3gpp_s13
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    A Python package with APIs for handling 3GPP S13/S13' Application Id in the
    bromelia Python Library context.

    :copyright: (c) 2021-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from .avps import *

from .messages import MeIdentityCheckAnswer as ECA
from .messages import MeIdentityCheckRequest as ECR