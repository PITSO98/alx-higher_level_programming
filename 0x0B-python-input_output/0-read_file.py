#!/usr/bin/python3
"""
Reads from a file and prints
"""


def read_file(filename=""):
    """Reads from filename and prints

    """

    with open(filename) as fl:
        read_text = fl.read()
        print(read_text, end="")
