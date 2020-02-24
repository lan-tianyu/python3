from socket import socket, AF_INET, SOCK_STREAM


secret_key = b'peekabo'

def echo_handler(client_sock):
    if not server_authenticate(client_sock, secret_key):
        client_sock.close()
        return
    