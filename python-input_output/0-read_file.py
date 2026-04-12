#!/usr/bin/python3
'''This module reads from file.'''


def read_file(filename=""):
    """Reads a file."""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
