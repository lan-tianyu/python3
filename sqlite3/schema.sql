DROP TABLE company;
CREATE TABLE company (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INT NOT NULL,
    address CHAR(50),
    salary REAL
);