#!/usr/bin/python3
def no_c(my_string):
    count = my_string.count(c)

    while "c" in my_string or "C" in my_string:
        my_string.remove("c")
        my_string.remove("C")

    return my_string
