#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    max = 0
    person = ''
    for k, v in a_dictionary.items():
        if v >= max:
            max = v
            person = k
    return person
