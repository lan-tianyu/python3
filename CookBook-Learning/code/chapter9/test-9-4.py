from functools import wraps
import logging

logging.basicConfig(level=logging.DEBUG)


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__name__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(log.level)
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


print(add(3, 4))


@logged(logging.CRITICAL, name='example', message='hhdahd')
def spam():
    print('spam')


spam()