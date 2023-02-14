#!/usr/bin/python3
'''
Defines the Base class
'''
import json


class Base:
    '''
    Initializes with a private class attribute
    Defines the __init__():
        argument:
            id: initialized to None
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        when id is None, the private class attribute is incremented
        and assigned to the public instance attribute, else
        it is as is
        '''
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(list_dicts))
