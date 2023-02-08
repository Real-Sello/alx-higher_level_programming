#!/usr/bin/python3
"""Defines a function that returns a JSON object"""
import json


def from_json_string(my_str):
    """return a python object represented by a JSON string"""
    return json.loads(my_str)
