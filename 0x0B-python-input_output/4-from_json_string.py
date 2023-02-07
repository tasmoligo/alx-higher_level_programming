#!/usr/bin/python3
'''
Defines a function below
'''
import json


def from_json_string(my_str):
    '''
    returns an object (Python data structure) represented by a JSON string

    arguments:
        my_str: the string to convert

    return:
        object represented by a JSON string
    '''
    return json.loads(my_str)
