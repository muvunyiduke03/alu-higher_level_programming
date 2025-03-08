#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    Represents a square.
    The size of a square is crucial for computations like area or perimeter,
    and having it private enables the class to control access and modification.
    """

    def __init__(self, size):
        """
        Initialize a new square.
        
        Args:
             size: The size of the square (no type/value verification).
        """
        self.__size = size
