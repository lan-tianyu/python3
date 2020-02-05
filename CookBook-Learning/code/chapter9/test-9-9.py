import types
from functools import wraps


class Profield:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


def profield(func):
    ncalls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)

    wrapper.ncalls = lambda: ncalls
    return wrapper


@Profield
def add(x, y):
    return x + y


class Spam:
    @Profield
    def bar(self, x):
        print('bar....', x)


s = Spam()
s.bar(3)

print(add(4, 5))
print(add(6, 7))
s.bar(5)
s.bar(8)
print(add.ncalls, Spam.bar.ncalls)


@profield
def add1(x, y):
    return x + y


add1(3, 4)
add1(4, 5)
add1(3, 6)
print(add1.ncalls())