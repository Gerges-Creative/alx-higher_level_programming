#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()

    [new_list[i]=replace if new_list[i] == search for i in range(len(new_list))]

    return new_list
