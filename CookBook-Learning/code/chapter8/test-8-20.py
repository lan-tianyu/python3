import math
import operator


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({!r:}, {!r:})".format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(3, 4)
print(p)
print(vars(p))
print(p.distance(0, 0))
d = getattr(p, 'distance')(0, 0)
print(d)

dd = operator.methodcaller('distance', 0, 0)(p)
print(dd)

points = [Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8), Point(9, 10)]

points.sort(key=operator.methodcaller('distance', 5, 6))
print(points)

d = operator.methodcaller('distance', 0, 0)
print(d(p))