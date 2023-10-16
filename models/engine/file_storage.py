#!/usr/bin/python3


"""
File Storage Module
serializes instances to a JSON file and deserializes
JSON file to instances
"""


import json
import models
import os


class FileStorage:
    """
    Class for serializing BaseModel and BaseModel
    subclass' objects

    Attributes:
        __file_path - string, path to JSON file
        __objects - dictionary to store objects by
            <class name>.id

    Methods:
        __init__(self):
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """
    def __init__(self):
        """
        Constructor method, create FileStorage object,
        initialize file_path and objects dict

        Attributes:
            __file_path - string
            __objects - dict

        Arguments:

        Return:
            object - FileStorage object
        """
        self.file_path = os.path.join(os.getcwd(), "file.json")
        self.objects = {}

    @property
    def file_path(self):
        """
        Return string file path cwd of FileStorage object

        Arguments:

        Return:
            string - file path
        """
        return self.__file_path

    @file_path.setter
    def file_path(self, path_value=None):
        """
        Setter, updates file path attribute

        Arguments:
            path_value - string

        Return:
            None
        """
        # self.validate_string(path_value)
        self.__file_path = os.path.join(os.getcwd(), "file.json")
        if path_value and path_value.strip():
            if os.path.exists(path_value.strip()):
                self.__file_path = path_value.strip()
        # self.__file_path = path_value

    @property
    def objects(self):
        """
        Getter for objects dict

        Arguments:

        Return:
            dict - __objects dict
        """
        return self.__objects

    @objects.setter
    def objects(self, objects_dict):
        """
        Setter for objects dict

        Argumenst:
            objects_dict - dict

        Return:
            None
        """
        # validate_dictionary(objects_dict)
        self.__objects = {key: value for key, value
                          in objects_dict.items()
                          if isinstance(value, models.base_model.BaseModel)}

    def all(self):
        """
        Returns __objects dict

        Arguments:

        Return:
            dict - __objects
        """
        return self.objects

    def new(self, obj):
        """
        Adds an object to __objects

        Arguments:
            obj - BaseModel object or BaseModel subclass

        Return:
            None
        """
        # self.validate_object(obj)
        if not isinstance(obj, models.base_model.BaseModel):
            return
        new_name = obj.__class__.__name__
        new_id = getattr(obj, 'id', None)
        if not new_name or not new_id:
            return
        key = "{}.{}".format(new_name, new_id)
        self.objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        (path: __file_path)

        Arguments:

        Return:
            None
        """
        with open(self.file_path, mode='w+', encoding='utf-8') as file_handle:
            objects_repr = {object_key: object_value.to_dict()
                            for object_key, object_value in self.objects.items()}
            objects_json = json.dumps(objects_repr)
            file_handle.write(objects_json)

    def reload(self):
        """
        Deserializes the JSON file to __objects

        Arguments:

        Return:
            None
        """
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file_handle:
                objects_json = file_handle.read()
                objects_repr = json.loads(objects_json)
                for repr_key, repr_value in objects_repr.items():
                    class_name = repr_value['__class__']
                    obj = models.standard_models[class_name](**repr_value)
                    self.new(obj)
        except FileNotFoundError:
            pass
