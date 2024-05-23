"""Define user class"""
from models.base_model import BaseModel

class User(BaseModel):
    """Represent a User.
    
    Attributes:
        email (str): Email of the user
        password (str): Password of the user
        first_name (str): Firstname of the user
        last_name (str): Last of the user
    """

    email  = ""
    password = ""
    first_name = ""
    last_name = ""