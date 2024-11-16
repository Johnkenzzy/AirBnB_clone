#!/usr/bin/python3
"""
Module file_storage
This module defines the class FileStorage
"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """Serializes/deserializes instances to a JSON file and vice versa"""
    __file_path = "file.json"
    __objects = {}
    class_map = {
            "BaseModel": BaseModel, "User": User, "State": State,
            "City": City, "Amenity": Amenity, "Place": Place,
            "Review": Review
            }

    def all(self):
        """Returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serializable_objects = {}

        for key, obj in self.__objects.items():
            serializable_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(serializable_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects if the JSON file exits"""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding="utf-8") as file:
                    data = json.load(file)

                for key, obj_dict in data.items():
                    class_name = obj_dict.get("__class__")
                    if class_name:
                        cls = self.class_map.get(class_name)
                        if cls:
                            obj = cls(**obj_dict)
                            self.__objects[key] = obj

            except json.JSONDecodeError:
                pass
