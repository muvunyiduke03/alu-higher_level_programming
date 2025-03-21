#!/usr/bin/python3
"""
Module: 6-base_geometry
Defines a class BaseGeometry with a public instance method area
that raises an exception.
"""


class BaseGeometry:
    """
    A class to represent geometric shapes.
    """

    def area(self):
        """
        Raises an Exception to indicate that the method is not implemented.
        """
        raise Exception("area() is not implemented")
