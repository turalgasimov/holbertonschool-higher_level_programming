#!/usr/bin/python3
"""This module returns
a list of lists of integers
representing the Pascal's triangle of n"""


def pascal_triangle(n):
    """Pascal triangle handler"""
    pascal_list = []

    if n <= 0:
        return pascal_list
