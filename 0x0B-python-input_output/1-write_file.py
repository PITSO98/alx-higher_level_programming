#!/usr/bin/python3
"""
Module to write to file
"""


def write_file(filename="", text=""):
    ''' Writes text to file '''
    with open(filename, 'w') as fl:
        fl.write(text)
        x = fl.tell()
    return x
