#!/usr/bin/python3
import json
from models.base_model import BaseModel

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

    def all(self):
        """Return the dictionary __object stored"""
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


