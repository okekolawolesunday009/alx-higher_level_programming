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
        <class '0-square.Square'>
        {}
    """
    def __init__(self, size):
        """
         Args:
            self: represents the instance of class.
            size (int) : the size of shape passed.
         Returns:
            int: size of int otherwise valueEror
        """
        self.__size = size
