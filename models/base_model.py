#!/usr/bin/python3
"""
Module base_model
This module defines the parent class BaseModel
"""
import time
datetime = __import__("datetime").datetime
uuid4 = __import__("uuid").uuid4


class BaseModel():
    """This defines all common attributes and methods of other classes"""

    def __init__(self, **kwargs):
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
                        value = datetime.fromisoformat(value)
                        value if isinstance(value, str) else value
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of Square"""
        class_name = self.__class__.__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates updated_at with the current datetime"""
        curr_date = datetime.now()
        self.updated_at = curr_date

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return (instance_dict)



my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
# my_new_model = BaseModel(you="me")
# my_new_model.name = "My_First_Model"
# my_new_model.my_number = 89
print(my_new_model.id)
print(my_model_json)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
