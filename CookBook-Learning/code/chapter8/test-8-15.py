class A:
    def spam(self, x):
        print('spam...', x)

    def foo(self):
        print('foo...')


class B1:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        return self._a.spam(x)

    def foo(self):
        print('b1...foo...')
        return self._a.foo()

    def bar(self):
        print('b...bar...')


class B2:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        print('B2...spam...')

    def bar(self):
        print('B2...bar...')

    def __getattr__(self, name):
        return getattr(self._a, name)


b1 = B1()
b1.spam(123)
b1.foo()
b1.bar()

b2 = B2()
b2.spam(122)
b2.foo()
b2.bar()

print('-' * 70)


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        print('__getattr__', name)
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('__setattr__', name, value)
            setattr(self._obj, name, value)

    def __delattr__(self, name):
        if name.startswith('_'):
            super.__setattr__(name)
        else:
            print('__delattr__', name)
            setattr(self._obj, name)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self):
        print('Spam.bar....')
        print(self.x)


s = Spam(3)
p = Proxy(s)
print(vars(p))
p.x = 3456
print(vars(p), vars(s))
print('-' * 70)


class A:
    def spam(self, x):
        print('A.spam...', x)

    def foo(self):
        print('A.foo...')


class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        print('B.spam...', x)
        self._a.spam(x)

    def bar(slef):
        print('B.bar...')

    def __getattr__(self, name):
        print('B.getattr...')
        return getattr(self._a, name)


b = B()
print(vars(b))
b.spam(4354)
b.foo()
b.bar()


class ListLike:
    def __init__(self):
        self._items = []

    def __getattr__(self, name):
        return getattr(self._items, name)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __delitem__(self, index):
        del self._items[index]



a = ListLike()
a.append(2)
print(a._items)
a.append(7)
print(a[0])
