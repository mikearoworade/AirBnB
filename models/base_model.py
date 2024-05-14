#!/usr/bin/python3
"""Define the BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Represent the BaseModel of the HuheBnB"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args
            **kwargs (dict): key / value pairs of attributes.
        """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """Return string representation of an object"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)