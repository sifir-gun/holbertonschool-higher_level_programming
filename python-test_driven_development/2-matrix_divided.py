#!/usr/bin/python3
"""
This module defines a function matrix_divided which divides all
elements of a matrix by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Each element of the matrix must be an integer or float, and each row of
    the matrix must have the same size.

    Args:
        matrix (list of lists of int/float): Matrix to divide.
        div (int/float): The divisor.

    Returns:
        list of lists of float: New matrix with divided values.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """

    # Verify matrix is a list of lists of integers or floats
    if (
        not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(ele, (int, float)) for row in matrix for ele in row)
    ):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Check if all rows are the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round to 2 decimal places
    return [[round(ele / div, 2) for ele in row] for row in matrix]
