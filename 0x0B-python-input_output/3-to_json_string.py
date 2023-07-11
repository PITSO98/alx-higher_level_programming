#!/usr/bin/python3
"""
Module to work with JSON
"""

import json


def to_json_string(my_obj):
    """ Returns json of an object """
    return json.dumps(my_obj)
