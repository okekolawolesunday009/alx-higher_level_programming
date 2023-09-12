#!/usr/bin/python3
"""Defines a class Base Geometry"""


class BaseGeometry:
    """class Geometry"""
    def area(self):
        """raise Exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raise either TypeError or ValueError"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """subclass of BaseGeometry"""
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area of rectancle"""
        return (self.__width * self.__height)

    def __str__(self):
        """The function for use in print() and str()
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
