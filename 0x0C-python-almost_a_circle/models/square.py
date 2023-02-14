#!/usr/bin/python3
'''Defines a Square class thaat inherits from rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Represents a square object'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initializs the square'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String representation of the square'''
        s1 = f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}"
        s2 = f" - {self.height}"
        return s1 + s2

    @property
    def size(self):
        '''size getter'''
        return self.height

    @size.setter
    def size(self, value):
        '''size setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Public method that assigns attributes
        arguments:
            *args - positional argument
            **kwargs - key-word argument
        '''
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.height, self.height, self.x, self.y)
                    else:
                        self.id = args[i]
                if i == 1:
                    self.width = args[i]
                    self.height = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            if kwargs and len(kwargs) != 0:
                for k, v in kwargs.items():
                    if k == "id":
                        if v is None:
                            self.__init__(
                                    self.height, self.height, self.x, self.y)
                        else:
                            self.id = v
                    elif k == "size":
                        self.width = v
                        self.height = v
                    elif k == "x":
                        self.x = v
                    elif k == "y":
                        self.y = v

    def to_dictionary(self):
        '''Returns the dictionary representation of a Square'''
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
