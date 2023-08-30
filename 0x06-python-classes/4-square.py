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

    Example:
        Area: 9
        'Square' object has no attribute 'size'
        'Square' object has no attribute '__size'
        Area: 25
    """
    def __init__(self, size=0):
        self.size = size

    ''' size getter'''
    def size(self):
        return self.__size

        ''' size setter'''
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''area of square'''
        return self.__size ** 2