#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lenList = len(my_list)

    if idx < 0 or idx > lenList:
        return my_list

    my_list.remove(my_list[idx])

    return my_list
