# -*- coding: utf-8 -*-
"""
    bromelia.process
    ~~~~~~~~~~~~~~~~

    This module contains all implementations for handling the Diameter 
    messages processing step. It contains classes for creating and 
    parsing Diameter Requests and Answers.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""
import base64
import logging

from .avps import *
from .constants import *
from .exceptions import ProcessRequestException

process_message_logging = logging.getLogger("ProcessDiameterMessage")


def process_request(association, message):
    logging.debug("Processing Diameter Request.")
    list_of_avps_by_code = [avp.code for avp in message.avps]

    connection = association.connection

    local_node_host_name = connection.local_node.host_name.encode("utf-8")
    local_node_realm = connection.local_node.realm.encode("utf-8")

    if DESTINATION_HOST_AVP_CODE in list_of_avps_by_code:
        if not list(filter(lambda avp: avp.data == local_node_host_name, message.avps)):
            logging.debug("Diameter Request has Destination-Host AVP, "\
                          "however it was addressed to another node.")
            
            raise ProcessRequestException("Request does not comply with "\
                                          "local consumption rules.")

        logging.debug("Diameter Request has Destination-Host AVP and "\
                      "contains the hostname of local node.")

    elif (DESTINATION_HOST_AVP_CODE not in list_of_avps_by_code and 
          DESTINATION_REALM_AVP_CODE in list_of_avps_by_code):

        if not list(filter(lambda avp: avp.data == local_node_realm, message.avps)):
            logging.debug("Diameter Request does not include "\
                          "Destination-Host AVP, but it does "\
                          "include an invalid Destination-Realm "\
                          "AVP which was addressed to another realm.")

            raise ProcessRequestException("Request does not comply with "\
                                          "local consumption rules.")

        logging.debug("Diameter Request does not include Destination-Host "\
                      "AVP, but it does include a valid Destination-Realm "\
                      "AVP which contains realm of local node.")
        
    elif (DESTINATION_HOST_AVP_CODE not in list_of_avps_by_code and 
          DESTINATION_REALM_AVP_CODE not in list_of_avps_by_code):

        logging.debug("Diameter Request does not include neither "\
                      "Destination-Host AVP nor Destination-Realm AVP.")

    else:
        raise ProcessRequestException("Request does not comply with local "\
                                      "consumption rules.")

    """
    PUT HERE code to create a function or objects to call for process a
    specific Diameter request which is not part of the DEFAULT DIAMETER APPLICATION
    """

    association.postprocess_recv_requests.put(message)
    association.postprocess_recv_requests_lock.acquire()
    association.num_requests += 1
    association.postprocess_recv_requests_ready.set()


def process_answer(association, message):
    logging.debug("Processing Diameter Answer.")

    association.postprocess_recv_answers_lock.acquire()

    end_to_end_key = message.header.end_to_end.hex()
    hop_by_hop_key = message.header.hop_by_hop.hex()

    if end_to_end_key in association.end_to_end_identifiers:

        if hop_by_hop_key in association.pending_requests:

            if message.header.end_to_end == association.pending_requests[hop_by_hop_key].header.end_to_end:

                association.pending_requests.pop(hop_by_hop_key)
                association.postprocess_recv_answers.update({hop_by_hop_key: message})
                association.num_answers += 1
                association.postprocess_recv_answers_ready.set()

            else:
                pass
                """suspicious peer"""

        else:
            pass
            """detected multiple identical answers, which MAY be received 
            as a result of a failover. PUT HERE code to start procedure to 
            pass the connection handler to another diameter association.
            """
    
    association.postprocess_recv_answers_lock.release()


class ProcessDiameterMessage:
    @staticmethod
    def process_answer_from_existing_pending_request(association, message):
        process_message_logging.debug("Processing Diameter Answer.")

        end_to_end_key = message.header.end_to_end.hex()
        hop_by_hop_key = message.header.hop_by_hop.hex()

        if end_to_end_key in association.end_to_end_identifiers:
            if hop_by_hop_key in association.pending_requests:
                if message.header.end_to_end == association.pending_requests[hop_by_hop_key].header.end_to_end:
                    association.pending_requests.pop(hop_by_hop_key)
                else:
                    pass
                    """suspicious peer"""

            else:
                pass
                """detected multiple identical answers, which MAY be received 
                as a result of a failover. PUT HERE code to start procedure to 
                pass the connection handler to another diameter association.
                """
    
    @staticmethod
    def is_valid_origin_host_avp(avp, connection):
        if avp.code == ORIGIN_HOST_AVP_CODE:
            
            process_message_logging.debug(f"Origin-Host AVP validation.")

            checklist_mandatory_info = 0
        
            process_message_logging.debug(f"flags: {avp.get_flags()}.")
            if avp.flags == FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED:
                checklist_mandatory_info += 1
            
            process_message_logging.debug(f"length: {avp.get_length()}.")
            if avp.get_length() == AVP_HEADER_LENGTH + len(avp.data):
                checklist_mandatory_info += 1

            data = avp.data.decode("utf-8")
            process_message_logging.debug(f"data: {data}.")
            if data == connection.peer_node.host_name:
                checklist_mandatory_info += 1


            if checklist_mandatory_info == 3:
                process_message_logging.debug(f"Result: PASS.")
                return True
            process_message_logging.debug(f"Result: FAIL.")
            return False


    @staticmethod
    def is_valid_origin_realm_avp(avp, connection):
        if avp.code == ORIGIN_REALM_AVP_CODE:
            process_message_logging.debug(f"Origin-Realm AVP validation.")

            checklist_mandatory_info = 0
        
            process_message_logging.debug(f"flags: {avp.get_flags()}.")
            if avp.flags == FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED:
                checklist_mandatory_info += 1
            
            process_message_logging.debug(f"length: {avp.get_length()}.")
            if avp.get_length() == AVP_HEADER_LENGTH + len(avp.data):
                checklist_mandatory_info += 1

            data = avp.data.decode("utf-8")
            process_message_logging.debug(f"data: {data}.")
            if data == connection.peer_node.realm:
                checklist_mandatory_info += 1


            if checklist_mandatory_info == 3:
                process_message_logging.debug(f"Result: PASS.")
                return True
            process_message_logging.debug(f"Result: FAIL.")
            return False


    @staticmethod
    def is_valid_origin_state_id_avp(avp, connection):
        if (avp.code == ORIGIN_STATE_ID_AVP_CODE):
            return True
        return False


    @staticmethod
    def is_valid_result_code_avp(avp):
        if avp.code == RESULT_CODE_AVP_CODE:
            
            process_message_logging.debug(f"Result-Code AVP validation.")

            checklist_mandatory_info = 0
        
            process_message_logging.debug(f"flags: {avp.get_flags()}.")
            if avp.flags == FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED:
                checklist_mandatory_info += 1
            
            process_message_logging.debug(f"length: {avp.get_length()}.")
            if avp.get_length() == AVP_LENGTH_UNSIGNED32:
                checklist_mandatory_info += 1

            process_message_logging.debug(f"data: {avp.data.hex()}.")


            if checklist_mandatory_info == 2:
                process_message_logging.debug(f"Result: PASS.")
                return True
            process_message_logging.debug(f"Result: FAIL.")
            return False


    @staticmethod
    def is_valid_disconnect_cause_avp(avp):
        if (avp.code == DISCONNECT_CAUSE_AVP_CODE) and (avp.data == DISCONNECT_CAUSE_REBOOTING):
            return True
        return False


    @staticmethod
    def is_valid_host_ip_address_avp(avp, connection):
        if (avp.code == HOST_IP_ADDRESS_AVP_CODE):
            host_ip_address = "{}.{}.{}.{}".format(int(avp.data[2]),int(avp.data[3]),int(avp.data[4]),int(avp.data[5]))
            return True
            # if connection.peer_node.ip_address == host_ip_address:
            #     return True
            # process_message_logging.debug("Host IP Address from Peer Node not valid!")
            # return False


    @staticmethod
    def is_valid_product_name_avp(avp, connection):
        if (avp.code == PRODUCT_NAME_AVP_CODE):
            return True
        return False


    @staticmethod
    def is_valid_vendor_id_avp(avp, connection):
        if (avp.code == VENDOR_ID_AVP_CODE):
            return True
        return False


    @staticmethod
    def is_valid_session_id_avp(avp):
        if avp.code == SESSION_ID_AVP_CODE:
            process_message_logging.debug(f"Session-Id AVP validation.")

            checklist_mandatory_info = 0
        
            process_message_logging.debug(f"flags: {avp.get_flags()}.")
            if avp.flags == FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED:
                checklist_mandatory_info += 1
            
            process_message_logging.debug(f"length: {avp.get_length()}.")
            if avp.get_length() == (AVP_HEADER_LENGTH + len(avp.data)):
                checklist_mandatory_info += 1

            process_message_logging.debug(f"data: {avp.data.hex()}.")


            if checklist_mandatory_info == 2:
                process_message_logging.debug(f"Result: PASS.")
                return True
            process_message_logging.debug(f"Result: FAIL.")
            return False


    @staticmethod
    def is_valid_auth_application_id_avp(avp):
        if avp.code == AUTH_APPLICATION_ID_AVP_CODE:
            process_message_logging.debug(f"Auth-Application-Id AVP validation.")

            checklist_mandatory_info = 0
        
            process_message_logging.debug(f"flags: {avp.get_flags()}.")
            if avp.flags == FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED:
                checklist_mandatory_info += 1

            process_message_logging.debug(f"length: {avp.get_length()}.")
            if avp.get_length() == AVP_LENGTH_UNSIGNED32:
                checklist_mandatory_info += 1
        
            #process_message_logging.debug(f"data: {avp.data.hex()}.")
            #if avp.data in AuthApplicationIdAVP.values:
            #    checklist_mandatory_info += 1
        

            if checklist_mandatory_info == 2: # == 3
                process_message_logging.debug(f"Result: PASS.")
                return True
            process_message_logging.debug(f"Result: FAIL.")
            return False


    @staticmethod
    def is_valid_auth_request_type_avp(avp):
        if avp.code == AUTH_REQUEST_TYPE_AVP_CODE:
            process_message_logging.debug(f"Auth-Request-Type AVP validation.")

            checklist_mandatory_info = 0
        
            process_message_logging.debug(f"flags: {avp.get_flags()}.")
            if avp.flags == FLAG_NOT_VENDOR_SPECIFIC_AND_MANDATORY_AND_NOT_PROTECTED:
                checklist_mandatory_info += 1
            
            process_message_logging.debug(f"length: {avp.get_length()}.")
            if avp.get_length() == AVP_LENGTH_INTEGER32:
                checklist_mandatory_info += 1

            process_message_logging.debug(f"data: {avp.data.hex()}.")
            if avp.data in AuthRequestTypeAVP.values:
                checklist_mandatory_info += 1


            if checklist_mandatory_info == 3:
                process_message_logging.debug(f"Result: PASS.")
                return True
            process_message_logging.debug(f"Result: FAIL.")
            return False


class ProcessDeviceWatchdog():
    def __init__(self, association, message):
        self.association = association
        self.connection = association.connection
        self.message = message

        self.checklist_mandatory_avps = 0
        self.checklist_optional_avps = 0
        self.checklist_error_avps = 0
        self.is_valid = False

        if message.header.flags == FLAG_REQUEST:
            self.process_request()
        elif message.header.flags == FLAG_RESPONSE:
            self.process_answer()
        else:
            """What should we do if find an error?"""
            pass


    def process_request(self):
        for avp in self.message.avps:
            if ProcessDiameterMessage.is_valid_origin_host_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_origin_realm_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_origin_state_id_avp(avp, self.connection):
                self.checklist_optional_avps += 1


        if (self.checklist_mandatory_avps == 2) and (self.checklist_optional_avps == 0 or self.checklist_optional_avps == 1):
            self.is_valid = True
        else:
            self.is_valid = False


    def process_answer(self):
        ProcessDiameterMessage.process_answer_from_existing_pending_request(self.association, self.message)

        for avp in self.message.avps:
            if ProcessDiameterMessage.is_valid_result_code_avp(avp):
                self.checklist_mandatory_avps += 1

            if ProcessDiameterMessage.is_valid_origin_host_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_origin_realm_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_origin_state_id_avp(avp, self.connection):
                self.checklist_optional_avps += 1


        if (self.checklist_mandatory_avps == 3) and (self.checklist_optional_avps == 0 or self.checklist_optional_avps == 1):
            self.is_valid = True
        else:
            self.is_valid = False


class ProcessDisconnectPeer():
    def __init__(self, association, message):
        self.association = association
        self.connection = association.connection
        self.message = message

        self.checklist_mandatory_avps = 0
        self.checklist_optional_avps = 0
        self.checklist_error_avps = 0
        self.is_valid = False

        if message.header.flags == FLAG_REQUEST:
            self.process_request()
        elif message.header.flags == FLAG_RESPONSE:
            self.process_answer()
        else:
            """What should we do if find an error?"""
            pass


    def process_request(self):
        for avp in self.message.avps:
            if ProcessDiameterMessage.is_valid_origin_host_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_origin_realm_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_disconnect_cause_avp(avp):
                self.checklist_mandatory_avps += 1


        if (self.checklist_mandatory_avps == 3):
            self.is_valid = True
        else:
            self.is_valid = False


    def process_answer(self):
        ProcessDiameterMessage.process_answer_from_existing_pending_request(self.association, self.message)

        for avp in self.message.avps:
            if ProcessDiameterMessage.is_valid_result_code_avp(avp):
                self.checklist_mandatory_avps += 1

            if ProcessDiameterMessage.is_valid_origin_host_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_origin_realm_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1


        if (self.checklist_mandatory_avps == 3) and (self.checklist_error_avps >= 0 and self.checklist_error_avps <= 2):
            self.is_valid = True
        else:
            self.is_valid = False


class ProcessCapabilityExchange():
    def __init__(self, association, message):
        self.association = association
        self.connection = association.connection
        self.message = message

        self.checklist_mandatory_avps = 0
        self.checklist_optional_avps = 0
        self.checklist_error_avps = 0
        self.is_valid = False

        if message.header.flags == FLAG_REQUEST:
            self.process_request()
        elif message.header.flags == FLAG_RESPONSE:
            self.process_answer()
        else:
            """What should we do if find an error?"""
            pass


    def process_request(self):
        for avp in self.message.avps:
            if ProcessDiameterMessage.is_valid_origin_host_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_origin_realm_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_host_ip_address_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_vendor_id_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_product_name_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_origin_state_id_avp(avp, self.connection):
                self.checklist_optional_avps += 1


        if (self.checklist_mandatory_avps == 5) and (self.checklist_optional_avps >= 0 and self.checklist_optional_avps <= 7):
            self.is_valid = True
        else:
            self.is_valid = False


    def process_answer(self):
        ProcessDiameterMessage.process_answer_from_existing_pending_request(self.association, self.message)
        for avp in self.message.avps:
            if ProcessDiameterMessage.is_valid_result_code_avp(avp):
                self.checklist_mandatory_avps += 1

            if ProcessDiameterMessage.is_valid_origin_host_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_origin_realm_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_host_ip_address_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_vendor_id_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_product_name_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_origin_state_id_avp(avp, self.connection):
                self.checklist_optional_avps += 1


        if (self.checklist_mandatory_avps == 6) and (self.checklist_optional_avps >= 0 or self.checklist_optional_avps <= 7):
            self.is_valid = True
        else:
            self.is_valid = False


def process_device_watchdog(association, message):
    return ProcessDeviceWatchdog(association, message)


def process_disconnect_peer(association, message):
    return ProcessDisconnectPeer(association, message)


def process_capability_exchange(association, message):
    return ProcessCapabilityExchange(association, message)


def process_eap(data):
    eap_code = convert_to_1_byte(data[0])
    eap_id = convert_to_1_byte(data[1])
    eap_length = data[2:4]

    # review each authentication vector parameter (index of list)
    if (eap_code == EAP_CODE_REQUEST):
        eap_type = convert_to_1_byte(data[4])
        eap_aka_subtype = convert_to_1_byte(data[5])
        eap_aka_reserved = data[6:8]

        if (eap_type == EAP_TYPE_UMTS_AUTHENTICATION_AND_KEY_AGREEMENT_EAP):
            if (eap_length == convert_to_2_bytes(8)) and (eap_aka_subtype == NOTIFICATION):
                return {"code": eap_code, "data": None, "subtype": eap_aka_subtype}

            elif (eap_length == convert_to_2_bytes(12)) and (eap_aka_subtype == NOTIFICATION):
                return {"code": eap_code, "data": 4000, "subtype": eap_aka_subtype}

            elif (eap_length == convert_to_2_bytes(68)) and (eap_aka_subtype == AKA_CHALLENGE):
                eap_attr_at_rand = data[9:30]
                eap_attr_at_autn = data[30:51]
                eap_attr_at_mac = data[51:73]

                return {"code": eap_code, "data": base64.b64encode(data).decode("utf-8"), "subtype": eap_aka_subtype}

            elif (eap_length == convert_to_2_bytes(124)) and (eap_aka_subtype == AKA_CHALLENGE):
                eap_attr_at_rand = data[9:30]
                eap_attr_at_autn = data[30:51]
                eap_attr_at_iv = data[51:73]
                eap_attr_at_encr_data = data[73:100]
                eap_attr_at_mac = data[100:21]

                return {"code": eap_code, "data": base64.b64encode(data).decode("utf-8"), "subtype": eap_aka_subtype}

            else:
                logging.info("It looks like we have a bad formated EAP content.")
        
    elif (eap_code == EAP_CODE_FAILURE):
        return {"code": eap_code, "data": None, "subtype": None}

    elif (eap_code == EAP_CODE_SUCCESS):
        return {"code": eap_code, "data": None, "subtype": None}
        

def process_diameter_eap(association, message):
    process = ProcessDiameterEap(association, message)
    return process.is_valid


class ProcessDiameterEap():
    def __init__(self, association, message):
        self.association = association
        self.connection = association.connection
        self.message = message

        self.checklist_mandatory_avps = 0
        self.checklist_optional_avps = 0
        self.checklist_error_avps = 0
        self.is_valid = False

        if message.header.flags == FLAG_REQUEST_AND_PROXYABLE:
            self.process_request()
        elif message.header.flags == FLAG_RESPONSE_AND_PROXYABLE:
            self.process_answer()
        else:
            """What should we do if find an error?"""
            pass


    def process_answer(self):
        ProcessDiameterMessage.process_answer_from_existing_pending_request(self.association, self.message)

        for avp in self.message.avps:
            if ProcessDiameterMessage.is_valid_session_id_avp(avp):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_auth_application_id_avp(avp):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_auth_request_type_avp(avp):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_result_code_avp(avp):
                self.checklist_mandatory_avps += 1

            elif ProcessDiameterMessage.is_valid_origin_realm_avp(avp, self.connection):
                self.checklist_mandatory_avps += 1

        if (self.checklist_mandatory_avps == 5):
            self.is_valid = True
        else:
            self.is_valid = False
