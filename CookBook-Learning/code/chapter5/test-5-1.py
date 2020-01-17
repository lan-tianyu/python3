import os

base_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
file1 = os.path.join(base_dir, 'tmp/somefile.txt')
file2 = os.path.join(base_dir, 'tmp/somefile2.txt')

with open(file1, 'rt') as f:
    data = f.read()

print('data---\n', data)

with open(file2, 'wt') as f2, open(file1, 'xt') as f1:
    print('abcf', file=f2)
    print('abcfabcfabcfabcf', file=f2)
    print('abcf', file=f1)
    print('abcfabcfabcfabcf', file=f1)

with open(file1, 'rt', encoding='utf-8', errors='ignore') as f:
    print(f.read())

with open(file1, 'rt', encoding='utf-8', errors='ignore') as f:
    print(f.read())