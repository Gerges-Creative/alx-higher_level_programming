#!/usr/python3
def remove_char_at(str, n):
    for i in range(len(str)):
        if i == n:
            str[i] = ''
