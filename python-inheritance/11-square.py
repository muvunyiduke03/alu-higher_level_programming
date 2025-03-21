#!/usr/bin/python3
"""
Module: 11-square
Defines a class Square that inherits from rectangle.
Provides methods to calculate the area of a square 
and validate its size.
"""

Rectangle = __import__('9-rectangle').Rectangle


class sqaure(Rectangle):
    """
    A class to represent a square.
    Inherits from Rectangle class.

    Attributes:
        __size (int): The size of the square's side,
        validated as a positive integer.
    """

    def __init__(self, size):
        """
        Initializes a square instance.
 
        Args:
            size (int): The size of the square's side,
            must be a position integer.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the string representation of the square.
        
        Returns:
            str: The square description in the format
            [Square] <width>/<height>.
        """
        return f"[Square] {self.__size}/{self.__size}"
