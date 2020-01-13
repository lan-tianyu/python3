from datetime import date, timedelta, datetime
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    print('start_date: ', start_date)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_day = start_date + timedelta(days=days_in_month)
    return start_date, end_day


def date_range(first, end, step):
    while first < end:
        yield first
        first += step


a_day = timedelta(days=1)
print(a_day)
first_day = datetime(2013, 2, 11)
first_day, end_day = get_month_range(first_day)
generator_date = date_range(first_day, end_day, a_day)
for d in list(generator_date):
    print(d)
