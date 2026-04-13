#!/usr/bin/python3
'''This module  returns the dictionary description.'''
import json


def class_to_json(obj):
    '''returns the dictionary description.'''
    return json.dumps(obj.__dict__)
    