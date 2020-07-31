import os
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


"""
https://my.oschina.net/u/4277138/blog/3267049
"""


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_NAME = 'pydb.db'
DB_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, DB_NAME))

ModelBase = declarative_base()


class User(ModelBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=True)
    books = relationship('Book')


class Book(ModelBase):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=True)
    user_id = Column(String(20), Foreignkey('User.id'))


engine = create_engine(DB_URI)
# ModelBase.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


session.add(User(name='james'))
session.add(User(name='durant'))
session.add(User(name='curry'))
session.commit()

users = session.query(User).all()
for u in users:
    print(u)


session.add(Book(name='book1', user_id=1))
session.add(Book(name='book2', user_id=1))
session.add(Book(name='book3', user_id=1))
session.add(Book(name='book1', user_id=2))
session.add(Book(name='book2', user_id=3))
session.add(Book(name='book3', user_id=3))
session.commit()

books = session.query(Book).all()
for b in books:
    print(b)
