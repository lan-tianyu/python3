import requests
import sys
import imp

r = requests.get('http://127.0.0.1:1500/fib.py')
data = r.content.decode('utf-8')
print(data)


def load_module(url):
    r = requests.get(url)
    source = r.content.decode('utf-8')
    mod = sys.modules.setdefault(url, imp.new_module(url))
    code = compile(source, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod


fib = load_module('http://127.0.0.1:1500/fib.py')
print(list(fib.fib_list(10)))


spam = load_module('http://127.0.0.1:1500/spam.py')
spam.hello('hdaoksk fsfsf')

print(fib, spam)