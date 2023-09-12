#!/usr/bin/python3
"""Defines a class Base Geometry"""


class BaseGeometry:
    """class Geometry"""
    def area(self):
        """raise Exception error"""
        raise Exception("area() is not implemented")
    @staticmethod
    def integer_validator(self, name, value):
        """raise either TypeError or ValueError"""
        if not isinstance(value, int):
            raise TypeError("{name} must be an integer")
        elif value < 0:
            raise ValueError("{name} must be greater than 0")
