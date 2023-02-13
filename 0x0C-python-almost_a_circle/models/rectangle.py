#!/usr/bin/python3
'''
Defines the Base class
'''


class Base:
    '''
    Initializes with a private class attribute
    Defines the __init__():
        argument:
            id: initialized to None
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        when id is None, the private class attribute is incremented
        and assigned to the public instance attribute
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


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
        '''
        self.__width = width
        self.__height = height
        self.__x = x
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
