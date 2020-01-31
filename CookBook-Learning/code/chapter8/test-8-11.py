import math


class Structure1:
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure1):
    _fields = ['name', 'shares', 'price']


class Point(Structure1):
    _fields = ['x', 'y']


class Circle(Structure1):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius**2


s = Stock('ACM', 50, 30.0)
# s1 = Stock('ACM', 50)`
c = Circle(2)
print(vars(c), c.area)
p = Point(1, 2)
print(vars(p), p.x, p.y)


class Structure2:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


class Stock(Structure2):
    _fields = ['name', 'shares', 'price']


s = Stock('ACM', 50, 30.0)
s1 = Stock('ACM', 50, price=30.0)
print(vars(s), vars(s1))


class Structure3:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


class Stock(Structure3):
    _fields = ['name', 'shares', 'price']


s = Stock('ACM', 50, 30.0)
print(vars(s))
s1 = Stock('ACM', 50, 30.0, data=2)
print(vars(s1))
s2 = Stock('ACM', 50, price=30.0, data=2)
print(vars(s2))