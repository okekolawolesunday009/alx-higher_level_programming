#!/usr/bin/python3
"""function that prints the number FIRST NAME AND LAST NAME togeda  IN """


def say_my_name(first_name, last_name=""):
    """function that prints the number FIRST NAME AND LAST NAME togeda
    Args:
        first_name: the name
        last_name: the last name
    Raises:
        TypeError: for size not int or float
        ValueError: size <= 0
    """
    if not isinstance(first_name, ):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {} {}', first_name, last_name)