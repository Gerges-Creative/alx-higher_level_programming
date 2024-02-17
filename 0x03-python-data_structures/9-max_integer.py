#!/usr/bin/python3
def max_integer(my_list=[]):
    lenList = len(my_list)

    if lenList == 0:
        return None

    max = my_list[0]
    for i in range(lenList):
        if max < my_list[i]:
            max = my_list[i]

    return max
