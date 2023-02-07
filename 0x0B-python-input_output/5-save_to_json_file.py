#!/usr/bin/python3
'''
Defines a functon below
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    writes an Object to a text file, using a JSON representation

    arguments:
        my_obj: the object to convert and save
        filename: the file to save to
    '''
    conv_obj = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as a_file:
        obj = a_file.write(conv_obj)
        return obj
