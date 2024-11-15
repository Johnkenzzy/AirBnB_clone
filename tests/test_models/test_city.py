#!/usr/bin/python3
"""Unittest for module city

Contains the test cases:
    TestCityInstantiation
    TestCityAttributes
    TestCityInheritance
"""
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestCityInstantiation(unittest.TestCase):
    """Tests instantiation of City and default attribute values."""

    def test_city_is_instance_of_base_model(self):
        """Test that City is an instance of BaseModel."""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_has_unique_id(self):
        """Test that each City instance has a unique id."""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_city_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        city = City()
        self.assertIsInstance(city.created_at, datetime)

    def test_city_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        city = City()
        self.assertIsInstance(city.updated_at, datetime)

    def test_city_default_state_id(self):
        """Test that the default state_id attribute is an empty string."""
        city = City()
        self.assertEqual(city.state_id, "")

    def test_city_default_name(self):
        """Test that the default name attribute is an empty string."""
        city = City()
        self.assertEqual(city.name, "")

    def test_city_kwargs_instantiation(self):
        """Test instantiation with keyword arguments."""
        kwargs = {
            "id": "1234-5678",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "state_id": "CA-123",
            "name": "Los Angeles",
        }
        city = City(**kwargs)
        self.assertEqual(city.id, "1234-5678")
        self.assertEqual(city.state_id, "CA-123")
        self.assertEqual(city.name, "Los Angeles")


class TestCityAttributes(unittest.TestCase):
    """Tests handling of City-specific attributes."""

    def test_assign_state_id(self):
        """Test assigning a value to state_id."""
        city = City()
        city.state_id = "CA-001"
        self.assertEqual(city.state_id, "CA-001")

    def test_assign_name(self):
        """Test assigning a value to name."""
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")


class TestCityInheritance(unittest.TestCase):
    """Tests inherited methods and attributes from BaseModel."""

    def test_city_str_representation(self):
        """Test the string representation of a City instance."""
        city = City()
        expected_str = f"[City] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), expected_str)

    def test_city_to_dict_contains_class(self):
        """Test that to_dict includes the __class__ key with value 'City'."""
        city = City()
        self.assertEqual(city.to_dict()["__class__"], "City")

    def test_city_save_updates_updated_at(self):
        """Test that save method updates updated_at."""
        city = City()
        prev_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, prev_updated_at)


class TestCityEdgeCases(unittest.TestCase):
    """Edge cases for the City class."""

    def test_empty_kwargs_instantiation(self):
        """Test instantiation with empty kwargs."""
        city = City(**{})
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_large_string_name(self):
        """Test assigning a very large string to the name attribute."""
        city = City()
        large_string = "x" * 10000
        city.name = large_string
        self.assertEqual(city.name, large_string)

    def test_large_string_state_id(self):
        """Test assigning a very large string to the state_id attribute."""
        city = City()
        large_string = "y" * 10000
        city.state_id = large_string
        self.assertEqual(city.state_id, large_string)


if __name__ == "__main__":
    unittest.main()
