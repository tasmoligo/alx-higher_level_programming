#!/usr/bin/python3
'''reassembling a bytecode'''
import math


class MagicClass:
    '''defines a class'''

    def __init__(self, radius=0):
        '''Instantiating the class'''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        '''defining the area'''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        '''defining the circumference'''
        return 2 * math.pi * self.__radius
