#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    multiply = a_dictionary.copy()
    for key in a_dictionary:
        value = multiply[key]
        multiply[key] = value * 2

    return multiply
