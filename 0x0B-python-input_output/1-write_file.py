#!/usr/bin/python3
'''
Defines the function below
'''


def write_file(filename="", text=""):
    '''
    writes a string to a text file (UTF8)
    and returns the number of characters written

    arguments:
        filename: the file to write to
        text: the content of the file

    return:
        number of characters written(int)
    '''
    with open(filename, mode="w", encoding="utf-8") as a_file:
        return a_file.write(text)
