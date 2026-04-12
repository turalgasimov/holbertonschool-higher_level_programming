#!/usr/bin/python3
'''This module reads from file.'''


def read_file(filename=""):
    """Reads a file."""
    with open(filename, encoding="utf-8") as f:
        read_data  = f.read()
        print(read_data)
