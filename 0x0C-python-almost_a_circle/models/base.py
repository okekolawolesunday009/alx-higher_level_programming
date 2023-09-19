#!/usr/bin/python3
"""Defines a base class"""


import json
import csv
import os.path

class Base:
    """class base doc"""
    __nb_objects = 0
    def __init__(self, id=None):
       if id is not None:
            self.id = id
       else:
           Base.__nb_objects += 1
           self.id =   Base.__nb_objects          
    
    def to_json_string(list_dictionaries):
        """coverts to json"""
        if list_dictionaries is None:
            return "[]"
        else:
            json_data = json.dumps(list_dictionaries)
            return (json_data)
        
    def save_to_file(cls, list_objs):
        """saves file to json"""
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
    
    
    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON
        string representation json_string
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with
        all attributes already set
        """

        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            new_base = cls(1, 1)
        if cls == Square:
            new_base = cls(1)
        new_base.update(**dictionary)
        return new_base

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        instance_list = []
        filename = "{}.json".format(cls.__name__)
        if os.path.isfile(filename):
            with open(filename) as f:
                instance_object = cls.from_json_string(f.read())
                for instance_dict in instance_object:
                    instance_list.append(cls.create(**instance_dict))
                return instance_list
        else:
            return []