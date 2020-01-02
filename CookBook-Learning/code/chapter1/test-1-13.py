from operator import itemgetter

rows = [{
    'fname': 'Brian',
    'lname': 'Jones',
    'uid': 1003
}, {
    'fname': 'David',
    'lname': 'Beazley',
    'uid': 1002
}, {
    'fname': 'John',
    'lname': 'Cleese',
    'uid': 1001
}, {
    'fname': 'Big',
    'lname': 'Jones',
    'uid': 1004
}]

row_by_fname = sorted(rows, key=itemgetter('fname'))
print(row_by_fname)

row_by_uid = sorted(rows, key=itemgetter('uid'))
print(row_by_uid)

row_by_fnameandlname = sorted(rows, key=itemgetter('lname', 'fname'))
print(row_by_fnameandlname)


# 性能不如itemgetter
row_by_fname = sorted(rows, key=lambda r: r['fname'])
print(row_by_fname)

row_by_uid = sorted(rows, key=lambda r: r['uid'])
print(row_by_uid)



