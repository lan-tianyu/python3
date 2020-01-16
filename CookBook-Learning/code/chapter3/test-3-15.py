from datetime import datetime

text = '2012-02-29'
y = datetime.strptime(text, '%Y-%m-%d')
print(y)

z = datetime.now()
diff = z - y
print(diff)

# print(z)
# print(datetime.strptime(z, '%A %B %d %Y'))


def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))


print(parse_ymd('2109-2-1'))