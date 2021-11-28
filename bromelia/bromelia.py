# -*- coding: utf-8 -*-
"""
    bromelia.bromelia
    ~~~~~~~~~~~~~~~~~

    This module contains the orchestrator to allow a seamless
    Diameter application implementation.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import logging
import multiprocessing
import sys
import threading
import time
from copy import copy
from types import SimpleNamespace

from ._internal_utils import _convert_file_to_config
from ._internal_utils import application_id_look_up
from ._internal_utils import get_app_name
from .avps import DestinationHostAVP
from .avps import DestinationRealmAVP
from .avps import OriginHostAVP
from .avps import OriginRealmAVP
from .avps import ResultCodeAVP
from .avps import SessionIdAVP
from .base import DiameterAnswer
from .base import DiameterRequest
from .config import *
from .constants import *
from .exceptions import BromeliaException
from .setup import Diameter
from .utils import is_3xxx_failure
from .utils import is_4xxx_failure
from .utils import is_5xxx_failure


worker_logger = logging.getLogger("Worker")
bromelia_logger = logging.getLogger("Bromelia")


def get_application_string_by_id(application_id):
    applications = [ application for application in globals().items() if "DIAMETER_APPLICATION_" in application[0] ]
    for _string, _id in applications:
        if _id == application_id:
            return _string.split("DIAMETER_APPLICATION_")[1].lower()


def get_formatted_answer_as_per_request(answer, request):
    answer.header.application_id = request.header.application_id
    answer.header.hop_by_hop = request.header.hop_by_hop
    answer.header.end_to_end = request.header.end_to_end

    if request.has_avp("session_id_avp"):
        answer.session_id_avp.data = request.session_id_avp.data
        answer.refresh()
    return answer


class Global(object):
    """Helper class to allow the creation of Bromelia attributes on the go. It
    works as a namespace.
    """
    pass


class PendingAnswer:
    """Helper class to allow the pending answer tracking of expected Diameter
    Answers for a set of Diameter Requests. It supports the Bromelia class inner 
    workings.
    """
    def __init__(self):
        self.recv_event = threading.Event()
        self.stop_event = threading.Event()
        self.message = None


class Worker(multiprocessing.Process):
    associations = dict()
    recv_queues = list()


    def __init__(self, app, manager):
        multiprocessing.Process.__init__(self)
        self.daemon = True

        self.name = Worker.set_name(app.config["APPLICATIONS"])
        self.app = app
        self.is_open = manager.Event()

        self.recv_queue = manager.Queue()
        self.send_queue = manager.Queue()

        self.send_event = manager.Event()
        self.send_lock = manager.Lock()
        self.recv_lock = manager.Lock()

        self.pending_answers = dict()

        self.update_associations()
        self.update_recv_queues()

        worker_logger.debug(f"Initializing Worker {self}")


    @staticmethod
    def set_name(applications):
        name = ""
        for application in applications:
            app_name = application_id_look_up(application["app_id"])[0]
            name += f'{app_name};'
        return name[:-1].replace(" ", "_")


    def update_associations(self):
        for application in self.app.config["APPLICATIONS"]:
            association = {application["app_id"]: self}
            Worker.associations.update(association)


    def update_recv_queues(self):
        Worker.recv_queues.append([self.recv_queue, self.recv_lock])


    def send_handler(self):
        while True:
            if self.send_queue.empty():
                worker_logger.debug("The send_queue is empty and there is no "\
                                    "notification to go ahead")

                self.send_event.wait(timeout=1)

                worker_logger.debug("Got go ahead for send_event Event")


            worker_logger.debug(f"[{self.name}] There is/are "\
                                f"{self.send_queue.qsize()} message(s) "\
                                f"available to be sent")

            if self.send_queue.qsize() == 1:
                outgoing_message = self.send_queue.get()
                hop_by_hop = outgoing_message.header.hop_by_hop

                worker_logger.debug(f"[{self.name}][{hop_by_hop.hex()}] "\
                                    f"Sending to endpoint")

                self.app.send_message(outgoing_message)

                self.send_event.clear()
                self.send_lock.release()

            elif self.send_queue.qsize() > 1:
                outgoing_messages = list()

                while not self.send_queue.empty():
                    outgoing_message = self.send_queue.get()
                    hop_by_hop = outgoing_message.header.hop_by_hop

                    outgoing_messages.append(outgoing_message)
                
                    worker_logger.debug(f"[{self.name}][{hop_by_hop.hex()}] "\
                                        f"Sending to endpoint")

                self.app.send_messages(outgoing_messages)

                self.send_event.clear()
                self.send_lock.release()


    def recv_handler(self):
        while True:
            incoming_message = self.app.get_message()

            if incoming_message:
                user_name = None
                if incoming_message.has_avp("user_name_avp"):
                    user_name = incoming_message.user_name_avp.data

                worker_logger.debug(f"Message from Diameter Layer Process: "\
                                    f"{application_id_look_up(incoming_message.header.application_id)[0]}, "\
                                    f"{incoming_message.header.get_command_code()}, "\
                                    f"{incoming_message.header.hop_by_hop.hex()}, "\
                                    f"DATA LENGTH: {len(incoming_message)}, "\
                                    f"USERNAME: {user_name}")
    
                hop_by_hop = incoming_message.header.hop_by_hop

                self.recv_lock.acquire()
                self.recv_queue.put(incoming_message)
                self.recv_lock.release()
    
                worker_logger.debug(f"[{self.name}][{hop_by_hop.hex()}] "\
                                    f"Putting into recv_queue Queue")


    #: it starts under worker.start() call
    def run(self):
        with self.app.context():
            try:
                while self.app.is_open():
                    self.is_open.set()

                    recv_thrd = threading.Thread(name="recv_handler", 
                                                 target=self.recv_handler, 
                                                 daemon=True)

                    send_thrd = threading.Thread(name="send_handler", 
                                                 target=self.send_handler, 
                                                 daemon=True)

                    recv_thrd.start()
                    send_thrd.start()

                    recv_thrd.join()
                    send_thrd.join()

            except KeyboardInterrupt:
                sys.exit(0)

            self.is_open.clear()


    def is_running(self):
        return self.is_open.is_set()


class Bromelia:
    """The Bromelia object implements a WSGI-like application but for Diameter 
    protocol and acts as the central object. It will spin up one or more 
    processes by using the Worker class. The number of processes depends on the 
    number of Diameter interfaces needed for a given Diameter application. 
    
    Each process created by running Worker objects will represent a single 
    Diameter interface sending to / receiving byte stream from a Peer Node. Such
    traffic will be proxied to the centralized process which holds the Bromelia 
    object. The Bromelia object is responsible for process either Diameter 
    requests or Diameter answers according to the Diameter interface and 
    properly forward it to the expected Diameter interface.

    It is strongly recommended to define initially right after the Bromelia
    instantiation the set of Diameter messages to be used in each Diameter
    interface.
    
    Usually you create a :class:`Bromelia` instance in your main module.

    Usage::

        >>> from bromelia import Bromelia
        >>> app = Bromelia()
        >>> app.run()
    """

    def __init__(self, config_file=None):
        bromelia_logger.debug(f"Initializing Bromelia application")
        self.config_file = config_file
        self.configs = _convert_file_to_config(self.config_file, globals())
        self.app_name = get_app_name(self.config_file)
        self.routes = {}
        self._routes = {}
        self.sessions = {}
        self.g = Global()
        self.testing_answer = None
        
        self.recv_queues = None
        self.associations = None

        self.request_threshold = threading.Barrier(parties=REQUEST_THRESHOLD)
        self.request_id = 0

        self.answer_threshold = threading.Barrier(parties=ANSWER_THRESHOLD)
        self.answer_id = 0

        self.send_threshold = threading.Barrier(parties=SEND_THRESHOLD)


    def is_valid_session_key(self, session_key):
        session = self.sessions.get(session_key, None)
        if session is not None:
            return True
        return False


    def _create_applications(self, debug, is_logging):
        apps = list()
        
        for config in self.configs:
          app = Diameter(config=config, 
                         debug=debug, 
                         is_logging=is_logging,
                         app_name=self.app_name)
          apps.append(app)

        return apps


    def _run(self, debug, is_logging):
        apps = self._create_applications(debug, is_logging)

        bromelia_logger.debug(f"Route found: {self.routes})")

        with multiprocessing.Manager() as manager:
            for app in apps:
                bromelia_logger.debug(f"Initializing Worker for app {app}")
                worker = Worker(app, manager)

                bromelia_logger.debug(f"Starting Worker for app {app}")
                worker.start()

            self.recv_queues = Worker.recv_queues
            self.associations = Worker.associations

            bromelia_logger.debug(f"Loading recv_queues: {self.recv_queues}")
            bromelia_logger.debug(f"Loading associations: {self.associations}")

            self.main()


    def run(self, debug=False, is_logging=False, block=True):
        threading.Thread(target=self._run, 
                         args=(debug, is_logging)).start()

        #: Wait spinning up Diameter objects in the connection layer processes
        while True:
            time.sleep(BROMELIA_LOADING_TICKER)
            if self.associations is not None and self.recv_queues is not None:
                break

        #: Block til all Diameter objects are opened in the connection layer
        #: processes - that is, connection are established
        associations = copy(self.associations)
        while block:
            time.sleep(BROMELIA_LOADING_TICKER)
            if not associations:
                break

            for key in list(associations.keys()):
                association = associations[key]

                if association.is_open.is_set():
                    associations.pop(key)


    def main(self):
        bromelia_logger.debug(f"Starting Main Bromelia Loop")

        thrds = list()
        while True:
            time.sleep(BROMELIA_TICKER)

            for recv_queue, recv_lock in self.recv_queues:
                if not recv_queue.empty():
                    recv_lock.acquire()
                    message = recv_queue.get()
                    recv_lock.release()
                    
                    if message.header.is_request():
                        thrd = threading.Thread(name=f"recv_request_{self.request_id}", 
                                                target=self.callback_route, 
                                                args=(message,))
                        self.request_id += 1

                    else:
                        thrd = threading.Thread(name=f"recv_answer_{self.answer_id}", 
                                                target=self.handler_pending_answers, 
                                                args=(message,))
                        self.answer_id += 1

                    thrd.start()
                    thrds.append(thrd)

            for thrd in thrds:
                if not thrd.is_alive():
                    thrd.join()
                    thrds.remove(thrd)


    def route(self, application_id, command_code):
        def outer_function(route_function):
            def inner_function(*args, **kwargs):
                if application_id not in self.routes:
                    _route = {application_id: {command_code: route_function}}
                    self.routes.update(_route)
                else:
                    _command_code = {command_code: route_function}
                    self.routes[application_id].update(_command_code)

                self._routes.update({route_function.__name__: route_function})

            return inner_function()
        return outer_function


    def handler_pending_answers(self, message):
        try:
            self.answer_threshold.wait(timeout=PROCESS_TIMER)
        except threading.BrokenBarrierError:
            self.answer_threshold.reset()

        application_id = message.header.application_id
        hop_by_hop = message.header.hop_by_hop
        
        worker = self.associations[application_id]
        logging_info = f"[{worker.name}][{hop_by_hop.hex()}]"\
                       f"[PENDING:{len(worker.pending_answers)}]"

        bromelia_logger.debug(f"{logging_info} Check if it is an expected "\
                              f"answer")

        if hop_by_hop in worker.pending_answers.keys():
            bromelia_logger.debug(f"{logging_info} Found Hop-By-Hop in "\
                                  f"Pending answer")

            pending_answer = worker.pending_answers[hop_by_hop]

            pending_answer.message = message
            bromelia_logger.debug(f"{logging_info} Update Pending answer "\
                                  f"with the received answer")

            pending_answer.recv_event.set()
            pending_answer.stop_event.wait()

            worker.pending_answers.pop(message.header.hop_by_hop, None)


    def get_error_answer_for_request(self, request):
        application_id = request.header.application_id

        config = self.associations[application_id].app.config
        avps = [
                    SessionIdAVP(request.session_id_avp.data),
                    ResultCodeAVP(DIAMETER_UNABLE_TO_COMPLY),
                    OriginHostAVP(config["LOCAL_NODE_HOSTNAME"]),
                    OriginRealmAVP(config["LOCAL_NODE_REALM"]),
                    DestinationRealmAVP(request.origin_realm_avp.data),
                    DestinationHostAVP(request.origin_host_avp.data)
        ]

        return DiameterAnswer(header=request.header, avps=avps)


    def callback_route(self, request):
        try:
            self.request_threshold.wait(timeout=PROCESS_TIMER)
        except threading.BrokenBarrierError:
            self.request_threshold.reset()

        application_id = request.header.application_id
        command_code = request.header.command_code
        hop_by_hop = request.header.hop_by_hop

        worker = self.associations[application_id]
        logging_info = f"[{worker.name}][{hop_by_hop.hex()}]"

        callback_function = self.routes[application_id][command_code]
        bromelia_logger.debug(f"{logging_info} {callback_function}")

        try:
            answer = callback_function(request)

        except Exception as e:
            bromelia_logger.exception(f"{logging_info} Error has been "\
                                      f"raised in callback_function: {e.args}")
            answer = None

        if not isinstance(answer, DiameterAnswer):
            bromelia_logger.exception(f"{logging_info} There is no answer "\
                                      f"processed to be sent. We are sending "\
                                      f"UNABLE_TO_COMPLY")

            error_answer = self.get_error_answer_for_request(request)
            self.send_message(error_answer)

            raise BromeliaException("Route function must return "\
                                    "DiameterAnswer object")


        answer = get_formatted_answer_as_per_request(answer, request)

        if (is_3xxx_failure(answer) or 
            is_4xxx_failure(answer) or 
            is_5xxx_failure(answer)):

            answer.header.set_error_bit(True)

        if answer.has_avp("experimental_result_avp"):
            if answer.has_avp("result_code_avp"):
                answer.pop("result_code_avp")


        bromelia_logger.debug(f"{logging_info} Sending answer")
        self.send_message(answer)


    def send_message(self, message, recv_answer=True):
        application_id = message.header.application_id
        hop_by_hop = message.header.hop_by_hop

        if self.associations is None:
            return self.testing_answer
            
        worker = self.associations[application_id]
        logging_info = f"[{worker.name}][{hop_by_hop.hex()}]"

        bromelia_logger.debug(f"{logging_info} Application needs to send a "\
                              f"message")
        
        if not worker.is_running():
            bromelia_logger.debug(f"{logging_info} It seems the worker is "\
                                  f"not running anymore")
            return None

        bromelia_logger.debug(f"{logging_info} Putting message into "\
                              f"send_queue Queue")

        try:
            self.send_threshold.wait(timeout=SEND_THRESHOLD_TICKER)
        except threading.BrokenBarrierError:
            self.send_threshold.reset()

        worker.send_lock.acquire()
        worker.send_queue.put(message)
        worker.send_event.set()

        bromelia_logger.debug(f"{logging_info} Just put message into "\
                              f"send_queue Queue and notified send_event Event")

        if message.header.is_request() and recv_answer:
            pending_answer = PendingAnswer()
            worker.pending_answers.update({hop_by_hop: pending_answer})
            bromelia_logger.debug(f"{logging_info} Added Pending answer")

            pending_answer.recv_event.wait()
            bromelia_logger.debug(f"{logging_info} Notification from "\
                                  f"Pending answer")

            pending_answer.recv_event.clear()
            pending_answer.stop_event.set()
            bromelia_logger.debug(f"{logging_info} Cleanup of Pending answer")

            return pending_answer.message


    def load_messages_into_application_id(self, messages, application_id):
        def decorated_message(message):
            def proxy(**attrs):
                _config = None

                for config in self.configs:
                    for application in config["APPLICATIONS"]:
                        if application["app_id"] == application_id:
                            _config = config

                default_attrs = {
                            "origin_host": _config["LOCAL_NODE_HOSTNAME"],
                            "origin_realm": _config["LOCAL_NODE_REALM"],
                }

                attrs.update(**default_attrs)

                peer_node_realm = _config["PEER_NODE_REALM"]
                local_node_hostname = _config["LOCAL_NODE_HOSTNAME"]

                if issubclass(message, DiameterRequest):
                    request_attrs = {"destination_realm": peer_node_realm}
                    attrs.update(**request_attrs)

                if "session_id" in message.mandatory:
                    attrs.update({"session_id": local_node_hostname})

                return message(**attrs)

            return proxy

        application_string = get_application_string_by_id(application_id)
        self.__dict__.update({application_string: SimpleNamespace()})

        for message in messages:
            _name = [letter for letter in message.__name__ if letter.isupper()]
            short_message_name = "".join(_name).upper()

            setattr(self.__dict__[application_string], 
                    short_message_name, 
                    decorated_message(message))


    def get_route(self, route_name):
        return self._routes[route_name]