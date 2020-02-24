from socketserver import BaseRequestHandler, UDPServer
from socket import socket, AF_INET, SOCK_DGRAM
import time


class TImeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)


def time_server(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(address)
    while True:
        mas, addr = sock.recvfrom(8192)
        print('Got message from ', addr)
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), addr)


if __name__ == '__main__':
    # serv = UDPServer(('', 20000), TImeHandler)
    # serv.serve_forever()
    time_server(('', 20000))
