#!/usr/bin/python3
""" Module for class """
from models.base import Base


class Rectangle(Base):
    """subclass that inherits from the base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiator of the class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """ print in stdout the Rectangle instance with the character # """
        for a in range(self.y):
            print("")
        for i in range(self.__height):
            for b in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ Returns the string representation """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))
