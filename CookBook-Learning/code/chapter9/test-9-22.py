import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


with timethis('counting'):
    n = 1000000
    while n > 0:
        n -= 1


@contextmanager
def list_transaction(orig_list):
    print('orig_list', orig_list)
    working = list(orig_list)
    print('working', working)
    yield working
    orig_list[:] = working
    print('orig_list', orig_list)


items = [1, 2, 3]
with list_transaction(items) as working:
    working.append(1)
    working.append(4)
    print('working', working)
    raise RuntimeError('oops')
