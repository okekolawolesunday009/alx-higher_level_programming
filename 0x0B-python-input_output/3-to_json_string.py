#!/usr/bin/python3
import json
"""JSON OF AN OBJ"""


def to_json_string(my_obj):
    """functionize to JSON """
    json_data = json.dumps(my_obj)
    return json_data
