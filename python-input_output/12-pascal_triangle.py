#!/usr/bin/python3
"""
This module defines the function pascal_triangle
which returns the Pascal's triangle up to n rows.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]  # First element is always 1
        for j in range(1, i):
            # Compute the value based on the previous row
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
