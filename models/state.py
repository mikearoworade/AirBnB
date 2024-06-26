"""Define State class"""
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from os import getenv

STORAGE_TYPE = getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """Represents a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    if STORAGE_TYPE == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)   
        cities = relationship("City", back_populates="state", cascade="all, delete-orphan") # One to many relationship
    else:
        name = ""

        @property
        def cities(self):
            """Get a list of all related City objects"""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list