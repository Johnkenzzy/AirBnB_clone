#!/usr/bin/python3
"""Unittest for module review

Contains the test cases:
    TestReviewInstantiation
    TestReviewAttributes
    TestReviewInheritance
    TestReviewEdgeCases
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime


class TestReviewInstantiation(unittest.TestCase):
    """Tests instantiation of Review and default attribute values."""

    def test_review_is_instance_of_base_model(self):
        """Test that Review is an instance of BaseModel."""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_review_has_unique_id(self):
        """Test that each Review instance has a unique id."""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_review_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        review = Review()
        self.assertIsInstance(review.created_at, datetime)

    def test_review_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        review = Review()
        self.assertIsInstance(review.updated_at, datetime)


class TestReviewAttributes(unittest.TestCase):
    """Tests default and custom attribute handling in Review."""

    def test_default_place_id(self):
        """Test that the default place_id attribute is an empty string."""
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_default_user_id(self):
        """Test that the default user_id attribute is an empty string."""
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_default_text(self):
        """Test that the default text attribute is an empty string."""
        review = Review()
        self.assertEqual(review.text, "")

    def test_assign_text(self):
        """Test assigning a value to text."""
        review = Review()
        review.text = "Great place!"
        self.assertEqual(review.text, "Great place!")

    def test_assign_user_id(self):
        """Test assigning a value to user_id."""
        review = Review()
        review.user_id = "user_123"
        self.assertEqual(review.user_id, "user_123")

    def test_assign_place_id(self):
        """Test assigning a value to place_id."""
        review = Review()
        review.place_id = "place_456"
        self.assertEqual(review.place_id, "place_456")


class TestReviewInheritance(unittest.TestCase):
    """Tests inherited methods and attributes from BaseModel."""

    def test_review_str_representation(self):
        """Test the string representation of a Review instance."""
        review = Review()
        expected_str = f"[Review] ({review.id}) {review.__dict__}"
        self.assertEqual(str(review), expected_str)

    def test_review_to_dict_contains_class(self):
        """Test that to_dict includes the __class__ key with value 'Review'."""
        review = Review()
        self.assertEqual(review.to_dict()["__class__"], "Review")

    def test_review_save_updates_updated_at(self):
        """Test that save method updates updated_at."""
        review = Review()
        prev_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(review.updated_at, prev_updated_at)


class TestReviewEdgeCases(unittest.TestCase):
    """Edge cases for the Review class."""

    def test_large_string_text(self):
        """Test assigning a very large string to the text attribute."""
        review = Review()
        large_text = "x" * 10000
        review.text = large_text
        self.assertEqual(review.text, large_text)

    """def test_invalid_text_type(self):
        # Test assigning a non-string value to text attribute.
        review = Review()
        with self.assertRaises(TypeError):
            review.text = 12345

    def test_non_string_user_id(self):
        # Test assigning a non-string value to user_id.
        review = Review()
        with self.assertRaises(TypeError):
            review.user_id = 9876

    def test_non_string_place_id(self):
        # Test assigning a non-string value to place_id.
        review = Review()
        with self.assertRaises(TypeError):
            review.place_id = 5432"""


if __name__ == "__main__":
    unittest.main()
