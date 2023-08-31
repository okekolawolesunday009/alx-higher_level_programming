#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represents a square.
    This class defines a basic square. More details about the class and its
    usage can be provided here.

    Attributes:
        size

    Methods:
        __init__: instance of the class is created
        area: gets the area of square
    Raises:
            TypeError: When the value passed in is not an integer
            ValueError: When the value passed in is less than 0
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        ''' size getter'''
        return self.__size

    @size.setter
    def size(self, value):
        ''' size setter'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''area of square'''
        return (self.__size ** 2)
