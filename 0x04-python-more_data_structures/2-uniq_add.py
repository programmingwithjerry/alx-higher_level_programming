#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int_list = set(my_list)
    counter = 0

    for i in uniq_int_list:
        counter += i

    return (counter)
