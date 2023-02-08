#!/usr/bin/python3
"""Defines a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr, value):
    """Adds new attribute to an object if possible
    Raises:
        TypeError exception if the attribute cannot be added
    """
    if not hasattr(obj, "__setattr__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
