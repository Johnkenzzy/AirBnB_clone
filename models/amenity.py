#!/usr/bin/python3
"""
Module amenity
This module defines the Amenity class that inherits from BaseModel class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity in the application projet.

        Attributes:
            name (str): The name of the amenity.
    """
    name = ""
