import itertools


def count(n):
    while True:
        yield n
        n += 1


c = count(10)
print(c, next(c))

for x in itertools.islice(c, 10, 24):
    print('x:', x)