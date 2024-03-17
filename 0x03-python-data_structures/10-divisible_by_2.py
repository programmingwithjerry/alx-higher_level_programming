#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result = []
    for element in my_list:
        result.append(True if not element % 2 else False)
    return result
