#!/usr/bin/python3
"""
Module to append text to file
"""


def append_write(filename="", text=""):
    ''' Appends text to file '''
    with open(filename, 'a') as fl:
        x = fl.write(text)
    return x
