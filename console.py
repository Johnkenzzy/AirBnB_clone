#!/usr/bin/python3
"""
This program contains the entry point of command interpreter
Class HBNBCommand is defined in this module and inherits from cmd.Cmd
"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter to make and view changes in hbnb project classes"""
    prompt = "(hbnb) "

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
        if class_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
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

        if class_name not in ['BaseModel', 'User']:
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

        if class_name not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
            return
        
        if not instance_id:
            print("** instance id missing **")
            return

        key = f"{class_name}.{class_id}"
        instance = storage.all().get(key)
        
        if instance:
            del storage.all()[key]
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances of a class"""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ['BaseModel', 'User']:
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
        if class_name not in ['BaseModel', 'User']:
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
