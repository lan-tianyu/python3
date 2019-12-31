def drop_first_last(grade):
    first, *middle, last = grade
    return sum(middle) / len(middle)


grade = [1, 2, 3, 4, 5, 6, 7]
print(drop_first_last(grade))

record = ('Dave', 'dave@exaple.com', '123-456-7890', '234-567-8901')
name, email, *phone = record
print(name, email, phone)

record1 = ['Dave', 'dave@exaple.com', '123-456-7890', '234-567-8901']
name1, email1, *phone1 = record1
print(name1, email, phone1)

record2 = ['Dave', 'dave@exaple.com']
name2, email2, *phone2 = record2
print(name2, email2, phone2)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(sum(trailing) / len(trailing), current)

records = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4)]


def do_foo(x, y):
    print('do_foo', x, y)


def do_bar(s):
    print('do_bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    else:
        do_bar(*args)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fileld, homedir, sh = line.split(':')
print(uname, homedir, sh)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(year, name)
name1, *ign, (*ign, year1) = record
print(name1, year1)


items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head, tail)