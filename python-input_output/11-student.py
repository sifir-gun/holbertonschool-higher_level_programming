#!/usr/bin/python3
"""
This module defines the Student class with methods for JSON serialization
and reloading from a JSON dictionary.
"""


class Student:
    """
    Defines a student by their first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        If attrs is a list of strings, only those attributes listed
        will be retrieved. Otherwise, all attributes will be retrieved.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of the student.
        """
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(
                self, key)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values
        from the given dictionary.

        Args:
            json (dict): A dictionary containing
            new values for the student's attributes.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
