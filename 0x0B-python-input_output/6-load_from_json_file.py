#!/usr/bin/python3
'''
Defines a function below
'''
import json


def load_from_json_file(filename):
    '''
    creates an Object from a “JSON file”

    arguments:
        filename: the file to load from
    '''
    with open(filename, encoding="utf-8") as a_file:
        my_str = a_file.read()
        return json.loads(my_str)
