import os
import re
import requests

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('spam'))

filenames = os.listdir('.\code\chapter2')
print(filenames)
print([name for name in filenames if name.startswith('test')])


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return requests.get(name).content
    else:
        with open(name) as f:
            return f.readlines()


choices = ['https:', 'http:','ftp:']
url = 'https://example.com'
print(url.startswith(tuple(choices)))

url = 'https://example.com'
print(re.match(r'(https|http|ftp):', url))