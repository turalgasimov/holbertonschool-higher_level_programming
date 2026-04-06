#!/usr/bin/python3
'''This module inherits list.'''


class MyList(list):
    '''Inherits list.'''

    def print_sorted(self):
        print(sorted(self))
