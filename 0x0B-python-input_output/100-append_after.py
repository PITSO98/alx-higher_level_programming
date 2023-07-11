#!/usr/bin/python3
"""Module 100-append_after
Inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends the new_string
    """

    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fl:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fl.write(s)
