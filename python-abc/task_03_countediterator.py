#!/usr/bin/python3
class CountedIterator:
    """
    CountedIterator est une classe qui étend un itérateur
    pour suivre le nombre d'éléments itérés.

    Attributes:
        iterator (iterator): L'itérateur sur les éléments à parcourir.
        count (int): Compteur du nombre d'éléments itérés.
    """

    def __init__(self, iterable):
        """
        Initialise l'itérateur et le compteur.

        Args:
            iterable (iterable): Un objet itérable (ex: liste, tuple).
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Renvoie l'élément suivant de l'itérateur et incrémente le compteur.

        Raises:
            StopIteration: Si tous les éléments ont été parcourus.

        Returns:
            object: L'élément suivant de l'itérateur.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Renvoie le nombre d'éléments itérés jusqu'à présent.

        Returns:
            int: Le nombre d'éléments itérés.
        """
        return self.count
