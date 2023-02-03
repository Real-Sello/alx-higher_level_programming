#!/usr/bin/python3
"""Divides all elements of a matrix.
This function divides all elements of a given matrix by a divisor.
Parameters:
matrix (list): A list of lists of equal length, representing the matrix.
div (int or float): The divisor.

Returns:
list: A new matrix of divided matrix elements.

Raises:
TypeError: If the matrix is not a list of lists of integers or floats,
or if the rows in the matrix are of unequal length, or if the divisor
is not an integer or float.

Description:
This function divides all elements of the matrix by the divisor,
and rounds the results to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    This function divides all elements of a given matrix by a divisor.
    """

    if type(matrix) is not list or matrix == [] or matrix is None:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(isinstance(x, list) for x in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(k) == len(matrix[0]) for k in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    for lists in matrix:
        if not all(isinstance(elems, (int, float)) for elems in lists):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newlist = [[round(elem / div, 2) for elem in lists] for lists in matrix]
    return newlist
