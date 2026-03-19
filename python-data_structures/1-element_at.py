#!/usr/bin/python3

def element_at(my_list, idx):
    if (len(my_list) <= idx) or idx < 0:
        print('Element at index {:d} is None'.format(idx))
        return None
    else:
        print('Element at index {:d} is {}'.format(idx, my_list[idx]))
