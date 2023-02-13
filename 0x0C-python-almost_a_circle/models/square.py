#!/usr/bin/python3
"""
class 'Square'
inherited from class 'Rectangle' in rectangle.py
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    sub-sub-class 'Square' of sub-class 'Rectangle' of class 'Base'
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor
        init method of class Square
        Arguments:
            size: size of Square object
            x: argument x
            y: argument y
            id: id value set to None at default
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        public getter for 'size'
        """
        val = self.width
        return val

    @size.setter
    def size(self, value):
        """
        public setter for 'size'
        Arguments:
            value: value assigned to width and height
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """
        returns string representation of the instance
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        Arguments:
            args: a list of arguments
            kwargs: a list of keyword arguments
        """
        if len(args) != 0:
            try:
                self.id = args[0]
            except IndexError:
                pass

            try:
                self.size = args[1]
            except IndexError:
                pass

            try:
                self.x = args[2]
            except IndexError:
                pass

            try:
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        public method that returns a dictionary representation of a square
        """
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["size"] = self.size
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary