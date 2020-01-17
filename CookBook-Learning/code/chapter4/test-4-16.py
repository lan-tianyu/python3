import os
import sys

CHUNKSIZE = 8192


def recv(size):
    pass


def process_data(data):
    pass


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == 'b':
            break
        process_data(data)


def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(chunk)


base_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
file1 = os.path.join(base_dir, 'tmp/somefile.txt')

with open(file1) as f:
    for chunk in iter(lambda: f.read(10000), b''):
        n = sys.stdout.write(chunk)

print(n)

