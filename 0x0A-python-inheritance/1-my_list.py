#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """prints sorted list"""

    def print_sorted(self):
        """prints the list sorted ascending order"""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
