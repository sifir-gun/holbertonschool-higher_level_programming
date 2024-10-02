#!/usr/bin/python3
"""
This script contains a function that writes an object to a text file
using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj (any): The Python object to write to the file.
        filename (str): The name of the file to write the object to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
