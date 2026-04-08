#!/usr/bin/python3
"""This module contains a class VerboseList."""
from abc import ABC, abstractmethod


class VerboseList(list):
    '''class VerboseList'''

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")


    def extend(self, item):
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")


    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)


    def pop(self, index=None):
        if index is None:
            print(f"Popped [{self[-1]}] from the list.")
            super().pop()
        else:
            print(f"Popped [{self[index]}] from the list.")
            super().pop(index)