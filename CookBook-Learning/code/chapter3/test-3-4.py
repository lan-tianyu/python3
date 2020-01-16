import os

x = 1234
print(bin(x), oct(x), hex(x))
print(format(x, 'b'), format(x, 'o'), format(x, 'x'))

print('-' * 50)

y = -1234
print(bin(x), oct(x), hex(x))
print(format(2**32 + x, 'b'), format(8**29 + x, 'o'), format(2**32 + x, 'x'))

print('-' * 50)

print(int('4d2', 16))
print(int('10011010010', 2))

os.chmod('CookBook-Learning/tmp/somefile.txt', 0o0775)
