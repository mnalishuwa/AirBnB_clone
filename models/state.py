#!/usr/bin/python3


"""
State Module
"""

import models.base_model


class State(models.base_model.BaseModel):
    """
    State model blueprint

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
