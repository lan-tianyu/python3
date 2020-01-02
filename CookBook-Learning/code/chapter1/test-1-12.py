from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't",
    'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're",
    'under'
]
word_counts = Counter(words)
print(word_counts)
top_three = word_counts.most_common(3)
print(top_three)

print(word_counts['look'])

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    nums = word_counts.get(word, 0)
    word_counts[word] = nums + 1
print(word_counts, word_counts['eyes'])

word_counts.update(morewords)
print(word_counts)

a = Counter(words)
b = Counter(morewords)
print(a, '\n', b)

print('a + b', a + b)
print('a - b', a - b)
