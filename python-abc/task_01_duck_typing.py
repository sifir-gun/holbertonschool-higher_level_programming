#!/usr/bin/python3
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract class Shape that defines the interface for shapes.
    Classes inheriting from Shape must implement the area and perimeter methods
    """

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Circle class that represents a circle.
    """

    def __init__(self, radius):
        """Initialize a circle with the given radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    """
    Rectangle class that represents a rectangle.
    """

    def __init__(self, width, height):
        """Initialize a rectangle with the given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.
    Uses duck typing, so the shape can be any object that implements
    the area and perimeter methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
