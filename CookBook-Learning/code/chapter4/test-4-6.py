from collections import deque


class LineHistory:
    def __init__(self, lines, hislen=3):
        self.lines = lines
        self.history = deque(maxlen=hislen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('CookBook-Learning/tmp/somefile.txt') as f:
    lines = LineHistory(f)
    for line in lines:
        print('line: ', line)
        if 'Python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')


print('-' * 50)
with open('CookBook-Learning/tmp/somefile.txt') as f:
    lines2 = LineHistory(f)
    print(lines2)
    print(next(iter(lines2)))
