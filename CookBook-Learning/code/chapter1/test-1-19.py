import os

files = os.listdir('.\code\chapter1')
print('files:', files)
if any(name.endswith('.py') for name in files):
    print('There is python')
else:
    print('Sorry, no Python')

nums = [n for n in range(10)]
s = sum(n * n for n in nums)
print('nums:', nums, ', s:', s)

s = ('ACME', 50.0, 123.45)
print(','.join(str(x) for x in s))

portfolio = [{
    'name': 'GOOG',
    'shares': 50
}, {
    'name': 'YHOO',
    'shares': 75
}, {
    'name': 'AOL',
    'shares': 20
}, {
    'name': 'SCOX',
    'shares': 65
}]
print(min(s['shares'] for s in portfolio))
print(min(portfolio, key=lambda s: s['shares']))