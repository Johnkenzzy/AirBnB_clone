#!/usr/bin/python3
"""Unittest for module state

Contains the test cases:
    TestStateInstantiation
    TestStateAttributes
    TestStateInheritance
"""
import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestStateInstantiation(unittest.TestCase):
    """Tests instantiation of State and default attribute values."""

    def test_state_is_instance_of_base_model(self):
        """Test that State is an instance of BaseModel."""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_has_unique_id(self):
        """Test that each State instance has a unique id."""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_state_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        state = State()
        self.assertIsInstance(state.created_at, datetime)

    def test_state_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        state = State()
        self.assertIsInstance(state.updated_at, datetime)

    def test_state_default_name(self):
        """Test that the default name attribute is an empty string."""
        state = State()
        self.assertEqual(state.name, "")

    def test_state_kwargs_instantiation(self):
        """Test instantiation with keyword arguments."""
        kwargs = {
            "id": "1234-5678",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "name": "California",
        }
        state = State(**kwargs)
        self.assertEqual(state.id, "1234-5678")
        self.assertEqual(state.name, "California")


class TestStateAttributes(unittest.TestCase):
    """Tests handling of State-specific attributes."""

    def test_assign_name(self):
        """Test assigning a value to name."""
        state = State()
        state.name = "New York"
        self.assertEqual(state.name, "New York")


class TestStateInheritance(unittest.TestCase):
    """Tests inherited methods and attributes from BaseModel."""

    def test_state_str_representation(self):
        """Test the string representation of a State instance."""
        state = State()
        expected_str = f"[State] ({state.id}) {state.__dict__}"
        self.assertEqual(str(state), expected_str)

    def test_state_to_dict_contains_class(self):
        """Test that to_dict includes the __class__ key with value 'State'."""
        state = State()
        self.assertEqual(state.to_dict()["__class__"], "State")

    def test_state_save_updates_updated_at(self):
        """Test that save method updates updated_at."""
        state = State()
        prev_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, prev_updated_at)


class TestStateEdgeCases(unittest.TestCase):
    """Edge cases for the State class."""

    def test_empty_kwargs_instantiation(self):
        """Test instantiation with empty kwargs."""
        state = State(**{})
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)

    def test_large_string_name(self):
        """Test assigning a very large string to the name attribute."""
        state = State()
        large_string = "x" * 10000
        state.name = large_string
        self.assertEqual(state.name, large_string)


if __name__ == "__main__":
    unittest.main()
