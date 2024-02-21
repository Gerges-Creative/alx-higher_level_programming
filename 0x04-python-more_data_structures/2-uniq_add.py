#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    sum = 0

    for i in my_list:
        if i not in new:
            new.append(i)
            sum += i

    return sum
