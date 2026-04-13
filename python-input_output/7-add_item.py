#!/usr/bin/python3
'''This module adds all arguments
to a Python list, and then them to a file.'''
import json
import sys
import os
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


def add_n_save():
    '''adds all arguments
    to a Python list, and then save them to a file.'''

    filename = "add_item.json"
    new_list = []

    for i in range(1, len(sys.argv)):
        new_list.append(sys.argv[i])

    try:
        data = load(filename)
    except FileNotFoundError:
        data = []

    data += new_list
    save(data, filename)


if __name__ == "__main__":
    add_n_save()
