import select
import socket
import time
import os
from concurrent.futures import ThreadPoolExecutor


class EventHandler:
    def fileno(self):
        raise NotImplementedError('must implement')

    def wants_to_receive(self):
        return False

    def handle_receive(self):
        return True

    def wants_to_send(self):
        return False

    def handle_send(self):
        pass


def event_loop(handlers):
    print('handlers', handlers)
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        print('wants_recv', wants_recv, 'wants_send', wants_send)
        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])
        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()


class UDPServer(EventHandler):
    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(address)

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True


class UDPTimeServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(1)
        self.sock.sendto(time.ctime().encode('ascii'), addr)


class UDPEchoServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(8199)
        self.sock.sendto(msg, addr)


class TCPServer(EventHandler):
    def __init__(self, address, client_handler, handler_list):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.scok.bind(address)
        self.sock.listen(1)
        self.client_handler = client_handler
        self.handler_list = handler_list

    def fileno(self):
        return self.sock.fileno

    def wants_to_receive(self):
        return True

    def handle_receive(self):
        client, addr = self.sock.accept()
        self.handler_list.append(self.client_handler(client,
                                                     self.handler_list))


class TCPClient(EventHandler):
    def __init__(self, sock, handler_list):
        self.sock = sock
        self.handler_list = handler_list
        self.outgoing = bytearray()

    def fileno(self):
        return self.sock.fileno()

    def close(self):
        self.sock.close()
        self.handler_list.remove(self)

    def wants_to_send(self):
        return True if self.outgoing else False

    def handle_send(self):
        nsent = self.sock.send(self.outgoing)
        self.outgoing = self.outgoing[nsent:]


class TCPEchoClient(TCPClient):
    def wants_to_receive(self):
        return True

    def handle_receive(self):
        data = self.sock.recv()
        if not data:
            self.close()
        else:
            self.outgoing.extend(data)


class ThreadPoolHandler(EventHandler):
    def __init__(self, nworkers):
        if os.name == 'posix':
            self.signal_done_sock, self.done_sock = socket.socketpair()
        else:
            server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            server.bind(('127.0.0.1', 0))
            server.listen(1)
            self.signal_done_sock = socket.socket(socket.AF_INET,
                                                  socket.SOCK_DGRAM)
            self.signal_done_sock.connect(server.getsockname())
            self.done_sock, _ = self.accept()
            server.close()
        self.pending = []
        self.pool = ThreadPoolExecutor(nworkers)

    def fileno(self):
        return self.done_sock.fileno()

    def _complete(self, callback, r):
        self.pending.append((callback, r.result))
        self.signal_done_sock.send(b'x')

    def run(self, func, args=(), kwargs={}, *, callback):
        r = self.pool.submit(func, *args, **kwargs)
        r.add_done_callback(lambda r: self._complete(callback, r))

    def wants_to_receive(self):
        return True

    def handle_receive(self):
        for callback, result in self.pending:
            callback(result)
            self.done_sock.recv(1)
        self.pending = []


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


class UDPFibServer(UDPServer):
    def handler_receive(self):
        msg, addr = self.sock.recvfrom(128)
        n = int(msg)
        pool.run(fib, (n, ), callback=lambda r: self.respond(r, addr))

    def respond(self, result, addr):
        self.sock.sendto(str(result).encode('ascii'), addr)


if __name__ == '__main__':
    # handlers = [UDPServer(('', 14000)), UDPEchoServer(('', 15000))]
    # event_loop(handlers)

    # handlers = []
    # handlers.append(TCPServer(('', 16000), TCPEchoClient, handlers))
    # event_loop(handlers)

    pool = ThreadPoolHandler(16)
    handlers = [pool, UDPFibServer(('', 16000))]
    event_loop(handlers)

