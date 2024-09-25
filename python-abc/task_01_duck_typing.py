#!/usr/bin/python3
"""
This module defines an abstract class `Shape` and two concrete subclasses:
`Circle` and `Rectangle`. Each subclass implements the abstract methods
`area` and `perimeter` to calculate the respective geometric properties.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    This class defines the blueprint for shapes with abstract methods
    for calculating the area and the perimeter.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.

        This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.

        This method must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    A class representing a circle.

    This class inherits from `Shape` and implements the methods to
    calculate the area and perimeter of a circle.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a new Circle instance with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.

        Formula: π * radius^2

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Returns the perimeter (circumference) of the circle.

        Formula: 2 * π * radius

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    A class representing a rectangle.

    This class inherits from `Shape` and implements the methods to
    calculate the area and perimeter of a rectangle.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with a given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle.

        Formula: width * height

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.

        Formula: 2 * (width + height)

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of the given shape.

    This function accepts any object that follows the `Shape` interface,
    meaning it must implement the `area` and `perimeter` methods.

    Args:
        shape (Shape): An instance of a
        class that implements the `Shape` interface.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
