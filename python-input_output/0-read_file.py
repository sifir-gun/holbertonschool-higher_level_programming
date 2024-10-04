#!/usr/bin/python3
"""
This script contains a function that reads the content of a file and prints it
to the standard output.
"""


def read_file(filename=""):
    """
    Reads the content of a file and prints it to the standard output.

    Args:
        filename (str, optional): The path of the file to read.
            Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
