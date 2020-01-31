from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:
    def __init__(self, address, fmaily=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = fmaily
        self.type = type
        # self.sock = None
        self.connections = []

    def __enter__(self):
        # if self.sock is not None:
        #     raise RuntimeError('Already connected')
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, ext_ty, ext_val, tb):
        print('connections:', self.connections)
        self.connections.pop().close()
        # self.sock = None


conn = LazyConnection(('www.python.org', 80))
with conn as s1:
    s1.send(b'GET /index.html HTTP/1.0\r\n')
    s1.send(b'Host: www.python.org\r\n')
    s1.send(b'\r\n')
    resp = b''.join(iter(partial(s1.recv, 8192), b''))
    print('resp1', resp)
    with conn as s2:
        s2.send(b'GET /index.html HTTP/1.0\r\n')
        s2.send(b'Host: www.python.org\r\n')
        s2.send(b'\r\n')
        resp = b''.join(iter(partial(s2.recv, 8192), b''))
        print('resp2', resp)

