#!/usr/bin/python3
"""Creating a base class"""

import json
import csv
import os

class Base:
    """Defining class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing class Base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id        

        @staticmethod
        def to_json_string(list_dictionaries):
            """Returning json string representation of list of dictionaries"""
            if list_dictionaries is None or list_dictionaries == []:
                return "[]"
            if (type(list_dictionaries) != list or
                    not all(type(x) == dict for x in list_dictionaries)):
                raise TypeError("list_dictionaries must be a list of dictionaries")
            return json.dumps(list_dictionaries)

        @classmethod
        def save_to_file(cls, list_objs):
            """Saving list of objects to file"""
            if (type(list_objs) != list and
                    list_objs is not None or
                    not all(isinstance(x, cls) for x in list_objs)):
                raise TypeError("list_objs must be a list of instances")

            filename = cls.__name__ + ".csv"
            with open(filename, 'w') as f:
                if list_objs is not None:
                    list_objs = [x.to_dictionary() for x in list_objs]
                     if cls.__name__ == 'Rectangle':
                         fields = ['id', 'width', 'height', 'x', 'y']
                     elif cls.__name__ == 'Square':
                         fields = ['id', 'size', 'x', 'y']
                    writer = csv.DictWriter(f, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(list_objs)
  
  @staticmethod
    def from_json_string(json_string):
        """Returning list of objects from json string"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)
        
    @classmethod
    def create(cls, **dictionary):
        """Creating an instance of class Base"""
        if cls.__name__ == 'Rectangle':
            new_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod


