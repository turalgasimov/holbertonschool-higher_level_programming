#!/usr/bin/python3
'''This module adds all arguments 
to a Python list, and then save them to a file.'''
import json, sys
from 5-save_to_json_file import save_to_json_file as s
from 6-load_from_json_file import load_from_json_file as l


def add_n_save():
    '''adds all arguments 
    to a Python list, and then save them to a file.'''

    filename = "add_item.json"

    with open(filename, "w") as f:
        data = l(filename)
        data = list(data)

        for _ in sys.argv:
            data.append(_)

        s(data, filename)
