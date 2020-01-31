class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_func(self):
        print('public_func')
        self._internal_func()

    def _internal_func(self):
        print('_internal_func')


a = A()
a.public_func()
# a._internal_func()
print(a.public)
# print(a._internal)

print('-' * 70)


class B:
    def __init__(self):
        self.__private = 0

    def __private_func(self):
        print('__private_func')

    def public_func(self):
        print('public_func')
        self.__private_func()
        print(self.__private)


b = B()
b.public_func()

print('-' * 70)

class C(B):
    def __init__(self):
        super().__init__()
        self._B__private = 1
        self.__private = 2

    def __private_func(self):
        self._B__private_func()
        print('this is c __private_func')

    def public_func(self):
        # self.public_func()
        print('this is c public_func')
        self.__private_func()
        print(self._B__private, self.__private)


c = C()
c.public_func()