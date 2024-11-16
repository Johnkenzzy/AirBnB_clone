#!/usr/bin/python3
"""Unittest for module BaseModel

Contains the test cases:
    TestBaseModelInstantiation
    TestBaseModelStr
    TestBaseModelSave
    TestBaseModelToDict
"""
import unittest
from datetime import datetime, timedelta
from uuid import UUID
from models.base_model import BaseModel
import time


class TestBaseModelInstantiation(unittest.TestCase):
    """Tests instantiation of BaseModel and initialization of attributes."""

    def test_id_type(self):
        """Test that id is a valid UUID."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertTrue(UUID(model.id), "Generated id is not a valid UUID.")

    def test_unique_id(self):
        """Test that each instance has a unique id."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_type(self):
        """Test that created_at is a datetime object."""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_type(self):
        """Test that updated_at is a datetime object."""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_created_and_updated_at_initially_equal(self):
        """Test that created_at and updated_at are the same at instantiation."""
        model = BaseModel()
        self.assertEqual(model.created_at, model.updated_at)

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs."""
        kwargs = {
            "id": "1234-5678-9012",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, "1234-5678-9012")
        self.assertEqual(model.created_at.isoformat(), kwargs["created_at"])
        self.assertEqual(model.updated_at.isoformat(), kwargs["updated_at"])

    def test_ignore_class_key_in_kwargs(self):
        """Test that __class__ key in kwargs is ignored."""
        model = BaseModel(__class__="DummyClass")
        self.assertNotEqual(model.__class__.__name__, "DummyClass")


class TestBaseModelStr(unittest.TestCase):
    """Tests the __str__ method of BaseModel."""

    def test_str_format(self):
        """Test the output format of __str__."""
        model = BaseModel()
        expected = f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected)


class TestBaseModelSave(unittest.TestCase):
    """Tests the save method of BaseModel."""

    def test_save_updates_updated_at(self):
        """Test that save method updates updated_at attribute."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        time.sleep(0.01)
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_save_updated_at_increases(self):
        """Test that updated_at is set to a later time after save."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        time.sleep(0.01)
        model.save()
        self.assertGreater(model.updated_at, initial_updated_at)


class TestBaseModelToDict(unittest.TestCase):
    """Tests the to_dict method of BaseModel."""

    def test_to_dict_type(self):
        """Test that to_dict returns a dictionary."""
        model = BaseModel()
        self.assertIsInstance(model.to_dict(), dict)

    def test_to_dict_contains_all_keys(self):
        """Test that to_dict includes all instance attributes plus __class__."""
        model = BaseModel()
        model_dict = model.to_dict()
        expected_keys = {"id", "created_at", "updated_at", "__class__"}
        self.assertTrue(expected_keys.issubset(model_dict.keys()))

    def test_to_dict_class_name(self):
        """Test that __class__ in to_dict is correct."""
        model = BaseModel()
        self.assertEqual(model.to_dict()["__class__"], "BaseModel")

    def test_created_at_to_dict_format(self):
        """Test that created_at is in ISO format in to_dict output."""
        model = BaseModel()
        self.assertEqual(model.to_dict()["created_at"], model.created_at.isoformat())

    def test_updated_at_to_dict_format(self):
        """Test that updated_at is in ISO format in to_dict output."""
        model = BaseModel()
        self.assertEqual(model.to_dict()["updated_at"], model.updated_at.isoformat())

    def test_to_dict_does_not_modify_instance(self):
        """Test that to_dict does not modify the original instance."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertNotIn("__class__", model.__dict__)
        self.assertIn("__class__", model_dict)


class TestBaseModelEdgeCases(unittest.TestCase):
    """Edge case tests for BaseModel."""

    def test_save_without_changes(self):
        """Test save on instance without changes."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        time.sleep(0.01)
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_empty_kwargs_instantiation(self):
        """Test instantiation with empty kwargs."""
        model = BaseModel(**{})
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_invalid_datetime_in_kwargs(self):
        """Test handling of invalid datetime format in kwargs."""
        with self.assertRaises(ValueError):
            BaseModel(created_at="not-a-datetime")

    def test_to_dict_with_large_number_of_attrs(self):
        """Test to_dict with an instance having many attributes."""
        model = BaseModel()
        for i in range(100):
            setattr(model, f"attr_{i}", i)
        model_dict = model.to_dict()
        self.assertEqual(model_dict["attr_99"], 99)
        self.assertEqual(len(model_dict), 104)


if __name__ == "__main__":
    unittest.main()
