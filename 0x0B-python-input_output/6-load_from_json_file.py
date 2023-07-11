#!/usr/bin/python3
"""
Creates an object from JSON file
"""


import json


def load_from_json_file(filename):
    """Creates an object from filename

    """

    with open(filename, 'r') as f:
        return json.load(f)
