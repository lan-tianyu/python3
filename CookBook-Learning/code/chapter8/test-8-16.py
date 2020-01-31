import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


class NewDate(Date):
    pass


d = Date.today()
c = NewDate.today()
t = Date(2018, 12, 28)
print(vars(d), vars(c), vars(t), t.today())

