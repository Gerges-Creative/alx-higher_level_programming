#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    best = 0
    for key in a_dictionary:
        value = a_dictionary[key]
        if value > best:
            best = value
            name = key

    return name