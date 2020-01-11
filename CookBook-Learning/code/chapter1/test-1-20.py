from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c.get('x'), c.get('y'), c.get('z'))

print(len(c))

c['z'] = 5
c['y'] = 7
print(c)
del c['x']
print(c)

values = ChainMap()
values['x'] = 1
print(values)
values = values.new_child()
print(values)
values['x'] = 2
print(values)
values = values.new_child()
print(values)
values['x'] = 3
print(values)
print(values['x'])

print('-' * 50)

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged)
print(merged['z'])

merged = dict(a)
merged.update(b)
print(merged)
print(merged['z'])
a['x'] = 13
print(merged, merged['x'])

print('-' * 50)

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c, c.get('z'))
a['x'] = 12
print(c, c.get('x'))
