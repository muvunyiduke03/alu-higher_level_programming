#!/usr/bin/python3


class Rectangle:
    """
    A class used to represent a rectangle
    
    Attributes
    ----------
    width : int
        width of the rectangle (default is 0)
    height : int
        height of the rectangle (default is 0)
    
    Methods
    -------
    area():
        Returns the area of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Parameters
        ----------
        width : int, optional
            width of the rectangle (default is 0)
        height : int, optional
            Height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """
        Getter method for the width attribute
        
        Returns
        -------
        int
            The width of the rectangle
        """
        return self.__width
    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute
        
        Parameters
        ----------
        value : int
            Width of the rectangle
        
        Raises
        ------
        TypeError
            If width is not integer
        ValueError
            If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """
        Getter method for the height attribute
        
        Returns
        -------
        int
            The height of the rectangle
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute
        
        Parameters
        ----------
        value : int
            Height of the rectangle
        
        Raises
        ------
        TypeError
            If height is not an integer
        ValueError
            If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value
