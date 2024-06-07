#!/usr/bin/python3
import json
from models import base_model, amenity, city, place, review, state, user
from datetime import datetime

strptime = datetime.strptime

class FileStorage:
    """Represents an abstracted storage engine
    
    Attributes:
        __file_path (str): The name of the file to save objects
        __object (dict): A dictionary tahat stores every object by <class>.id.. Empty
    """
    __file_path = "file.json" # Private class attribute
    __objects = {} # Empty instantiated object

    """CNC - this variable is a dictionary with:
    keys: Class Names
    values: Class type (used for instantiation)
    """
    CNC = {
        'BaseModel': base_model.BaseModel,
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }

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
        fname = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(fname, mode='r', encoding='utf-8') as f_obj:
                loaded_objs = json.load(f_obj)
        except:
            return
        for obj_id, dict_val in loaded_objs.items():
            clsname = dict_val['__class__']
            FileStorage.__objects[obj_id] = FileStorage.CNC[clsname](**dict_val)
        
    def delete(self, obj=None):
        """Detele a given object from __objects, if it exist, else do nothing"""
        if obj:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        else:
            pass

    def close(self):
        """Call the reload method."""
        self.reload()

