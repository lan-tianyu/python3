from itertools import dropwhile, islice

with open('CookBook-Learning/tmp/somefile.txt') as f:
    for line in dropwhile(lambda line: line.startswith('Python'), f):
        print(line, end='')
print('-' * 50)

with open('CookBook-Learning/tmp/somefile.txt') as f:
    lines = [line for line in f if not line.startswith('Python')]
    for line in lines:
        print(line, end='')

print('-' * 50)

items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, None, 3):
    print(x)
print('-' * 50)
for x in islice(items, 5, None):
    print(x)

print('-' * 50)
for x in islice(items, 3, 6):
    print(x)
