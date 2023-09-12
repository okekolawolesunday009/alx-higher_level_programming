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
class Rectangle(BaseGeometry):
    """subclass of BaseGeometry"""
    def __init__(self, width, height):
        self._width = None
        self._height = None
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self_height = height
    
