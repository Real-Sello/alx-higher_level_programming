#!/usr/bin/python3
"""Class Square module"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """This class is a square, which is a type of rectangle. It is a
    subclass of the Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """This function is the constructor for the Square class. It
        initializes the instance variables for the square."""
        super().__init__(id, x, y, size, size)

    def __str__(self):
        """This function returns a string representation of the square."""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """This function is the getter for the size property."""
        return self.width

    @size.setter
    def size(self, value):
        """This function is the setter for the size property."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This function updates the attributes of the square."""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This function returns a dictionary representation of the square."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
