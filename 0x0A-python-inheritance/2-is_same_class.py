#!/usr/bin/python3
"""defines a function is_same_class"""


def is_same_class(obj, a_class):
    """function that returns True or False if obj is === an instance of the specified class"""
    if type(obj) == (a_class):
       return True
    else:
        return False
        