#!/usr/bin/python3
import json

def from_json_string(my_str):
    py_string = json.loads(my_str)
    print(type(py_string))