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
        self.size = size  # Utilise le setter pour valider

    @property
    def size(self):
        """
        Getter pour récupérer la taille du carré.

        Returns:
            int: La taille du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter pour définir et valider la taille du carré.

        Args:
            value (int): La nouvelle taille du carré.

        Raises:
            TypeError: Si la taille n'est pas un entier.
            ValueError: Si la taille est inférieure à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Retourne l'aire du carré.

        Returns:
            int: L'aire du carré (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Imprime le carré avec le caractère # dans stdout.
        Si la taille est égale à 0, imprime une ligne vide.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
