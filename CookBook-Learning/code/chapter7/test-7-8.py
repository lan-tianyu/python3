from functools import partial
import math


def spam(a, b, c, d):
    print(a, b, c, d)


s1 = partial(spam, 1, d=2)
s1('a', 'c')

points = [(1, 2), (3, 4), (5, 6), (7, 8)]


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


pt = (4, 3)
print(points.sort(key=partial(distance, pt)))
print(points)


def output_result(result, log=None):
    if log is not None:
        log.debug('result:{}'.format(result))


def add(x, y):
    return x + y


if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    from functools import partial
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')
    print('-' * 70)
    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()
