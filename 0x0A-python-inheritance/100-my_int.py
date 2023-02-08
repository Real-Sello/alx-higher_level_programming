#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """Inverts == and != int operators =="""

    def __eq__(self, other):
        """Overriding == opeartor with != behavior."""
        return not int.__eq__(self, other)

    def __ne__(self, other):
        """Overriding != operator with == behavior."""
        return not int.__ne__(self, other)
