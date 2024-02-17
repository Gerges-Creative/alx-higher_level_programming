#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)
    if len_s == 0:
        first_char = None
    else:
        first_char = sentence[0]

    tuple_s = len_s, first_char

    return tuple_s
