#!/usr/bin/python3
'''Defines a class named Square'''


class Square:
    '''Creates a class named Square'''
    def __init__(self, size=0):
        '''This is the instantiationnof the class with ptional size'''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        '''This returns the area of the square'''
        return (self.__size * self.__size)
