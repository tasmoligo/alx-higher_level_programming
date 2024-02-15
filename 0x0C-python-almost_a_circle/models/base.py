#!/usr/bin/python3
""" Module for class """

import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiator of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation
        of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        if not isinstance(list_dictionaries, list) \
                or not all(isinstance(i, list) for i in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionary")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_filels(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file. """
        filename = __class__.__name__ + ".json"
        with open(filename, "w") as openfile:
            if list_objs is None:
                openfile.write("[]")
            else:
                for arg in list_objs:
                    json_string = arg.to_dictionary()
                openfile.write(Base.to_json_string(json_string)
