#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    n = my_list
    if idx < 0 or idx >= len(n):
        return n
    else:
        n[idx] = element
        return my_list, n
