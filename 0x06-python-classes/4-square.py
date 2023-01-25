#!/usr/bin/python3
'''Defines a class named Square'''


class Square:
    '''Creates a class named square'''
    def __init__(self, size=0):
        '''Instatiates the created class where
        size is the size of the square'''
        self.size = size
    @property
    def size(self):
        '''Gets the size of the square'''
        return self.__size
    @size.setter
    def size(self, value):
        '''Sets the size of the swuare'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
    def area(self):
        '''Returns the area ofnthe square'''
        return (self.__size * self.__size)
