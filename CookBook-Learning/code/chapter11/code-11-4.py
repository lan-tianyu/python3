import ipaddress

net = ipaddress.ip_network('123.45.67.64/27')

for a in net:
    print(a)

print('-' * 70)
net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
for a in net6:
    print(a)

print('-' * 70)

print(net.num_addresses)
print(net[0], net[-1], sep=' || ')

a = ipaddress.ip_address('123.45.67.69')
print(a in net)

b = ipaddress.ip_address('123.45.67.96')
print(b in net)

inet = ipaddress.ip_interface('123.45.67.73/27')
print(inet.network, inet.ip, sep=',\t')

print('-' * 70)
a = ipaddress.ip_address('127.0.0.1')
print(a)

from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect((str(a), 8080))
