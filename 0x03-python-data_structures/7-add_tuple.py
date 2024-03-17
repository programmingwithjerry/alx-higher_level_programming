#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_of_tuple_a = len(tuple_a)
    len_of_tuple_b = len(tuple_b)
# check for tuple_a
    if len_of_tuple_a < 1:
        tuple_a = (0, 0)
    elif len_of_tuple_a < 2:
        tuple_a = (tuple_a[0], 0)

# check for tuple_b
    if len_of_tuple_b < 1:
        tuple_b = (0, 0)
    elif len_of_tuple_b < 2:
        tuple_b = (tuple_b[0], 0)

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
