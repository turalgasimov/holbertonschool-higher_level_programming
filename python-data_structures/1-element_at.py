#!/usr/bin/python3

def element_at(my_list, idx):
    if len(my_list) <= idx:
        print('Element at index {:d} is None'.format(idx))
        return
    else:
        print('Element at index {:d} is {}'.format(idx, my_list[idx]))
