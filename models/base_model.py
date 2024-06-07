#!/usr/bin/python3
"""Define the BaseModel class"""
import models
import os
from uuid import uuid4
from datetime import datetime, timezone
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')

if STORAGE_TYPE == 'db':
    Base = declarative_base()
else:
    class Base:
        pass

class BaseModel:
    """Represent the BaseModel of the HugeBnB
        Attributes:
            id(sqlalchemy String): The BaseModel
            created_at(sqlalchemy DateTime)
            updated_at(sqlalchemy DateTime)
    """
    if STORAGE_TYPE == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))
        updated_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))

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
        dic = self.__dict__.copy()
        dic.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(clsname, self.id, dic)
    
    def save(self):
        """Update updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__.
            This method will be the first piece of the serialization/deseriaization process. This create a dictionary representation with "simple object type" of our BaseModel.
        """
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat() #return string
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return my_dict
    
    def delete(self):
        """Delete current instance from storage"""
        models.storage.delete(self)