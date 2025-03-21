#!/usr/bin/python3
"""
Module: 101-add_attribute
Defines a function to add a new attribute to an object if possible.
"""

def add_attribute(obj, name, value):
    """
    adds a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        name (str): The name of the attribute.
        value: The value to assign to the attribute.
 
    Raises:
        TypeError: If the object can't have anew attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name,value)
