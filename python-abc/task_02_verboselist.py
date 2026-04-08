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


    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item