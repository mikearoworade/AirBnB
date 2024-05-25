from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


my_model = BaseModel()
my_model_json = my_model.to_dict()
print(my_model_json)
print()
fs = FileStorage()

# All Classes
all_states = fs.all()
print(all_states)



