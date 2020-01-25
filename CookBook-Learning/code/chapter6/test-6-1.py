import os
import re
import csv
from collections import namedtuple

dir_path = os.path.abspath(os.path.join(os.path.abspath(__file__),
                                        '../../../'))
file_name = os.path.join(dir_path, 'tmp/stock.csv')

# with open(file_name) as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     print('headers', headers)
#     Row = namedtuple('Row', headers)
#     for r in f_csv:
#         print('r: ', r)
#         row = Row(*r)
#         print('row:', row)

print('-' * 70)

col_types = [str, float, str, str, float, int]

with open(file_name) as f:
    f_csv = csv.reader(f, delimiter='\t')
    headers = [re.sub(r'[^a-zA-Z_]', '_', h) for h in next(f_csv)]
    print('headers:', headers)
    Row = namedtuple('Row', headers)
    print('Row:', Row)
    for r in f_csv:
        print('r:', r)
        r_r = tuple(convert(value) for convert, value in zip(col_types, r))
        row = Row(*r_r)
        print('row:', row)

print('-' * 30, 'Reading as dicts with type conversion')
field_types = [('Price', float), ('Change', float), ('Volume', int)]

with open(file_name) as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        row.update((key, conversion(row[key])) for key, conversion in field_types)
        print('row', row)


