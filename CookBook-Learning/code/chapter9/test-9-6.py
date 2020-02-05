from functools import wraps, partial
import logging
logging.basicConfig(level=logging.DEBUG)


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    logname = name if name else func.__name__
    logmsg = message if message else func.__name__
    log = logging.getLogger(logname)

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


@logged
def spam():
    print('spam.....')


spam()


@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')


spam()


@logged()
def spam():
    print('Spam!')