#!/usr/bin/python3
'''Defines a class named Square with
2 private instance and 2 public method'''


class Square:
    '''Creates a class named square'''
    def __init__(self, size=0, position=(0, 0)):
        '''Instatiates the created class where
        size is the size of the square
        position is the coordinate of the square'''
        self.size = size
        self.__position = position

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

    @property
    def position(self):
        '''Gets the position of the square'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Sets the position of the square'''
        if (not isinstance(value, tuple) or len(value) != 2 or
                not (num >= 0 for num in value) or
                not (isinstance(num, int) for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        '''Returns the area of the square'''
        return (self.__size * self.__size)

    def my_print(self):
        '''Prints the square with the character # to stdout'''
        if self.__size == 0:
            print('')
        [print('') for i in range(0, self.__position[1])]
        for j in range(0, self.__size):
            [print('_', end='') for k in range(0, self.__position[0])]
            [print('#', end='') for m in range(0, self.__size)]
            print('')
