#!/usr/bin/python3
"""
Module review
This module defines the Review class that inherits from BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review left by a user for a place.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who created the review.
        text (str): The text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
