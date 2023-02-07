#!/usr/bin/python3
'''
Defines the function that does the below
'''


def read_file(filename=""):
    '''
    reads a text file (UTF8) and prints it to stdout

    argument:
        filename: name of file to read
    '''
    with open(filename, mode="r", encoding="utf-8") as a_file:
        file_read = a_file.read()
        print(file_read)
