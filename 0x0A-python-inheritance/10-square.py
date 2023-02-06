#!/usr/bin/python3
"""A class square that inherits from a rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square that inherits from Rectangle"""

    def __init__(self, size):
        """Square initialization"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Method to calculate area of the square"""

        return self.__size * self.__size
