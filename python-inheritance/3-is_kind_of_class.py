#!/usr/bin/python3
"""
This module contains a function that checks if an object
is an instance of a class, or a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or if it's an instance
    of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or a subclass, False otherwise.
    """
    return isinstance(obj, a_class)
