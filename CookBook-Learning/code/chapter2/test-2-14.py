data = ['ACME', 50, 91.1]
# print(','.join(data))
print(','.join([str(d) for d in data]))

a, b, c = data
print(a, b, c, sep=';')


def sample():
    yield 'hh'
    yield 'I'
    yield 'a213'
    yield '1heheal'
    yield '2hehal'
    yield '3hel'
    yield '4heal'


print('*:;'.join(sample()))


def combine(source, max_size):
    size = 0
    parts = []
    for part in source:
        parts.append(part)
        size += len(part)
        if size > max_size:
            print('oversize, {}, {}'.format(size, max_size))
            yield ''.join(parts)
            parts = []
            size = 0
            # parts.append(part)
    yield ''.join(parts)


with open('./tmp/result.txt', 'w') as f:
    for part in combine(sample(), 5):
        f.write(part)