from functools import wraps


def decoratorl(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decoratorl')
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator2')
        return func(*args, **kwargs)

    return wrapper


@decoratorl
@decorator2
def add(x, y):
    return x + y


print(add(2, 3))
print(add.__wrapped__(2, 3))
