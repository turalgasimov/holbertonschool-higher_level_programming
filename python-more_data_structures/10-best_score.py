#!/usr/bin/python3

def best_score(a_dictionary):
    max = 0
    person = None
    for k, v in a_dictionary.items():
        if v >= max:
            max = v
            person = k
    return person
