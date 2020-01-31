from time import localtime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


d = Date.__new__(Date)
print(d, vars(d))
data = dict(year=2018, month=12, day=28)
for k, v in data.items():
    setattr(d, k, v)
print(d.year, d.month, d.day, vars(d))


dd = Date.today()
print(vars(dd))



