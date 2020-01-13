import math

a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c)
print(math.isinf(a), math.isinf(b), math.isnan(c))

print(a + 45, a / 10, 10 / a)
print(a / a, a + b)
print(c + 23, c * 2, c / 2, math.sqrt(c))

d = float('nan')
print(c == d, c is d, math.isnan(d))
