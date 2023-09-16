#!/usr/bin/python3
"""1-rectanggle"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """subclass of rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
    
    @property
    def size(self):
        """Get/set the x of the Rectangle."""
        return self.width
    
    @size.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.width = value
        self.height = value

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
                    self.height = args[1]
                if len(args) >= 3:
                    self.x = args[2]
                if len(args) >= 4:
                    self.y = args[3]
        else:
            if len(kwargs) > 0:
                for key in kwargs.keys():
                    if key == "id":
                        self.id = kwargs["id"]
                    if key == "size":
                        self.width = kwargs["size"]
                    if key == "x":
                        self.x = kwargs["x"]
                    if key == "y":
                        self.y = kwargs["y"]

    def to_dictionary(self):
        """returns dictionary"""
        dictionary = {
            'id': self.id,
            'size': self.__size,
            'x': self.__x,
            'y': self.__y
        }
        return dictionary
    
