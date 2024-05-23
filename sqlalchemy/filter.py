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

# More Filter
# query = session.query(Employees).filter(Employees.id != 3)
# for employee in query:
#     print('Name: ', employee.name, 'Position: ', employee.position)

# like operator
# query = session.query(Employees).filter(Employees.name.like('E%')) # Nmae that start with E
# for employee in query:
#     print('Name: ', employee.name, 'Position: ', employee.position)

# in operator
# query = session.query(Employees).filter(Employees.id.in_([1,3])) # Nmae that start with E
# for employee in query:
#     print('Name: ', employee.name, 'Position: ', employee.position)

# and, or operator
query = session.query(Employees).filter(or_(Employees.id > 1, Employees.name.like('E%'))) # Nmae that start with E
for employee in query:
    print('Name: ', employee.name, 'Position: ', employee.position)