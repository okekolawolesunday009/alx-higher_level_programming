#!/usr/bin/python3
class Square:
     def __ini__(self, size=0):
           """Initializes a new square
           Args:
            size (int): The size of the new square.
        """
           if not isinstance(size, int):
               raise TypeError("size must be an integer")
           elif size < 0:
               raise ValueError("size must be >= 0")
           self.__size = size

        

