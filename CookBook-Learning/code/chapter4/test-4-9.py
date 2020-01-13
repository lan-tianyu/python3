from itertools import permutations, combinations, combinations_with_replacement

items = ['a', 'b', 'c']
for p in permutations(items):
    print('p:', p)

print('-' * 50)
for p in permutations(items, 2):
    print('p:', p)

print('-' * 50)
for c in combinations(items, 3):
    print('c:', c)

print('-' * 50)
for c in combinations(items, 2):
    print('c:', c)

print('-' * 50)
for c in combinations(items, 1):
    print('c:', c)


print('-' * 50)
for c in combinations_with_replacement(items, 2):
    print('c:', c)

print('-' * 50)
for c in combinations_with_replacement(items, 3):
    print('c:', c)