#!/usr/bin/python3
"""
This program contains the entry point of command interpreter
Class HBNBCommand is defined in this module and inherits from cmd.Cmd
"""
import cmd
import sys
import shlex
import ast
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter to make and view changes in hbnb project classes"""
    prompt = "(hbnb) "
    class_list = [
            'BaseModel', 'User', 'State', 'City',
            'Amenity', 'Place', 'Review'
            ]
    class_map = {
            "BaseModel": BaseModel, "User": User, "State": State,
            "City": City, "Amenity": Amenity, "Place": Place,
            "Review": Review
            }

    def do_quit(self, line):
        """Quit command to exit the program gracefully"""
        return (True)

    def do_EOF(self, line):
        """EOF command to handle the end of file (EOF) input"""
        print()
        return (self.do_quit(line))

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it and prints the id

            Ex: create BaseModel
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        cls = self.class_map[class_name]
        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance

           Ex: show BaseModel 1234-1234-1234
        """
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        instance_id = args[1] if len(args) > 1 else None

        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        if not instance_id:
            print("** instance id missing **")
            return

        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)

        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class

            Ex: destroy BaseModel 1234-1234-1234
        """
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        instance_id = args[1] if len(args) > 1 else None

        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        if not instance_id:
            print("** instance id missing **")
            return

        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)

        if instance:
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances of a class"""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        filtered_objs = []

        for obj in all_objs.values():
            if type(obj).__name__ == class_name:
                filtered_objs.append(str(obj))

        print(filtered_objs)

    def do_update(self, line):
        """Updates an instance based on the class name and id

            Ex: update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = shlex.split(line)

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        instance_id = args[1] if len(args) > 1 else None
        if not instance_id:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        obj_key = f"{class_name}.{instance_id}"
        if obj_key not in all_objs:
            print("** no instance found **")
            return

        attr_name = args[2] if len(args) > 2 else None
        if not attr_name:
            print("** attribute name missing **")
            return

        attr_value = args[3] if len(args) > 3 else None
        if not attr_value:
            print("** value missing **")
            return

        obj = all_objs[obj_key]

        if attr_name in ("id", "created_at", "updated_at"):
            print("** attribute cannot be updated **")
            return

        current_value = getattr(obj, attr_name, None)
        if isinstance(current_value, int):
            try:
                attr_value = int(attr_value)
            except ValueError:
                print("** invalid value type **")
                return
        elif isinstance(current_value, float):
            try:
                attr_value = float(attr_value)
            except ValueError:
                print("** invalid value type **")
                return
        elif isinstance(current_value, str):
            attr_value = str(attr_value)

        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_count(self, line):
        """Retrieve the number of instances of a class"""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        num_of_instances = 0

        for obj in all_objs.values():
            if type(obj).__name__ == class_name:
                num_of_instances += 1

        print(num_of_instances)

    def default(self, line):
        """
        Handles special commands in dot notation.
        Examples:
            <class name>.all()
            <class name>.count()
            <class name>.show(<id>)
            <class name>.destroy(<id>)
            <class name>.update(<id>, <attribute>, <value>)
        """
        if "." not in line or "(" not in line or ")" not in line:
            print(f"** Unknown command: {line} **")
            return

        try:
            class_name, rest = line.split(".", 1)
            command, args = rest.split("(", 1)
            args = args.rstrip(")")
        except ValueError:
            print(f"** Unknown command: {line} **")
            return

        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        if command == "all":
            self.do_all(f"{class_name}")
        elif command == "count":
            self.do_count(f"{class_name}")
        elif command == "show":
            self.do_show(f"{class_name} {args}")
        elif command == "destroy":
            self.do_destroy(f"{class_name} {args}")
        elif command == "update":
            self._handle_update(class_name, args)
        else:
            print(f"** Unknown command: {line} **")

    def _handle_update(self, class_name, args):
        """
        Handle update commands.
        Examples:
            <class name>.update(<id>, <attribute name>, <attribute value>)
            <class name>.update(<id>, <dictionary of attributes>)
        """
        parts = args.split(", ", 1)
        if len(parts) < 2:
            print("** instance id missing **")
            return

        instance_id = parts[0].strip("\"'")
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)

        if not instance:
            print("** no instance found **")
            return

        if "{" in parts[1] and "}" in parts[1]:
            try:
                attributes = ast.literal_eval(parts[1])
                if not isinstance(attributes, dict):
                    pass
            except (SyntaxError, ValueError):
                print("** invalid dictionary format **")
                return

            for attr, value in attributes.items():
                setattr(instance, attr, value)
            instance.save()
        else:
            attr_parts = parts[1].split(", ", 1)
            if len(attr_parts) < 2:
                print("** attribute value missing **")
                return

            attr_name = attr_parts[0].strip("\"'")
            attr_value = attr_parts[1].strip("\"'")
            setattr(instance, attr_name, attr_value)
            instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
