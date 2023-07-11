#!/usr/bin/python3
"""Module to work on files with JSON """

import json


def save_to_json_file(my_obj, filename):
    """ Prints JSON of object to file """
    with open(filename, 'w') as fl:
        fl.write(json.dumps(my_obj))
