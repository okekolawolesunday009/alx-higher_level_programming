#!/usr/bin/python3
"""Defines a sublass of Mylist of class list """


class MyList(list):
    """
        MyList: subclass that inherits from list
    """
    def __init__(self, *arg):
        """function is used to call the constructor """

    def print_sorted(self):
        """prints out sorted list"""
        print(f"{sorted(self)}")
