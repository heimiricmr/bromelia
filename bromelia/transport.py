# -*- coding: utf-8 -*-
"""
    bromelia.transport
    ~~~~~~~~~~~~~~~~~~

    This module defines the TCP transport layer connections that are used
    by the Diameter application protocol underlying.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import copy
import logging
import random
import selectors
import socket
import threading
from typing import Any, Literal

from .config import TRACKING_SOCKET_EVENTS_TIMEOUT

tcp_connection = logging.getLogger("TcpConnection")
tcp_client = logging.getLogger("TcpClient")
tcp_server = logging.getLogger("TcpServer")


class TcpConnection():
    def __init__(self, local_ip_address: str, local_port: str = 0, peer_ip_address: str = '', peer_port: str = 0) -> None:
        self._recv_buffer = b""
        self._send_buffer = b""
        self.send_data_stream_queued = False
        self.data_stream = b""
        self._recv_data_stream = b""

        self._recv_data_available = threading.Event()
        self.write_mode_on = threading.Event()
        self.read_mode_on = threading.Event()

        self.lock = threading.Lock()

        self.recv_data_consumed = False

        self.local_ip_address = local_ip_address
        self.local_port = local_port
        self.peer_ip_address = peer_ip_address
        self.peer_port = peer_port

        self.sock = None
        self.is_connected = False
        self.sock_id = "".join(random.choice('0123456789ABCDEF') for i in range(16))

        tcp_connection.debug(f"Creating Socket with ID {self.sock_id}")

        self._stop_threads = False

        self.selector = selectors.DefaultSelector()
        self.tracking_events_count = 0
        self.connection_attempts = 3

        self.events_mask = selectors.EVENT_READ


    def is_write_mode(self) -> bool:
        if self.events_mask & selectors.EVENT_WRITE:
            return True
        return False


    def is_read_mode(self) -> bool:
        if self.events_mask & selectors.EVENT_READ:
            return True
        return False

    def is_read_write_mode(self) -> bool:
        if self.events_mask & (selectors.EVENT_READ | selectors.EVENT_WRITE):
            return True
        return False


    def close(self) -> None:
        if not self.is_connected:
            raise ConnectionError("There is no transport connection up for "\
                                  "this PeerNode")

        self.is_connected = False
        try:
            self.selector.unregister(self.sock)
            tcp_connection.debug(f"[Socket-{self.sock_id}] De-registering "\
                                 f"Socket from Selector address: "\
                                 f"{self.selector.get_map()}")

            self.sock.close()
            tcp_connection.debug(f"[Socket-{self.sock_id}] Shutting "\
                                 f"down Socket")

        except KeyError as e:
            tcp_connection.debug(f"[Socket-{self.sock_id}] There is no "\
                                 f"such Selector registered")

        self._stop_threads = True


    def run(self) -> None:
        if not self.is_connected:
            raise ConnectionError(f"[Socket-{self.sock_id}] There is no "\
                                  f"transport connection up for this Peer")
        threading.Thread(name="transport_layer_thread",
                         target=self._run).start()


    def _run(self) -> None:
        while self.is_connected and not self._stop_threads:
            self.events = self.selector.select(timeout=TRACKING_SOCKET_EVENTS_TIMEOUT)
            self.tracking_events_count += TRACKING_SOCKET_EVENTS_TIMEOUT

            for key, mask in self.events:
                if key.data is not None:
                    self.data_stream += key.data

                if mask & selectors.EVENT_WRITE:
                    tcp_connection.debug(f"Selector notified EVENT_WRITE")
                    self.write()

                if mask & selectors.EVENT_READ:
                    tcp_connection.debug(f"Selector notified EVENT_READ")
                    self.read()


    def _set_selector_events_mask(self, mode: Literal["r", "w", "rw"], msg: Any = None) -> None:
        self.lock.acquire()
        if mode == "r":
            tcp_connection.debug(f"[Socket-{self.sock_id}] Updating "\
                                 f"selector events mask [READ]")

            self.events_mask = selectors.EVENT_READ
            self.selector.modify(self.sock, self.events_mask)
            self.write_mode_on.clear()
            self.read_mode_on.set()

        elif mode == "w":
            tcp_connection.debug(f"[Socket-{self.sock_id}] Updating "\
                                 f"selector events mask [WRITE]")

            self.events_mask = selectors.EVENT_WRITE
            self.selector.modify(self.sock, self.events_mask, data=msg)
            self.write_mode_on.set()
            self.read_mode_on.clear()


        elif mode == "rw":
            tcp_connection.debug(f"[Socket-{self.sock_id}] Updating "\
                                 f"selector events mask [READ/WRITE]")

            self.events_mask = selectors.EVENT_READ | selectors.EVENT_WRITE
            self.selector.modify(self.sock, self.events_mask, data=msg)
            self.write_mode_on.set()
            self.read_mode_on.set()

        else:
            tcp_connection.debug(f"[Socket-{self.sock_id}] Updating "\
                                 f"selector events mask: Invalid entry")
        self.lock.release()


    def _write(self) -> None:
        if self._send_buffer:
            try:
                sent = self.sock.send(self._send_buffer)
                tcp_connection.debug(f"[Socket-{self.sock_id}] Just sent "\
                                     f"{sent} bytes in _send_buffer")

            except BlockingIOError:
                tcp_connection.exception(f"[Socket-{self.sock_id}] An error "\
                                         f"has occurred")

                self._stop_threads = True

            else:
                self._send_buffer = self._send_buffer[sent:]

            tcp_connection.debug(f"[Socket-{self.sock_id}] Stream data "\
                                 f"has been sent")


    def write(self) -> None:
        if not self.send_data_stream_queued and self.data_stream:
            self._send_buffer += self.data_stream
            self.data_stream = b""
            self.send_data_stream_queued = True
            tcp_connection.debug(f"[Socket-{self.sock_id}] Stream data has "\
                                 f"been queued into _send_buffer: "\
                                 f"{self._send_buffer.hex()}")

        self._write()

        if self.send_data_stream_queued and not self._send_buffer:
            self._set_selector_events_mask("r")
            self.send_data_stream_queued = False
            tcp_connection.debug(f"[Socket-{self.sock_id}] There is no "\
                                 f"data to be sent for a while")


    def _read(self) -> None:
        try:
            data = self.sock.recv(4096*64)
            tcp_connection.debug(f"[Socket-{self.sock_id}] Data received: "\
                                 f"{data.hex()}")

        except:
            tcp_connection.exception(f"[Socket-{self.sock_id}] An Exception "\
                                     f"has been raised")

            self.error_has_raised = True
            self._stop_threads = True

        else:
            if data:
                self._recv_buffer += data
                tcp_connection.debug(f"[Socket-{self.sock_id}] _recv_buffer: "\
                                     f"{self._recv_buffer.hex()}")
            else:
                tcp_connection.debug(f"[Socket-{self.sock_id}] Peer closed "\
                                     f"connection")
                self._stop_threads = True


    def read(self) -> None:
        self._read()

        if self._recv_buffer:
            self._recv_data_stream += copy.copy(self._recv_buffer)
            self._recv_data_available.set()
            self._recv_buffer = b""

        tcp_connection.debug(f"[Socket-{self.sock_id}] _recv_buffer has "\
                             f"been cleaned up")

        self._set_selector_events_mask("r")


    def test_connection(self) -> bool:
        while True:
            try:
                self.sock.send(b"")
                return True

            except OSError as e:
                if e.args[0] == 10057:
                    self.connection_attempts -= self.connection_attempts
                    return False



import importlib
class SctpConnection(TcpConnection):
    def __init__(self, local_ip_address: str, local_port: str = 0, peer_ip_address: str = '', peer_port: str = 0):
        try:
            self.sctp = importlib.import_module("sctp")
            self._sctp = importlib.import_module("_sctp")
        except ModuleNotFoundError as ex:
            tcp_connection.error(f"Python 'pysctp' module is required. Cannot initialize SctpConnection.")
            raise ex
        super().__init__(local_ip_address, local_port, peer_ip_address, peer_port)

    def _write(self):
        if self._send_buffer:
            try:
                sent = self.sock.sctp_send(self._send_buffer)
                tcp_connection.debug(f"[Socket-{self.sock_id}] Just sent "\
                                     f"{sent} bytes in _send_buffer")

            except BlockingIOError:
                tcp_connection.exception(f"[Socket-{self.sock_id}] An error "\
                                         f"has occurred")

                self._stop_threads = True

            else:
                self._send_buffer = self._send_buffer[sent:]

            tcp_connection.debug(f"[Socket-{self.sock_id}] Stream data "\
                                 f"has been sent")
    def _read(self):
        try:
            fromaddr, flags, data, notif = self.sock.sctp_recv(4096*64)
            tcp_connection.debug(f"[Socket-{self.sock_id}] Data received: "\
                                 f"{data.hex()}")

        except:
            tcp_connection.exception(f"[Socket-{self.sock_id}] An Exception "\
                                     f"has been raised")

            self.error_has_raised = True
            self._stop_threads = True

        else:
            if data:
                self._recv_buffer += data
                tcp_connection.debug(f"[Socket-{self.sock_id}] _recv_buffer: "\
                                     f"{self._recv_buffer.hex()}")
            else:
                tcp_connection.debug(f"[Socket-{self.sock_id}] Peer closed "\
                                     f"connection")
                self._stop_threads = True

    def test_connection(self):
        state = self.sock.get_status()
        if self.sock.get_status().state == state.state_ESTABLISHED:
            return True
        else:
            self.connection_attempts -= self.connection_attempts
            return False


class TcpClient(TcpConnection):
    def __init__(self, local_ip_address: str, local_port: str = 0, peer_ip_address: str = '', peer_port: str = 0) -> None:
        super().__init__(local_ip_address, local_port, peer_ip_address, peer_port)


    def start(self) -> None:
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_client.debug(f"[Socket-{self.sock_id}] Client-side Socket: "\
                             f"{self.sock}")

            self.sock.setblocking(False)
            tcp_client.debug(f"[Socket-{self.sock_id}] Setting as "\
                             f"Non-Blocking")

            tcp_client.debug(f"[Socket-{self.sock_id}] Binding to the "\
                             f"Local Endpoint")
            self.sock.bind((self.local_ip_address, self.local_port))

            self.sock.connect_ex((self.peer_ip_address, self.peer_port))
            tcp_client.debug(f"[Socket-{self.sock_id}] Connecting to the "\
                             f"Remote Peer")
            self.is_connected = True

            self.selector.register(self.sock, selectors.EVENT_READ | selectors.EVENT_WRITE)
            tcp_client.debug(f"[Socket-{self.sock_id}] Registering Socket "\
                             f"Selector address: {self.selector.get_map()}")

        except Exception as e:
            tcp_client.exception(f"client_errors: {e.args}")


class SctpClient(TcpClient,SctpConnection):
    def __init__(self, local_ip_address: str, local_port: str = 0, peer_ip_address: str = '', peer_port: str = 0):
        SctpConnection.__init__(self, local_ip_address, local_port, peer_ip_address, peer_port)

    def test_connection(self):
        return SctpConnection.test_connection(self)

    def _read(self):
        return SctpConnection._read(self)

    def _write(self):
        return SctpConnection._write(self)

    def start(self):
        try:
            self.sock = self.sctp.sctpsocket_tcp(socket.AF_INET)
            tcp_client.debug(f"[Socket-{self.sock_id}] Client-side Socket: "\
                             f"{self.sock}")

            tcp_client.debug(f"[Socket-{self.sock_id}] Binding to the "\
                             f"Local Endpoint")
            self.sock.bind((self.local_ip_address, self.local_port))

            tcp_client.debug(f"[Socket-{self.sock_id}] Connecting to the "\
                             f"Remote Peer")
            self.sock.connect((self.peer_ip_address, self.peer_port))
            self.is_connected = True

            tcp_client.debug(f"[Socket-{self.sock_id}] Setting as "\
                             f"Non-Blocking")
            self.sock.setblocking(False)

            tcp_client.debug(f"[Socket-{self.sock_id}] Registering Socket "\
                             f"Selector address: {self.selector.get_map()}")
            self.selector.register(self.sock, selectors.EVENT_READ | selectors.EVENT_WRITE)

        except Exception as e:
            tcp_client.exception(f"client_errors: {e.args}")


class TcpServer(TcpConnection):
    def __init__(self, local_ip_address: str, local_port: str) -> None:
        super().__init__(local_ip_address, local_port)


    def start(self) -> None:
        try:
            self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_connection.debug(f"[Socket-{self.sock_id}] Server-side "\
                                 f"Socket: {self.server_sock}")

            self.server_selector = selectors.DefaultSelector()

            self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 4096*64)
            self.server_sock.bind((self.local_ip_address, self.local_port))
            self.server_sock.listen()
            tcp_server.debug(f"[Socket-{self.sock_id}] Listening on "\
                             f"{self.local_ip_address}:{self.local_port}")

            self.server_sock.setblocking(False)
            tcp_server.debug(f"[Socket-{self.sock_id}] Setting as "\
                             f"Non-Blocking")

            self.server_selector.register(self.server_sock, selectors.EVENT_READ | selectors.EVENT_WRITE)
            tcp_server.debug(f"[Socket-{self.sock_id}] Registering "\
                             f"Socket into Selector address: "\
                             f"{self.server_selector.get_map()}")

        except Exception as e:
            tcp_server.exception(f"server_error: {e.args}")


    def run(self) -> None:
        events = self.server_selector.select(timeout=None)
        for key, mask in events:
            tcp_server.debug(f"[Socket-{self.sock_id}] Event has been "\
                             f"raised on Main Socket: (mask, key) = "\
                             f"({mask}, {key})")

            if key.data is None:
                self.sock, self.remote_address = self.server_sock.accept()
                self.sock.setblocking(False)
                tcp_server.debug(f"[Socket-{self.sock_id}] New Socket "\
                                 f"bound to Main Socket: {self.sock}")

                self.is_connected = True
                self.selector.register(self.sock, selectors.EVENT_READ)
                tcp_server.debug(f"[Socket-{self.sock_id}] Registering "\
                                 f"New Socket into Selector address: "\
                                 f"{self.selector.get_map()}")

        super().run()


    def close(self) -> None:
        super().close()

        try:
            self.server_selector.unregister(self.server_sock)
            tcp_server.debug(f"De-registering Main Socket from Selector "\
                             f"address: {self.server_selector.get_map()}")

            self.server_sock.close()
            tcp_server.debug("Shutting down Main Socket")

        except KeyError:
            tcp_server.debug("There is no such Selector registered")


class SctpServer(TcpServer,SctpConnection):
    def __init__(self, local_ip_address: str, local_port: str):
        SctpConnection.__init__(self, local_ip_address, local_port)

    def test_connection(self):
        return SctpConnection.test_connection(self)

    def _read(self):
        return SctpConnection._read(self)

    def _write(self):
        return SctpConnection._write(self)

    def start(self):
        try:
            if self._sctp.getconstant("IPPROTO_SCTP") != 132:
                raise Exception("SCTP not supported by system")
            self.server_sock = self.sctp.sctpsocket_tcp(socket.AF_INET)
            # sock.initparams.max_instreams = 3
            # sock.initparams.max_ostreams = 3
            # sock.events.clear()
            # sock.events.data_io = 1

            tcp_connection.debug(f"[Socket-{self.sock_id}] Server-side "\
                                 f"Socket: {self.server_sock}")

            self.server_selector = selectors.DefaultSelector()

            self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 4096*64)
            self.server_sock.bind((self.local_ip_address, self.local_port))
            self.server_sock.listen()
            tcp_server.debug(f"[Socket-{self.sock_id}] Listening on "\
                             f"{self.local_ip_address}:{self.local_port}")

            self.server_sock.setblocking(False)
            tcp_server.debug(f"[Socket-{self.sock_id}] Setting as "\
                             f"Non-Blocking")

            self.server_selector.register(self.server_sock, selectors.EVENT_READ | selectors.EVENT_WRITE)
            tcp_server.debug(f"[Socket-{self.sock_id}] Registering "\
                             f"Socket into Selector address: "\
                             f"{self.server_selector.get_map()}")

        except Exception as e:
            tcp_server.exception(f"server_error: {e.args}")
