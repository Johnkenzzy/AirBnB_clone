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

    def __init__(self, *args, **kwargs):
        """Initialize User instance attributes"""
        super().__init__(*args, **kwargs)
        if not kwargs:
            self.email = self.email
            self.password = self.password
            self.first_name = self.first_name
            self.last_name = self.last_name
