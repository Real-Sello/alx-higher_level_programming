#!/usr/bin/python3
"""Class Student that defines a student"""


class Student:
    """Student data"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieved dictionary representation of a Student instance"""
        return self.__dict__
