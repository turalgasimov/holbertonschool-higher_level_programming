#!/usr/bin/python3
'''This module writes to text file.'''
import json


def save_to_json_file(my_obj, filename)::
    '''writes to text file.'''
    with open(filename, 'w') as f:
        json_data = json.dumps(my_obj)
        for line in json_data:
            f.write(line)
