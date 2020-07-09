from functools import wraps, partial
import logging
import time
logging.basicConfig(level=logging.DEBUG)


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    def decorator(func):
        logname = name if name else func.__module__
        logger = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper

    return decorator


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        print(func.__name__, et - st)
        return result

    return wrapper


@logged(logging.DEBUG)
def add(x, y):
    return x + y


print(add(5, 7))


@logged(logging.INFO, 'hello', 'hihi')
def spam():
    print('Spam')


spam()

add(1, 3)
add.set_message('Add called')
add(5, 6)

add.set_level(logging.INFO)
add(5, 33)


@logged(logging.WARNING)
@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown(100000)

print('-' * 80)

print(timethis(logged(logging.DEBUG)))

print(logged(logging.DEBUG)(timethis))