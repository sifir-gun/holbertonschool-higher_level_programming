#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that represents a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a new square instance.

        Args:
            size (int): The size of the square (both width and height).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The descrip of the square in the format [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
