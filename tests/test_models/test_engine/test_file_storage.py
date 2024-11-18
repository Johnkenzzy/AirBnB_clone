#!/usr/bin/python3                                                       """                                                                      Unittest for FileStorage class in module models.file_storge              This test module defines the test class Test_FileStorage                 """
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests the FileStorage class"""

    def setUp(self):
        """Set up a clean test environment"""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}
        self.test_file = "test_file.json"
        FileStorage._FileStorage__file_path = self.test_file

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_method(self):
        """Test the `all` method"""
        self.assertEqual(self.storage.all(), {})
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", self.storage.all())

    def test_new_method(self):
        """Test the `new` method"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save_method(self):
        """Test the `save` method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        with open(self.test_file, "r") as file:
            data = json.load(file)

        self.assertIn(f"BaseModel.{obj.id}", data)
        self.assertEqual(data[f"BaseModel.{obj.id}"]["id"], obj.id)

    def test_reload_method(self):
        """Test the `reload` method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}

        self.storage.reload()
        self.assertIn(f"BaseModel.{obj.id}", self.storage.all())
        self.assertEqual(self.storage.all()[f"BaseModel.{obj.id}"].id, obj.id)

    def test_reload_nonexistent_file(self):
        """Test reload with a nonexistent file"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_corrupt_file(self):
        """Test reload with a corrupt JSON file"""
        with open(self.test_file, "w") as file:
            file.write("{not valid JSON}")

        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_missing_class(self):
        """Test reload with a missing class in the JSON"""
        invalid_object = {"id": "1234", "__class__": "NonExistentClass"}
        with open(self.test_file, "w") as file:
            json.dump({"NonExistentClass.1234": invalid_object}, file)

        self.storage.reload()
        self.assertNotIn("NonExistentClass.1234", self.storage.all())

    def test_reload_partial_data(self):
        """Test reload with partial object data"""
        partial_object = {"id": "1234", "__class__": "BaseModel"}
        with open(self.test_file, "w") as file:
            json.dump({"BaseModel.1234": partial_object}, file)

        self.storage.reload()
        self.assertIn("BaseModel.1234", self.storage.all())
        self.assertEqual(self.storage.all()["BaseModel.1234"].id, "1234")

    def test_save_empty_objects(self):
        """Test save with no objects"""
        self.storage.save()
        with open(self.test_file, "r") as file:
            data = json.load(file)
        self.assertEqual(data, {})

    def test_class_map(self):
        """Test that class_map correctly maps classes"""
        for class_name, cls in self.storage.class_map.items():
            self.assertIn(class_name, [
                "BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"
                ])
            self.assertTrue(issubclass(cls, BaseModel))

    """def test_save_file_permissions(self):
        # Test save when file permissions do not allow writing
        if os.path.exists(self.test_file):
            os.chmod(self.test_file, 0o400)  # Read-only

        obj = BaseModel()
        self.storage.new(obj)

        with self.assertRaises(PermissionError):
            self.storage.save()

        os.chmod(self.test_file, 0o600)  # Restore permissions"""

    def test_reload_large_file(self):
        """Test reload with a large JSON file"""
        lg_dat = {f"BaseModel.{i}": BaseModel().to_dict() for i in range(1000)}
        with open(self.test_file, "w") as file:
            json.dump(lg_dat, file)

        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 1000)

    def test_new_invalid_object(self):
        """Test new with an invalid object"""
        self.storage.new(None)
        self.assertEqual(self.storage.all(), {})

    def test_new_duplicate_key(self):
        """Test new with a duplicate key"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj2.id = obj1.id
        self.storage.new(obj1)
        self.storage.new(obj2)
        key = f"BaseModel.{obj1.id}"
        self.assertEqual(self.storage.all()[key], obj2)


if __name__ == "__main__":
    unittest.main()
