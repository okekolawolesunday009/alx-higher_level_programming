#!/usr/bin/python3
"""A functional implementation of an empty class"""


class Rectangle:
    """
    class implementation of the rectangle

    Attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
    """

    number_of_instances = 0  # keep track of instances
    print_symbol = "#"  # class attribute for string representation

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle instance.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the width attribute

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Seter method for the width attribute

        Args:
            value (int): new width value

        Raises:
            TypeError: width must be an integer
            ValueError: width must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute

        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value: new height value

        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes area of the rectangle

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes perimeter of the rectangle

        Returns:
            int: perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns string representation of the rectangle.

        Returns:
           str: string containing the rectangle drawn with '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] *
                         self.__height)

    def __repr__(self):
        """
        Returns string representation of the rectangle object.

        Returns:
           str: string representation of the rectangle object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method to print a farewell message when an instance is
        deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangle and returns the one with the bigger/equal area

        Args:
           rect_1 (rectangle): The first rectangle to compare.
           rect_1 (rectangle): The second rectangle to compare.

        Raises:
            TypeError: rect_1/2 must be an integer.

        Returns:
            Rectangle: rectangle with bigger/equa area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def square(cls, size=0):
        """
        Creates a new Rectangle instance with width == height == size

        Args:
            size (int): size of the square (default 0)

        Returns:
            Rectangle: a new rectangle instance representing a square.
        """
        return cls(size, size)