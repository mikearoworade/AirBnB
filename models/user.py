"""Define user class"""
from models.base_model import Base
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """Represents a user for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table users.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        email: (sqlalchemy String): The user's email address.
        password (sqlalchemy String): The user's password.
        first_name (sqlalchemy String): The user's first name.
        last_name (sqlalchemy String): The user's last name.
        places (sqlalchemy relationship): The User-Place relationship.
        reviews (sqlalchemy relationship): The User-Review relationship
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", back_populates="users", cascade="all, delete-orphan") # One to many relationship
    reviews = relationship("Review", back_populates="users", cascade="all, delete-orphan") # One to many relationship