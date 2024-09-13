#!/usr/bin/python3
"""
This module defines the function text_indentation, which prints a text
with 2 new lines after each of these characters: '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints the text with 2 new lines after each
    of the characters: '.', '?', and ':'.

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    result = ""

    for char in text:
        result += char
        if char in special_chars:
            result += "\n\n"

    # Remove any extra spaces at the beginning or end of each printed line
    lines = result.split('\n')
    formatted_lines = [line.strip() for line in lines]

    print("\n".join(formatted_lines))
