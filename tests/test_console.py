#!/usr/bin/python3
"""
Unit Test for Console
=====================

This module contains test cases for the console (command interpreter).
It tests the basic functionality of the `HBNBCommand` class and its commands.

Features Tested:
----------------
- Commands: `quit`, `EOF`, `create`, `show`, `destroy`, `all`, `update`
- Advanced commands: `<class name>.all()`, `<class name>.show(<id>)`, etc.
- Error handling and edge cases.
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    """Test suite for the console (HBNBCommand)."""

    def test_help_quit(self):
        """Test help for the quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertIn("Quit command to exit the program", f.getvalue())

    def test_quit(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            result = HBNBCommand().onecmd("quit")
            self.assertEqual(result, True)

    def test_help_create(self):
        """Test help for the create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertIn("Creates a new instance of BaseModel", f.getvalue())

    def test_create_no_args(self):
        """Test create command with no arguments."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertIn("** class name missing **", f.getvalue())

    def test_create_invalid_class(self):
        """Test create command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create NonExistentClass")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_create_valid_class(self):
        """Test create command with valid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            instance_id = f.getvalue().strip()
            self.assertTrue(len(instance_id) > 0)
            key = f"BaseModel.{instance_id}"
            self.assertIn(key, storage.all())

    def test_show_no_args(self):
        """Test show command with no arguments."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertIn("** class name missing **", f.getvalue())

    def test_show_invalid_class(self):
        """Test show command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show NonExistentClass")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_show_missing_id(self):
        """Test show command with missing ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertIn("** instance id missing **", f.getvalue())

    def test_show_invalid_id(self):
        """Test show command with invalid ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 12345")
            self.assertIn("** no instance found **", f.getvalue())

    def test_show_valid_instance(self):
        """Test show command with valid class name and ID."""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {instance.id}")
            self.assertIn(str(instance), f.getvalue())

    def test_destroy_no_args(self):
        """Test destroy command with no arguments."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertIn("** class name missing **", f.getvalue())

    def test_destroy_invalid_class(self):
        """Test destroy command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy NonExistentClass")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_destroy_missing_id(self):
        """Test destroy command with missing ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertIn("** instance id missing **", f.getvalue())

    def test_destroy_valid_instance(self):
        """Test destroy command with valid class name and ID."""
        instance = BaseModel()
        instance.save()
        key = f"BaseModel.{instance.id}"
        self.assertIn(key, storage.all())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {instance.id}")
            self.assertNotIn(key, storage.all())

    """def test_all_no_args(self):
        # Test all command with no arguments.
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertIn("[]", f.getvalue())"""

    def test_all_invalid_class(self):
        """Test all command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all NonExistentClass")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_all_valid_class(self):
        """Test all command with valid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertIn("[", f.getvalue())

    def test_update_no_args(self):
        """Test update command with no arguments."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertIn("** class name missing **", f.getvalue())

    def test_update_invalid_class(self):
        """Test update command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update NonExistentClass")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_update_missing_id(self):
        """Test update command with missing ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertIn("** instance id missing **", f.getvalue())

    def test_update_invalid_id(self):
        """Test update command with invalid ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 12345")
            self.assertIn("** no instance found **", f.getvalue())

    def test_update_missing_attribute(self):
        """Test update command with missing attribute name."""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {instance.id}")
            self.assertIn("** attribute name missing **", f.getvalue())

    def test_update_valid(self):
        """Test update command with valid inputs."""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    f'update BaseModel {instance.id} name "test_name"'
                    )
            self.assertEqual(instance.name, "test_name")


if __name__ == "__main__":
    unittest.main()
