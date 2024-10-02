#!/usr/bin/python3
"""
This script contains a function that appends text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends text to a specified file.

    Args:
        filename (str, optional):
        The path to the file where the text will be appended.
            Defaults to an empty string.
        text (str, optional): The text to append to the file.
            Defaults to an empty string.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
