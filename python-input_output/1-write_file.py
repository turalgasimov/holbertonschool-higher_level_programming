#!/usr/bin/python3
'''This module writes to file.'''


def write_file(filename="", text=""):
    """Writes to file."""
    with open(filename, "w", encoding="utf-8") as f:
        write_file = f.write(text)
        return write_file
