# -*- coding: utf-8 -*-
"""
    bromelia.lib.etsi_3gpp_swm.definitions
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Defines handy structures that are used within the library for the 
    3GPP SWm Application Id.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""


class EapPayload(object):
    """Implementation of EAP Protocol as per IETF RFC 3748.
    """

    __slots__ = ("eap_code", "eap_id", "length", "eap_type", "content")

    def __init__(self, eap_code, eap_id, eap_type, content):          
        self.eap_code = eap_code
        self.eap_id = eap_id
        self.length = 1
        self.eap_type = eap_type
        self.content = content
