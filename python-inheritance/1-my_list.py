#!/usr/bin/python3
"""
This module provides a custom list class called MyList,
which inherits from the built-in list class.

MyList extends the functionality of the standard list by adding a
method that prints the list elements in ascending sorted order
without modifying the original list.

Example usage:

    Create an instance of MyList and use its methods:

        my_list = MyList()
        my_list.append(1)
        my_list.append(4)
        my_list.append(2)
        my_list.append(3)
        my_list.append(5)
        print(my_list)
        my_list.print_sorted()
        print(my_list)
"""


class MyList(list):
    """
    MyList is a subclass of the built-in list class that includes an
    additional method to print the list in sorted order.

    This class provides a simple way to display the list's elements in
    ascending order without altering the original list.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.

        This method does not modify the original list; it simply
        prints a sorted version of the list.
        """
        print(sorted(self))
