#!/usr/bin/python3
'''Defines a Square class thaat inherits from rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Represents a square object'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initializs the square'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String representation of the square'''
        s1 = f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}"
        s2 = f" - {self.height}"
        return s1 + s2

    @property
    def size(self):
        '''size getter'''
        return self.height

    @size.setter
    def size(self, value):
        '''size setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
