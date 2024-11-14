#!/usr/bin/python3
"""
Module city
This module defines the City class that inherits from BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents city classification within application.

        Attributes:
            state_id (str): The unique identifier of the State instance.
            name (str): The name of the city.
    """
    state_id = ""
    name = ""
