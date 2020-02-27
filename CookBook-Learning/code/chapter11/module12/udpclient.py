from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.sendto(b'hello', ('localhost', 15000))
print(s.recv(128))
s.sendto(b'hello', ('localhost', 15000))
# print(s.recv(128))
print(s.recvfrom(128))
