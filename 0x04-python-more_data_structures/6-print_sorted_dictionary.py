#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord_keys = list(a_dictionary.keys())
    list_ord_keys.sort()
        print("{}: {}".format(i, a_dictionary.get(i)))
