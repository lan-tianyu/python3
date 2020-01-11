import re
from calendar import month_abbr

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'\/', '-', text))
print(re.sub(r'(\d+)\/(\d+)\/(\d+)', r'\3-\2-\1', text))

pattern = re.compile(r'(\d+)\/(\d+)\/(\d+)')
print(pattern.sub(r'\3-\2-\1', text))


def change_date(m):
    print('m:', m, m.group(0))
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


print(pattern.sub(change_date, text))

newtext, n = pattern.subn(r'\3-\2-\1', text)
print(newtext, n)