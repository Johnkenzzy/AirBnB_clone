#!/usr/bin/python3
"""
Module place
This module defines the Place class that inherits from BaseModel class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place or accommodation in the project application.

    Attributes:
        city_id (str): The ID of the city where the place is located.
        user_id (str): The ID of the user who owns or manages the place.
        name (str): The name of the place.
        description (str): A detailed description of the place.
        number_rooms (int): Number of rooms in the place.
        number_bathrooms (int): Number of bathrooms in the place.
        max_guest (int): Maximum number of guests allowed.
        price_by_night (int): Price per night to stay at the place.
        latitude (float): Geographical latitude of the place.
        longitude (float): Geographical longitude of the place.
        amenity_ids (list of str): List of amenity IDs available at the place.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
