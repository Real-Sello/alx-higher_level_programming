#!/usr/bin/python3
"""Function that return the list of available attributes
    and methods of an object"""


def lookup(obj):
    """Return a list object"""
    return dir(obj)
