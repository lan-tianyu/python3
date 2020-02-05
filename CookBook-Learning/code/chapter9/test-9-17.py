from inspect import signature
import logging


def MyMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        super().__new__(cls, clsname, bases, clsdict)


def MyMeta1(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)


class MatchSignalturesMeta(type):
    def __init__(self, clsname, bases, clsdict):
        print('-' * 70)
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        print('sup', sup)
        for name, value in clsdict.items():
            print('name:', name, ' value:', value)
            if name.startswith('_') or not callable(value):
                continue
            prev_dfn = getattr(sup, name, None)
            print("prev_dfn", prev_dfn)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning('Signature mismatch in %s. %s != %s',
                                    value.__qualname__, prev_sig, val_sig)


class Root(metaclass=MatchSignalturesMeta):
    pass


class A(Root):
    def spam(x, y, *z):
        pass

    def foo(x, y, z=5):
        pass


class B(A):
    def spam(x, y, *z):
        pass

    def bar(x, y):
        pass

    def foo(x, y, z=3):
        pass