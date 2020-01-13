# with open('CookBook-Learning/tmp/somefile.txt') as f:
#     while True:
#         line = next(f, None)
#         if line is None:
#             break
#         print(line, end='')

items = [1, 2, 3]
it = iter(items)
print(it, next(it), next(it), next(it), next(it, None))


