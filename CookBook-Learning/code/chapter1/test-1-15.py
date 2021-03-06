from operator import itemgetter
from itertools import groupby
from collections import defaultdict

rows = [
    {
        'address': '5412 N CLARK',
        'date': '07/01/2012'
    },
    {
        'address': '5148 N CLARK',
        'date': '07/04/2012'
    },
    {
        'address': '5800 E 58TH',
        'date': '07/02/2012'
    },
    {
        'address': '2122 N CLARK',
        'date': '07/03/2012'
    },
    {
        'address': '5645 N RAVENSWOOD',
        'date': '07/02/2012'
    },
    {
        'address': '1060 W ADDISON',
        'date': '07/02/2012'
    },
    {
        'address': '4801 N BROADWAY',
        'date': '07/01/2012'
    },
    {
        'address': '1039 W GRANVILLE',
        'date': '07/04/2012'
    },
]


def grouby_func():
    rows.sort(key=itemgetter('date'))
    print(rows)
    print('-' * 80)

    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for item in items:
            print(' ', item)


grouby_func()
print('-' * 80)
rows = [
    {
        'address': '5412 N CLARK',
        'date': '07/01/2012'
    },
    {
        'address': '5148 N CLARK',
        'date': '07/04/2012'
    },
    {
        'address': '5800 E 58TH',
        'date': '07/02/2012'
    },
    {
        'address': '2122 N CLARK',
        'date': '07/03/2012'
    },
    {
        'address': '5645 N RAVENSWOOD',
        'date': '07/02/2012'
    },
    {
        'address': '1060 W ADDISON',
        'date': '07/02/2012'
    },
    {
        'address': '4801 N BROADWAY',
        'date': '07/01/2012'
    },
    {
        'address': '1039 W GRANVILLE',
        'date': '07/04/2012'
    },
]


def defaultdict_func():
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)
    for date, items in rows_by_date.items():
        print(date)
        for item in items:
            print(' ', item)


defaultdict_func()
