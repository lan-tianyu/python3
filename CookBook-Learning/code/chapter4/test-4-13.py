import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


base_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
print('base_dir', base_dir)
lognames = gen_find('somefile*.log', os.path.join(base_dir, 'tmp'))
files = gen_opener(lognames)
print('files', list(files))
lines = gen_concatenate(files)
print('lines', list(lines))
pylines = gen_grep('(?i)GET', lines)
# for line in pylines:
#     print('line--', line)

bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
bytes = [int(x) for x in bytecolumn if x != '-']
print('Total', sum(bytes))
