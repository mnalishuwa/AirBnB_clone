#!/usr/bin/python3


"""
Review Module
"""

import models.base_model


class Review(models.base_model.BaseModel):
    """
    Review model blueprint

    Attributes:
    name - string

    Methods:
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        super().__init__(*args, **kwargs)
