#!/usr/bin/python3
"""1-rectanggle"""


from models.base import Base


class Rectangle(Base):
    """Subclass of base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance (value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/set the x of the Rectangle."""
        return self.__x
    
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/set the y of the Rectangle."""
        return self.__y
    
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rectangle"""
        return (self.__width * self.__height)
    
    def display(self):
        """prints in stdout the Rectangle instance with the character # """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end ="")
            for _ in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """Return string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
    def update(self, *args, **kwargs):
        """
        Update attributes using positional arguments.
        Args:
            args: Positional arguments in the order width, height, x, y, id.
        """
        if len(args) > 0:
            for i in range(len(args)):
                if len(args) >= 1:
                    self.id = args[0]
                if len(args) >= 2:
                    self.width = args[1]
                if len(args) >= 3:
                    self.height = args[2]
                if len(args) >= 4:
                    self.x = args[3]
                if len(args) >= 5:
                    self.y = args[4]
        else:
            if len(kwargs) > 0:
                for key in kwargs.keys():
                    if key == "id":
                        self.id = kwargs["id"]
                    if key == "width":
                        self.width = kwargs["width"]
                    if key == "height":
                        self.height = kwargs["height"]
                    if key == "x":
                        self.x = kwargs["x"]
                    if key == "y":
                        self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns dictionary"""
        dictionary = {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height
        }
        return dictionary
