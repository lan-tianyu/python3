from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 6
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

print(d)

for key in d:
    print(key, d[key])

print(json.dumps(d))
