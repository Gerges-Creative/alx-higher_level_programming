#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = 0, 0
    if len(tuple_b) < 2:
        tuple_b = 0, 0
    tuple_c = []
    for i in range(2):
        tuple_c.append(tuple_a[i] + tuple_b[i])
    tuple_c = tuple(tuple_c)

    return tuple_c
