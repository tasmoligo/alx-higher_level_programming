#!/usr/bin/python3
"""
    Defines a function that compares two instancesof a class
"""


def is_same_class(obj, a_class):
    """
        eturns True if the object is exactly an instance
        of the specified class; otherwise False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
