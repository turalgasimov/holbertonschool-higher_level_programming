#!/usr/bin/python3
'''This module returns
the list of available
attributes and methods of an object.'''


def lookup(obj):
    '''Returns the list of
    available attributes and
    methods of an object'''

    atr = dir(obj)
    l = []
    for i in atr:
        l.append(i)
    return l
