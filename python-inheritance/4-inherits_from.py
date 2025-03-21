#!/usr/bin/python3
"""
Module: 4-inherits_from
Defines a function that checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a
    class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class,
        and not an instance of a_class itself; False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
