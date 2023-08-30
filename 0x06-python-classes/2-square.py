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
        <class '2-square.Square'>
        {'_Square__size': 3}
        <class '2-square.Square'>
        {'_Square__size': 0}
        'Square' object has no attribute 'size'
        'Square' object has no attribute '__size'
        size must be an integer
        size must be >= 0
    """
    def __init__(self, size=0):
        """Initializes a new square
            Args:
                size (int): The size of the new square.
            Return:
                size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
