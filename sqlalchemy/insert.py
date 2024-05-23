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

row1 = Employees(name='Michael', position='Software Engineer') 
session.add(row1) #insert one row

session.add_all([Employees(name='Eric', position='Cybersecurity Engineer'),
                Employees(name='Adeniyi', position='Pharmacist'),
                Employees(name='Samuel', position='Doctor')])  # Insert multiple rows

session.commit() # Commit changes
