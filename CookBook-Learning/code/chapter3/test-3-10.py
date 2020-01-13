import numpy as np

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)
print(m.T, '||', m.I)
print('-' * 50)

v = np.matrix([[2], [3], [4]])
print(v)
print('-' * 50)
print(m * v)
