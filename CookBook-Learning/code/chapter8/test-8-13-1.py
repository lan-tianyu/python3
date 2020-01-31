class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expect {}'.format(self.expected_type))
        super().__set__(instance, value)


class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise TypeError('Except value {} >= 0'.format(value))
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('miss size option')
        super().__init__(name=name, **opts)

    def __set__(self, instance, value):
        if len(value) > self.size:
            raise TypeError('Expect value {} length < {}'.format(
                value, self.size))
        return super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


# def check_attributes(**kwargs):
#     def decorate(cls):
#         for key, value in kwargs.items():
#             if isinstance(value, Descriptor):
#                 value.name = key
#                 setattr(cls, key, value)
#             else:
#                 setattr(cls, key, value(key))
#         return cls

#     return decorate




@check_attributes(name=SizedString(size=8),
                  shares=UnsignedInteger,
                  price=UnsignedFloat)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('ACM', 30, 50.0)
print(vars(s))
s.name = 'SCMDJL'
print(vars(s))
# s.shares = -1
# s.shares = 10.2
# s.price = 30