#!/usr/bin/python3
'''
Defines the Base class
'''


class Base:
    '''
    Initializes with a private class attribute
    Defines the __init__():
        argument:
            id: initialized to None
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        when id is None, the private class attribute is incremented
        and assigned to the public instance attribute, else
        it is as is
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
