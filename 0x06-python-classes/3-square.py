#!/usr/bin/python3
'''Defines a square'''


class Square:
    '''The square class'''
    def __init__(self, size=0):
        '''Instantiates a square with size'''
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''Returns the area of the square'''
        return (self.__size * self.__size)
