#!/usr/bin/python3

class BaseGeometry:
    def __init__(self, *arg):
        super().__init__(*arg)

    def area(self):
        raise Exception("area() is not implemented")