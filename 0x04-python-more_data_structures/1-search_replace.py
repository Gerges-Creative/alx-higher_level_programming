#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()

    new = [replace if new[i] == search else new[i] for i in range(len(new))]

    return new
