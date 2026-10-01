#!/usr/bin/python3
"""Module defining the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review of a place."""

    place_id = ""
    user_id = ""
    text = ""
