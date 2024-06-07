#!/usr/bin/python3
"""Define the City class"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import os
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')

class City(BaseModel, Base):
    """Represents a city for MySQL database
    Inherit from SQLAlchemy Base and links to the MySQL table cities.

    Attributes:
    __tablename__(str): THe name of the MySQL table to store Cities
        state_id (sqlalchemy String): The state id of the City
        name (sqlalchemy String): The city name
    """
    if STORAGE_TYPE == "db":
        __tablename__ = "cities"
        name = Column(String(60), nullable=False)
        state_id = Column(String(128), ForeignKey("states.id"), nullable=False)
        state = relationship("State", back_populates="cities") # Many to One
        places = relationship("Place", back_populates="cities", cascade="all")
    else:
        state_id = ''
        name = ''
        places = []