#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Return new matrix.

    Raises:
        TypeError:
        ZeroDivisionError:
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if (not all(isinstance(element, (int, float)) for
                row in matrix for element in row)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
