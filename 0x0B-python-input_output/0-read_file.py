#!/usr/bin/python3
"""Defines a function that read files on UTF-8"""


def read_file(filename=""):
    """Read the file on UTF-8 and print to stdout"""

    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
