#!/usr/bin/python3
""" class module int"""


class MyInt(int):
    """class inherits from int"""
    def __eq__(self, other):
        """Override the == operator to return True when values are not equal"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Override the != operator to return True when values are equal"""
        return not super().__ne__(other)
