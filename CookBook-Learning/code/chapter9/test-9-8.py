from functools import wraps


class A:
    def decorate1(slef, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorate1')
            return func(*args, **kwargs)

        return wrapper

    def decorate2(slef, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorate2')
            return func(*args, **kwargs)

        return wrapper


a = A()
print(vars(a))


@a.decorate1
def spam():
    print('spam')


@a.decorate1
@a.decorate2
def grok():
    pass


spam()
grok()

print('-' * 70)


class B(A):
    @A.decorate1
    # @A.decorate2
    def bar(self):
        print('B.bar....')


b = B()
b.bar()


@b.decorate1
def func():
    pass


func()