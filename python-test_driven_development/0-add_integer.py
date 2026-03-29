#!/usr/bin/python3
"""This module defines a function that adds two integers."""

def add_integer(a, b=98):
    """Add two numbers"""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    
    return a + b
