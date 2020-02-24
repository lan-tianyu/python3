from socket import socket, AF_INET, SOCK_STREAM
from xmlrpc.client import ServerProxy, SafeTransport
import ssl
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

CERTFILE = os.path.join(dir_path, 'server_cert.pem')

# s = socket(AF_INET, SOCK_STREAM)
# s_ssl = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs=CERTFILE)
# s_ssl.connect(('localhost', 20000))
# print(s_ssl.send(b'Hello World'))
# print(s_ssl.recv(8192))


class VerifyCertSafeTransport(SafeTransport):
    def __init__(self, cafile, certfile=None, keyfile=None):
        SafeTransport.__init__(self)
        self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        self._ssl_context.load_verify_locations(cafile)
        if certfile:
            self._ssl_context.load_cert_chain(certfile, keyfile)
        self._ssl_context.verify_mode = ssl.CERT_REQUIRED

    def make_connection(self, host):
        s = super().make_connection((host, {'context': self._ssl_context}))
        return s


s = ServerProxy('http://localhost:15000', transport=VerifyCertSafeTransport(CERTFILE), allow_none=True)
s.set('foo', 'bar')
s.set('spam', [1, 2, 3, 4])
print(s.keys())
print(s.get('foo'))
print(s.delete('foo'), s.keys())
print(s.exists('spam'))