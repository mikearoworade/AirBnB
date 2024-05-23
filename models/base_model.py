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
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, tformat)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """Return string representation of an object"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
    
    def save(self):
        """Update updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__.
            This method will be the first piece of the serialization/deseriaization process. This create a dictionary representation with "simple object type" of our BaseModel.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat() #return string
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict