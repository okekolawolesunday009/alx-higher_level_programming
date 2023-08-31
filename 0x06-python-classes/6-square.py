#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square.
    This class defines a basic square. More details about the class and its
    usage can be provided here.

    Attributes:
        size, position

    Methods:
        __init__: instance of the class is created
        area: gets the area of square
        position: position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''size getter'''
        return self.__size

    @size.setter
    def size(self, value)i:
        '''size setter'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position of Square getter."""
        return self.__position

    @position.setter
    def position(self, value):
        """position of Square getter."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area of Square ."""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
