#!/usr/bin/python3
"""
Defines a function that print a square using character #
if size is less than 0, raise a ValueError exception
with the message size must be >= 0
"""


def print_square(size):
    """
    size (int): The height/width of the square.
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")
