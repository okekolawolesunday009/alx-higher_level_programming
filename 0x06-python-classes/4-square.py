#!/usr/bin/python


class Square:
    def __init__(self, size=0):
        self.size = size

        ''' size getter'''
        def size(self):
            return self.__size

        ''' size setter'''
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            '''area of square'''
            return self.__size ** 2