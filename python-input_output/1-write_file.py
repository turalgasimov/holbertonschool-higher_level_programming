#!/usr/bin/python3
'''This module writes to file.'''


def read_file(filename="", text=""):
    """Writes to file."""
    with open(filename, encoding="utf-8") as f:
        write_file = f.write(text)
        return write_file
