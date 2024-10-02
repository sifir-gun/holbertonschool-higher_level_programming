#!/usr/bin/python3
"""
This script contains a function that writes text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes text to a specified file.

    Args:
        filename (str, optional):
        The path to the file where the text will be written.
            Defaults to an empty string.
        text (str, optional): The text to write to the file.
            Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
