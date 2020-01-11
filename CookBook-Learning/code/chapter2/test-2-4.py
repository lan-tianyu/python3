import re

text1 = '11/02/2018'
text2 = 'nov 27, 2018'

print(re.match(r'\d+\/\d+\/\d+', text1))

print(re.match(r'\w+\s\d+,\s\d+', text2))

pattern = re.compile(r'\d+\/\d+\/\d+')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(pattern.match(text))
print(pattern.findall(text))

pattern = re.compile(r'(\d+)\/(\d+)\/(\d+)')
print(pattern.match(text))
print(pattern.findall(text))

print(pattern.match(text1))
print(pattern.findall(text1))

for year, month, day in pattern.findall(text):
    print('{}-{}-{}'.format(year, month, day))

for i in pattern.finditer(text):
    print(i.group())
    print(i.groups())

pattern = re.compile(r'(\d+)\/(\d+)\/(\d+)$')
print(pattern.match('21/02/2018dxz'))
print(pattern.match('21/02/2018'))

print(re.findall(r'(\d+)\/(\d+)\/(\d+)', text))