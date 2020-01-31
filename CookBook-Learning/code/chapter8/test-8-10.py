import math

# class lazyproperty:
#     def __init__(self, func):
#         self.func = func

#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         else:
#             value = self.func(instance)
#             setattr(instance, self.func.__name__, value)
#             return value


def lazyproperty(func):
    name = '__lazy__' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value

    return lazy


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius**2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return math.pi * self.radius * 2


c = Circle(4.0)
print(vars(c))
print(c.area)
# del c.area
print(vars(c))
# c.area = 25
print(c.area)
print(c.perimeter)
