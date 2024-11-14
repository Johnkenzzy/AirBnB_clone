#!/usr/bin/python3
"""
Module state
This module defines the State class that inherits from BaseModel class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Classifies the State object, representing a state or region.

        Attributes:
            name (str): The name of the state.
    """
    name = ""
