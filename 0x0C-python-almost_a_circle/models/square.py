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
    def size(self, value):
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
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary"""
        dictionary = {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
        return dictionary 
