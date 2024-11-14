#!/usr/bin/python3
"""
Module base_model
This module defines the parent class BaseModel
"""
import time
from datetime import datetime
from uuid import uuid4
# from models import storage


class BaseModel():
    """This defines all common attributes and methods of other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes"""
        curr_date = datetime.now() # .strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.name = None
        self.my_number = None
        self.id = str(uuid4())
        self.created_at = curr_date
        self.updated_at = curr_date

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        if isinstance(value, str):
                            value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            from models import storage
            storage.new(self)

    def __str__(self):
        """Returns a string representation of Square"""
        class_name = self.__class__.__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return (instance_dict)


