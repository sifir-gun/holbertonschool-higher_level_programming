#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div,
    rounding the results to 2 decimal places.

    Arguments:
    matrix -- list of lists of integers or floats
    div -- number (integer or float) by which to divide the matrix elements

    Returns:
    A new matrix with each element of the original matrix divided by div.

    Raises:
    TypeError -- if matrix is not a list of lists of integers/floats,
                 if the rows of the matrix are not of the same size,
                 or if div is not a number (integer or float)
    ZeroDivisionError -- if div is 0
    """
    # Vérification du type de la matrice
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Vérification que chaque élément est un entier ou un flottant
    # et que toutes les lignes sont de même taille
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    # Vérification du type de div et gestion de NaN et inf
    if not isinstance(div, (int, float)) or div != div or div == float('inf'):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Division de chaque élément et arrondi à 2 décimales
    return [[round(element / div, 2) for element in row] for row in matrix]
