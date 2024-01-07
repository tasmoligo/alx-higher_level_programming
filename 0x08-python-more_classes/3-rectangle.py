#!/usr/bin/python3


class Rectangle:
    """defines a rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns thr string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        a = self.__height
        b = self.__width
        rectangle = ""
        for i in range(a):
            for j in range(b):
                rectangle += "#"
            if i < a - 1:
                rectangle += "\n"
        return rectangle
