import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return math.pi * self.radius * 2


c = Circle(4.0)
print(c.area, c.diameter, c.perimeter)
print('-' * 70)


class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # @property
    def get_first_name(self):
        return self._first_name

    # @first_name.setter
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expect a string')
        self._first_name = value

    # @first_name.deleter
    def del_first_name(self):
        raise AttributeError('can not delete attribute')


a = Person('Gudio')
print(a._first_name)
a.set_first_name('GUdio hh')
print(a._first_name)
