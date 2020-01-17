import os

base_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
file_b = os.path.join(base_dir, 'tmp/somfile.data')
file_b2 = os.path.join(base_dir, 'tmp/somfile.data2')


def read_into_buff(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        print(f.readinto(buf))
    return buf


buf = read_into_buff(file_b)
print(buf, buf[0:5])


with open(file_b2, 'wb') as f:
    f.write(buf)
