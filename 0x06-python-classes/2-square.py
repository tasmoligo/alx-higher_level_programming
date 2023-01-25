#!/usr/bin/python3
'''Defines a class named Square'''


class Square:
    '''Creates a class'''
    def __init__(self, size=0):
        '''Instantiates the class with optional where
        size is the size of the square.'''

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
