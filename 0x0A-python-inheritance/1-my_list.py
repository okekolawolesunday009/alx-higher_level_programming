#!/usr/bin/python3
"""Defines a sublass of Mylist of class list """


class MyList(list):
    def __init__(self, *arg):
        """function is used to call the constructor """
        super().__init__(*arg)

    def print_sorted(self):
        """prints out sorted list"""
        return self.sort()
