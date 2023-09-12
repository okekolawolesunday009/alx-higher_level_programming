#!/usr/bin/python3
""""Defines to write obj file from JSON"""


import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        return json_data
