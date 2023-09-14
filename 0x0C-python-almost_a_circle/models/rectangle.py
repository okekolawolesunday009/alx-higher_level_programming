#!/usr/bin/python3
"""1-rectanggle"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
      super().__init__(id)
      self.__width = width 
      self.__height = height
      self.__x = x 
      self.__y = y
    
    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height
    
    @height.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/set the x of the Rectangle."""
        return self.__x
    
    @x.setter
    def width(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/set the y of the Rectangle."""
        return self.__y
    
    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

