p = (4, 5)
x, y = p
# x, y, z = p   # ValueError: not enough values to unpack (expected 3, got 2)
print(x, y)

data = ['acm', 50, 90.1, (2012, 12, 21)]

# name, shares, price = data    # ValueError: too many values to unpack (expected 3)
name, shares, price, date = data
print(name, shares, price, date)

name, shares, price, (year, month, day) = data
print(name, shares, price, year, month, day)

_, share1, _, date1 = data   # 占位符
print(share1, date1)


s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)
