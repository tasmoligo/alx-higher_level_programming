#!/usr/bin/python3
"""Geometry class module"""


class BaseGeometry:
    """A geometry class"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value

        Args:
        name  = str
        value = int

        Raises:
        TypeError, ValueError
        """
        self.name = name
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.value = value
