#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage."""

    def setUp(self):
        """Back up file.json and the stored objects."""
        self.saved = dict(models.storage.all())
        models.storage.all().clear()
        if os.path.exists("file.json"):
            os.rename("file.json", "tmp_backup.json")

    def tearDown(self):
        """Restore file.json and the stored objects."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("tmp_backup.json"):
            os.rename("tmp_backup.json", "file.json")
        models.storage.all().clear()
        models.storage.all().update(self.saved)

    def test_storage_type(self):
        """Test storage is a FileStorage and all() returns a dict."""
        self.assertIsInstance(models.storage, FileStorage)
        self.assertIsInstance(models.storage.all(), dict)

    def test_new(self):
        """Test new() stores the object under <class>.<id>."""
        m = BaseModel()
        self.assertIs(models.storage.all()["BaseModel." + m.id], m)

    def test_save_and_reload(self):
        """Test objects survive a save/reload cycle."""
        m, u = BaseModel(), User()
        u.first_name = "Betty"
        models.storage.save()
        models.storage.all().clear()
        models.storage.reload()
        objs = models.storage.all()
        self.assertIn("BaseModel." + m.id, objs)
        self.assertEqual(objs["User." + u.id].first_name, "Betty")
        self.assertIsInstance(objs["User." + u.id], User)

    def test_reload_without_file(self):
        """Test reload() does nothing if the file doesn't exist."""
        models.storage.reload()
        self.assertEqual(models.storage.all(), {})


if __name__ == '__main__':
    unittest.main()
