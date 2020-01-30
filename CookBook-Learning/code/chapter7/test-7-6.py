add = lambda x, y: x + y
print(add('hello', 'world'))


def add1(x, y):
    return x + y


print(add1('hello', 'world'))

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']

print(sorted(names, key=lambda name: name.split()[-2].lower()))
print(*(lambda: name.split()[-2].lower() for name in names))
