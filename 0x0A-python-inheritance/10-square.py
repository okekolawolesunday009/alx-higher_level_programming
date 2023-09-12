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
        return ("[Retangle] {}/{}".format(self.__width, self.__size))

class Square(Rectangle):
    """subclass of rectangle"""
    def __init__(self, size):
        super().__init__(size)
        self.integer_validator("size", int)
        self.__size = size
    def area(self):
        """area of square"""
        return (self.__width * self.__size)