from functools import wraps
import inspect


def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('debug---', func.__name__)
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(
        inspect.Parameter('debug',
                          inspect.Parameter.KEYWORD_ONLY,
                          default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)

    return wrapper


@optional_debug
def spam(a, b, c):
    print(a, b, c)


@optional_debug
def a(x):
    print('a...', x)


@optional_debug
def b(x, y, z):
    print('b...', x, y, z)


@optional_debug
def c(x, y):
    print('c...', x, y)


spam(1, 23, 56, debug=True)
a(1)
b(1, 2, 3, debug=True)
c(2, 3)
print(inspect.signature(b))
