#!/usr/bin/python3
"""This module returns
a list of lists of integers
representing the Pascal's triangle of n"""


def pascal_triangle(n):
    """Pascal triangle handler"""
    pascal_list = []

    if n <= 0:
        return pascal_list

    for i in range(1, n + 1):
        row = [1] * i
        pascal_list.append(row)

        if i-1 > 1:
            for j in range(1, len(row)-1):
                row[j] = pascal_list[i-2][j-1] + pascal_list[i-2][j]
                pascal_list[i-1] = row
  
    return pascal_list
