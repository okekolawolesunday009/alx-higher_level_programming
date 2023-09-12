#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    with open(filename, mode='w', encoding='utf-8') as file:
        json_str = json.dumps(my_obj)
        file.write(json_str)