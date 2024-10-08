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
    Abstract class Shape with abstract methods area and perimeter.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle class that implements the area and perimeter methods from Shape.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Returns the perimeter of the circle.
        If the radius is negative, it returns the perimeter as if the radius
        were positive (absolute value).
        """
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Rectangle class that implements the area and perimeter methods from Shape.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of the given shape.
    Uses duck typing to avoid explicit type checking.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
