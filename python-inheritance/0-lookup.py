#!/usr/bin/python3
"""
Module: 0-lookup
Provides a function to retrieve the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """Returns a list of available attributes
    and methods of an object
    Args:
        obj: The object to inspect.

    Returns:
        List: A list of strings representing
        the attributes and methods of the object.
    """
    return dir(obj)
