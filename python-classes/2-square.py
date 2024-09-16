#!/usr/bin/python3
"""
Ce module définit une classe Square qui représente un carré.
"""


class Square:
    """
    Classe qui définit un carré avec un attribut privé : size.
    """

    def __init__(self, size=0):
        """
        Initialisation d'un carré avec une taille optionnelle.

        Args:
            size (int): La taille du carré (doit être un entier >= 0).

        Raises:
            TypeError: Si la taille n'est pas un entier.
            ValueError: Si la taille est inférieure à 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
