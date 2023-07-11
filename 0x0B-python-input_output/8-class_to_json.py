#!/usr/bin/python3
'''
create object for JSON serialization
'''


def class_to_json(obj):
    ''' Returns dictionary description with data list '''
    return obj.__dict__
