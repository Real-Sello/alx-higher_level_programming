#!/usr/bin/python3
"""
Divides all elements of a matrix.

This function divides all elements of a given matrix by a divisor.

Parameters:
matrix (list): A list of lists of equal length, representing the matrix.
div (int or float): The divisor.

Returns:
list: A new matrix of divided matrix elements.

Raises:
TypeError: If the matrix is not a list of lists of integers or floats, or if the rows in the matrix are of unequal length, or if the divisor is not an integer or float.

Description:
This function divides all elements of the matrix by the divisor, and rounds the results to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    This function divides all elements of a given matrix by a divisor.
    Parameters:
        matrix (list): A list of lists of equal length, representing the matrix.
        div (int or float): The divisor.
    Returns:
        list: A new matrix of divided matrix elements.
    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats, or if the rows in the m      atrix are of unequal length, or if the divisor is not an integer or float.
    Description:
        This function divides all elements of the matrix by the divisor, and rounds the results to 2 d      ecimal places.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
