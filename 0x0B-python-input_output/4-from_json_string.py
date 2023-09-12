#!/usr/bin/python3
import json
"""PY data from JSON"""


def from_json_string(my_str):
    """functionize of JSON to PY DATA STRUCTURE"""
    py_string = json.loads(my_str)
    return (py_string)
