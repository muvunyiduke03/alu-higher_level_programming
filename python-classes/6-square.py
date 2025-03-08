#!/usr/bin/python3
"""
This module defines a class Square that represents a square
with a private size and position.
"""


class Square:
    """
    Represents a square defined by its size and its position.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): A tuple of 2 positive integers representing
                            the position (horizontal and vertical offsets)
                            where the square should be printed.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position (offset) of the square.
                                        Defaults to (0, 0).

        Raises:
            TypeError: if size is not an integer or if position is not a tuple
                       of 2 positive integers.
            ValueError: if size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
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
        """
        Set the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (
            type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the character '#'.

        The square is printed with the horizontal and vertical offsets
        specified by position. If size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print("")
            return

        # Print vertical offset: position[1] newlines.
        for _ in range(self.__position[1]):
            print("")

        # For each row, print horizontal offset (spaces) followed by '#' characters.
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
