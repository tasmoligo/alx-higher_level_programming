#!/usr/bin/python3
'''
Defines a function below
'''
import json


def to_json_string(my_obj):
    '''
    returns the JSON representation of an object (string)

    arguments:
        my_obj: the object to convert

    return:
        JSON representation of an object (string)
    '''
    return json.dumps(my_obj)
