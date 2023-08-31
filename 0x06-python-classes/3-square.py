#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represents a square.
    This class defines a basic square. More details about the class and its
    usage can be provided here.
    
    Attributes:
        size

    Methods:
        Nil

    Example:
        Area: 9
        'Square' object has no attribute 'size'
        'Square' object has no attribute '__size'
        Area: 25
    """
    def __init__(self, size=0):
        """Initializes a new square
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square.
            Arguments:
                self: instance of a class
            Returns:
                self * self
        """
        return (self.__size ** 2)
