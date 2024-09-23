#!/usr/bin/python3
"""
This module contains a function that checks if an object
is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
