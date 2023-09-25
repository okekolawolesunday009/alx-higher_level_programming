#!/usr/bin/python3
"""Defines a class Base Geometry"""


class BaseGeometry:
    """class Geometry"""
    def area(self):
        """raise Exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raise either TypeError or ValueError"""
        if not isinstance (value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """subclass of BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self_height = height
