#!/usr/bin/python3
""" Module that inherits from a class """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Inherits from BaseGeometry. """
    def __init__(self, width, height):
        """ Initializes a Rectangle class. """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
