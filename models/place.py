#!/usr/bin/python3


"""
Place Module
"""


import models.base_model


class Place(models.base_model.BaseModel):
    """
    Place model blueprint

    Attributes:
    name - string

    Methods:
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        super().__init__(*args, **kwargs)
