#!/usr/bin/python3

class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if not isinstance(value, int ):
            raise TypeError("{name} must be an integer")
        elif value < 0:
            raise ValueError("{name} must be greater than 0")
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        return (self.__width * self.__height)
    def __str__(self):
        """The function for use in print() and str()
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__size))

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size)
        self.integer_validator("size", int)
        self.__size = size
    def area(self):
        return (self.__width * self.__size)
    def __str__(self):
        """The function for use in print() and str()
        """
        return ("[square] {}/{}".format(self.__width, self.__size))

