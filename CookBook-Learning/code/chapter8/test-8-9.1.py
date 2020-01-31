class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value, self.expected_type):
            raise TypeError('expect type: ', self.expected_type)
        instance.__dict__[self.name] = value

    def __delete__(slef, instance):
        del instance.__dict__[slef.name]


def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls

    return decorate


@typeassert(name=str, share=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('ada', 3242, 3243.0)
print(s.name, s.shares, s.price)
