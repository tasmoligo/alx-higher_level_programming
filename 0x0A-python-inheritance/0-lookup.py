#!/usr/bin/python3
"""
Defines the function that returns  the list of available methods
and attributes of an object
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    """
    return dir(obj)
