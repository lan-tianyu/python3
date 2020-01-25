from struct import Struct
from collections import namedtuple
import numpy as np


def write_records(records, format, f):
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    # print('chunks: ', chunks, *chunks)
    return (record_struct.unpack(chunk) for chunk in chunks)


records = [(1, 2.3, 4.5), (6, 7.8, 9.0), (12, 13.4, 56.7)]
with open('data.b', 'wb') as f:
    write_records(records, '<idd', f)
with open('data.b', 'rb') as f:
    records_ = read_records('<idd', f)
    print(*records_)


Record = namedtuple('Record', ['kind', 'x', 'y'])
with open('data.b', 'rb') as f:
    records = (Record(*r) for r in read_records('<idd', f))
    for r in records:
        print(r.kind, r.x, r.y)
    



with open('data.b', 'rb') as f:
    records = np.fromfile(f, dtype='<i,<d,<d')
    print(records, *records)