a = [1, 2, 3, 4, 5]
print(list(reversed(a)), a)

with open('CookBook-Learning/tmp/somefile.txt') as f:
    # print(f.readlines())
    print('-' * 50)
    print(list(reversed(f.readlines())))
    print(list(reversed(list(f))))


class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


print(list(reversed(CountDown(30))))
print(list(CountDown(30).__reversed__()))
