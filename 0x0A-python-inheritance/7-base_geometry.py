#!/usr/bin/python3
"""
function that creates a class BaseGeometry
"""


class BaseGeometry:
    """Empty class"""

    def area(self):
        """Public instance method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
