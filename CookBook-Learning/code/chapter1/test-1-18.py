from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('joesy@example.com', '123456')
print(sub, sub.addr, sub.joined)

print(len(sub))
addr, joined = sub
print(addr, joined)


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


records = [('a', 1, 2), ('c', 3, 4), ('b', 5, 6)]
print(compute_cost(records))

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


s = Stock('ACME', 100, 123.45)
print(s)
# s.shares = 75
s = s._replace(shares=75)
print(s)

print(compute_cost(records))

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {
    'name': 'ACME',
    'shares': 123,
    'price': 3455,
    'date': '2020-2-3',
    'time': '32w56478t'
}
print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))