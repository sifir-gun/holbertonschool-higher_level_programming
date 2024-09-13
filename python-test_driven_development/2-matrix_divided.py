#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): A list of lists where each element is an
        integer or float.
        div (int or float): The number by which to divide the matrix elements.

    Returns:
        list of lists: A new matrix with each element divided by div
        and rounded to 2 decimal places
        2 decimal places.

    Raises:
        TypeError: If the matrix contains non-numbers
        or the rows are not the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is zero.
    """

    # Check if matrix is a list of lists of integers/floats
    if not (
        isinstance(matrix, list) and
        all(isinstance(row, list) for row in matrix)
    ):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Check if all rows are of the same size
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    return [[round(num / div, 2) for num in row] for row in matrix]
