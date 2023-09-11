#!/usr/bin/python3
"""defines a functioninherits_from"""


def inherits_from(obj, a_class):
    """
        function returns true if obj is an instance of class
        inherited(d or indirect from specified class)
    """
    current_class = type(obj)
    while current_class is not None:
        if current_class == a_class:
            return True
        current_class = current_class.__base__
    return False