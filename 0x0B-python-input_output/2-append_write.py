#!/usr/bin/python3
'''
Defines the function below
'''


def append_write(filename="", text=""):
    '''
    appends a string at the end of a text file (UTF-8)
    and returns the number of characters added

    arguments:
        filename: name of file to append to
        text: content to append

    return:
        number of characters added(int)
    '''
    with open(filename, mode="a", encoding="utf-8") as a_file:
        return a_file.write(text)
