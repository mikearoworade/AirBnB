from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

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

# Get single user
query = session.query(Employees).get(1)
print('Name: ', query.name, 'Position: ', query.position)

# Filter Employee
query = session.query(Employees).filter(Employees.name == 'Eric')
for employee in query:
    print('Name: ', employee.name, 'Position: ', employee.position)

query = session.query(Employees).all()
for employee in query:
    print('Name: ', employee.name, 'Position: ', employee.position)
