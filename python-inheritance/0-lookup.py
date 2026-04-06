#!/usr/bin/python3
'''This module returns
the list of available
attributes and methods of an object.'''


def lookup(obj):
    '''Returns the list of
    available attributes and
    methods of an object'''

    atr = dir(obj)
    atr_list = []
    for i in atr:
        atr_list.append(i)
    return atr_list
