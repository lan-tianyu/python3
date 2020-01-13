from itertools import chain

a = [1, 2, 3]
b = ['a', 'b', 'c', 'd', 1, 3, {'a': 1}, {'b': 2}]

for i in chain(a, b):
    print('i-- {}'.format(i))

c = chain(a, b)
print(c, list(c))


for x in a+b:
    print(x)