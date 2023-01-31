#!/usr/bin/python3
'''Defines a function that adds two integers.'''


def add_integer(a, b=98):
    '''Function to add two numbers
    Numbers must be of integer or float type else
    a TypeError will be raised.'''

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a + b)
