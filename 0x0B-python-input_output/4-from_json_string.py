#!/usr/bin/python3
import json

def from_json_string(my_str):
    py_string = json.loads(my_str)
    return (py_string)
    print(py_string)
