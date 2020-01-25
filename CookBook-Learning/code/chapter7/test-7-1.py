def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


print(avg(1, 2, 3, 4))
print(avg(1, 10))


def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)


anyargs(1)
anyargs(1, 2, 3)
anyargs(1, 2, {
    3,
    4,
    5,
})

anyargs(1, 2, {'a': 3, 'b': 4, 'c': 5}, {'a': 3, 'b': 4, 'c': 5})
