"""
This module provides functions for serializing a Python dictionary to a
JSON file and deserializing a JSON file back into a Python dictionary.

Functions:
- serialize_and_save_to_file(data, filename):
Serializes and saves a dictionary to a JSON file.
- load_and_deserialize(filename):
Loads and deserializes a JSON file back into a dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The Python dictionary to be serialized.
        filename (str): The filename where the JSON data will be saved.
        If the file exists, it will be replaced.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file back into a Python dictionary.

    Args:
        filename (str):
        The filename from which to load and deserialize the JSON data.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
