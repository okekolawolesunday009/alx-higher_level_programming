#!/usr/bin/python3
"""function that prints the number SQUARES IN #"""


def print_square(size):
    """function that prints the number SQUARES IN #
    Args:
        size: the size of square
    Raises:
        TypeError: for size not int or float
        ValueError: size <= 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif not all(isinstance(size, float) or size < 0):
        raise TypeError('size must be an integer')
    elif size == 0:
        return
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print()