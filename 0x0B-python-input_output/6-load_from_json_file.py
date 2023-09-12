#!/usr/bin/python3
""""Defines to write obj file from JSON"""


import json

"""creates an Object from a “JSON file”:"""
def load_from_json_file(filename):
    with open(filename, mode='w', encoding='utf-8') as file:
        json_obj= json.loads(file)
        file.write(json_obj)