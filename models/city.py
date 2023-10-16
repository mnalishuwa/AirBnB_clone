#!/usr/bin/python3


"""
City Module
"""

import models.base_model


class City(models.base_model.BaseModel):
    """
    City model blueprint

    Attributes:
    state_id - State.id
    name - string

    Methods:
    """
    state = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        super().__init__(*args, **kwargs)
