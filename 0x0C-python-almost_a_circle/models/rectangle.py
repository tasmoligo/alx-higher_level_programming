#!/usr/bin/python3
'''Defines a rectangle class which inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''
    Represents a rectangleobject which inherits properties from the Base class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Defines a rectangle
        arguments:
            width: an int
            height: an int
            x: an int
            y: an int
            id: an int
        '''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        self.__height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        self.__x = value

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        self.__y = value
