#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_list.sort()
    next = -1
    sum = 0

    for i in my_list:
        if i == next:
            continue
        sum += i
        next = i
    return sum
