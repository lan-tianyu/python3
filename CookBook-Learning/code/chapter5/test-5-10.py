import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


base_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
file_b = os.path.join(base_dir, 'tmp/somfile.data')
file_b2 = os.path.join(base_dir, 'tmp/somfile.data2')

# size = 1000000
# with open('data', 'wb') as f:
#     f.seek(size-1)
#     f.write(b'\x00')

m = memory_map('data')
print(len(m), m[:10])

m[0:11] = b'Hello World'
m.close()

with open('data', 'rb') as f:
    print(f.read(11))

with memory_map('data') as m:
    v = memoryview(m).cast('I')
    print(len(m), m[0:10])
    print(v)