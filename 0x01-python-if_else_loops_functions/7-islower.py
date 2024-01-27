#!/usr/bin/python3
def islower(c):
    if len(c) == 1 and c >= "a" and c <= "z":
        return True
    elif c == '':
        raise ValueError("Traceback (most recent call last): [Anything]")
    else:
        return False
