#!/usr/bin/python3
"""JSON OF AN OBJ"""

import json

def to_json_string(my_obj):
    """functionize to JSON """
    json_data = json.dumps(my_obj)
    return json_data
