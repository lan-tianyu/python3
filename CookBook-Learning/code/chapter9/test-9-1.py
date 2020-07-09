import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        print(func.__name__, et - st)
        return result

    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown(1000)
countdown(1000000)
countdown(10000000)


class A:
    @classmethod
    def method(self):
        pass


class B:
    def method(self):
        pass
    method = classmethod(method)