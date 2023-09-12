#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs == type(str)):
            return (getattr(self, attrs) for attr in attrs)
        if (attrs == type(str)):
            return self.__dict__ 