print('fib...')


def fib(n):
    a = 1
    b = 1
    for i in range(1, n + 1):
        b, a = a + b, b
    return b


def fib_list(n):
    for i in range(n + 1):
        yield fib(i)

