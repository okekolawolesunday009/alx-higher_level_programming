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
        return ("[Retangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """subclass of rectangle"""
    def __init__(self, size):
        super().__init__(size, size)

    def __str__(self):
        """
            Returns a custom string representation of the square.

            Returns:
                str: A string in the format '[Rectangle] <size>/<size>'.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
