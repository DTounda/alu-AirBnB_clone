#!/usr/bin/python3
"""Module defining BaseModel, the parent of all AirBnB classes."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines the common attributes and methods of all other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance or rebuild one from a dictionary."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Return the string [<class name>] (<id>) <__dict__>."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current time and save to storage."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        data = dict(self.__dict__)
        data["__class__"] = self.__class__.__name__
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        return data
