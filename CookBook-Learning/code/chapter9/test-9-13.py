import weakref


class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('Can not instantiate directly')


class Spam(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print('Spam.grok...', x)


Spam.grok(3564)
# s = Spam()


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = super().__call__(*args, **kwargs)
        return self.instance


class Spam1(metaclass=Singleton):
    def __init__(self):
        print('init spam')


a = Spam1()
b = Spam1()
print(a, b, vars(b))
print(a is b)


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache(args)
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


class Spam2(metaclass=Cached):
    def __init__(self, name):
        print('init spam2(!r:)...hdhah'.format_map(name))
        self.name = name


a = Spam2('dwfw')
b = Spam2('dwrertr')
print(a, b, a is b)



