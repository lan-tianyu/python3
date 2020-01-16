import numpy as np

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x * 2)
# print(x + 10)
print(x + y)

print('-' * 50)
ax = np.array([1, 2, 3, 4])
bx = np.array([5, 6, 7, 8])
print(ax * 2, ax + 10)
print(ax + bx, ax * bx)


def f(x):
    return 3 * x**2 - 2 * x + 7


print(f(ax))
print(np.sqrt(ax))
print(np.cos(ax))

grid = np.zeros(shape=(1000, 1000), dtype=float)
print(grid)
print('-' * 50)
grid += 90
print(grid)
print(np.sin(grid))

print('-' * 50)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[1])
print(a[:, 1])
print(a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a)

print(a + [100, 101, 102, 103])
print(a)
print('-' * 50)
print(np.where(a > 10, a, 10))
