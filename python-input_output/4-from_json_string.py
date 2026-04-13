#!/usr/bin/python3
'''This module returns json->obj.'''
import json


def from_json_string(my_str):
    '''Returns json->obj.'''
    return json.loads(my_str)
