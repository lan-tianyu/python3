import time
from functools import wraps
from inspect import signature


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
    """[summary]
    countdown
    """    
    while n > 0:
        n -= 1


countdown(1000000)
print(countdown.__name__)
print(countdown.__doc__)
print(signature(countdown))
countdown.__wrapped__(100)