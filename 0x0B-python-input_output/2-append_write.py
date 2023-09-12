#!/usr/bin/python3
"""append string"""


def append_write(filename="", text=""):
    """append the string to file"""
    try:
        with open(filename, "a", encoding='utf-8') as file:
            lines = file.write(text)
            return (lines)
    except FileNotFoundError:
        print("No such file or directory")
        return None
