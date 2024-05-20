#!/usr/bin/python3
"""Define the City class"""
from models.base_model import BaseModel

class City(BaseModel):
    """Represents the city class
    Attributes:
        state_id (str): The state id
        name (str): The city name
    """

    state_id = ""
    name = ""