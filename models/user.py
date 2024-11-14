#!/use/bin/python3
"""
Module user
This module defines the User class
User class inherits from BaseModel class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Difines essential users attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
