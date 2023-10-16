#!/usr/bin/python3


"""
Amenity Module
"""

import models.base_model


class Amenity(models.base_model.BaseModel):
    """
    Amenity model blueprint

    Attributes:
    name - string

    Methods:
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        super().__init__(*args, **kwargs)
