#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b, where a and b must be integers or floats.
    Floats are cast to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Vérification des valeurs spéciales inf et nan
    if isinstance(a, float) and (a == float('inf') or a == float('nan')):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b == float('inf') or b == float('nan')):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
