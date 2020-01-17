print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=';')
print('ACME', 50, 91.5, sep=';', end='!!\n')

for i in range(5):
    print(i, end=' ')

print('-' * 50)
row = ('ACME', 50, 91.5)
print(*row, sep=',')
# print(','.join(str(x) for x in row))

a = 'Hello World'
b = b'Hello World'
print(b[0], a[0])

