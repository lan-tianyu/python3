import binascii
import base64

s = b'hello'
h = binascii.b2a_hex(s)
print('h', h)
print(binascii.a2b_hex(h))

h = base64.b16encode(s)
print('h', h)
print(base64.b16decode(h))
print(h.decode('ascii'))