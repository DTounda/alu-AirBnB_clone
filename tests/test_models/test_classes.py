#!/usr/bin/python3
"""Unit tests for User, State, City, Amenity, Place and Review."""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

ATTRS = {
    User: {"email": "", "password": "", "first_name": "", "last_name": ""},
    State: {"name": ""},
    City: {"state_id": "", "name": ""},
    Amenity: {"name": ""},
    Review: {"place_id": "", "user_id": "", "text": ""},
    Place: {"city_id": "", "user_id": "", "name": "", "description": "",
            "number_rooms": 0, "number_bathrooms": 0, "max_guest": 0,
            "price_by_night": 0, "latitude": 0.0, "longitude": 0.0,
            "amenity_ids": []},
}


class TestClasses(unittest.TestCase):
    """Test cases for classes inheriting from BaseModel."""

    def test_inheritance(self):
        """Test every class inherits from BaseModel."""
        for cls in ATTRS:
            self.assertTrue(issubclass(cls, BaseModel))

    def test_default_attributes(self):
        """Test class attribute defaults and types."""
        for cls, attrs in ATTRS.items():
            obj = cls()
            for name, value in attrs.items():
                with self.subTest(cls=cls.__name__, attr=name):
                    self.assertEqual(getattr(obj, name), value)
                    self.assertIs(type(getattr(obj, name)), type(value))

    def test_to_dict_class_name(self):
        """Test to_dict() holds the right class name."""
        for cls in ATTRS:
            self.assertEqual(cls().to_dict()["__class__"], cls.__name__)

    def test_from_dict(self):
        """Test every class can be rebuilt from its dictionary."""
        for cls in ATTRS:
            obj = cls()
            self.assertEqual(cls(**obj.to_dict()).id, obj.id)


if __name__ == '__main__':
    unittest.main()
