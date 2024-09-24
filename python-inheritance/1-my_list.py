#!/usr/bin/python3
"""
Defines a class MyList that is a subclass of
list with a method to print the list sorted.
"""


class MyList(list):
    """
    A subclass of list that can print its elements in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
