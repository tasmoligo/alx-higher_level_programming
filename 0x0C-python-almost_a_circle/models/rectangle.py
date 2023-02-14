#!/usr/bin/python3
'''Defines a rectangle class which inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''
    Represents a rectangle object which inherits properties from the Base class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Defines a rectangle
        arguments:
            width: an int
            height: an int
            x: an int
            y: an int
            id: an int
        '''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        self.__height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        self.__x = value

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        self.__y = value

    def area(self):
        '''Returns the area of the rectangle'''
        return self.width * self.height

    def display(self):
        '''Prints the rectangle with the # character'''
        for i in range(self.y):
            print("")
        for j in range(self.height):
            for k in range(self.width + self.x):
                if k < self.x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print("")

    def __str__(self):
        '''Returns the string representation of the rectangle'''
        r1 = f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}"
        r2 = f" - {self.width}/{self.height}"
        return r1 + r2

    def update(self, *args, **kwargs):
        '''Assigns an argument to each attribute'''
        if args or len(args) != 0:
            for i in range(len(args)):
                if args[i] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            if kwargs or len(kwargs) != 0:
                for k, v in kwargs.items():
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    if k == "id":
                        self.id = v
                    if k == "width":
                        self.width = v
                    if k == "height":
                        self.height = v
                    if k == "x":
                        self.x = v
                    if k == "y":
                        self.y = v
