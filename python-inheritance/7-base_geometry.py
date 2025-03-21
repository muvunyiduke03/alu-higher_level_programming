#!/usr/bin/python3
"""
Module: 7-base_geometry
Defines a class BaseGeometry with methods for area calculation
and integer validation.
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
    
    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the parameter (always a string).
            value (any): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
