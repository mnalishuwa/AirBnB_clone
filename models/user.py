#!/usr/bin/python3


"""
User module
"""

import models.base_model


class User(models.base_model.BaseModel):
    """
    User class - subclass of BaseModel class

    Attributes:
        email - str
        password - str
        first_name - str
        last_name - str

    Methods:
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        super().__init__(*args, **kwargs)
