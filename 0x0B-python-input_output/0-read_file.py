#!/usr/bin/python3


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints it to stdout. """
    with open(filename, "r") as f:
        read_data = f.read()
    for characters in read_data:
        print(characters, end="")
        if characters == '\0':
            print(characters)
