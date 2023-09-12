#!/usr/bin/python3
"""Reads a file from main"""


def read_file(filename=""):
    """reads a file out to the console"""
    with open(filename, "r", encoding='utf-8') as file:
        data = file.read()
    print("{}".format(data))
