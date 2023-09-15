#!/usr/bin/python3
"""Defines a base module"""


import json

class Base:
    __nb_objects = 0
    def __init__(self, id=None):
       if id is not None:
            self.id = id
       else:
           Base.__nb_objects += 1
           self.id =   Base.__nb_objects          
    
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            json_data = json.dumps(list_dictionaries)
            return (json_data)
        
    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls.__name__)
        list_dist = []
        if list_objs is None:
            pass
        else:
            for i in range(len(list_objs)):
                list_dist.append(list_objs[i].to_dictionary())
        lists = cls.to_json_string(list_dist)
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(lists)
    
    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        else:
            json_data = json.loads(json_string)
            return (json_data)

