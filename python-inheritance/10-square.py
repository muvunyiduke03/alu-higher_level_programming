#!/usr/bin/python3
"""
Module: 10-square
Defines a class Square that inherits from Rectangle.
Provides methods to calculate the area of a square and validate its position.
"""

Rectangle = __import__('9-rectangle').rectangle


class Square(Rectangle):
    """
    A class to represent a square.
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """
        initialize a square instance.
        
        Args:
            size (int): The size of the square's side, must be a
            position integer."""
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
