from functools import wraps
from inspect import signature


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func

        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(
                            value, bound_types[name]))
            return func(*args, **kwargs)

        return wrapper

    return decorate


@typeassert(int, int)
def add(x, y):
    return x + y


print(add(4, 5))
# add(1, 'he')


@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)


spam(1, 2)
spam(1, 'd', 3)
# spam(1, 'd', 'a')

sig = signature(spam)
print(sig, sig.parameters)
print(sig.parameters['x'].name)
print(sig.parameters['x'].default)
print(sig.parameters['x'].kind)

bound_types = sig.bind_partial(int, z=int)
print(bound_types, bound_types.arguments)

bound_values = sig.bind(1, 2, 3)
print(bound_values, bound_values.arguments)
for k, v in bound_values.arguments.items():
    print(k, v)

for k, v in bound_types.arguments.items():
    print(k, v)


@typeassert(int, list)
def bar(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items


print(bar(1))
print(bar(1, [3]))

