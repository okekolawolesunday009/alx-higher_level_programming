#!/usr/bin/python3
"""defines a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """function that returns True or False if obj is === an instance of the inherited class"""
    current_class = type(obj)
    while current_class is not None:
        if current_class == a_class:
            return True
        current_class = current_class.__base__
    return False