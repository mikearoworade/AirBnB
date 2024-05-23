from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

engine = create_engine('sqlite:///hr.db')
Base = declarative_base()

class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# query = session.query(Employees).get(1)
# print(query.name, query.position)
# query.name = 'Michael Aroworade'
# session.commit()

# query = session.query(Employees).get(1)
# print(query.name, query.position)

query = session.query(Employees).filter(Employees.id == 1)
query.update({Employees.name: 'Michael'})
session.commit()

