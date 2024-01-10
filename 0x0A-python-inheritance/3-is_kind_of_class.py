#!/usr/bin/python3
"""
    Defines a function that compares two instancesof a class
"""


def is_kind_of_class(obj, a_class):
    """
        Returns True if the object is an instance or
        object is an instance of a class that inherited from
        of specified class; otherwise False.
    """
    return isinstance(obj, a_class)
