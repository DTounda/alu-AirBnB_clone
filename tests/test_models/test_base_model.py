#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel."""

    def test_id_is_unique_string(self):
        """Test that each instance gets a unique string id."""
        a, b = BaseModel(), BaseModel()
        self.assertIsInstance(a.id, str)
        self.assertNotEqual(a.id, b.id)

    def test_datetimes(self):
        """Test created_at and updated_at are datetime objects."""
        m = BaseModel()
        self.assertIsInstance(m.created_at, datetime)
        self.assertIsInstance(m.updated_at, datetime)

    def test_str(self):
        """Test the string representation."""
        m = BaseModel()
        self.assertEqual(
            str(m), "[BaseModel] ({}) {}".format(m.id, m.__dict__))

    def test_save_updates_updated_at(self):
        """Test save() changes updated_at only."""
        m = BaseModel()
        old = m.updated_at
        m.save()
        self.assertGreater(m.updated_at, old)

    def test_to_dict(self):
        """Test to_dict() content and formats."""
        m = BaseModel()
        m.name = "My"
        d = m.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["name"], "My")
        self.assertEqual(d["created_at"], m.created_at.isoformat())
        self.assertIsInstance(d["updated_at"], str)

    def test_from_dict(self):
        """Test re-creating an instance from a dictionary."""
        m = BaseModel()
        m.my_number = 89
        n = BaseModel(**m.to_dict())
        self.assertEqual(n.id, m.id)
        self.assertEqual(n.my_number, 89)
        self.assertEqual(n.created_at, m.created_at)
        self.assertIsInstance(n.created_at, datetime)
        self.assertFalse(hasattr(n, "__class__") and "__class__" in n.__dict__)
        self.assertIsNot(m, n)

    def test_args_ignored(self):
        """Test that *args are not used."""
        m = BaseModel("x", 1)
        self.assertNotIn("x", m.__dict__.values())


if __name__ == '__main__':
    unittest.main()
