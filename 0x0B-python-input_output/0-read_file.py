#!/usr/bin/python3
""" Reads and writes a file. """


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints it to stdout. """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    for characters in read_data:
        print(characters, end="")
        if characters == '\0':
            print(characters)
