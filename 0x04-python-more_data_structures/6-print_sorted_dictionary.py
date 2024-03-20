#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord_keys = list(a_dictionary.keys())
    sorted_list_ord_keys = list_ord_keys.sort()
    for i in sorted_list_ord_keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
