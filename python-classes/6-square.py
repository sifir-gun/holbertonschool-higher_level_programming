#!/usr/bin/python3
"""
Ce module définit une classe Square qui représente un carré avec une position.
"""


class Square:
    """
    Classe qui définit un carré avec un attribut privé : size et position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialisation d'un carré avec une taille et une position optionnelles.

        Args:
            size (int): La taille du carré (doit être un entier >= 0).
            position (tuple): La position du carré (doit être un tuple de 2 entiers >= 0).

        Raises:
            TypeError: Si la taille ou la position ne sont pas valides.
            ValueError: Si la taille est inférieure à 0.
        """
        self.size = size  # Utilise le setter pour valider
        self.position = position  # Utilise le setter pour valider

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

    @property
    def position(self):
        """
        Getter pour récupérer la position du carré.

        Returns:
            tuple: La position du carré sous la forme d'un tuple (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter pour définir et valider la position du carré.

        Args:
            value (tuple): Un tuple de 2 entiers positifs définissant la position.

        Raises:
            TypeError: Si la position n'est pas un tuple de 2 entiers >= 0.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        L'impression tient compte de la position définie par le tuple (x, y).
        """
        if self.__size == 0:
            print("")
            return

        # Ajout des lignes vides en fonction de la position y
        for _ in range(self.__position[1]):
            print("")

        # Impression du carré avec des espaces en fonction de la position x
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
