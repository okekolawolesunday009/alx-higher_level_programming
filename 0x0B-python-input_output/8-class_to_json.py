#!/bin/usr/python3
"""function that returns the dictionary description 
    with simple data structure
"""


def class_to_json(obj):
    """function returns dict
        Args:
            obj(instance of a class): element which dict is to be printed out
    """
    return obj.__dict__