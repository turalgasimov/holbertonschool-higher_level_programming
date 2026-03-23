#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dict = a_dictionary
    for i in a_dictionary.values():
        i *= 2
    return dict
