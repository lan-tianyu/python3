import cmath
import numpy as np

a = complex(2, 4)
print(a)
b = 3 - 5j
print(a + b, a - b, a * b, a / b, abs(a))

print(cmath.sin(a), cmath.cos(a), cmath.exp(a))

print('-' * 50)
a = np.array([2 + 3j, 4 + 5j, 6 - 7j, 8 + 9j])
print(a, a + 2, np.sinc(a))

print(cmath.sqrt(-1))