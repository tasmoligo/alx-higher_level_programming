#!/usr/bin/python3
""" Module that inherits. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Inherits from Rectangle class. """
    def __init__(self, size, x=0, y=0, id=None):
        """ Instantiator of the class. """
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns the string representation """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.size))

    @property
    def size(self):
        """ gets the size. """
        return self.__width

    @size.setter
    def size(self, value):
        """ sets the value. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """ Assigns attrubutes using non key-word(*args)
        and keyworded arguments(****<F7kwargs)
        """
        if args and args is not None:
            count = 0
            for arg in args:
                if count == 0:
                    if args is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1
        elif kwargs and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ Returns the dictionary representation of a square"""
        my_dict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return my_dict
