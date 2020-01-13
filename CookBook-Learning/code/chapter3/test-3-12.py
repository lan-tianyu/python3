from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta

a = timedelta(days=2, hours=3)
print(a)
b = timedelta(hours=3.5)
c = a + b
print(c, c.seconds, c.days, c.total_seconds())

print('-' * 40)

a = datetime(2019, 2, 13)
print(a)
b = datetime(2019, 3, 1)
print(b - a)
c = datetime(2012, 2, 13)
d = datetime(2012, 3, 1)
print(d - c)

print('-' * 50)
a = datetime(2012, 9, 23)
# print(a + timedelta(months=1))

print(a + relativedelta(months=+1))
print(a + relativedelta(months=+4))

b = datetime(2012, 12, 21)
d = b - a
print(d)
d = relativedelta(b, a)
print(d, d.months, d.days)