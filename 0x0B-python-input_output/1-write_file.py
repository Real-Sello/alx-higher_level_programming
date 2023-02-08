#!/usr/bin/python3
"""Defines a function that write a file on UTF-8"""


def write_file(filename="", text=""):
    """Function that writes a file on UTF-8"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
