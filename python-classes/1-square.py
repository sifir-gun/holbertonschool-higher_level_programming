#!/usr/bin/python3
"""
Ce module définit une classe Square qui représente un carré.
"""


class Square:
    """
    Classe qui définit un carré avec un attribut privé : size.
    """

    def __init__(self, size):
        """
        Initialisation d'un carré avec une taille.

        Args:
            size (int): La taille du carré.
        """
        self.__size = size  # Attribut privé
