#!/usr/bin/python

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

    Result:
    Area: 7921 for size: 89
    Area: 9 for size: 3
    size must be an intege
    """
    def __init__(self, size=0):
        self.__size = size

    def size(self):
        ''' size getter'''
        return self.__size

    def size(self, value):
        ''' size setter'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''area of square'''
        return (self.__size ** 2)
