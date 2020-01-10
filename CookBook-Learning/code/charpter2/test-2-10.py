import re

s = ' hello     world \n'
print(s.strip(), s.lstrip(), s.rstrip())

print(s.replace(' ', ''))

print(re.sub('\s+', '', s))

with open('CookBook-Learning\\code\\charpter2\\test-2-7.py') as f:
    lines = (re.sub('\s', '', line) for line in f)
    for line in lines:
        print line
