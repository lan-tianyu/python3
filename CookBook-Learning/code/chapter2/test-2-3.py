from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Date1242.csv', 'Date[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat[0-9]*')])

print(fnmatch('foo.txt', '.TXT'))
print(fnmatchcase('foo.txt', '.TXT'))