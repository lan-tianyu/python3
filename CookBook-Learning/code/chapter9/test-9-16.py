from inspect import Signature, Parameter, signature

parms = [
    Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
    Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
    Parameter('z', Parameter.KEYWORD_ONLY, default=None)
]

sig = Signature(parms)
print(sig, sig.parameters.items())


def func(*args, **kwargs):
    bound_value = sig.bind(*args, **kwargs)
    for name, value in bound_value.arguments.items():
        print(name, value)
    print('-' * 20)


func(1, 2, z=3)
func(1)
func(1, y=342, z=4)
func(1, z=44)


def make_sig(*names):
    parms = [
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names
    ]
    return Signature(parms)


class Structure:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')       


class Point(Structure):
    __signature__ = make_sig('x', 'y')


s = Stock('dsfd', 70, 90.435)
print(s, vars(s))
print(signature(Stock))
print(signature(Point))