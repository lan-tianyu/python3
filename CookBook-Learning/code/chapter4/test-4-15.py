import heapq
import os

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
print(list(heapq.merge(a, b)))

base_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
file1 = os.path.join(base_dir, 'tmp/somefile.log')
file2 = os.path.join(base_dir, 'tmp/somefile.txt')
file3 = os.path.join(base_dir, 'tmp/merge.log')

with open(file1, 'rt') as f1, open(file2, 'rt') as f2, open(file3, 'wt') as f3:
    for line in heapq.merge(f1, f2):
        f3.write(line)
