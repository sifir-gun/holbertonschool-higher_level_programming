#!/usr/bin/python3
"""
This script contains a function that converts a Python object to a JSON string.
"""

import json


def to_json_string(my_obj):
    """
    Converts a Python object to its JSON string representation.

    Args:
        my_obj (any): The Python object to be converted into a JSON string.

    Returns:
        str: The JSON string representation of the Python object.
    """
    return json.dumps(my_obj)
