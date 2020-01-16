from datetime import timedelta, datetime

weekdays = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
    'Sunday'
]


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname) 
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    print(day_num, day_num_target, days_ago)
    target_day = start_date - timedelta(days=days_ago)
    return target_day


a = datetime(2019, 3, 2)
print(get_previous_byday('Friday', a))
print(get_previous_byday('Friday'))
