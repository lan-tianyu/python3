prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(prices)
max_price = max(prices)
print(min_price, max_price)

kk = zip(prices.values(), prices.keys())
for e in kk:
    print(e)

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price, max_price)

print(min(prices.values()))
print(max(prices.values()))

print(prices.get[min(prices, key=lambda k: prices[k])])
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))
