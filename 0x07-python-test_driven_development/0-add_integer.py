#!/usr/bin/python3
"""defines a add function"""


def add_integer(a, b=0):
    """represents a add function'
     Args:
        a: first integer 
        b: second integer and optional
    Raises:
        TypeError: a arguments must be integers
                   b arguments must be integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integers")
    elif not isinstance(b, int):
        raise TypeError("b must be  an integer")
    return int(a + b)
