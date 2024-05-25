from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///company.db')
Base = declarative_base()

class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)
    projects = relationship('Projects', back_populates='employees')

class Projects(Base):
    __tablename__= 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    emp_id = Column(Integer, ForeignKey('employees.id'))
    employees = relationship('Employees', back_populates='projects')

# Employees.projects = relationship('Projects', back_populates='employees')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

emp1 = Employees(name='Michael Aroworade', position='DevOps Engineer')
emp1.projects = [Projects(name='Python for Everyone'), Projects(name='Python DSA')]
session.add(emp1)

rows = [
    Employees(
        name='Eric Imoh',
        position='Frontend Developer',
        projects=[Projects(name='React JS'), Projects(name='Javascript')]
    ),
    Employees(
        name='Adeniyi Aroworade',
        position='Data Analytics',
        projects=[Projects(name='Data Analytics'), Projects(name='Power BI')]
    )
]
session.add_all(rows) 

session.commit()