#!/usr/bin/python3
"""This module contains a class CountedIterator."""
from abc import ABC, abstractmethod


class CountedIterator:
    """class CountedIterator"""

    def __init__(self, iterator, counter=0):
        self.iterator = iter(self)
        self.counter = counter


    @property
    def get_count(self):
        return self.counter


    def __next__(self):
        self.counter += 1
        item = super().next(self)
        if item is None:
            raise StopIteration
        else:
            return item