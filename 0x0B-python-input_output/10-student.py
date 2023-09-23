#!/usr/bin/python3
""" Class that defines a student """


class Student:
    """
    Class that defines a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict containig the attributes of the student instance
            attrs: optional
        """
        if (attrs == type(str)):
            return (getattr(self, attrs) for attr in attrs)
        if (attrs == type(str)):
            return self.__dict__ 