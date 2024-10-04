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
    A custom class representing an object with attributes:
    name, age, and is_student.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Indicates if the person is a student.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a new instance of CustomObject.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the attributes of the object in a formatted manner.
        Format:
        Name: John
        Age: 25
        Is Student: True
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance of the object and
        saves it to the specified file.

        Args:
            filename (str):
            The name of the file where the serialized object will be saved.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an instance of CustomObject from the specified file.

        Args:
            filename (str):
            The name of the file from which to load the serialized object.

        Returns:
            CustomObject: The deserialized instance of CustomObject,
            or None in case of an error.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                return obj
        except Exception:
            return None
