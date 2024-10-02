#!/usr/bin/python3
"""
This script contains a function that converts a JSON string to a Python object.
"""


import json


def from_json_string(my_str):
    """
    Converts a JSON string to its corresponding Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        any: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
