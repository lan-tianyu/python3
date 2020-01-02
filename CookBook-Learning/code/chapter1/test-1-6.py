from collections import defaultdict

d = {'a': [1, 2, 3], 'b': [4, 5]}
e = {'a': [1, 4, 7], 'b': [2, 5]}

print(d.get('a'), d.get('b'))
print(e.get('a'), e.get('b'))

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(1)
e['b'].add(4)
print(e)

dd = {}
dd.setdefault('a', []).append(1)
dd.setdefault('a', []).append(2)
dd.setdefault('b', []).append(4)
print(dd)

pairs = dict(a=[1, 2, 3], b=[5, 9, 10])
print(pairs)

d = {}
for key, value in pairs.items():
    if key not in d:
        d[key] = d
    else:
        d[key].append(value)

d = defaultdict(list)
print(d)
for key, value in pairs.items():
    d[key].append(value)
print(d)

