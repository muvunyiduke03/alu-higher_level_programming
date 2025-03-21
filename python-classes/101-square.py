#!/usr/bin/python3


class Square:
    """
    A class used to represent a Square

    Attributes
    ----------
    size : int
        size of the square (default is 0)
    position : tuple
        position of the square (default is (0, 0))

    Methods
    -------
    area():
        Returns the area of the square

    my_print():
        Prints the square using the # character
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Parameters
        ----------
        size : int, optional
            Size of the square (default is 0)
        position : tuple, optional
            Position of the square (default is (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size attribute

        Returns
        -------
        int
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute

        Parameters
        ----------
        value : int
            Size of the square

        Raises
        ------
        TypeError
            If size is not an integer
        ValueError
            If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for the position attribute

        Returns
        -------
        tuple
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute

        Parameters
        ----------
        value : tuple
            Position of the square

        Raises
        ------
        TypeError
            If position is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square

        Returns
        -------
        int
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #, considering position and size
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square for printing

        Returns
        -------
        str
            The square as a string
        """
        if self.__size == 0:
            return ""
        result = ""
        for i in range(self.__position[1]):
            result += "\n"
        for i in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result.strip()