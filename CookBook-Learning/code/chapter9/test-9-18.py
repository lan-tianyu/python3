import operator
import types
import sys


def named_tuple(classname, fieldnames):
    cls_dict = {
        name: property(operator.itemgetter(n))
        for n, name in enumerate(fieldnames)
    }
    print('cls_dict', cls_dict)

    def __new__(cls, *args):
        print('args', args, 'fieldnames', fieldnames)
        if len(args) != len(fieldnames):
            raise TypeError("Expected {} arguements".format(len(fieldnames)))
        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__

    cls = types.new_class(classname, (tuple, ), {},
                          lambda ns: ns.update(cls_dict))
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls


Point = named_tuple('Point', ['x', 'y'])
p = Point(1, 2)
print(vars(p), p.x)