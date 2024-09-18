#!/usr/bin/python3
"""
Module qui définit une classe Rectangle
"""


class Rectangle:
    """
    Classe qui définit un rectangle par sa largeur et sa hauteur.
    """

    def __init__(self, width=0, height=0):
        """
        Initialise les instances de la classe Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Récupère la largeur du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Définit la largeur du rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Récupère la hauteur du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Définit la hauteur du rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Retourne l'aire du rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Retourne le périmètre du rectangle.
        Si la largeur ou la hauteur est égale à 0, le périmètre est 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères du rectangle
        avec le caractère '#'.
        Si la largeur ou la hauteur est égale à 0, retourne une chaîne vide.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for _ in range(self.__height):
            rect.append("#" * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """
        Retourne une chaîne de caractères qui permet de recréer une nouvelle instance
        du rectangle en utilisant eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"
