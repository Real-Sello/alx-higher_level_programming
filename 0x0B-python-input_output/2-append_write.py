#!/usr/bin/python3
"""append a string at the end of a file"""


def append_write(filename="", text=""):
    """A function that appends a file"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
