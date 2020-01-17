from collections import Iterable


def flattern(items, ignore_type=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_type):
            yield from x
        else:
            yield x


b = [1, [1, 2], 2, [3, 4, 5], 5]
print(list(flattern(b)))

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
print(list(flattern(items)))