import sqlite3

conn = sqlite3.connect('pydb.db')
print('open datatbase')

# conn.execute('''DROP TABLE company;''')

# conn.commit()

# conn.execute('''
# CREATE TABLE company (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INT NOT NULL,
#     address CHAR(50),
#     salary REAL
# );''')

conn.commit()

conn.execute('''
INSERT INTO company (name, age, address, salary) VALUES ('dafa', 27, 'Haikou', 20000.00), ('sdqwc', 30, 'Haikou', 12000.00)
''')

conn.commit()

cursor = conn.execute("SELECT id,name,age,address,salary from company;")
for row in cursor:
    id, name, age, address, salary = row[:]
    print(id, name, age, address, salary)

conn.close()