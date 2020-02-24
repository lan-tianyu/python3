# from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler
# # from socket import socket, AF_INET, SOCK_STREAM
# from socketserver import ThreadingTCPServer

# # s = socket(AF_INET, SOCK_STREAM)
# # s.connect(('localhost', 200000))
# # s.send(b'hello')
# # s.recv(8192)

# # class EchoHandler(BaseRequestHandler):
# #     def handle(self):
# #         print('Got connect from ', self.client_address)
# #         while True:
# #             msg = self.request.recv(8192)
# #             if not msg:
# #                 break
# #             self.request.send(msg)

# class EchoHandler(StreamRequestHandler):
#     def handle(self):
#         print('Got connect from ', self.client_address)
#         for line in self.rfile:
#             self.wfile.write(line)

# if __name__ == '__main__':
#     # serv = TCPServer(('', 20000), EchoHandler)
#     # serv.serve_forever()
#     # serv = ThreadingTCPServer(('', 20000), EchoHandler)
#     # serv.serve_forever()
#     from threading import Thread
#     NWORKERS = 16
#     serv = TCPServer(('', 20000), EchoHandler)
#     for n in range(NWORKERS):
#         t = Thread(target=serv.serve_forever)
#         t.daemon = True
#         t.start()
#     serv.serve_forever()

from socket import socket, AF_INET, SOCK_STREAM


def echo_handler(address, client_sock):
    print('Got connection from {}'.format(address))
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)
    client_sock.close()


def echo_server(address, backlog=5):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_sock, client_addr = sock.accept()
        echo_handler(client_addr, client_sock)


if __name__ == '__main__':
    echo_server(('', 20000))