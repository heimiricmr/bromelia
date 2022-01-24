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


def decorate_answer(answer, request):
    answer.header.application_id = request.header.application_id
    answer.header.hop_by_hop = request.header.hop_by_hop
    answer.header.end_to_end = request.header.end_to_end

    if request.has_avp("session_id_avp"):
        answer.session_id_avp.data = request.session_id_avp.data
        answer.refresh()

    if (is_3xxx_failure(answer) or
        is_4xxx_failure(answer) or
        is_5xxx_failure(answer)):

        answer.header.set_error_bit(True)

    if answer.has_avp("experimental_result_avp"):
        if answer.has_avp("result_code_avp"):
            answer.pop("result_code_avp")

    return answer


def make_logging(msg):
    if msg.has_avp("user_name"):
        worker_logger.debug(f"Message from Diameter Layer Process: "\
                            f"{application_id_look_up(msg.header.application_id)[0]}, "\
                            f"{msg.header.get_command_code()}, "\
                            f"{msg.header.is_request()}, "\
                            f"{msg.header.hop_by_hop.hex()}, "\
                            f"LEN: {len(msg)}, "\
                            f"USERNAME: {msg.user_name_avp.data}")
    else:
        worker_logger.debug(f"Message from Diameter Layer Process: "\
                            f"{application_id_look_up(msg.header.application_id)[0]}, "\
                            f"{msg.header.get_command_code()}, "\
                            f"{msg.header.is_request()}, "\
                            f"{msg.header.hop_by_hop.hex()}, "\
                            f"LEN: {len(msg)}")


def setup_logging_info(worker, msg):
    return f"[{worker.name}][{msg.header.hop_by_hop.hex()}]"


class WorkerLogger():
    def __init__(self, worker):
        self.worker = worker
        worker_logger.debug(f"Initializing Worker {worker}")


    def debug(self, msg, diameter_message=None, *args, **kwargs):
        if diameter_message is not None:
            hop_by_hop = diameter_message.header.hop_by_hop
            msg = f"[{self.worker.name}] [{hop_by_hop.hex()}] {msg}"
        else:
            msg = f"[{self.worker.name}] {msg}"

        worker_logger.debug(msg, *args, **kwargs)


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
    def __init__(self, msg):
        self.recv_event = threading.Event()
        self.stop_event = threading.Event()
        self.msg = msg


    def wait(self):
        self.recv_event.wait()
        self.recv_event.clear()
        self.stop_event.set()


    def update_msg(self, msg):
        self.msg = msg


    def notify(self):
        self.recv_event.set()
        self.stop_event.wait()


class Worker(multiprocessing.Process):
    associations = dict()
    recv_queues = list()


    def __init__(self, app, manager):
        multiprocessing.Process.__init__(self)
        self.daemon = True
        self.logger = WorkerLogger(self)

        self.is_open = manager.Event()
        self.name = Worker.set_name(app.config["APPLICATIONS"])
        self.app = app

        self.recv_queue = manager.Queue()
        self.send_queue = manager.Queue()

        self.send_event = manager.Event()
        self.send_lock = manager.Lock()
        self.recv_lock = manager.Lock()

        self.pending_answers = dict()

        self.update_associations()
        self.update_recv_queues()

        self.logger.debug(f"Initializing Worker for app {app}")


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


    def send_message(self, message):
        self.app.send_message(message)
        self.send_event.clear()
        self.send_lock.release()


    def send_messages(self, messages):
        self.app.send_messages(messages)
        self.send_event.clear()
        self.send_lock.release()


    def get_incoming_message(self):
        return self.app.get_message()


    def get_outgoing_message(self):
        return self.send_queue.get()


    def set_outgoing_message(self, msg):
        self.send_lock.acquire()
        self.send_queue.put(msg)
        self.send_event.set()


    def get_outgoing_messages(self):
        outgoing_messages = list()
        while not self.send_queue.empty():
            outgoing_message = self.get_outgoing_message()
            outgoing_messages.append(outgoing_message)


    def notify_incoming_message(self, message):
        self.recv_lock.acquire()
        self.recv_queue.put(message)
        self.recv_lock.release()


    def get_pending_answer(self, hop_by_hop):
        return self.pending_answers[hop_by_hop]


    def is_pending_answer(self, msg):
        if msg.header.hop_by_hop in self.pending_answers.keys():
            return True
        return False


    def insert_pending_answer(self, p_answer):
        self.pending_answers.update({p_answer.msg.header.hop_by_hop: p_answer})


    def remove_pending_answer(self, p_answer):
        p_answer.notify()
        self.pending_answers.pop(p_answer.msg.header.hop_by_hop, None)


    def is_send_queue_empty(self):
        if self.send_queue.empty():
            self.logger.debug("The send_queue is empty and there is no "\
                              "notification to go ahead")
            return True
        return False


    def send_handler(self):
        while True:
            if self.is_send_queue_empty():
                self.send_event.wait(timeout=1)

            else:
                self.logger.debug(f"There is/are {self.send_queue.qsize()} "\
                                  f"message(s) available to be sent")

                if self.send_queue.qsize() == 1:
                    outgoing_message = self.get_outgoing_message()
                    self.send_message(outgoing_message)

                elif self.send_queue.qsize() > 1:
                    outgoing_messages = self.get_outgoing_messages()
                    self.send_messages(outgoing_messages)


    def recv_handler(self):
        while True:
            msg = self.get_incoming_message()

            if msg:
                make_logging(msg)
                self.notify_incoming_message(msg)
                self.logger.debug("Putting into recv_queue Queue", msg)


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


    def check_associations_spawned(self):
        while True:
            time.sleep(BROMELIA_LOADING_TICKER)
            if self.associations is not None and self.recv_queues is not None:
                break

    
    def check_associations_ready(self, block=True):
        associations = copy(self.associations)
        while block:
            time.sleep(BROMELIA_LOADING_TICKER)
            if not associations:
                break

            for key in list(associations.keys()):
                association = associations[key]

                if association.is_open.is_set():
                    associations.pop(key)


    def _run(self, debug, is_logging):
        apps = self._create_applications(debug, is_logging)

        bromelia_logger.debug(f"Routes found: {self.routes})")

        with multiprocessing.Manager() as manager:
            for app in apps:
                worker = Worker(app, manager)
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
        self.check_associations_spawned()
        
        #: Block til all Diameter objects are opened in the connection layer
        #: processes - that is, connection are established
        self.check_associations_ready(block)


    def get_incoming_message(self):
        for recv_queue, recv_lock in self.recv_queues:
            if not recv_queue.empty():
                recv_lock.acquire()
                msg = recv_queue.get()
                recv_lock.release()
                return msg


    def get_worker_by_message(self, request):
        return self.associations[request.header.application_id]


    def create_message_thread(self, msg):
        if msg.header.is_request():
            self.request_id += 1
            thrd = threading.Thread(name=f"recv_request_{self.request_id}",
                                    target=self.callback_route,
                                    args=(msg,))
        else:
            self.answer_id += 1
            thrd = threading.Thread(name=f"recv_answer_{self.answer_id}",
                                    target=self.handler_pending_answers,
                                    args=(msg,))

        thrd.start()
        return thrd


    def main(self):
        bromelia_logger.debug(f"Starting Main Bromelia Loop")

        thrds = list()
        while True:
            time.sleep(BROMELIA_TICKER)

            msg = self.get_incoming_message()
            if msg is not None:
                thrd = self.create_message_thread(msg)
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


    def handler_pending_answers(self, msg):
        try:
            self.answer_threshold.wait(timeout=PROCESS_TIMER)
        except threading.BrokenBarrierError:
            self.answer_threshold.reset()

        worker = self.get_worker_by_message(msg)

        logging_info = setup_logging_info(worker, msg)
        bromelia_logger.debug(f"{logging_info} Check if it is an expected "\
                              f"answer")

        if worker.is_pending_answer(msg):
            bromelia_logger.debug(f"{logging_info} Found Hop-By-Hop in "\
                                  f"Pending answer")

            p_answer = worker.get_pending_answer(msg.header.hop_by_hop)
            p_answer.update_msg(msg)

            worker.remove_pending_answer(p_answer)


    def create_error_answer(self, request):
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


    def get_request_callback(self, request):
        application_id = request.header.application_id
        command_code = request.header.command_code

        return self.routes[application_id][command_code]


    def callback_route(self, request):
        try:
            self.request_threshold.wait(timeout=PROCESS_TIMER)
        except threading.BrokenBarrierError:
            self.request_threshold.reset()

        worker = self.get_worker_by_message(request)
        callback_function = self.get_request_callback(request)

        logging_info = setup_logging_info(worker, request)

        try:
            answer = callback_function(request)
        except Exception as e:
            answer = None
            bromelia_logger.exception(f"{logging_info} Error has been "\
                                      f"raised in callback_function: {e.args}")


        if not isinstance(answer, DiameterAnswer):
            bromelia_logger.exception(f"{logging_info} There is no answer "\
                                      f"processed to be sent. We are sending "\
                                      f"UNABLE_TO_COMPLY")

            answer = self.create_error_answer(request)
            self.send_message(answer)

            raise BromeliaException("Route function must return "\
                                    "DiameterAnswer object")


        answer = decorate_answer(answer, request)
        self.send_message(answer)

        bromelia_logger.debug(f"{logging_info} Sending answer")


    def send_message(self, msg, recv_answer=True):
        if self.associations is None:
            return self.testing_answer
            
        worker = self.get_worker_by_message(msg)

        logging_info = setup_logging_info(worker, msg)
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

        worker.set_outgoing_message(msg)
        bromelia_logger.debug(f"{logging_info} Just put message into "\
                              f"send_queue Queue and notified send_event Event")

        if msg.header.is_request() and recv_answer:
            p_answer = PendingAnswer(msg)

            worker.insert_pending_answer(p_answer)
            bromelia_logger.debug(f"{logging_info} Added Pending answer")

            p_answer.wait()
            bromelia_logger.debug(f"{logging_info} Notification from "\
                                  f"Pending answer")

            return p_answer.msg


    def load_messages_into_application_id(self, msgs, application_id):
        def decorated_message(msg):
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

                if issubclass(msg, DiameterRequest):
                    request_attrs = {"destination_realm": peer_node_realm}
                    attrs.update(**request_attrs)

                if "session_id" in msg.mandatory:
                    attrs.update({"session_id": local_node_hostname})

                return msg(**attrs)

            return proxy

        application_string = get_application_string_by_id(application_id)
        self.__dict__.update({application_string: SimpleNamespace()})

        for msg in msgs:
            _name = [letter for letter in msg.__name__ if letter.isupper()]
            short_message_name = "".join(_name).upper()

            setattr(self.__dict__[application_string], 
                    short_message_name, 
                    decorated_message(msg))


    def get_route(self, route_name):
        return self._routes[route_name]