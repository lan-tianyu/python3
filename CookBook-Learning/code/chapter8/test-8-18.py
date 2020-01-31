from collections import defaultdict


class LoggedMappingMixin:
    __slots__ = ()

    def __getitem__(self, key):
        print('Getting...', key)
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print("Setting...", key)
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print("Deleting...", key)
        return super().__delitem__(key)


class SetOnceMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError('{} has already in self'.format(key))
        return super().__setitem__(key, value)


class StringKeysMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('expect key: {} be a string'.format(key))
        return super().__setitem__(key, value)


class LoggedDict(LoggedMappingMixin, dict):
    pass


class SetDefaultDict(SetOnceMappingMixin, defaultdict):
    pass


d = LoggedDict()
d['x'] = 1
print(d, d.get('x'))
del d['x']
print(d, d.get('x'))

print('-' * 70)

d = SetDefaultDict(list)
d['x'].append(2)
d['x'].append(3)
print(d, d.get('x'))
del d['x']
print(d, d.get('x'))

print('-' * 70)


def LoggedMapping(cls):
    # cls_getitem = cls.__getitem__
    # cls_setitem = cls.__setitem__
    # cls_delitem = cls.__delitem__

    # def __getitem__(self, key):
    #     print('Getting ' + str(key))
    #     return cls_getitem(self, key)

    # def __setitem__(self, key, value):
    #     print('Setting {} = {!r}'.format(key, value))
    #     return cls_setitem(self, key, value)

    # def __delitem__(self, key):
    #     print('Deleting ' + str(key))
    #     return cls_delitem(self, key)

    # cls.__getitem__ = __getitem__
    # cls.__setitem__ = __setitem__
    # cls.__delitem__ = __delitem__
    # return cls

    cls_getitme = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(slef, key):
        print('Getting...', key)
        return cls_getitme(key)

    def __setitem__(self, key, value):
        print('Setting...', key, value)
        return cls_setitem(key, value)

    def __delitem__(self, key):
        print('Deleting...', key)
        return cls_delitem(key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__

    return cls


@LoggedMapping
class LoggedDict2(dict):
    pass


d = LoggedDict2()
print(d)
d = dict(x=1)
print(d, d.get('x'))
del d['x']
print(d, d.get('x'))

print('-' * 70)