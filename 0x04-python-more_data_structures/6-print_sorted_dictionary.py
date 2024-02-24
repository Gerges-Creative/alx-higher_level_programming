#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    sort_d = sorted(a_dictionary)

    for key in sort_d:
        print("{}: {}".format(key, a_dictonary[key])
