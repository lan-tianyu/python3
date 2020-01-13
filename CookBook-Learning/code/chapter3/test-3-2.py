a = 4.2
b = 2.1
print(a + b)

import math
from decimal import Decimal, localcontext

a = Decimal('4.2')
b = Decimal('2.1')
print(a + b, a + b == Decimal('6.3'))

print('-' * 50)

a = Decimal(1.7)
b = Decimal(1.2)
print(a / b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

print('-' * 50)

nums = [1.23e+18, -1.23e+18]
print(sum(nums))

print(math.fsum(nums))
