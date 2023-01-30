#!/usr/bin/pyrhon3
'''Defines a Rectangle class.'''


class Rectangle:
    '''Represents the class with width and height properties.'''
    def __init__(self, width=0, height=0):
        '''Instantiates then class
        width and height are defaulted to 0
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Gets the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the width of the rectangle to the value gotten'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Gets the width of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the width of the rectangle to the value gotten'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__value = value
