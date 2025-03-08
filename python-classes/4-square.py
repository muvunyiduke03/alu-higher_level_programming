#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    Represents a square with a private attribute for its size.

    The size is made private to control its type and value.
    The getter and setter allow controlled access to the private
    attribute __size, enabling validation when setting its value.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance with an optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with value validation.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the current square area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
