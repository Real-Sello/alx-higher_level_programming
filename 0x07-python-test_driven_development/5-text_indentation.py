#!/usr/bin/python3
"""
Defines function that prints a text
with 2 new lines after each of these characters: ., ? and :.
There should be no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    """
     Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    l = len(text)
    c = 0
    if text[0] == " ":
        while text[c] == " ":
            c += 1
    while c < l:
        if text[c] == " " and text[c - 1] == ".":
            while text[c] == " ":
                c += 1
        if text[c] == " " and text[c - 1] == "?":
            while text[c] == " ":
                c += 1
        if text[c] == " " and text[c - 1] == ":":
            while text[c] == " ":
                c += 1
        if text[c] == " " and text[c - 1] == "\n":
            while text[c] == " ":
                c += 1
        if text[c] == "." or text[c] == "?" or text[c] == ":":
            print("{}".format(text[c]))
            print("")
        else:
            print("{}".format(text[c]), end="")
        c += 1
