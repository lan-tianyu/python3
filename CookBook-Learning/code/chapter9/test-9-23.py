a = 13

exec('b=a+3')
print(b)


def test():
    a = 13
    b = 0
    loc = locals()
    exec('b = a + 3')
    print('loc', loc)
    b = loc['b']
    print(b)


test()


def test1():
    x = 0
    exec('x += 1')
    print('test1...', x)


test1()


def test2():
    x = 0
    loc = locals()
    print('loc', loc)
    exec('x o-+= 1')
    x = loc['x']
    print('loc', loc)
    print('test2..', x)


test2()