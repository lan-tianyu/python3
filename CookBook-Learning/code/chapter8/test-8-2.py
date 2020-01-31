from datetime import date

d = date(2012, 2, 13)
print(format(d))
print(format(d, '%A, %B, %d, %Y'))
print('{:%d %b %y}'.format(d))


_format = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d/day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _format.get(code)
        return fmt.format(d=self)


d = Date(2012, 2, 3)
print(d, format(d))
print(format(d, 'mdy'))
print('{:ymd}'.format(d))
print('{:mdy}'.format(d))
