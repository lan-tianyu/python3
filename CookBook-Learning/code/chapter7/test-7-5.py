def spam(a, b=42):
    print(a, b)


spam(1)
spam(a=2)
spam(b=24, a=3)
print('-' * 10)


def spam1(a, b=None):
    if b is None:
        b = []
    b.append(a)
    print(a, b)
    print(id(a), id(b))
    print('-' * 10)


spam1(1)
spam1(a=2)
spam1(a=2, b=[4])
spam1(b=[2, 4, 5, 6], a=3)
# spam1(2, '')

_no_value = object()


def spam2(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    # b.append(a)
    print(a, b)


spam2(1)
spam2(a=2)
spam2(a=2, b=[4])
spam2(b=[2, 4, 5, 6], a=3)