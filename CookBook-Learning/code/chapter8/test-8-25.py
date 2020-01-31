import logging
import weakref

a = logging.getLogger('foo')
b = logging.getLogger('bar')
print(a is b)

c = logging.getLogger('foo')
print(c is a)


class Spam:
    def __init__(self, name):
        print('Initialize spam...', name)
        self.name = name


_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    print('_spam_cache', _spam_cache)
    return s


a = get_spam('foo')
b = get_spam('bar')
print(a is b)
c = get_spam('foo')
print(c is a)

print('-' * 70)


class Spam1:
    _spam_cache = weakref.WeakValueDictionary()

    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self, name):
        print('Initialize spam1...', name)
        self.name = name


s = Spam1('a')
t = Spam1('a')
print(s is t)


class CacheManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam2._new(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        print('_cache', self._cache)
        return s

    def clear(self):
        return self._cache.clear()


class Spam2:
    manager = CacheManager()

    def __init__(self, name):
        self.name = name

    def get_spam(name):
        return Spam2.manager.get_spam(name)


class Spam3:
    def __init__(self, *args, **kwargs):
        raise RuntimeError('Can not instantiate directly')

    def _new(cls, name):
        print('instantiate spam3')
        self = cls.__new__(cls)
        self.name = name
        return self


a = Spam2('a')
b = Spam2('b')
aa = Spam2('a')
print('a is b', a is b)
print('a is aa', a is aa)
