import re

data = b'Hello World'
print(data[:5])
print(data.startswith(b'Hell'))
print(data.split(), data.split(','))
print(data.replace(b'Hello', b'hello haha'), data)

data = bytearray('Hello World')
print(data, data[:5])
print(data.startswith(b'Hell'))
print(data.split(), data.split(','))
print(data.replace(b'Hello', b'hello haha'), data)

print('-' * 50)

data = b'FOO:BAR,SPAM'
pat1 = re.compile(r':|,')
pat2 = re.compile(r'[:,]')
print(pat1.split(data))
print(pat2.split(data))


pat11 = re.compile(b':|,')
pat22 = re.compile(b'[:,]')
print(pat11.split(data))
print(pat22.split(data))

print('-' * 50)

a = 'Hello World'
print(a[0], a[5])

b = b'Hello World'
print(b[0], b[5])
print(b.decode('ascii'))


print(b'{} {} {}'.format(b'ACME', 100, 490.1))
print(b'{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1))