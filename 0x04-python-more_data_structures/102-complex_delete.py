#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for dict_value in list_keys:
        if value == a_dictionary.get(dict_value):
            del a_dictionary[dict_value]

    return (a_dictionary)
