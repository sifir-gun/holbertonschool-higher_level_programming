#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
and has a method to print the list in sorted order.
"""


class MyList(list):
    """
    A custom list class that can print its elements in a sorted order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
