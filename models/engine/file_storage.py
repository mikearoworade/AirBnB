#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Represents an abstracted storage engine
    
    Attributes:
        __file_path (str): The name of the file to save objects
        __object (dict): A dictionary tahat stores every object by <class>.id.. Empty
    """
    __file_path = "file.json" # Private class attribute
    __objects = {} # Empty instantiated object

    def __init__(self):
        """Constructor"""
        pass

    def all(self, cls=None):
        """Return the dictionary __object stored"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return FileStorage.__objects
    
    def new(self, obj):
        """Store a new object
        Sets in __objects the obj with key <obj class name>.id
        """
        objclsname = obj.__class__.__name__
        key  = "{}.{}".format(objclsname, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __object to JSON file (__file_path)"""
        objdict = {
            key: val.to_dict()
            for key, val in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file to __objects, if __file_path exists, else do nothing"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                FileStorage.__objects = {
                    key: eval(val["__class__"])(**val)
                    for key, val in objdict.items()
                }
        except FileNotFoundError:
            return
        
    def delete(self, obj=None):
        """Detele a given object from __objects, if it exist, else do nothing"""
        if obj:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        else:
            pass

