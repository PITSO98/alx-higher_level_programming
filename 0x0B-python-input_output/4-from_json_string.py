#!/usr/bin/python3
"""
Module that works with JSON
"""

import json


def from_json_string(my_str):
    """ Returns an object  """
    return json.loads(my_str)
