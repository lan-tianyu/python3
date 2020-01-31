# class A:
#     def spam(self):
#         print('A.spam')

# class B(A):
#     def spam(self):
#         print('B.spam')
# #         super().spam()

# a = A()
# a.spam()
# print('-' * 70)

# b = B()
# b.spam()
# print('-' * 70)


class A:
    def __init__(self):
        self.x = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1


aa = A()
print(aa.x)
print('-' * 70)

bb = B()
print(bb.x, bb.y)
print('-' * 70)


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)


p = Proxy(dict(a=1, b=2, c=3))
print(p)
print(p.get('a'))
# p.__setattr__('a', 2)
# print(p.get('a'))

print('-' * 70)


class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('C.__init__')


c = C()
print(C.__mro__)