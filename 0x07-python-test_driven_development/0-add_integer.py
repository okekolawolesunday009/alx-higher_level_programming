#!/usr/bin/python3
"""defines a add function"""


def add_integer(a, b=0):
    """represents a add function'
     Args:
        a: first integer 
        b: second integer
    Raises:
        TypeError: a arguments must be integers
                   b arguments must be integers
    """
    if not isinstance(a, int):
        raise TypeError("a arguments must be integers")
    elif not isinstance(b, int):
        raise TypeError("b is not an integer")
    return a + b