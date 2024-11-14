#!/usr/bin/python3
"""
Module file_storage
This module defines the class FileStorage
"""
import os
import json
from models.base_model import BaseModel


class FileStorage():
    """Serializes/deserializes instances to a JSON file and vice versa"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return (FileStorage.__objects)
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serializable_objects = {}
        for key, obj in FileStorage.__objects.items():
            serializable_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(serializable_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects if the JSON file exits"""
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                    data = json.load(file)
                for key, obj_dict in data.items():
                    class_name = obj_dict.get("__class__")
                    if class_name:
                        cls = globals().get(class_name)
                        if cls:
                            obj = cls(**obj_dict)
                            FileStorage.__objects[key] = obj
            except json.JSONDecodeError:
                pass

