#!/usr/bin/python3

def no_c(my_string):
    n = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        n += i
    return n
