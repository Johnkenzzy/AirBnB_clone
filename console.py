#!/usr/bin/python3
"""
This program contains the entry point of command interpreter
Class HBNBCommand is defined in this module and inherits from cmd.Cmd
"""
import cmd
import sys
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
        if class_name != "BaseModel":
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
        class_id = args[1] if len(args) > 1 else None

        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        
        if not class_id:
            print("** instance id missing **")
            return

        key = f"{class_name}.{class_id}"
        instance = storage.all().get(key)
        
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class"""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        class_id = args[1] if len(args) > 1 else None

        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        
        if not class_id:
            print("** instance id missing **")
            return

        key = f"{class_name}.{class_id}"
        instance = storage.all().get(key)
        
        if instance:
            del storage.all()[key]
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        
        all_objs = storage.all()
        filtered_objs = []

        for obj in all_objs.values():
            if type(obj).__name__ == class_name:
                filtered_objs.append(str(obj))

        print(filtered_objs)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
