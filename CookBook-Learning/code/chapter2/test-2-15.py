import sys
import string

s = '{name} has {n} messages'
print(s.format(name='Gudio', n=37))

name = 'Gudioo'
n = 377
print(s.format_map(vars()))


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Gudiooo', 3777)
print(s.format_map(vars(a)))

# print(s.format(name='Gudio'))


class safesub(dict):
    # def __init__(self):
    #     super().__init__()

    def __missing__(self, key):
        return '{' + key + '}'


print(s.format_map(safesub(dict(name='GudioTest'))))


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = '32Gudio'
n = 123456
print(sub('hello {name}'))
print(sub('you have {n} messages'))
print(sub('{name} have {n} messages, {color}'))


s = string.Template('$name have $n messages')
print(s.substitute(vars()))

