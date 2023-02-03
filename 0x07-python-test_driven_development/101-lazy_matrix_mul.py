#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


class LazyMatrixMultiplicationError(Exception):
    pass
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """


def lazy_matrix_mul(m_a, m_b):
    try:
        return np.dot(m_a, m_b)
    except ValueError as e:
        raise LazyMatrixMultiplicationError("Matrices"
                                            "are not multiplicable") from e
