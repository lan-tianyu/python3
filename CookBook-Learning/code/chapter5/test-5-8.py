import os
# from functools import partial

base_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
file_b = os.path.join(base_dir, 'tmp/somfile.data')

with open(file_b, 'wb') as f:
    f.write(
        b'dlsdsdsfdlkfdfgmdfkdfsklfsk jskfjsfjsfslrfldsfdttrtrgrtyr'
    )

with open(file_b, 'rb') as f:
    # records = partial(f.read(), 32, b'')
    records = f.read(32)

print(records)
