"""
Ce module fournit une classe CustomObject qui peut être sérialisée et
désérialisée en utilisant le module pickle. La classe représente une personne
avec un nom, un âge, et un indicateur si la personne est étudiante ou non.

Fonctions :
- serialize(self, filename) : Sérialise l'instance actuelle dans un fichier.
- @classmethod deserialize(cls, filename) :
Désérialise une instance de CustomObject depuis un fichier.
"""

import pickle


class CustomObject:
    """
    Une classe personnalisée représentant un objet avec les attributs :
    nom, âge et is_student.

    Attributs :
        name (str) : Le nom de la personne.
        age (int) : L'âge de la personne.
        is_student (bool) : Indique si la personne est étudiante.
    """

    def __init__(self, name, age, is_student):
        """
        Initialise une nouvelle instance de CustomObject.

        Args:
            name (str) : Le nom de la personne.
            age (int) : L'âge de la personne.
            is_student (bool) : Si la personne est étudiante.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet de manière formatée.
        """
        print(f"Nom : {self.name}")
        print(f"Âge : {self.age}")
        print(f"Est étudiant : {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'instance actuelle de l'objet et
        l'enregistre dans le fichier spécifié.

        Args:
            filename (str) :
            Le nom du fichier où l'objet sérialisé sera sauvegardé.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Objet sérialisé et sauvegardé dans {filename}.")
        except (OSError, pickle.PicklingError) as e:
            print(f"Échec de la sérialisation de l'objet : {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise une instance de CustomObject à partir du fichier spécifié.

        Args:
            filename (str) :
            Le nom du fichier à partir duquel charger l'objet sérialisé.

        Returns:
            CustomObject : L'instance désérialisée de CustomObject,
            ou None en cas d'erreur.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Échec de la désérialisation de l'objet : {e}")
            return None
