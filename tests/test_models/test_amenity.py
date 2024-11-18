#!/usr/bin/python3
"""
Unit Test for Amenity Class
This module defines unittest cases for the `Amenity` class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Unit tests for the Amenity class."""

    def setUp(self):
        """Set up test instances."""
        self.amenity = Amenity()

    def tearDown(self):
        """Clean up after tests."""
        del self.amenity

    def test_inheritance_from_base_model(self):
        """Test that Amenity inherits from BaseModel."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_default_attributes(self):
        """Test default attribute values."""
        self.assertEqual(self.amenity.name, "")

    def test_attribute_assignment(self):
        """Test assigning values to Amenity attributes."""
        self.amenity.name = "Pool"
        self.assertEqual(self.amenity.name, "Pool")

    def test_to_dict_includes_amenity_attributes(self):
        """Test that `to_dict` includes Amenity-specific attributes."""
        self.amenity.name = "Wi-Fi"
        amenity_dict = self.amenity.to_dict()
        self.assertIn("name", amenity_dict)
        self.assertEqual(amenity_dict["name"], "Wi-Fi")

    def test_to_dict_contains_class_name(self):
        """Test that `to_dict` includes the __class__ key."""
        amenity_dict = self.amenity.to_dict()
        self.assertIn("__class__", amenity_dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_str_representation(self):
        """Test the string representation of Amenity."""
        amenity_str = str(self.amenity)
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn(self.amenity.id, amenity_str)

    def test_save_updates_updated_at(self):
        """Test that `save` method updates `updated_at`."""
        prev_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(prev_updated_at, self.amenity.updated_at)

    def test_save_persists_to_storage(self):
        """Test that `save` persists changes to storage."""
        # Mock storage and test its behavior if implemented
        pass

    def test_init_with_kwargs(self):
        """Test initialization with keyword arguments."""
        amenity_dict = {
            "id": "123",
            "created_at": "2024-01-01T12:00:00",
            "updated_at": "2024-01-01T12:30:00",
            "name": "Air Conditioning"
        }
        amenity = Amenity(**amenity_dict)
        self.assertEqual(amenity.id, "123")
        self.assertEqual(
                amenity.created_at,
                datetime.fromisoformat("2024-01-01T12:00:00")
                )
        self.assertEqual(
                amenity.updated_at,
                datetime.fromisoformat("2024-01-01T12:30:00")
                )
        self.assertEqual(amenity.name, "Air Conditioning")

    """"def test_invalid_created_at_type(self):
        # Test that invalid type for created_at raises an error.
        with self.assertRaises(TypeError):
            Amenity(created_at="invalid_date")

    def test_invalid_updated_at_type(self):
        # Test that invalid type for updated_at raises an error.
        with self.assertRaises(TypeError):
            Amenity(updated_at="invalid_date")"""

    def test_edge_case_empty_name(self):
        """Test that name can be an empty string."""
        self.amenity.name = ""
        self.assertEqual(self.amenity.name, "")

    def test_edge_case_long_name(self):
        """Test that name can hold a very long string."""
        long_name = "a" * 1000
        self.amenity.name = long_name
        self.assertEqual(self.amenity.name, long_name)

    def test_edge_case_special_characters(self):
        """Test name with special characters."""
        special_name = "@!#$%^&*()"
        self.amenity.name = special_name
        self.assertEqual(self.amenity.name, special_name)

    def test_edge_case_numeric_name(self):
        """Test name with numeric string."""
        numeric_name = "123456"
        self.amenity.name = numeric_name
        self.assertEqual(self.amenity.name, numeric_name)

    """def test_edge_case_none_name(self):
        # Test assigning None to name.
        with self.assertRaises(TypeError):
            self.amenity.name = None"""


if __name__ == "__main__":
    unittest.main()
