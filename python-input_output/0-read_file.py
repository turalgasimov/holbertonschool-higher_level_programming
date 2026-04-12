#!/usr/bin/python3
'''This module reads from file.'''


def read_file(filename=""):
    """Reads a file."""
    with open(filename, 'r') as f:
        print(f.read())