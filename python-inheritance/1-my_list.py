#!/usr/bin/python3
"""
Module: 1-my_list
Defines a MyList class that inherits from list and adds a method to print
the list sorted in ascending order.
"""
class Mylist(list):
    """
    A custom list class that extends the built-in list.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.

        Assumes that all elements of the list are integers.
        """
        print(sorted(self))
