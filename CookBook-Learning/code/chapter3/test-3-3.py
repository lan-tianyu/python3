x = 1234.56789
print(format(x, '0.4f'))
print(format(x, '16.3f'))
print(format(x, '>16.3f'))
print(format(x, '<16.3f'))
print(format(x, '^16.3f'))
print(format(x, ','))
print(format(x, ',.4f'))
print(format(x, 'e'))
print(format(x, '0.2E'))

print('{:^20.2e}'.format(x))
print('{:^20.2f}'.format(x))
print('{:-20.2f}'.format(x))
print('{:>20.2f}'.format(x))