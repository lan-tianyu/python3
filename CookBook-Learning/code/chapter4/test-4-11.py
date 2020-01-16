from itertools import zip_longest

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
ypts1 = [101, 78, 37, 15, 62]
ypts2 = [101, 78, 37, 15, 62, 99, 35]

for x, y in zip(xpts, ypts):
    print('x: {}, y: {}'.format(x, y))

print('-' * 50)

for x, y in zip(xpts, ypts1):
    print('x: {}, y: {}'.format(x, y))

print('-' * 50)

for x, y in zip(xpts, ypts2):
    print('x: {}, y: {}'.format(x, y))

print('-' * 50)

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    print('i: {}'.format(i))

print('-' * 50)

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip_longest(a, b):
    print('i: {}'.format(i))

print('-' * 50)

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers, values))
print(s)

print('-' * 50)
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print('i- {}'.format(i))

d = zip(a, b, c)
dd = list(zip(a, b, c))
print(d, dd)