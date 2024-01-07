#!/usr/bin/python3
"""Module that add two integrs"""


def add_integer(a, b=98):
    """
        Function that adds two integers
        a = first argument
        b = second argument
        Raises a TypeError if neither of the arguments are int or float
        Returns the sum of the two arguments typecasted to int
    """
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a + b)
