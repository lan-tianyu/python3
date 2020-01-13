from collections import defaultdict

my_list = ['a', 'b', 'c']
for index, c in enumerate(my_list):
    print("index: {}, c: {}".format(index, c))

print('-' * 50)
for index, c in enumerate(my_list, 2):
    print("index: {}, c: {}".format(index, c))

print('-' * 50)
data = [(1, 2), (3, 4), (5, 6), (7, 8)]
for n, (x, y) in enumerate(data):
    print(x, x, y)

with open('CookBook-Learning/tmp/somefile.txt') as f:
    lines = f.readlines()

print('-' * 50)
words_sunmmery = defaultdict(list)
for lineno, line in enumerate(lines):
    words = [w.strip() for w in line.split()]
    for idx, word in enumerate(words):
        words_sunmmery[word].append(idx)
print(words_sunmmery)
