#!/usr/bin/python3


class Square:
    """
    A class used to represent a Square

    Attributes
    ----------
    size : float or int
        size of the square (default is 0)

    Methods
    -------
    area():
        Returns the area of the square
    """

    def __init__(self, size=0):
        """
        Parameters
        ----------
        size : float or int, optional
            Size of the square (default is 0)
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute

        Returns
        -------
        float or int
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute

        Parameters
        ----------
        value : float or int
            Size of the square

        Raises
        ------
        TypeError
            If size is not a number (float or integer)
        ValueError
            If size is less than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square

        Returns
        -------
        float or int
            The area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Override the default Not Equals behavior"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Override the default Less Than behavior"""
        return self.area() < other.area()

    def __le__(self, other):
        """Override the default Less Than or Equal To behavior"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Override the default Greater Than behavior"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Override the default Greater Than or Equal To behavior"""
        return self.area() >= other.area()
