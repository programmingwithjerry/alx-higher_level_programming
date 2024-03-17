#!/usr/bin/python3


def no_c(my_string):
    remove_c_and_C = my_string.translate({ord('c'): None})
    remove_c_and_C = remove_c_and_C.translate({ord('C'): None})
    return remove_c_and_C
