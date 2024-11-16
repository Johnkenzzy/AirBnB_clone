#!/usr/bin/python3
"""Unittest for module place

Contains the test cases:
    TestPlaceInstantiation
    TestPlaceAttributes
    TestPlaceInheritance
    TestPlaceEdgeCases
"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime


class TestPlaceInstantiation(unittest.TestCase):
    """Tests instantiation of Place and default attribute values."""

    def test_place_is_instance_of_base_model(self):
        """Test that Place is an instance of BaseModel."""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_place_has_unique_id(self):
        """Test that each Place instance has a unique id."""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_place_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        place = Place()
        self.assertIsInstance(place.created_at, datetime)

    def test_place_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        place = Place()
        self.assertIsInstance(place.updated_at, datetime)


class TestPlaceAttributes(unittest.TestCase):
    """Tests default and custom attribute handling in Place."""

    def test_default_city_id(self):
        """Test that the default city_id attribute is an empty string."""
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_default_user_id(self):
        """Test that the default user_id attribute is an empty string."""
        place = Place()
        self.assertEqual(place.user_id, "")

    def test_default_name(self):
        """Test that the default name attribute is an empty string."""
        place = Place()
        self.assertEqual(place.name, "")

    def test_default_number_rooms(self):
        """Test that the default number_rooms attribute is 0."""
        place = Place()
        self.assertEqual(place.number_rooms, 0)

    def test_default_number_bathrooms(self):
        """Test that the default number_bathrooms attribute is 0."""
        place = Place()
        self.assertEqual(place.number_bathrooms, 0)

    def test_default_amenity_ids(self):
        """Test that the default amenity_ids attribute is an empty list."""
        place = Place()
        self.assertEqual(place.amenity_ids, [])

    def test_assign_name(self):
        """Test assigning a value to name."""
        place = Place()
        place.name = "Beach House"
        self.assertEqual(place.name, "Beach House")

    def test_assign_number_rooms(self):
        """Test assigning a value to number_rooms."""
        place = Place()
        place.number_rooms = 5
        self.assertEqual(place.number_rooms, 5)

    def test_assign_amenity_ids(self):
        """Test assigning a list of amenity IDs."""
        place = Place()
        place.amenity_ids = ["wifi", "pool", "gym"]
        self.assertEqual(place.amenity_ids, ["wifi", "pool", "gym"])


class TestPlaceInheritance(unittest.TestCase):
    """Tests inherited methods and attributes from BaseModel."""

    def test_place_str_representation(self):
        """Test the string representation of a Place instance."""
        place = Place()
        expected_str = f"[Place] ({place.id}) {place.__dict__}"
        self.assertEqual(str(place), expected_str)

    def test_place_to_dict_contains_class(self):
        """Test that to_dict includes the __class__ key with value 'Place'."""
        place = Place()
        self.assertEqual(place.to_dict()["__class__"], "Place")

    def test_place_save_updates_updated_at(self):
        """Test that save method updates updated_at."""
        place = Place()
        prev_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(place.updated_at, prev_updated_at)


class TestPlaceEdgeCases(unittest.TestCase):
    """Edge cases for the Place class."""

    def test_large_string_name(self):
        """Test assigning a very large string to the name attribute."""
        place = Place()
        large_string = "x" * 10000
        place.name = large_string
        self.assertEqual(place.name, large_string)

    def test_large_number_rooms(self):
        """Test assigning a very large number of rooms."""
        place = Place()
        place.number_rooms = 10000
        self.assertEqual(place.number_rooms, 10000)

    def test_negative_price_by_night(self):
        """Test assigning a negative value to price_by_night."""
        place = Place()
        place.price_by_night = -100
        self.assertEqual(place.price_by_night, -100)

    def test_non_numeric_latitude(self):
        """Test assigning a non-numeric value to latitude."""
        place = Place()
        with self.assertRaises(TypeError):
            place.latitude = "invalid_latitude"

    def test_invalid_amenity_ids_type(self):
        """Test assigning a non-list value to amenity_ids."""
        place = Place()
        with self.assertRaises(TypeError):
            place.amenity_ids = "not_a_list"


if __name__ == "__main__":
    unittest.main()
