#!/usr/bin/python3
""" Creates a file. """


def write_file(filename="", text=""):
    """ Checks if a file exists and creates it. """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
