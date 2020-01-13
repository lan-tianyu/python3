from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b, a * b)
c = a * b
print(c, c.numerator, c.denominator, float(c), c.limit_denominator(8))

x = 3.75
print(Fraction(*x.as_integer_ratio()))