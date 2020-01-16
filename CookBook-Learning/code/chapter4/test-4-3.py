def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


print(list(frange(1, 10, 0.4)))


def countdown(x):
    print('starting countdown:{}'.format(x))
    while x:
        yield x
        x -= 1
    print('done')


xx = countdown(3)
print(next(xx))
print(next(xx))
next(xx)
next(xx)