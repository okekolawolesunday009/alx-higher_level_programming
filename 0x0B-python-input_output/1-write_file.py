#!/usr/bin/python3
"""prints number of string"""


def write_file(filename="", text=""):
    """writes to a file"""
    with open(filename, "w+", encoding='utf-8') as file:
        data = file.write(text)
        return data
