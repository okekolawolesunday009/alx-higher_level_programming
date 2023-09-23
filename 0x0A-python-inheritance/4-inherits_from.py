#!/usr/bin/python3
"""defines a functioninherits_from"""


def inherits_from(obj, a_class):
    """
        function returns true if obj is an instance of class
        inherited(d or indirect from specified class)
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
