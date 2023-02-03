#!/usr/bin/python3

import numpy as np


class LazyMatrixMultiplicationError(Exception):
    pass


def lazy_matrix_mul(m_a, m_b):
    try:
        return np.dot(m_a, m_b)
    except ValueError as e:
        raise LazyMatrixMultiplicationError("Matrices"
                                            "are not multiplicable") from e
