from functools import wraps, partial
import logging
logging.basicConfig(level=logging.DEBUG)


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__name__
        logmsg = message if message else func.__name__
        log = logging.getLogger(logname)

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
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

    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, message='djakda')
def spam():
    print('spam')


spam()
print(add(3, 4))
add.set_message('dajlda ')
print(add(2, 4))
add.set_level(logging.WARNING)
print(add(2, 4))