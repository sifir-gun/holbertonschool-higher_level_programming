#!/usr/bin/python3
"""
This script contains a function that creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The path to the file that contains the JSON data.

    Returns:
        any: The Python object created from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
