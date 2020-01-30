x = 10
a = lambda y: x + y
print(a(10))
x = 20
b = lambda y: x + y

print(a(10), b(10))

x = 10
aa = lambda y, x=x: x + y
print(a(10))
x = 20
bb = lambda y, x=x: x + y

print(a(10), b(10))

print('-' * 20)

funcs = [lambda x, n=n: x+n for n in range(5)]

for f in funcs:
    print(f(0))