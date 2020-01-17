import os

path = '/Users/beazley/Data/data.csv'
print(os.path.basename(path), os.path.dirname(path))

print(os.path.join('tmp', 'data', os.path.basename(path)))


path = '~/Data/data.csv'
print(os.path.expanduser(path))
print(os.path.splitext(path))
