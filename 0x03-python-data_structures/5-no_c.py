#!/usr/bin/python3
def no_c(my_string):
    idxc, idxC = -1, -1

    while "c" in my_string or "C" in my_string:
        idxc = my_string.find("c")
        idxC = my_string.find("C")
        if idxc != -1:
            my_string = my_string[:idxc] + my_string[idxc + 1:]
        if idxC != -1:
            my_string = my_string[:idxC] + my_string[idxC + 1:]

    return my_string
