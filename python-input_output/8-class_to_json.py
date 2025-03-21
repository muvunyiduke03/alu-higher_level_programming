#!/usr/bin/python3
"""
Module: 8-class_to_json
Defines a function that returns the dictionary description for
JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON
    serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
