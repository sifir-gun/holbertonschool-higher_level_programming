#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b, where a and b must be integers or floats.
    Floats are cast to integers before addition.
    """
    # Vérification des types et des valeurs NaN
    if not isinstance(a, (int, float)) or a != a:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b != b:
        raise TypeError("b must be an integer")

    # Vérification des valeurs infinies
    if isinstance(a, float) and a == float('inf'):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and b == float('inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
