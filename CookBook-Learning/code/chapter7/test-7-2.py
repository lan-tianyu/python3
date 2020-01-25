def recv(maxsize, *, block):
    print('maxsize:', maxsize)
    # print(*)
    print('block:', block)


recv(1024, block=0)


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip < m else m
    return m


print(minimum(1, 5, 2, -5, 10))
print(minimum(1, 5, 2, -5, 10, clip=-9))
print(minimum(1, 5, 2, -5, 10, clip=0))