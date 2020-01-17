import gzip
import bz2
import os

base_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
file_gz = os.path.join(base_dir, 'tmp/somfile.gz')
file_bz2 = os.path.join(base_dir, 'tmp/somfile.bz2')

with gzip.open(file_gz, 'wt') as f_gz, bz2.open(file_bz2, 'wt') as f_bz:
    f_gz.write('cedas侧阿里拉萨的骄傲考虑到打卢克的萨达是撒')
    f_bz.write('考虑到打卢克的萨达是撒cedas侧阿里拉萨的骄傲')


with gzip.open(file_gz, 'at', compresslevel=5) as f_gz, bz2.open(file_bz2, 'at', compresslevel=2) as f_bz:
    f_gz.write('cedas侧阿里拉萨的骄傲考虑到打卢克的萨达是撒')
    f_bz.write('cedas侧阿里拉萨的骄傲考虑到打卢克的萨达是撒')


with gzip.open(file_gz, 'rt') as f_gz, bz2.open(file_bz2, 'rt') as f_bz:
    print(f_gz.read())
    print(f_bz.read())