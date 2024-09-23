#!/usr/bin/python3
"""
This module defines a class BaseGeometry with a method to raise an exception.
"""


class BaseGeometry:
    """
    A class representing geometry with an unimplemented area method.
    """
    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")
