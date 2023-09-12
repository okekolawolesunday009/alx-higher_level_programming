#!/usr/bin/python3
"""prints number of string"""

def write_file(filename="", text=""):
    """writes to a file"""
    with open(filename, "w", encoding='utf-8') as file:
        file.write(text)
    with open(filename, "r", encoding='utf-8') as file:
        lines = len(file.readlines())
        print(lines)