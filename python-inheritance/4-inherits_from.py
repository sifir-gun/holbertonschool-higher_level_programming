#!/usr/bin/python3
"""
This module contains a function that checks if an object
is an instance of a class that inherited (directly or indirectly)
from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that inherited (directly or
    indirectly) from a_class, but not if obj is an instance of a_class itself.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
