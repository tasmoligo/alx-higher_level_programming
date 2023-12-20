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

    @property
    def size(self):
        '''retrieve property'''
        return self.__size

    @size.setter
    def size(self, value):
        '''property to set the value of size'''
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def __eq__(self, other):
        '''compares if the two squares equal'''
        return self.area() == other.area()

    def __ne__(self, other):
        '''compares two square instances'''
        return self.area() != other.area()

    def __gt__(self, other):
        '''compares two square instances'''
        return self.area() > other.area()

    def __ge__(self, other):
        '''compares two square instances'''
        return self.area() >= other.area()

    def __le__(self, other):
        '''compares two square instances'''
        return self.area() <= other.area()

    def __lt__(self, other):
        '''compares two square instances'''
        return self.area() < other.area()
