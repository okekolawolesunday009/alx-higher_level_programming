#!/usr/bin/python3
""""Defines to write obj file to JSON"""


import json


def save_to_json_file(my_obj, filename):
    """saves to JSON format"""
    with open(filename, mode='w', encoding='utf-8') as file:
        json_obj = json.dumps(my_obj)
        file.write(json_obj)
