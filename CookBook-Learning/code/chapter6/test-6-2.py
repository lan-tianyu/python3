import json
import os
from collections import OrderedDict

data = {'name': 'ACME', 'shares': 100, 'price': 542.23}

json_str = json.dumps(data)
print('json_str', json_str, isinstance(json_str, str))

dir_path = os.path.abspath(os.path.join(os.path.abspath(__file__),
                                        '../../../'))
file_name = os.path.join(dir_path, 'tmp/data.json')

with open(file_name, 'w') as f:
    json.dump(data, f)

with open(file_name, 'r') as f:
    print(json.load(f))

print(json.dumps(False))

s = '{"name": "ACME", "shares": 50, "price": 490.1}'
data = json.loads(s, object_pairs_hook=OrderedDict)
print('data:', data)


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


data2 = json.loads(s, object_hook=JSONObject)
print(data2, ' ', data2.name, data2.shares)

print('-' * 70)
data = json.loads(s)
print(json.dumps(data))
print(json.dumps(data, indent=4))

print('-' * 70)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
print(p, p.x, p.y)


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


classes = {'Point': Point}


def unserialize_instance(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for key, value in d.items():
            setattr(obj, key, value)
        return obj

    else:
        return d

    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d

s = json.dumps(p, default=serialize_instance)
print('s:', s)
a = json.loads(s, object_hook=unserialize_instance)
print(a, a.x, a.y)

