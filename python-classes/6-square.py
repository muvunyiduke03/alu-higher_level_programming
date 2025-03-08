#!/usr/bin/python3
"""
This module defines a class Square that represents a square
with a private size and a private position.
"""


class Square:
    """
    Represents a square defined by its size and its position.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): A tuple of 2 positive integers indicating
            the position (horizontal and vertical offsets) where the square
            should be printed.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or type(value[1]) is not int or \
            value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the character '#' considering the position.

        If size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print("")
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print("")
        # Print each line of the square with horizontal offset.
        for _ in range(self.__size):
            line = " " * self.__position[0] + "#" * self.__size
            print(line)
