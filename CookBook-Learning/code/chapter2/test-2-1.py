import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))

fileds = re.split(r'(;|,|\s)\s*', line)
print(fileds)

values = fileds[::2]
delimiters = fileds[1::2] + ['']
print(values, delimiters)
print(''.join(v+d for v, d in zip(values, delimiters)))

print(re.split(r'(?:,|;|\s)\s*', line))



