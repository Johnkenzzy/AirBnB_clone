#!/usr/bin/python3
"""Unittest for module user

Contains the test cases:
    TestUserInstantiation
    TestUserAttributes
    TestUserInheritance
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUserInstantiation(unittest.TestCase):
    """Tests instantiation of User and default attribute values."""

    def test_user_is_instance_of_base_model(self):
        """Test that User is an instance of BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_has_unique_id(self):
        """Test that each User instance has a unique id."""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_user_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        user = User()
        self.assertIsInstance(user.created_at, datetime)

    def test_user_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        user = User()
        self.assertIsInstance(user.updated_at, datetime)

    def test_user_default_attributes(self):
        """Test that default attributes are initialized as empty strings."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_kwargs_instantiation(self):
        """Test instantiation with keyword arguments."""
        kwargs = {
            "id": "1234-5678",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "email": "test@example.com",
            "password": "password123",
            "first_name": "Test",
            "last_name": "User",
        }
        user = User(**kwargs)
        self.assertEqual(user.id, "1234-5678")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")

    def test_ignore_class_key_in_kwargs(self):
        """Test that __class__ key in kwargs is ignored."""
        user = User(__class__="AnotherClass")
        self.assertEqual(user.__class__.__name__, "User")


class TestUserAttributes(unittest.TestCase):
    """Tests handling of User-specific attributes."""

    def test_assign_email(self):
        """Test assigning a value to email."""
        user = User()
        user.email = "user@example.com"
        self.assertEqual(user.email, "user@example.com")

    def test_assign_password(self):
        """Test assigning a value to password."""
        user = User()
        user.password = "pass123"
        self.assertEqual(user.password, "pass123")

    def test_assign_first_name(self):
        """Test assigning a value to first_name."""
        user = User()
        user.first_name = "John"
        self.assertEqual(user.first_name, "John")

    def test_assign_last_name(self):
        """Test assigning a value to last_name."""
        user = User()
        user.last_name = "Doe"
        self.assertEqual(user.last_name, "Doe")


class TestUserInheritance(unittest.TestCase):
    """Tests inherited methods and attributes from BaseModel."""

    def test_user_str_representation(self):
        """Test the string representation of a User instance."""
        user = User()
        expected_str = f"[User] ({user.id}) {user.__dict__}"
        self.assertEqual(str(user), expected_str)

    def test_user_to_dict_contains_class(self):
        """Test that to_dict includes the __class__ key with value 'User'."""
        user = User()
        self.assertEqual(user.to_dict()["__class__"], "User")

    def test_user_save_updates_updated_at(self):
        """Test that save method updates updated_at."""
        user = User()
        prev_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, prev_updated_at)

    def test_user_to_dict_contains_user_attributes(self):
        """Test that to_dict includes User-specific attributes."""
        user = User()
        user_dict = user.to_dict()
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)


class TestUserEdgeCases(unittest.TestCase):
    """Edge cases for the User class."""

    def test_empty_kwargs_instantiation(self):
        """Test instantiation with empty kwargs."""
        user = User(**{})
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_invalid_datetime_in_kwargs(self):
        """Test handling of invalid datetime format in kwargs."""
        with self.assertRaises(ValueError):
            User(created_at="not-a-datetime")

    def test_large_string_assignment(self):
        """Test assigning a very large string to an attribute."""
        user = User()
        large_string = "x" * 10000
        user.email = large_string
        self.assertEqual(user.email, large_string)


if __name__ == "__main__":
    unittest.main()
