#!/usr/bin/python3
"""
Module: 3-is_kind_of_class
Defines a function that checks if an object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance or inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
