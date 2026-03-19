#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        t = (tuple_a[0]+tuple_b[0], tuple_a[1]+tuple_b[1])
    else:
        if len(tuple_a) < 2:
            if len(tuple_a) == 0:
                t = tuple_b.copy()
                return t
            t = (tuple_a[0]+tuple_b[0], 0+tuple_b[1])
        elif len(tuple_b) < 2:
            if len(tuple_b) == 0:
                t = tuple_a.copy()
                return t
            t = (tuple_a[0]+tuple_b[0], tuple_a[1]+0)
    return t
