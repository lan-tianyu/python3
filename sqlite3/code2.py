import os
from sqlalchemy import Column, String, INTEGER, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_URI = os.path.join(BASE_DIR, 'pydb.db')
print(BASE_DIR, DB_URI)

ModelBase = declarative_base()
engine = create_engine('sqlite:///{}'.format(DB_URI))


class User(ModelBase):
    __tablename__ = 'user'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(20))

    def __repr__(self):
        return "<USER(id={},name={})>".format(self.id, self.name)


ModelBase.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

print('{0}add{0}'.format('-' * 30))
session.add(User(name='Bob'))
session.add(User(name='hah'))
session.add(User(name='sweet'))
session.commit()

u = session.query(User).filter(User.id == 1).all()
u = session.query(User).all()
print('type', type(u))
print('user', u)
for row in u:
    print(row.id, row.name)


print('{0}query{0}'.format('-' * 30))
u = session.query(User).filter(User.id == 3).all()
print(u)

u = session.query(User).filter(User.name == 'hah').all()
print(u)

u = session.query(User).filter(User.name == 'hah1').all()
print(u)


print('{0}update{0}'.format('-' * 30))
u = session.query(User).filter(User.name == 'hah').all()
for r in u:
    r.name = 'sweethahah'
session.commit()

u = session.query(User).all()
print(u)


print('{0}delete{0}'.format('-' * 30))
target = session.query(User).filter(User.id % 2 == 0).all()
print('target', target)
for t in target:
    session.delete(t)
    session.commit()

u = session.query(User).all()
print('type', type(u))
print('user', u)
for row in u:
    print(row.id, row.name)
session.close()