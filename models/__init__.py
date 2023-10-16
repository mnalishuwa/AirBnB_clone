#!/usr/bin/python3


from .amenity import Amenity
from .base_model import BaseModel
from .city import City
from .engine import file_storage
from .place import Place
from .review import Review
from .state import State
from .user import User


standard_models = {Amenity.__name__: Amenity,
                   BaseModel.__name__: BaseModel,
                   City.__name__: City,
                   Place.__name__: Place,
                   Review.__name__: Review,
                   State.__name__: State,
                   User.__name__: User}

storage = file_storage.FileStorage()
storage.reload()
