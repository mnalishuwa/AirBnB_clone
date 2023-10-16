#!/usr/bin/python3

"""
BaseModel module docs:
    Defines all common attributes/methods for subclasses
"""


from datetime import datetime, timezone
import json
import models
import re
import uuid

ISO_DT_YMD_RGX = (r"\d\d\d\d-(([0][1-9])|([1][0-2]))-(([0][1-9])"
                  "|([1-2]\d)|([3][0-1]))")  # noqa
ISO_TM_HMSM_RGX = (r"[T](([0-1]\d)|([2][0-3])):[0-5]\d:[0-5]\d"
                   "[.]\d{1,7}")  # noqa
UTC_OFFSET_HM_RGX = (r"(([+](([0]\d)|([1][0-4])):[0-5]\d)"
                     "|([-](([0]\d)|([1][0-2])):[0-5]\d))?")  # noqa


class BaseModel:
    """
    Base class template

    Attributes:
        __nb_objects - number of objects/instances

    Methods:
        __init__(self, id) - constructor method
    """

    def __init__(self, *args, **kwargs):
        """
        BaseModel constructor method

        Arguments:
            id

        Attributes:
            id

        Return:
            object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    # self.date_string_validator(value)
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    # Override built-in __str__ method
    def __str__(self):
        """
        Return the string representation of BaseModel object

        Arguments:

        Return:
            string - BaseModel object representation
        """
        class_name = self.__class__.__name__
        obj_dict = {key: value for key, value in self.__dict__.items()}
        return str("[{}] ({}) {}".format(class_name,
                                         self.id,
                                         obj_dict))

    def date_string_validator(self, date_string):
        """
        Validate string is isoformat for datetime
        convertion. Raises TypeError, ValueError

        Arguments:
        string - date_string

        Return:
        None
        """
        iso_dt_rgx = r"{}{}{}".format(ISO_DT_YMD_RGX,
                                      ISO_TM_HMSM_RGX,
                                      UTC_OFFSET_HM_RGX)
        if not re.match(iso_dt_rgx, date_string):
            print("date {} not valid isoformat\n".format(date_string))

    def date_validator(self, name, dt):
        """
        Check if the date object passed is valid

        Arguments:
            name - str
            dt - datetime
        Return:
            None
        """
        pass

    def save(self):
        """
        Updates the attribute updated at

        Arguments:

        Return:
            None
        """
        models.storage.save()
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        """
        Returns all key/value pairs of __dict__ of instance,
        including classname

        Arguments:

        Return:
            dictionary - dict object containing all key/value
        writable attributes
        """
        obj_dict = {key: value for key, value in self.__dict__.items()}
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        return obj_dict
