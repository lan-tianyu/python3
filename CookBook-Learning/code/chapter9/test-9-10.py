import time
from functools import wraps
from abc import ABCMeta, abstractmethod


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result

    return wrapper


class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n >= 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n >= 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n >= 0:
            n -= 1


s = Spam()
s.instance_method(356587)
s.class_method(1000000)
s.static_method(435477)


class A(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def method(cls):
        pass



a = A()
print(a, vars(a))