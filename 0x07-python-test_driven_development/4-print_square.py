#!/usr/bin/python3
"""Defines a function that prints a square"""


def print_square(size):
    """
    Prints a square with the character '#'

    Args:
    size - size of the square

    Errors:
    TypeError - if size is not an integer
    ValueError - if size is less than zerp
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
