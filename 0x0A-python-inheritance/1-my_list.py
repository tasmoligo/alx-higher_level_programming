#!/usr/bin/python3-
""" Inherits from a list class. """


class MyList(list):
    """
        Inherits from list
    """
    def print_sorted(self):
        """
            Prints a list in ascending order
        """
        print(sorted(self))
