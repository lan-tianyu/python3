import os
import glob
from fnmatch import fnmatch

base_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))

print(os.path.isdir(base_dir))

names = os.listdir(base_dir)
print('names', names)

dirnames = [
    name for name in os.listdir(base_dir)
    if os.path.isdir(os.path.join(base_dir, name))
]
print('dirnames', dirnames)

base_dir = os.path.dirname(__file__)
filenames = [
    name for name in os.listdir(base_dir)
    if os.path.isfile(os.path.join(base_dir, name))
]
print('filenames', filenames)

filenames = [name for name in os.listdir(base_dir) if fnmatch(name, '*.py')]
print('filenames', filenames)

filenames = [name for name in os.listdir(base_dir) if name.endswith('.py')]
print('filenames', filenames)


print('-' * 50)

# pyfiles = glob.glob(r'.py')
# print('pyfiles', pyfiles)

name_sz_data = [(name, os.stat(os.path.join(base_dir, name)), os.path.getmtime(os.path.join(base_dir, name))) for name in filenames]
print('name_sz_data', name_sz_data)
