from functools import wraps
import logging


def logged(level, name=None, message=None):
    def decorator(func):
        logname = name if name else func.__module__
        logger = logging.getLogger(logname)
        logmsg = message if message else func.__name__
        print('logmsg', logmsg)
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Example use
@logged(logging.ERROR)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


print(add(2, 3))
spam()