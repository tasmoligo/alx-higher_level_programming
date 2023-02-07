#!/usr/bin/python3
'''
DEfines a function that does the following
'''


def lookup(obj):
    '''
    Returns the list of available attributes and methods of an object "obj"
    '''
    return list(dir(obj))
